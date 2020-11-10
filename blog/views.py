from django.shortcuts import render
# from django.http import HttpResponse



# Create your views here.
def posts_list(request):
    name = ['nazi', 'era', 'abai']
    return render(request, 'blog/index.html', locals())