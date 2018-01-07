from django.conf.urls import url

from blog import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='post_detail'),
    url(r'^tag/(?P<pk>[0-9]+)/$', views.TagView.as_view(), name='tag'),

    url(r'^tags/$', views.tags, name='tags'),
    url(r'^links/$', views.links, name='links'),
    url(r'^category/(?P<name>.*)/$', views.category_view, name='category'),
    url(r'^news/$', views.news_list, name='news'),
]

# url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
# url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesView.as_view(), name='archives'),

#url(r'^category/(?P<pk>[0-9]+)/$', views.category_view, name='category'),

#url(r'^category/(?P<pk>[0-9]+)/$', views.category_view, name='category'),