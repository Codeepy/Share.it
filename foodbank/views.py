import smtplib

from django.shortcuts import render
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Name *', max_length=50)
    email = forms.EmailField(label='Email *', max_length=50)
    message = forms.CharField(label='Message *', max_length=4000, widget=forms.Textarea)

def contact(request):
    if request.method == 'POST':
        from django.core.mail import send_mail
        print "POST ", request.POST
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            sender = form.cleaned_data['email']
            subject = "Contact Us Form"

            message = "From: " + name + " (" + sender + ")\n\n"
            message += form.cleaned_data['message']

            recipients = ['codeepy@gmail.com']

            result = "Your message has been delivered. Thank you for contacting SHARE.IT!!"
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

def home(request):
    return render(request, "home.html")

def api(request):
    return render(request, "api.html")
    
def donation(request):
    return render(request, "donation.html")

def login(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")

def map(request):
    return render(request, "map.html")
