from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from bagianVisitor.forms import contactForm
from .models import Contact
from logAuth.models import ImageServ,PostImage, Post
from django.shortcuts import render
from logAuth.models import LogoImg

def index(request):
    image_list = ImageServ.objects.filter(is_enabled=True)
    logo_list = LogoImg.objects.filter(is_enabled=True)
    context = {'imageList': image_list, 'logoList': logo_list}
    return render(request, 'visit/index.html', context)

def contact(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for reaching out! we will contact you soon.')
            return redirect('contactPage')  
    else:
        form = contactForm()
    return render(request, 'visit/contact.html', {'form': form})

def update(request):
    posts = Post.objects.all().order_by('-id')
    for post in posts:
        post.images = PostImage.objects.filter(post=post)
    return render(request, 'visit/updates.html', {'posts': posts})
    
def payment(request):
    return render(request, 'visit/payment.html')

def service(request):
    return render(request, 'visit/service.html')

