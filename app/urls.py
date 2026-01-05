from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from blogs import views as BlogsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('category/', include('blogs.urls')),
     path('blogs/<slug:slug>/', BlogsView.blogs, name='blogs'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
