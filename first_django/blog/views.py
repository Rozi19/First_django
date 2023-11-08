from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'title': 'Blog post 1',
        'author': 'Roza',
        'content': 'my first Blog',
        'posted_date': 'Nov 06 2023'
    },
    {
        'title': 'Blog post 2',
        'author': 'Mihret',
        'content': 'I am Mihret Tesema, I am so happy to be here',
        'posted_date': 'Nov 01 2023'
    }
]

def home(request):

    context = {
            'posts': posts
        }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
