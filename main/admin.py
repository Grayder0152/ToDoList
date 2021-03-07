from django.contrib import admin
from .models import Task
from django.contrib.auth.models import User, Group


@admin.register(Task)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'task')
    list_display_links = ('title',)


admin.site.unregister(User)
admin.site.unregister(Group)
