from django.contrib import admin

# Register your models here.

from share_it.models import VolunteerProfile, FoodBankProfile, Profile

admin.site.register(VolunteerProfile)
admin.site.register(FoodBankProfile)
admin.site.register(Profile)