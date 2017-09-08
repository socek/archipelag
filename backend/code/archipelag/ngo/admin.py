from django.contrib.admin import StackedInline
from django.contrib.admin import site
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from archipelag.ngo.models import NgoUser


class NgoUserInline(StackedInline):
    model = NgoUser
    can_delete = False
    verbose_name_plural = 'ngo'


class UserAdmin(BaseUserAdmin):
    inlines = (NgoUserInline, )

site.unregister(User)
site.register(User, UserAdmin)
