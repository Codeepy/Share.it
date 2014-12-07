
from Pubnub import Pubnub
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404, redirect

# Create your views here.
from django.template import RequestContext
from django.contrib.auth.models import User, Group
from share_it.forms import RegistrationForm, RegistrationForm2, RegistrationFormWithAddress, EditRegistrationForm
from share_it.models import VolunteerProfile, FoodBankProfile, Profile

pubnub = Pubnub(publish_key="pub-c-04ece9e5-b55d-4c71-b157-a43e178af836",
                subscribe_key="sub-c-9133d8cc-73eb-11e4-ad9d-02ee2ddab7fe",
                )


def _callback(message, channel):
    print(message)

def error(message):
    print(message)

def callback(message):
    print(message)

def publish(channel="foodbank_broadcast", message="test_message"):
    pubnub.publish(channel,message, callback=callback, error=error)

def subscribe(channel="foodbank_broadcast"):
    pubnub.subscribe(channel, callback=_callback, error=error)


def broadcast(request):
    if request.POST:
        message = request.POST['msg']
        print message
        publish("foodbank_broadcast",message)
        #subscribe()
    pubnub.here_now("foodbank_broadcast",callback=callback,error=error)
    context = RequestContext(request,
                           {'request': request,
                            'user': request.user})
    return render_to_response("account/publish.html", context_instance=context)

def notifications(request):
    context = RequestContext(request,
                           {'request': request,
                            'user': request.user})
    return render_to_response("account/subscribe.html", context_instance=context)


#Login
def login_user(request):
    logout(request)
    username = password = ''
    login_form = AuthenticationForm()
    if request.POST:
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            print 'valid'
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            #user = authenticate(username=username, password=password)
            #if user is not None:
            #    if user.is_active:
            login(request, login_form.get_user())
            return HttpResponseRedirect(request.POST.get('next', '/account/profile'))
        else:
            print 'invalid'
            print login_form.errors
            return render(request, 'account/login.html', {'form': login_form, 'error': 'true'})
    return render(request, "account/login.html", {"form": login_form, "next": request.GET.get('next')})

@login_required(login_url='/login/')
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')

def register_user(request):

    registration_form = RegistrationForm()
    if request.POST:
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            print 'valid'
            user = User.objects.create_user(username=registration_form.cleaned_data['username'],
                                            email=registration_form.cleaned_data['email'],
                                            password=registration_form.cleaned_data['password1'])
            user.save()
            group = Group.objects.get(name='Volunteer')
            user.groups.add(group)
            profile = VolunteerProfile.create(user=user,phone_number=registration_form.cleaned_data['phone_number'])
            profile.save()
            return HttpResponseRedirect('/')
        else:
            print 'invalid'
            print registration_form.errors
            return render(request, "account/register_user.html", {'form': registration_form, 'error': 'true'})

    return render(request, "account/register_user.html", {"form": registration_form})

def register_foodbank(request):
    print 'Get foodbank'
    registration_form = RegistrationForm2()
    if request.POST:
        registration_form = RegistrationForm2(request.POST)
        if registration_form.is_valid():
            print 'valid'
            user = User.objects.create_user(username=registration_form.cleaned_data['username'],
                                            email=registration_form.cleaned_data['email'],
                                            password=registration_form.cleaned_data['password1'])
            user.save()
            group = Group.objects.get(name='Food Bank')
            user.groups.add(group)
            profile = FoodBankProfile.create(user=user,phone_number=registration_form.cleaned_data['phone_number'],
                                             address_line1= registration_form.cleaned_data['address_line1'],
                                             city=registration_form.cleaned_data['city'],
                                            country=registration_form.cleaned_data['country'],
                                            post_code=registration_form.cleaned_data['post_code'],
                                            address_line2=registration_form.cleaned_data['address_line2'])
            profile.save()
            return HttpResponseRedirect('/')
        else:
            print 'invalid'
            print registration_form.errors
            return render(request, "account/register_foodbank.html", {'form': registration_form, 'error': 'true'})

    return render(request, "account/register_foodbank.html", {"form": registration_form})

def register(request):
    print 'register'
    registration_form = RegistrationFormWithAddress()
    if request.POST:
        registration_form = RegistrationFormWithAddress(request.POST)
        if registration_form.is_valid():
            print 'valid'
            user = User.objects.create_user(username=registration_form.cleaned_data['username'],
                                            email=registration_form.cleaned_data['email'],
                                            password=registration_form.cleaned_data['password1'],
                                            first_name=registration_form.cleaned_data['first_name'],
                                            last_name=registration_form.cleaned_data['last_name'])
            user.save()
            #group = Group.objects.get(name='Volunteer')
            group = registration_form.cleaned_data['user_group']
            user.groups.add(group)
            profile = Profile.create(user=user,phone_number=registration_form.cleaned_data['phone_number'],
                                             address_line1= registration_form.cleaned_data['address_line1'],
                                             city=registration_form.cleaned_data['city'],
                                            country=registration_form.cleaned_data['country'],
                                            post_code=registration_form.cleaned_data['post_code'],
                                            address_line2=registration_form.cleaned_data['address_line2'])
            profile.save()
            return HttpResponseRedirect('/')
        else:
            print 'invalid'
            print registration_form.errors
            return render(request, "account/register.html", {'form': registration_form, 'error': 'true'})

    return render(request, "account/register.html", {"form": registration_form})

@login_required
def profile(request):
    print 'member'
    if request.user.is_authenticated():
        user = request.user
        profile = get_object_or_404(Profile, user=user)
        print profile
        #check if std_profile exist!! it should.
    if request.POST:
        print 'POST'
        profile_form = EditRegistrationForm(request.POST)
        print profile_form
        #profile_form.fields['email'].widget.attrs['readonly'] = True
        if profile_form.is_valid():
            print 'Valid'
            #Not pythonic; There should be a better way to do this!! Read about ModelForms and Formsets
            user.first_name=profile_form.cleaned_data['first_name']
            user.last_name = profile_form.cleaned_data['last_name']
            user.save(update_fields=['first_name','last_name'])
            profile.phone_number = profile_form.cleaned_data['phone_number']
            profile.address_line1 = profile_form.cleaned_data['address_line1']
            profile.address_line2 = profile_form.cleaned_data['address_line2']
            profile.city = profile_form.cleaned_data['city']
            profile.country = profile_form.cleaned_data['country']
            profile.post_code = profile_form.cleaned_data['post_code']
            profile.save()#update_fields=['level_of_study','university','subject'])
            return redirect('profile')
        else:
            print profile_form.errors
            return render(request, 'account/profile.html', {'form': profile_form, 'error': 'true'})
    else:
        print 'GET'
        data = {'user_group': user.groups.all()[0], 'email': user.email, 'first_name': user.first_name, 'last_name': user.last_name, 'username': user.username,
                'phone_number': profile.phone_number, 'address_line1':profile.address_line1,
                'address_line2': profile.address_line2, 'city':profile.city,
                'country':profile.country, 'post_code':profile.post_code}
        print data
        profile_form = EditRegistrationForm(initial=data)
        #profile_form.fields['email'].widget.attrs['readonly'] = True
        return render(request, 'account/profile.html', {'form': profile_form})
