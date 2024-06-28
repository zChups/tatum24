from django.contrib.auth.models import User
from snippets.models import Language, Snippet  # Adjust the import according to your app name


def erase_db():
    print("Cancelling the DB")
    Language.objects.all().delete()
    Snippet.objects.all().delete()


def init_db():
    if Language.objects.exists() or Snippet.objects.exists():
        return

    languages = [
        {"name": "Python", "slug": "python", "language_code": "python"},
        {"name": "JavaScript", "slug": "javascript", "language_code": "javascript"},
        {"name": "HTML", "slug": "html", "language_code": "html"},
    ]

    snippets = [
        {"title": "Hello World in Python", "language": "Python", "author": "admin", "description": "Prints Hello World",
         "code": "print('Hello World')"},
        {"title": "Hello World in JavaScript", "language": "JavaScript", "author": "admin",
         "description": "Alerts Hello World", "code": "alert('Hello World');"},
        {"title": "Hello World in HTML", "language": "HTML", "author": "admin", "description": "Displays Hello World",
         "code": "<h1>Hello World</h1>"},
    ]

    for lang in languages:
        Language.objects.create(name=lang["name"], slug=lang["slug"], language_code=lang["language_code"])

    admin_user = User.objects.get(username='gim')  # Adjust this if needed

    for snip in snippets:
        lang = Language.objects.get(name=snip["language"])
        Snippet.objects.create(
            title=snip["title"],
            language=lang,
            author=admin_user,
            description=snip["description"],
            code=snip["code"]
        )

    print("DUMP DB")
    print(Language.objects.all())  # check
    print(Snippet.objects.all())
