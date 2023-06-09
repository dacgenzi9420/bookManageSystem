from django.contrib import admin
from .models import Books,Record

class BooksAdmin(admin.ModelAdmin):
    list_display = ['id','name','status']


class RecordAdmin(admin.ModelAdmin):
    list_display = ['id','name','sdate','s_time','s_time']

admin.site.register(Books,BooksAdmin)
admin.site.register(Record,RecordAdmin)
