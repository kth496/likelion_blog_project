from django.contrib import admin
from .models import Blog

#블로그를 사이트 admin에 등록 
admin.site.register(Blog)

