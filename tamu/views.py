from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
import xlwt
from tamu.models import Tamu

# Create your views here.
class PageView():
    def index(request):
        return render(request, 'pages/formpage.html')

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
        tamu.photo = request.POST.get('photo')
        tamu.save()
        messages.success(request, 'success added')
        return redirect(request, 'pages/success.html')

    def dashboard(request):
        tamu = Tamu.objects.all()
        return render(request, 'pages/dashboard.html', {'tamu': tamu})

    def update(request, pk):
        tamu = Tamu.objects.get(id = pk)
        return render(request,'pages/update.html',{'tamu':tamu})
        
    def edit(request,pk):
        tamu = Tamu.objects.get(id = pk)
        tamu.departure_time = request.POST.get('departure_time')
        tamu.save()
        messages.success(request, "Update Tamu success")
        return redirect('dashboard')    

    def delete(request, pk):
        tamu = Tamu.objects.get(id = pk)
        tamu.delete()
        messages.success(request, "Tamu Success Deleted")
        return redirect('dashboard')

    # export excel
    def export_tamu_xls(request):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="tamu.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Tamus')

        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['Id','Name', 'Origin of company', 'Assurance', 'Necessary', 'Appointment with', 'Arrival time', 'Departure time', 'Date', 'Photo']

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()

        rows = Tamu.objects.all().values_list('id','name', 'origin_of_company', 'assurance', 'necessary', 'appointment_with', 'arrival_time', 'departure_time', 'date', 'photo')
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)

        wb.save(response)
        return response