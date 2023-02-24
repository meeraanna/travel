from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        USERNAME=request.POST['username']
        PASSWORD = request.POST['password']
        USER=auth.authenticate(username=USERNAME,password=PASSWORD)

        if USER is not None:
            auth.login(request,USER)
            return redirect('/')
        else:
            messages.info(request,'invalid')
            return redirect('login')
    return render(request,'login.html')

def register(request):

    if request.method =='POST':
        USERNAME=request.POST['Username']
        FIRSTNAME=request.POST['First name']
        LASTNAME = request.POST['Last name']
        EMAIL=request.POST['Email']
        PASSWORD=request.POST['Password']
        CONFIRMPASSWORD = request.POST['Confirm password']

        if PASSWORD == CONFIRMPASSWORD:

            if User.objects.filter(username=USERNAME).exists():
                messages.info(request,'username already exist')
                return redirect('register')
            elif User.objects.filter(email=EMAIL).exists():
                messages.info(request,'email already exist')
                return redirect('register')
            else:
                user=User.objects.create_user(username=USERNAME,password=PASSWORD,
                                      first_name=FIRSTNAME,last_name=LASTNAME,
                                      email=EMAIL)

                user.save()
                print('user created')
                messages.info(request,'user created')
                return redirect('login')
        #
        else:
            messages.info(request,'password not matching')
            return redirect('register')

        return redirect('/')

    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')