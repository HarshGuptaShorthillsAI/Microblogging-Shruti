from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author':'Destiny Franks',
        'title':'Blog Post 1',
        'content':'This is the content of the first blog post.',
        'date_posted':'August 27, 2024'
    },
    {
        'author':'Jane Doe',
        'title':'Blog Post 2',
        'content':'This is the content of the second blog post.',
        'date_posted':'August 28, 2024'
    }
]


# Create your views here.
def home(request):
    context = {
        'posts':posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html')
