from django.contrib import admin
from .models import Faculty

# Register your models here.
@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('user',)