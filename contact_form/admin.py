from django.contrib import admin

# Register your models here.
from .models import UserData


class UserDataModelAdmin(admin.ModelAdmin):
	list_display=["__unicode__","name","surname","choice","email","message"]
	class Meta:
		model=UserData


admin.site.register(UserData, UserDataModelAdmin)