from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import Post


class LatestPostsFeed(Feed):
    title = 'Myoak'
    link = '/'
    description = 'New posts of my blog.'

    def items(self):
        return Post.objects.all()[:5]

    def item_title(self, item):
        return '[%s] %s' % (item.category, item.title)

    def item_description(self, item):
        return item.body
