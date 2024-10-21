from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from bagianVisitor.models import Contact
from .models import *
from .forms import *
from django.conf import settings
import os
from django.http import JsonResponse

def logPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if a user with the provided username exists
        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('loginPage')

        # Authenticate the user with the provided username and password
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            request.session['username'] = username    
            return redirect('homePageAdmin')
        else:
            messages.error(request, "Invalid Password")
            return redirect('loginPage')

    # Render the login page template (GET request)
    return render(request, 'admin/logpage.html')

def logout_page(request):
    logout(request)
    request.session.flush() 
    return redirect('loginPage')

def sess_login(request):
    if 'username' in request.session:
        return render(request, 'admin/home.html', {'username': request.session['username']})
    else:
        return redirect('loginPage')

@login_required(login_url='loginPage')
def home(request):
    return render(request, 'admin/home.html')

@login_required(login_url='loginPage')
def contactList(request):
    context = {}
    contactList = Contact.objects.all().order_by('-id')
    context['contactList'] = contactList
    return render(request, 'admin/contactList.html', context)

def deleteContact(request, slug):
    try:
        Contact.objects.get(slug=slug).delete()
    except:
        messages.error(request, 'Something went wrong')
        return redirect('contactListPage')

    return redirect('contactListPage')

@login_required(login_url='loginPage')
def postService(request):
    context = {}
    image_list = ImageServ.objects.all().order_by('-id')  
    context['image_list'] = image_list

    if request.method == 'GET':
        form = ImageForm()
        context['form'] = form
        return render(request, 'admin/service.html', context)  
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)  
        if form.is_valid():
            form.save()
            return redirect('postService')
        else:
            messages.error(request, 'Form is not valid. Please check the input fields.')
    else:
        form = ImageForm()
    return render(request, 'admin/service.html', context)

@login_required(login_url='loginPage')
def enable_image(request, pk):
    image = get_object_or_404(ImageServ, pk=pk)
    image.is_enabled = True
    image.save()
    return redirect('postService')

@login_required(login_url='loginPage')
def disable_image(request, pk):
    image = get_object_or_404(ImageServ, pk=pk)
    image.is_enabled = False
    image.save()
    return redirect('postService')

@login_required(login_url='loginPage')
def toggle_image_status(request, pk):
    if request.method == 'GET':
        image = get_object_or_404(ImageServ, pk=pk)
        is_enabled = request.GET.get('is_enabled') == 'true'
        image.is_enabled = is_enabled
        image.save()
        return JsonResponse({'status': image.is_enabled})
    else:
        return JsonResponse({'status': False, 'error': 'Invalid request method'})


@login_required(login_url='loginPage')
def delete_image(request, pk):
    image = get_object_or_404(ImageServ, pk=pk)
    image_path = image.image.path
    image.delete()
    if os.path.exists(image_path):
        os.remove(image_path)
    return redirect('postService')

@login_required(login_url='loginPage')
def create_post_view(request):
    if request.method == 'POST':
        length = request.POST.get('length')
        title = request.POST.get('title')
        description = request.POST.get('description')

        post = Post.objects.create(
            title=title,
            description=description
        )
        
        for file_num in range(0, int(length)):
            PostImage.objects.create(
                post=post,
                images=request.FILES.get(f'images{file_num}')
            )
        
        return JsonResponse({'message': 'The post has been created!'}, status=200)

    return render(request, 'admin/postUpdates.html')

@login_required(login_url='loginPage')
def listPost(request):
    context = {}
    posts = Post.objects.all().order_by('-id')
    context['posts'] = posts
    return render(request, 'admin/listPost.html', context)

def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    # Delete associated images
    images = PostImage.objects.filter(post=post)
    for image in images:
        if image.images:
            image_path = os.path.join(settings.MEDIA_ROOT, image.images.name)
            if os.path.exists(image_path):
                os.remove(image_path)
        image.delete()  # Delete the image record from database
    
    # Delete the post
    post.delete()
    
    messages.success(request, 'Post and associated images have been deleted.')
    return redirect('listPost')  # Redirect to the listPost view


@login_required(login_url='loginPage')
def postLogo(request):
    context = {}
    logo_list = LogoImg.objects.all().order_by('-id')  
    context['logo_list'] = logo_list

    if request.method == 'POST':
        form = LogoForm(request.POST, request.FILES)  
        if form.is_valid():
            form.save()
            messages.success(request, 'Logo has been added.')
            return redirect('postLogo')
        else:
            messages.error(request, 'Form is not valid. Please check the input fields.')
    else:
        form = LogoForm()
    
    context['form'] = form
    return render(request, 'admin/logo.html', context)

@login_required(login_url='loginPage')
def enable_logo(request, pk):
    image = get_object_or_404(LogoImg, pk=pk)
    image.is_enabled = True
    image.save()
    return redirect('postLogo')

@login_required(login_url='loginPage')
def disable_logo(request, pk):
    image = get_object_or_404(LogoImg, pk=pk)
    image.is_enabled = False
    image.save()
    return redirect('postLogo')

@login_required(login_url='loginPage')
def toggle_logo_status(request, pk):
    if request.method == 'GET':
        image = get_object_or_404(LogoImg, pk=pk)
        is_enabled = request.GET.get('is_enabled') == 'true'
        image.is_enabled = is_enabled
        image.save()
        return JsonResponse({'status': image.is_enabled})
    else:
        return JsonResponse({'status': False, 'error': 'Invalid request method'})

@login_required(login_url='loginPage')
def delete_logo(request, pk):
    image = get_object_or_404(LogoImg, pk=pk)
    image_path = image.image.path
    image.delete()
    if os.path.exists(image_path):
        os.remove(image_path)
    messages.success(request, 'Logo and associated images have been deleted.')
    return redirect('postLogo')