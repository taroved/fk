from django.shortcuts import get_object_or_404
from wsgiref.util import FileWrapper
from django.http import StreamingHttpResponse

from wagtail.wagtaildocs.models import Document, document_served


def document_serve(request, document_id, document_filename):
    doc = get_object_or_404(Document, id=document_id)
    wrapper = FileWrapper(doc.file)
    response = StreamingHttpResponse(wrapper, content_type='application/pdf')

    response['Content-Length'] = doc.file.size

    # Send document_served signal
    document_served.send(sender=doc, request=request)

    return response
