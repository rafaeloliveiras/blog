from django.shortcuts import render, render_to_response, get_object_or_404


# Create your views here.

def PostList(request):
    return render(request, 'blog/post_list.html')

def PostUnique(request):
    return render(request, 'blog/post_unique.html')

def CategoryList(request):
    return render(request, 'blog/blog_categories.html')