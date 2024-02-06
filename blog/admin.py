from django.contrib import admin
from .models import Profile, Post
from django.contrib.auth.models import User


# Register your models here.

#admin.site.unregister(User)
#Register Post
admin.site.register(Post)

class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User 
    fields = ["username"]
    inlines = [ProfileInline]



#admin.site.register( UserAdmin)

admin.site.register(Profile)