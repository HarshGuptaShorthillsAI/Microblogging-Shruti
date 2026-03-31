from django.shortcuts import render,redirect
from .models import Blog
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    blogs = Blog.objects.all()
    return render(request, 'micro/blogs.html', {'blogs': blogs})


@login_required
def new_blog(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        text = request.POST.get('blog')
        Blog.objects.create(
            user = request.user,
            image = image,
            text = text
        )
        return redirect("home")
    return render(request, "micro/new_blog.html")

@login_required
def update_blog(request,id):
    blog = Blog.objects.get(id=id)
    if request.user == blog.user:
        if request.method == 'POST':
            image = request.FILES.get('image')
            text = request.POST.get('blog')
            if image:
                blog.image = image
            blog.text = text
            blog.save()
            return redirect('home')
        else:
            return redirect('home')
    return redirect('home')
    # return render(request,"micro/update_blog.html",{"blog":blog})


@login_required
def delete_blog(request,id):
    blog = Blog.objects.filter(id=id).first()
    if request.user == blog.user:
        blog.delete()
        return redirect('home')   