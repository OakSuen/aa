"""project_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from blog.feeds import LatestPostsFeed
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap
from django.conf.urls.static import static
from django.conf import settings
import notifications.urls

sitemaps = {
    'posts': PostSitemap
}

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/', include('users.urls')),
    url(r'^users/', include('django.contrib.auth.urls')),
    url(r'', include('blog.urls')),
    url(r'^latest/rss/$', LatestPostsFeed(), name='rss'),
    url(r'^search/', include('haystack.urls')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'', include('ckeditor_uploader.urls')),
    url(r'', include('easy_comment.urls')),
    url(r'^notifications/', include(notifications.urls, namespace='notifications')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
