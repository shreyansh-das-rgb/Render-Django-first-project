from django.contrib import admin
from .models import member

class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstName", "lastName", "joined_date",)
  
admin.site.register(member, MemberAdmin)