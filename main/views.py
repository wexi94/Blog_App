from django.shortcuts import render , get_object_or_404
from django.contrib import messages
#from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic import ListView
from django.contrib.auth.models import User

class UserListView(ListView):
    model = User
    template_name = 'main/list.html'

def user_render_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    user = get_object_or_404(User, pk=pk)

    template_path = 'main/pdf2.html'
    context = {'user': user}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if we want to download the Report Automatically
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    #if you want to view the report in the browser
    response['Content-Disposition'] = ' filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response,)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def render_pdf_view(request):
    template_path = 'main/pdf1.html'
    context = {'myvar': 'this is your template context'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if we want to download the Report Automatically
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    #if you want to view the report in the browser
    response['Content-Disposition'] = ' filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response,)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
















def home(request):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    return render(request,'home.html')

# User Register
def register(request):
    form=SignupForm
    if request.method=='POST':
        regForm=SignupForm(request.POST)
        if regForm.is_valid():
            regForm.save()
            messages.success(request,'User has been registered.')
    return render(request,'registration/register.html',{'form':form})
