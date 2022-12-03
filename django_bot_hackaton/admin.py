from django.contrib import admin

from .forms import TeacherForm
from .models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'external_id', 'first_name',)
    form = TeacherForm
