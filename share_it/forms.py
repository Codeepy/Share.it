from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User, Group

__author__ = 'Abdu'

#class LoginForm(AuthenticationForm):

class RegistrationForm(forms.Form):
    """
    Form for registering a new user account.
    Validates that the requested username and email are not already in use, and
    requires the password to be entered twice.
    """
    required_css_class = 'required'

    username = forms.RegexField(regex=r'^[\w.@+-]+$',
                                max_length=30,
                                label="Username",
                                error_messages={'invalid':"This value may contain only letters, numbers and @/./+/-/_ characters."})
    email = forms.EmailField(label="E-mail")
    password1 = forms.CharField(widget=forms.PasswordInput,
                                label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput,
                                label="Password (again)")
    phone_number = forms.RegexField(regex=r'^\d{10}$',
                                error_message = ("Phone number must be entered 10 digits in the format: '999999'."))

    def clean_username(self):
        """
        Validate that the username is alphanumeric and is not already
        in use.

        """
        existing = User.objects.filter(username__iexact=self.cleaned_data['username'])
        if existing.exists():
            raise forms.ValidationError("A user with that username already exists.")
        else:
            return self.cleaned_data['username']

    def clean_email(self):
        """
        Validate that the supplied email address is unique for the
        site.

        """
        if User.objects.filter(email__iexact=self.cleaned_data['email']):
            raise forms.ValidationError("This email address is already in use. Please supply a different email address.")
        return self.cleaned_data['email']

    def clean(self):
        """
        Verifiy that the values entered into the two password fields
        match. Note that an error here will end up in
        ``non_field_errors()`` because it doesn't apply to a single
        field.

        """
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError("The two password fields didn't match.")
        return self.cleaned_data


class RegistrationForm2(RegistrationForm):
    address_line1 = forms.CharField(label="Address Line1")
    address_line2 = forms.CharField(label="Address Line2", required=False)
    city = forms.CharField(label="City")
    country = forms.CharField(label="Country")
    post_code = forms.CharField(label="Postcode")

class RegistrationForm3(RegistrationForm):
    user_group = forms.ModelChoiceField(queryset=Group.objects.all())
    address_line1 = forms.CharField(label="Address Line1", required=False)
    address_line2 = forms.CharField(label="Address Line2", required=False)
    city = forms.CharField(label="City", required=False)
    country = forms.CharField(label="Country", required=False)
    post_code = forms.CharField(label="Postcode", required=False)

    def clean(self):
        cleaned_data = super(RegistrationForm3, self).clean()
        cleaned_sub_data = self.cleaned_data
        cleaned_data.update(cleaned_sub_data)
        user_group = cleaned_data.get("user_group")
        subject = cleaned_data.get("subject")
        print user_group
        print cleaned_data
        if user_group == Group.objects.get(name='Food Bank'):
            # Only do something if both fields are valid so far.
            print 'yep'
            print cleaned_data.get("address_line1", None)
            if cleaned_data.get("address_line1", None) and  cleaned_data.get("city", None) \
            and cleaned_data.get("country", None) and  cleaned_data.get("post_code", None):
                print 'oo'
                return self.cleaned_data
            else:
                raise forms.ValidationError("You need to provide an address for a Food Bank user group!.")

