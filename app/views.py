from django.shortcuts import render
from blogs.models import Blog
from django.http import HttpResponse

# Create your views here.
def home(request):
    featured_posts = Blog.objects.filter(is_featured=True, status='Published').order_by('updated_at')
    posts = Blog.objects.filter(is_featured=False, status='Published')

    # Fetch about us
    try:
        # about = About.objects.get()
        about = None  # Placeholder for actual about us fetching logic
    except:
        about = None

    context = {
        'featured_posts': featured_posts,
        'posts': posts,
        'about': about,
    }

    return render(request, 'home.html', context)