from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models

# Create your models here.

class VolunteerProfile(models.Model):
    user = models.OneToOneField(User)
    phone_regex = RegexValidator(regex=r'^\d{10}$', message="Phone number must be entered in the format: '999999'. Up to 10 digits allowed.")
    phone_number = models.CharField(max_length=10,validators=[phone_regex], blank=False) # validators should be a list
    address = models.CharField(max_length=250, blank=True)
    long_position   = models.DecimalField(max_digits=8, decimal_places=3, null=True, blank=True)
    lat_position   = models.DecimalField(max_digits=8, decimal_places=3,null=True, blank=True)

    def __unicode__(self):
        return self.user.username

    @classmethod
    def create(cls, user, phone_number, long_position=None, lat_position= None):
        new_profile = cls(user=user, phone_number=phone_number, long_position=long_position, lat_position= lat_position)
        return new_profile

class FoodBankProfile(models.Model):
    user = models.OneToOneField(User)
    phone_regex = RegexValidator(regex=r'^d{9,10}$', message="Phone number must be entered in the format: '999999'. Up to 10 digits allowed.")
    phone_number = models.CharField(max_length=10,validators=[phone_regex], blank=False) # validators should be a list
    address_line1 = models.CharField(max_length=250, blank=False)
    address_line2 = models.CharField(max_length=250, blank=True)
    city = models.CharField(max_length=250, blank=False)
    county = models.CharField(max_length=250, blank=False)
    post_code = models.CharField(max_length=8, blank=False)
    long_position   = models.DecimalField(max_digits=8, decimal_places=3, null=True, blank=True)
    lat_position   = models.DecimalField(max_digits=8, decimal_places=3, null=True, blank=True)

    def __unicode__(self):
        return self.user.username

    @classmethod
    def create(cls, user, phone_number, address_line1, city, county, post_code, address_line2='',
               long_position=None, lat_position= None):
        new_profile = cls(user=user, phone_number=phone_number, address_line1= address_line1, city=city,
                          county=county,post_code=post_code, address_line2=address_line2,
                          long_position=long_position, lat_position= lat_position)
        return new_profile

class Profile(models.Model):
    user = models.OneToOneField(User)
    phone_regex = RegexValidator(regex=r'^d{9,10}$', message="Phone number must be entered in the format: '999999'. Up to 10 digits allowed.")
    phone_number = models.CharField(max_length=10,validators=[phone_regex], blank=False) # validators should be a list
    address_line1 = models.CharField(max_length=250, blank=True)
    address_line2 = models.CharField(max_length=250, blank=True)
    city = models.CharField(max_length=250, blank=True)
    county = models.CharField(max_length=250, blank=True)
    post_code = models.CharField(max_length=8, blank=True)
    long_position   = models.DecimalField(max_digits=8, decimal_places=3, null=True, blank=True)
    lat_position   = models.DecimalField(max_digits=8, decimal_places=3, null=True, blank=True)

    def __unicode__(self):
        return self.user.username

    @classmethod
    def create(cls, user, phone_number, address_line1='', city='', county='', post_code='', address_line2='',
               long_position=None, lat_position=None):
        new_profile = cls(user=user, phone_number=phone_number, address_line1= address_line1, city=city,
                          county=county,post_code=post_code, address_line2=address_line2,
                          long_position=long_position, lat_position= lat_position)
        return new_profile
