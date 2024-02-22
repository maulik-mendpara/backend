from django.shortcuts import render
from .forms import appoinmentform
from django.core.mail import send_mail


# Create your views here.
def index(request):
    if request.method=='POST':
        newappoin=appoinmentform(request.POST)
        if newappoin.is_valid():
            newappoin.save()
            print("Your appoinment has been saved!")

            #Email Send
            sub="Thank you!"
            msg=f"Dear User\n\nYour appointment has been booked!\n\nWe will contact you shortly.\n\If you have any problem, contact us anytime.\n\nThank & Regards\nKlinik - Rajkot\n+91 9724799469 | emergency@klinik.com | www.klinik.com"
            from_id=""
            to_id=[""]
            to_id=[request.POST['email']]
            
            send_mail(subject=sub,message=msg,from_email=from_id,recipient_list=to_id)

        else:
            print(newappoin.errors)
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def appointment(request):
    return render(request,'appointment.html')

def contact(request):
    return render(request,'contact.html')

def feature(request):
    return render(request,'feature.html')

def service(request):
    return render(request,'service.html')

def team(request):
    return render(request,'team.html')

def testimonial(request):
    return render(request,'testimonial.html')

def errorpage(request):
    return render(request,'404.html')