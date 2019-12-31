from django.contrib import admin

from .models import College

class CollegeAdmin(admin.ModelAdmin):
    list_display = ("name","faculty","batch","image")


admin.site.register(College, CollegeAdmin)
