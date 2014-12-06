import smtplib

from django.shortcuts import render
from django.http import HttpResponse

from django import forms
from django.db.models import Q, F

class ContactForm(forms.Form):
    name = forms.CharField(label='Name *', max_length=50)
    email = forms.EmailField(label='Email *', max_length=50)
    phone = forms.CharField(label='Phone', max_length=20, required=False)
    company = forms.CharField(label='Company Name', max_length=50, required=False)
    subject = forms.CharField(label='Subject *', max_length=100)
    message = forms.CharField(label='Message *', max_length=4000, widget=forms.Textarea)
    
def home(request):
    return render(request, "home.html")
    

def contact(request):
    if request.method == 'POST':
        from django.core.mail import send_mail
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            sender = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            company = form.cleaned_data['company']
            subject = form.cleaned_data['subject']

            message = "Name: " + name + "\n"
            message += "Phone: " + phone + "\n"
            message += "Company: " + company + "\n"
            message += "\nMessage:\n" + form.cleaned_data['message']

            recipients = ['vispox@hotmail.com']

            result = "Your message has been delivered. Thank you for contacting ViSpoX!!"
            try:
                send_mail(subject, message, sender, recipients)
            except smtplib.SMTPException:
                result = smtplib.SMTPException.message
            return render(request, "contact.html", {"result": result, "style": "display: block"})
        else:
            return render(request, "contact.html", {"result": "Failed to send the message. Please validate your data.",
                                                    "style": "display: block"})
    elif request.method == 'GET':
        return render(request, "contact.html", {"style": "display: none"})
        
def about(request):
    return render(request, "about.html")
    
def api(request):
    return render(request, "api.html")
    
def donation(request):
    return render(request, "donation.html")