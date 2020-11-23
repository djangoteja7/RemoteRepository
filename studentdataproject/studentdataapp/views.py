from django.shortcuts import render,redirect
from .models import StudentData
# Create your views here.
def student_data_insert(request):
    if request.method == "POST":
        name1 = request.POST.get('name')
        email1 = request.POST.get('email')
        mobile1 = request.POST.get('mobile')
        company1 = request.POST.get('company')
        salary1 = request.POST.get('salary')
        location1 = request.POST.get('location')
        data = StudentData(
            name=name1,
            email=email1,
            mobile=mobile1,
            company=company1,
            salary=salary1,
            location=location1
        )
        data.save()
        student=StudentData.objects.all()
        return render(request,'student_data_insert.html',{'student':student})
    else:
        student = StudentData.objects.all()
        return render(request, 'student_data_insert.html', {'student': student})

def student_data_update(request,id):
    student = StudentData.objects.get(id=id)
    return render(request, 'student_data_update.html', {'student': student})

def updated_data_save(request,id):
    student = StudentData.objects.get(id=id)
    student.name = request.POST.get('name')
    student.email = request.POST.get('email')
    student.mobile = request.POST.get('mobile')
    student.company = request.POST.get('company')
    student.salary = request.POST.get('salary')
    student.location = request.POST.get('location')
    student.save()
    return redirect('/')

def delete_data(request,id):
    student = StudentData.objects.get(id=id)
    if request.method=="POST":
        student.delete()
        return redirect('/')
    return render(request,'student_data_delete.html')




