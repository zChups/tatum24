from django.test import TestCase
from django.contrib.auth.models import User
from markdown import markdown
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from snippets.models import Language, Snippet


class SnippetModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='user', password='user')
        self.language = Language.objects.create(name='Python', slug='python', language_code='python')

    def test_save_method_with_markdown_and_highlight(self):
        """
        Test save method of Snippet model with markdown conversion and code highlighting.
        """
        original_description = 'This is a *test* snippet'
        snippet = Snippet.objects.create(
            title='Test Snippet',
            language=self.language,
            author=self.user,
            description=original_description,
            code='print("Hello, World!")'
        )

        # Check that description_html is correctly populated with markdown converted HTML
        self.assertEqual(snippet.description_html, markdown(original_description))

        # Check that highlighted_code is correctly populated with Pygments highlighted code
        expected_highlighted_code = highlight(snippet.code, snippet.language.get_lexer(), HtmlFormatter(linenos=True))
        self.assertEqual(snippet.highlighted_code, expected_highlighted_code)


# test_save_method_with_markdown_and_highlight: This test verifies the functionality
# of the save method in the Snippet model. It creates a Snippet instance
# with a markdown-formatted description and checks if description_html is
# correctly populated with the HTML converted from markdown. Additionally,
# it verifies that highlighted_code is correctly populated with Pygments-highlighted code.

# highlight is a pygments function



