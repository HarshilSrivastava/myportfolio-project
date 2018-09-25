from django.shortcuts import render,get_object_or_404
from .models import Blog

# Create your views here.
def home(request):
    return render(request, 'blog/home.html')
def allblogs(request):
    blogs = Blog.objects.order_by('-pub_date')
    return render(request, 'blog/allblogs.html',{'blogs':blogs})
def detail(request,blog_id):
    detailblog =get_object_or_404(Blog,pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':detailblog})
