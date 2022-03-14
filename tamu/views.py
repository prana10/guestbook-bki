from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
import xlwt
from tamu.models import DataList, Tamu, Assurance

# Create your views here.
class PageView():
    def index(request):
        datalist = DataList.objects.all()
        assurancelist = Assurance.objects.all()
        return render(request, 'pages/formpage.html', {
            'datalist': datalist,
            'assurancelist': assurancelist
        })

    def upload(request):
        tamu = Tamu()
        tamu.name = request.POST.get('name')
        tamu.origin_of_company = request.POST.get('origin_of_company')
        tamu.assurance = request.POST.get('assurance')
        tamu.necessary = request.POST.get('necessary')
        tamu.appointment_with = request.POST.get('appointment_with')
        tamu.arrival_time = request.POST.get('arrival_time')
        tamu.departure_time = request.POST.get('departure_time')
        tamu.date = request.POST.get('date')
        tamu.photo = request.FILES.get('photo')
        tamu.save()
        return redirect('success')

    def success(request):
        return render(request, 'pages/success.html', {'data_success': 'successfully submited'})