from django.shortcuts import render
from .models import User,Car
# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def signupform(request):
    return render(request,'signup.html')
def signup(request):
    username=request.POST['username']
    useremail = request.POST['useremail']
    userpassword = request.POST['userpassword']
    usermobile = request.POST['usermobile']
    u=User.objects.filter(user_email=useremail)
    if(u.count()==1):
        return render(request, 'signup.html', {'msg': 'Email Id Already Exist..'})
    else:
        u=User(user_name=username,user_email=useremail,user_password=userpassword,user_mobile=usermobile)
        res=u.save()
        return render(request,'signup.html',{'success':'Signup Done..'})
def login(request):
    useremail = request.POST['loginname']
    userpassword = request.POST['loginpassword']
    usertype=request.POST['logintype']
    if(usertype=='admin'):
        if(useremail=='admin@admin.com' and userpassword=='admin'):
            return render(request,'welcome_admin.html')
        else:
            return render(request,'index.html',{'msg':'Invalid Email Id or Password'})
    else:
        u=User.objects.filter(user_email=useremail,user_password=userpassword)
        if(u.count()==1):
            request.session['user_name']=u[0].user_name
            request.session['user_email']=u[0].user_email
            request.session['user_password']=u[0].user_password
            request.session['user_mobile']=u[0].user_mobile
            
            return render(request,'welcome_user.html')
        else:
            return render(request, 'index.html', {'msg': 'Invalid Email Id or Password'})



























def lostpwd(request):
    return render(request,'lostpwd.html')
def getpassword(request):
    useremail = request.POST['email']
    u = User.objects.filter(user_email=useremail)
    if(u.count()==1):
        return render(request,'lostpwd.html',{'msg':u})
    else:
        return render(request, 'lostpwd.html',{'msg1':'Invalid Email Id'})
def updateuserdetails(request):
    return render(request,'update_user_details.html')
def update_user_db(request):
    username=request.POST['username']
    userpassword = request.POST['userpassword']
    usermobile = request.POST['usermobile']
    useremail = request.POST['useremail']
    u=User.objects.get(user_email=useremail)
    u.user_name=username
    u.user_password=userpassword
    u.user_mobile=usermobile
    u.save()
    request.session['user_name']=username
    request.session['user_password']=userpassword
    request.session['user_mobile']=usermobile
    return render(request,'update_user_details.html',{'msg':'Record Updated'})
def back_user(request):
    return render(request,'welcome_user.html')
def registercar(request):
    return render(request,'register_car.html')
def register_car_db(request):
    carnumber=request.POST['CarNumber']
    carmodel = request.POST['Model']
    carseats = request.POST['Seats']
    carsource = request.POST['Source']
    carsource=carsource.lower()
    cardest = request.POST['Destination']
    cardest=cardest.lower()
    cardept = request.POST['DepartureTime']
    carretn = request.POST['ReturnTime']
    useremail=request.session['user_email']
    car=Car.objects.filter(car_number=carnumber)
    if(car.count()==1):
        return render(request, 'register_car.html', {'msg': 'This Car Already Exist..'})
    else:
        car=Car(car_number=carnumber,user_email=useremail,car_model=carmodel,car_seats=carseats,car_source=carsource,car_destination=cardest,car_depttime=cardept,car_retntime=carretn)
        car.save()
        request.session['car_number']=carnumber
        request.session['car_model']=carmodel
        request.session['car_seats']=carseats
        request.session['car_source']=carsource
        request.session['car_dest']=cardest
        request.session['car_dept']=cardept
        request.session['car_rettime']=carretn
        return render(request,'register_car.html',{'success':'Car Registered..'})
        	
def update_car_details(request):
    return render(request,'update_car.html')	
def update_car_db(request):
    carnumber=request.POST['CarNumber']
    carmodel = request.POST['Model']
    carseats = request.POST['Seats']
    carsource = request.POST['Source']
    cardest = request.POST['Destination']
    cardept = request.POST['DepartureTime']
    carretn = request.POST['ReturnTime']
    useremail=request.session['user_email']
    car=Car.objects.get(car_number=carnumber)
    car.car_number=carnumber
    car.car_model=carmodel
    car.car_seats=carseats
    car.car_source=carsource
    car.car_destination=cardest
    car.car_depttime=cardept
    car.car_retntime=carretn
    car.save()
    request.session['car_number']=carnumber
    request.session['car_model']=carmodel
    request.session['car_seats']=carseats
    request.session['car_source']=carsource
    request.session['car_dest']=cardest
    request.session['car_dept']=cardept
    request.session['car_rettime']=carretn
    return render(request,'update_car.html',{'success':'Car Updated..'})
def deleteaccount(request):
    useremail = request.session['user_email']
    u = User.objects.get(user_email=useremail)
    u.delete()
    return render(request,'delete_feedback.html')
def search(request):
    src = request.POST['src']
    dst = request.POST['dst']
    src=src.lower()
    dst=dst.lower()
    cars=Car.objects.filter(car_source=src,car_destination=dst)
    return render(request,'search.html',{'cars':cars})