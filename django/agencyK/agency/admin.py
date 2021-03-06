from django.contrib import admin
from .models import Shopping,Excursion,Relaxation,Tour
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

'''
    change the view for user information on admin site
'''
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

admin.site.register(Shopping)
admin.site.register(Excursion)
admin.site.register(Relaxation)
admin.site.register(Tour)