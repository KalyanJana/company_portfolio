from django.shortcuts import render
from .models import ContactUs
from django.core.mail import send_mail

def all_contactus(request):
    contactuses=ContactUs.objects.all()
    return render(request, 'contactus/all_contacts.html', {'contactuses':contactuses})


def index(request):
    if request.method =='POST':
        name =request.POST.get('name')
        phone =request.POST.get('phone')
        email =request.POST.get('email')
        subject =request.POST.get('subject')
        message =request.POST.get('message')

        data ={
            'name':name,
            'phone':phone,
            'email':email,
            'subject':subject,
            'message':message,
        }
        message ='''
        Message From:{}
        subject:{}
        Message Details:{}
        From:{}
        Phone No:{}
        '''.format(data['name'],data['subject'],data['message'],data['email'], data['phone'])
        send_mail(data['subject'],message,'',['janakalyan01@gmail.com'])
        return render(request, 'contactus/all_contacts.html', {})
    return render(request, 'contactus/all_contacts.html', {})
