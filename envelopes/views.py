from django.shortcuts import render
from django.utils import timezone
from .models import Main
from .forms import MainForm
from . import forms # new
from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from io import BytesIO
from xhtml2pdf import pisa

# Create your views here.
def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("utf-16")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse("Error in render_to_pdf function (views.py)")

# Opens up page as PDF
class ViewPDF(View):
    def get(self, request, *args, **kwargs):

        # set variables from dict sent in POST by pressing button
        data = {
            "viewsSenderTitle": request.GET['senderTitle'],
            "viewsSenderName": request.GET['senderName'].upper(),
            "viewsSenderAddress": request.GET['senderAddress'],
            "viewsSenderCity": request.GET['senderCity'].upper(),
            "viewsSenderProvince": request.GET['senderProvince'],
            "viewsSenderCountry": request.GET['senderCountry'],
            "viewsSenderZip": request.GET['senderZip'],

            "viewsReceiverTitle": request.GET['receiverTitle'],
            "viewsReceiverName": request.GET['receiverName'].upper(),
            "viewsReceiverAddress": request.GET['receiverAddress'],
            "viewsReceiverCity": request.GET['receiverCity'].upper(),
            "viewsReceiverProvince": request.GET['receiverProvince'],
            "viewsReceiverCountry": request.GET['receiverCountry'],
            "viewsReceiverZip": request.GET['receiverZip'],

            # set additional variables like printer assignment and time
            "viewsRequestDate": timezone.now().strftime('%Y-%m-%d, %H:%M:%S'),
        }

        pdf = render_to_pdf('envelopes/output.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

# Automatically downloads to PDF file
class DownloadPDF(View):
    def get(self, request, *args, **kwargs):

        pdf = render_to_pdf('envelopes/output.html', data)

        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Rendered_%s.pdf" %("12341231")
        content = "attachment; filename='%s'" %(filename)
        response['Content-Disposition'] = content
        return response

def base(request):
    form = MainForm()
    return render(request, 'envelopes/base.html', {'form': form})
