from django.contrib import admin
from .models import Company, SwitchIP, FollowUp
# Register your models here.

admin.site.register(Company)
admin.site.register(SwitchIP)
admin.site.register(FollowUp)