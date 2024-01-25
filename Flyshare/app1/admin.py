from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from app1.models import PostModel
# Register your models here.
admin.site.unregister(User)
class CustomUserAdmin(UserAdmin):
    # Define the fields to display in the User change list
    list_display = ('id','username', 'email', 'first_name', 'last_name', 'is_staff',)


class PostModelAdmin(admin.ModelAdmin):
    list_display = ('id','passenger_name', 'date_of_journey', 'gender', 'flight_number', 'pnr_number', 'source', 'destination', 'baggage_space', 'is_checked')
    
admin.site.register(PostModel,PostModelAdmin)
admin.site.register(User, CustomUserAdmin)
from django.contrib import admin
from .models import Room, Message
# # Register your models here.
admin.site.register(Room)
admin.site.register(Message)

