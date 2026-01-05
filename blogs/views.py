from django.shortcuts import render
from blogs.models import Blog
from blogs.models import Category
from django.shortcuts import get_object_or_404

# Create your views here.
def posts_by_category(request, category_id):
    posts = Blog.objects.filter(status='Published', category=category_id)
    category = get_object_or_404(Category, pk=category_id)

    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'posts_by_category.html', context)