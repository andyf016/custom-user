from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from userapp.models import CustomUser

# add custom fields to admin page
UserAdmin.fieldsets += ('Custom fields set', {'fields': ('display_name', 'homepage', 'age')}),

admin.site.register(CustomUser, UserAdmin)
