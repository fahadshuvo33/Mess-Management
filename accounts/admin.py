from django.contrib import admin

from accounts.models import *
# Register your models here.

admin.site.register(Mess_Admin)
admin.site.register(Mess)
admin.site.register(CustomUser)

