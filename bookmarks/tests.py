from django.test import TestCase
from django.contrib.auth.models import User
from snippets.models import Snippet, Language
from django.utils import timezone
from bookmarks.models import Bookmark


class BookmarkModelTest(TestCase):

    def setUp(self):
        # Create a language
        self.language = Language.objects.create(
            name='Python',
            slug='python',
            language_code='python'
        )

        # Create users
        self.user1 = User.objects.create_user(username='testuser1', password='testpassword')
        self.user2 = User.objects.create_user(username='testuser2', password='testpassword')

        # Create snippets
        self.snippet1 = Snippet.objects.create(
            title='Test Snippet 1',
            language=self.language,
            author=self.user1,
            description='A test snippet',
            code='print("Hello, world!")',
            pub_date=timezone.now(),
            update_date=timezone.now(),
            tags='test'
        )
        self.snippet2 = Snippet.objects.create(
            title='Test Snippet 2',
            language=self.language,
            author=self.user2,
            description='Another test snippet',
            code='print("Goodbye, world!")',
            pub_date=timezone.now(),
            update_date=timezone.now(),
            tags='test'
        )

        # Create bookmarks
        self.bookmark1 = Bookmark.objects.create(snippet=self.snippet1, user=self.user1)
        self.bookmark2 = Bookmark.objects.create(snippet=self.snippet2, user=self.user2)

    def test_bookmark_creation(self):
        # Test bookmark creation
        self.assertEqual(Bookmark.objects.count(), 2)

    def test_bookmark_str_method(self):
        # Test the __str__ method
        self.assertEqual(str(self.bookmark1), 'Test Snippet 1 bookmarked by testuser1')
        self.assertEqual(str(self.bookmark2), 'Test Snippet 2 bookmarked by testuser2')

    def test_bookmark_ordering(self):
        # Test ordering by user
        bookmarks = Bookmark.objects.all()
        self.assertEqual(bookmarks[0], self.bookmark2)  # user2 comes before user1 due to '-user' ordering
        self.assertEqual(bookmarks[1], self.bookmark1)

    def test_bookmark_related_name(self):
        # Test related_name for snippet
        self.assertEqual(self.snippet1.bookmarks.count(), 1)
        self.assertEqual(self.snippet2.bookmarks.count(), 1)

        # Test related_name for user
        self.assertEqual(self.user1.bookmarks.count(), 1)
        self.assertEqual(self.user2.bookmarks.count(), 1)

    def test_bookmark_snippet_interaction(self):
        # Test that Bookmark interacts properly with Snippet
        snippet_bookmarks = self.snippet1.bookmarks.all()
        self.assertIn(self.bookmark1, snippet_bookmarks)
        self.assertNotIn(self.bookmark2, snippet_bookmarks)

    def test_bookmark_user_interaction(self):
        # Test that Bookmark interacts properly with User
        user_bookmarks = self.user1.bookmarks.all()
        self.assertIn(self.bookmark1, user_bookmarks)
        self.assertNotIn(self.bookmark2, user_bookmarks)
