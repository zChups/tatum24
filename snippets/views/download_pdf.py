from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from snippets.models import Snippet


@login_required
def download_pdf_view(request, snippet_id):
    snippet = get_object_or_404(Snippet, pk=snippet_id)
    snippet.highlighted_code = highlight(snippet.code, snippet.language.get_lexer(), HtmlFormatter(linenos=False))
    html = render_to_string('snippets/snippet_pdf.html', {'snippet': snippet})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{snippet.title}.pdf"'
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse(f'We had some errors with code {pisa_status.err}')
    return response
