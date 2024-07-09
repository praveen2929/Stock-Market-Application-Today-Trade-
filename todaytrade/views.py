from django.shortcuts import render , redirect
from django.contrib import messages
import requests
from account.models import person
from account.models import notification
from course.models import course
from begineer.models import course as c1
from investor.models import course as c2
def is_login(request):
    userr =  request.session.get("email")
    print(userr)
    if userr:
        return True
    else:
        return False
def intraday(request): 
    is_data = is_login(request)
    if is_data:
        return render(request, 'intraday.html')
    else:
        return render(request, "login.html")



def home(request):
    return render(request, "index.html")
def contact(request):
    return render(request, "contact_us.html")

def about(request):
    return render(request, "about.html")
def course_registration(request):
    is_data = is_login(request)
    if is_data:
        return render(request, "course_register.html")
        
    else:
        return render(request, "login.html")
def courses(request):
    is_data = is_login(request)
    if is_data:
        return render(request, "courses.html")
    else:
        return render(request, "login.html")
def dii(request):
    is_data = is_login(request)
    if is_data:
        return render(request, "dii.html")
    else:
        return render(request, "login.html")
def explore(request):
    is_data = is_login(request)
    if is_data:
        return render(request, "explore.html")
    else:
        return render(request, "login.html")
def investor(request):
    is_data = is_login(request)
    if is_data:
        return render(request, "investor.html")
    else:
        return render(request, "login.html")
def IPO(request):
    is_data = is_login(request)
    if is_data:
        return render(request, "IPO.html")
    else:
        return render(request, "login.html")
def live_course(request):
    is_data = is_login(request)
    if is_data:
        return render(request, "live_course.html")
    else:
        return render(request, "login.html")
def login(request):
    if request.method=="POST":
        email = request.POST['email']
        password = request.POST['password']
        userr = person.objects.get(email=email)
        if userr:
            if userr.password == password:
                request.session["person_id"]= userr.id
                request.session["email"]= userr.email
                return redirect("/Dashboard")
            else:
                messages.info(request, "Invalid")
        else:
            messages.info(request, "Invalid")
    return render(request, "login.html")

def logout(request):
    request.session.clear()
    return redirect("/")
def MCX(request):
    is_data = is_login(request)
    if is_data:
        return render(request, "MCX.html")
    else:
        return render(request, "login.html")
def news(request):
    is_data = is_login(request)
    if is_data:
        return render(request, "news.html")
    else:
        return render(request, "login.html")
def premium_registration(request):
    is_data = is_login(request)
    if is_data:
        return render(request, "premium_registration.html")
    else:
        return render(request, "login.html")
def premium_services(request):
    is_data = is_login(request)
    if is_data:
        return render(request, "premium_services.html")
    else:
        return render(request, "login.html")
def sectors(request):
    is_data = is_login(request)
    if is_data:
        return render(request, "sectors.html")
    else:
        return render(request, "login.html")
def signup(request):
    if request.method=="POST":
        fname = request.POST['firstName']
        lname = request.POST['lastName']
        number = request.POST['Number']
        email = request.POST['Email']
        dob = request.POST['DOB']
        state = request.POST['State']
        city = request.POST['city']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password==cpassword:
            special = '~!@#$%^&*'
            if len(password) >=8:
                if person.objects.filter(email=email).exists():
                    
                    messages.info(request, "email already exist please login.")
                    return render(request, "signup.html")
                    
                else:
                    if person.objects.filter(number=number).exists():
                        messages.info(request, "number already exist.")
                        return render(request, "signup.html")
                        
                    else:
                        person.isactive=True
                        user = person.objects.create(fname=fname,lname=lname,number=number,email=email,date_of_birth=dob,State=state,city=city,password=password)
                        user.save()
                        print("user created")
                        return redirect('/signin')
            else:
                messages.info(request, "password must be of 8 character")
                return render(request, "signup.html")
             

        else:
            messages.info(request, "Please enter same password")
            return render(request, "signup.html")
    else:
        return render(request, "signup.html")
def stocks(request):
    is_data = is_login(request)
    if is_data:
        return render(request, "Stocks.html")
    else:
        return render(request, "login.html")
def trendingstock(request):
    is_data = is_login(request)
    if is_data:
        return render(request, "trendingstock.html")
    else:
        return render(request, "login.html")
def service(request):
    is_data = is_login(request)
    if is_data:
        return render(request, "service.html")
    else:
        return render(request, "login.html")
def trader(request,id):
    is_data = is_login(request)
    if is_data:
        return render(request, "trader.html")
    else:
        return render(request, "login.html")
    
def service(request):
    is_data = is_login(request)
    if is_data:
        return render(request, "service.html")
    else:
        return render(request, "login.html")
def traders(request,id):
   
    is_data = is_login(request)
    if is_data:
        d=course.objects.all()[:12]
        data = course.objects.get(id=id)
        return render(request, "traders.html",{'course': data,'courses':d})
    else:
        return render(request, "login.html")
def traders1_13(request,id):
   
    
    d=course.objects.all()[12:18]
    data = course.objects.get(id=id)
    return render(request, "traders1_13.html",{'course': data,'courses':d})
def traders1_16(request,id):
   
    
    d=course.objects.all()[18:33]
    data = course.objects.get(id=id)
    return render(request, "traders1_16.html",{'course': data,'courses':d})
def traders1_17(request,id):
   
    
    d=course.objects.all()[33:38]
    data = course.objects.get(id=id)
    return render(request, "traders1_17.html",{'course': data,'courses':d})
def traders1_18(request,id):
    d=course.objects.all()[38:45]
    data = course.objects.get(id=id)
    return render(request, "traders1_18.html",{'course': data,'courses':d})
def traders1_19(request,id):
   
    
    d=course.objects.all()[45:50]
    data = course.objects.get(id=id)
    return render(request, "traders1_19.html",{'course': data,'courses':d})
def traders1_20(request,id):
   
    
    d=course.objects.all()[50:53]
    data = course.objects.get(id=id)
    return render(request, "traders1_20.html",{'course': data,'courses':d})
def traders1_21(request,id):
   
    
    d=course.objects.all()[53:56]
    data = course.objects.get(id=id)
    return render(request, "traders1_21.html",{'course': data,'courses':d})
def traders1_22(request,id):
   
    
    d=c1.objects.all()[:9]
    data = c1.objects.get(id=id)
    return render(request, "traders1_22.html",{'course': data,'courses':d})
def traders1_23(request,id):
   
    
    d=c1.objects.all()[9:10]
    data = c1.objects.get(id=id)
    return render(request, "traders1_23.html",{'course': data,'courses':d})
def traders1_24(request,id):
   
    
    d=c1.objects.all()[10:11]
    data = c1.objects.get(id=id)
    return render(request, "traders1_24.html",{'course': data,'courses':d})
def traders1_25(request,id):
   
    
    d=c1.objects.all()[11:12]
    data = c1.objects.get(id=id)
    return render(request, "traders1_25.html",{'course': data,'courses':d})
def traders1_26(request,id):
   
    
    d=c1.objects.all()[12:14]
    data = c1.objects.get(id=id)
    return render(request, "traders1_26.html",{'course': data,'courses':d})
def traders1_27(request,id):
   
    
    d=c1.objects.all()[14:15]
    data = c1.objects.get(id=id)
    return render(request, "traders1_27.html",{'course': data,'courses':d})
def traders1_28(request,id):
   
    
    d=c1.objects.all()[15:20]
    data = c1.objects.get(id=id)
    return render(request, "traders1_28.html",{'course': data,'courses':d})
def traders1_29(request,id):
   
    
    d=c1.objects.all()[20:25]
    data = c1.objects.get(id=id)
    return render(request, "traders1_29.html",{'course': data,'courses':d})
def traders1_30(request,id):
   
    
    d=c1.objects.all()[25:26]
    data = c1.objects.get(id=id)
    return render(request, "traders1_30.html",{'course': data,'courses':d})
def traders1_31(request,id):
   
    
    d=c1.objects.all()[26:33]
    data = c1.objects.get(id=id)
    return render(request, "traders1_31.html",{'course': data,'courses':d})
def traders1_32(request,id):
   
    
    d=c2.objects.all()[:8]
    data = c2.objects.get(id=id)
    return render(request, "traders1_32.html",{'course': data,'courses':d})
def traders1_33(request,id):
   
    
    d=c2.objects.all()[8:9]
    data = c2.objects.get(id=id)
    return render(request, "traders1_33.html",{'course': data,'courses':d})
def traders1_34(request,id):
   
    
    d=c2.objects.all()[9:11]
    data = c2.objects.get(id=id)
    return render(request, "traders1_34.html",{'course': data,'courses':d})
def traders1_35(request,id):
   
    
    d=c2.objects.all()[11:13]
    data = c2.objects.get(id=id)
    return render(request, "traders1_35.html",{'course': data,'courses':d})
def traders1_36(request,id):
   
    
    d=c2.objects.all()[13:14]
    data = c2.objects.get(id=id)
    return render(request, "traders1_36.html",{'course': data,'courses':d})
def traders1_37(request,id):
   
    
    d=c2.objects.all()[14:15]
    data = c2.objects.get(id=id)
    return render(request, "traders1_37.html",{'course': data,'courses':d})
def traders1_38(request,id):
   
    
    d=c2.objects.all()[15:16]
    data = c2.objects.get(id=id)
    return render(request, "traders1_38.html",{'course': data,'courses':d})
def traders1_39(request,id):
   
    
    d=c2.objects.all()[16:17]
    data = c2.objects.get(id=id)
    return render(request, "traders1_39.html",{'course': data,'courses':d})

def Secret(request):
    person_id = request.session.get("person_id")
    person_data = person.objects.get(id=person_id)
    notify = notification.objects.all()
    
    p_data = {
        "i":person_data,
        "notification":notify
    }
    return render(request, "profile.html", p_data)
    
    
