from django.shortcuts import render,get_object_or_404
from .models import Blog


def home(request):
    blogs=Blog.objects  #Query set (여러개)
    return render(request, 'home.html', {'blogs':blogs})

def detail(request,blog_id):
    details=get_object_or_404(Blog, pk=blog_id) #id값을 갖는 Blog 클래스를 가져오거나 못가져오면 404 에러를 나타내라 (쿼리셋이아닌 객체 한개)
    return render(request,'detail.html',{'detail':details})

