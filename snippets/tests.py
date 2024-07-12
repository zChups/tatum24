from django.test import TestCase, Client
from django.utils import timezone
from django.contrib.auth.models import User, Group
from snippets.models import Snippet, Comment, Language
from django.urls import reverse

"""
    Function Testing
"""


class CommentTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test-user', password='password123')

        self.language = Language.objects.create(
            name='Python',
            slug='python',
            language_code='python'
        )
        self.snippet = Snippet.objects.create(
            title='Test Snippet',
            language=self.language,
            author=self.user,
            description='This is a test snippet',
            code='print("Hi dear!")'
        )

    def test_create_comment_valid(self):
        initial_count = Comment.objects.count()
        comment = Comment.objects.create(
            snippet=self.snippet,
            author=self.user,
            content='This is a valid comment'
        )

        self.assertEqual(Comment.objects.count(), initial_count + 1)
        self.assertEqual(comment.snippet, self.snippet)
        self.assertEqual(comment.author, self.user)
        self.assertEqual(comment.content, 'This is a valid comment')

    def test_create_comment_long_content(self):
        initial_count = Comment.objects.count()

        long_content = 'a' * 5000

        comment = Comment.objects.create(
            snippet=self.snippet,
            author=self.user,
            content=long_content
        )

        self.assertEqual(Comment.objects.count(), initial_count + 1)
        self.assertEqual(comment.snippet, self.snippet)
        self.assertEqual(comment.author, self.user)
        self.assertEqual(comment.content, long_content)

    def test_create_comment_unicode_content(self):
        initial_count = Comment.objects.count()
        unicode_content = 'Unicode characters: 한글, 漢字, こんに'

        comment = Comment.objects.create(
            snippet=self.snippet,
            author=self.user,
            content=unicode_content
        )
        self.assertEqual(Comment.objects.count(), initial_count + 1)
        self.assertEqual(comment.snippet, self.snippet)
        self.assertEqual(comment.author, self.user)
        self.assertEqual(comment.content, unicode_content)

    def test_update_comment(self):
        comment = Comment.objects.create(
            snippet=self.snippet,
            author=self.user,
            content='Original content'
        )
        comment.content = 'Updated content'
        comment.save()
        updated_comment = Comment.objects.get(id=comment.id)
        self.assertEqual(updated_comment.content, 'Updated content')

    def test_delete_comment(self):
        comment = Comment.objects.create(
            snippet=self.snippet,
            author=self.user,
            content='To be deleted'
        )
        initial_count = Comment.objects.count()
        comment.delete()
        self.assertEqual(Comment.objects.count(), initial_count - 1)

    def test_get_absolute_url(self):
        comment = Comment.objects.create(
            snippet=self.snippet,
            author=self.user,
            content='Test comment'
        )
        expected_url = reverse('snippet_detail', kwargs={'pk': self.snippet.pk})
        self.assertEqual(comment.get_absolute_url(), expected_url)


"""
    
    View Testing
    
"""


class EditSnippetViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test-user', password='password123')

        self.moderator = User.objects.create_user(username='moderator', password='password456')
        self.moderator_group = Group.objects.create(name='Moderator')
        self.moderator.groups.add(self.moderator_group)

        self.language = Language.objects.create(
            name='Python',
            slug='python',
            language_code='python'
        )

        self.snippet = Snippet.objects.create(
            title='Test Snippet',
            language=self.language,
            author=self.user,
            description='This is a test snippet',
            code='print("Hello, world!")',
            pub_date=timezone.now()
        )

    def test_edit_snippet_author(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('edit_snippet', args=[self.snippet.pk]), {
            'title': 'Updated Snippet Title',
            'language': self.language.pk,
            'description': 'Updated description',
            'code': 'print("Updated code!")',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'snippets/templates/snippets/edit_snippet.html')

    def test_edit_snippet_moderator(self):
        self.client.force_login(self.moderator)

        response = self.client.post(reverse('edit_snippet', args=[self.snippet.pk]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'snippets/templates/snippets/edit_snippet.html')

    def test_edit_snippet_no_permission(self):
        unauthorized_user = User.objects.create_user(username='unauthorized', password='password789')
        self.client.force_login(unauthorized_user)

        response = self.client.post(reverse('edit_snippet', args=[self.snippet.pk]), {
            'title': 'Attempt to Edit Snippet',
            'language': self.language.slug,
            'description': 'Attempt to modify',
            'code': 'print("Attempt to modify code")',
        })

        self.assertRedirects(response, reverse('snippet_detail', args=[self.snippet.pk]))
        updated_snippet = Snippet.objects.get(pk=self.snippet.pk)
        self.assertEqual(updated_snippet.title, 'Test Snippet')
