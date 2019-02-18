from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from api.models.user import *
from api.models.genre import *
from api.models.color import Color
from api.models.size import Size
from api.models.sex import Sex
from api.models.work import Work
from api.models.image import Image
from api.models.message import Message


admin.site.register(Genre)
admin.site.register(SubGenre)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Sex)
admin.site.register(Work)
admin.site.register(Image)
admin.site.register(Message)
admin.site.register(UserDetail)


class MyUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)


class MyUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('email',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    form = MyUserChangeForm
    add_form = MyUserCreationForm
    list_display = ('email', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(User, MyUserAdmin)
