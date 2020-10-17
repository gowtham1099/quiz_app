from django.contrib import admin
from .models import Programming, Maths, Result, Science

# Register your models here.

admin.site.register(Programming)
admin.site.register(Maths)
admin.site.register(Result)
admin.site.register(Science)
