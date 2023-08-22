from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required

@login_required
def protected_view(request):
    return render(request, 'form.html')



def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def department(request):
    return render(request, 'department.html')

def hospital(request):
    return render(request, 'hospital.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been successfully logged in.')
            return redirect('dashboard')  
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
    return render(request, 'form.html')

def logout_view(request):
    logout(request,)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('login') 

def make_appointment(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        date = request.POST['date']
        time = request.POST['time']
        department = request.POST['department']
        phone = request.POST['phone']
        message = request.POST['message']

        appointment = Appointment(
            name=name,
            email=email,
            date=date,
            time=time,
            department=department,
            phone=phone,
            message=message
        )
        appointment.save()

        # Redirect to a success page or any other page you want
        return redirect('dashboard')
    return render(request, 'appoint.html')

def appointment_list(request):
    appointments = Appointment.objects.all()
    context = {'appointments': appointments}
    return render(request, 'dashboard.html', context)


#  def ImgeHandlers(request):
#     img = ImageHandler.objects.all()
#     return render(request,'hospital.html',{'img':img})

