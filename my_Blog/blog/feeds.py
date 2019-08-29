from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import Post


class LatestPostsFeed(Feed):
    title = 'my blog'
    link = '/blog/'
    description = 'New Posts of My Blog'

    def items(self):
        return Post.published.all()[:5]

    def item_title(self , item):
        return item.title

    def item_description(self , item):
        return truncatewords(item.body , 30)
