from django.shortcuts import render, redirect
from .models import *
from .forms import *
from apps.homepage.models import *

def  blog(request):
    blogs = Blogs.objects.all()
    category = Category.objects.all()
    recents = Blogs.objects.all().order_by('-id')[:3]
    images = Images.objects.all()[:3]
    images2 = Images.objects.all().order_by('-id')[:3]
    settings = Settings.objects.latest('id')
    if request.method == 'POST':
        query = request.POST.get('news search')
        blogs = Blogs.objects.filter(title__contains=query)
        
    context = {
        'blogs': blogs, 
        'category': category,
        'settings': settings,
        'recents': recents,
        'images': images,
        'images2': images2,
        'home': 'Главная',
        'next': 'Новости',
    }
    return render(request, 'blog/blog-grid.html', context)

def single_blog(request, slug):
    blog = Blogs.objects.get(slug=slug)
    blog.count += 1
    blog.save()
    category = Category.objects.all()
    settings = Settings.objects.latest('id')
    recents = Blogs.objects.all().order_by('-id')[:3]
    images = Images.objects.all()[:3]
    images2 = Images.objects.all().order_by('-id')[:3]
    comments = Commenst.objects.filter(news=blog)
    form = NewsForm(request.POST, instance=blog)
    if request.method == 'POST':
        form = NewsForm(request.POST, instance=blog)
        if form.is_valid():
            name1 = form.cleaned_data['name']
            comment1 = form.cleaned_data['comment']

            c = Commenst(news=blog, name=name1, comment=comment1)
            c.save()

        return redirect('blog_detail', slug=slug)
    else:
        form = NewsForm()

    context = {
        'blog': blog, 
        'category': category,
        'settings': settings,
        'recents': recents,
        'images': images,
        'images2': images2,
        'home': 'Главная',
        'next': 'Новости',
        'form':form,
        'comments': comments
    }
    return render(request, 'blog/blog-details.html', context)

def categy(request, slug):
    categor = Category.objects.get(slug = slug)
    category = Category.objects.all()
    blogs = Blogs.objects.filter(category = categor)
    recents = Blogs.objects.all().order_by('-id')[:3] 
    images = Images.objects.all()[:3] 
    settings = Settings.objects.latest('id')
    context = {
        'blogs': blogs,
        'recents': recents,
        'images': images,
        'settings': settings,
        'category': category,
        'home': 'Главная',
        'next': 'Новости',
    }
    return render(request, 'blog/blog-grid.html', context)

