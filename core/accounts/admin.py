from django.contrib import admin
from .models import Profile , UserDocument , Mostanadat 
# Register your models here.


@admin.register(Mostanadat)
class Mostanadat_ADMIN(admin.ModelAdmin):
    list_display = ["name_document" , ] 
    

@admin.register(Profile)
class Profile_ADMIN(admin.ModelAdmin):
    list_display  = ['user','national_id','father_name','father_national_id']
    # search_fields = ['user','national_id','father_name','father_national_id'] 
    
    
@admin.register(UserDocument)
class UserDocument_ADMIN(admin.ModelAdmin):
    list_display = ['user','created_at','updated_at']
    