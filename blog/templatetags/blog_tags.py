from django import template
from django.db.models.aggregates import Count
from django.db.models import Q
import datetime
from django.db.models import Sum

register = template.Library()

from blog.models import Post, Tag, Category, News


@register.simple_tag
def show_tags():
    return Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0).order_by("-num_posts")


@register.simple_tag
def tag_posts():
    num_post_list = []
    for each in Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0).order_by("-num_posts"):
        num_post_list.append(each.num_posts)
    return num_post_list


@register.simple_tag
def total_posts():
    return Post.objects.count()


@register.simple_tag
def show_most_viewed_posts(count=15):
    most_viewed_posts = Post.objects.order_by('-views')[:count]
    return most_viewed_posts


@register.simple_tag
def get_blogtime():
    d1 = datetime.date(2017, 6, 30)
    d2 = datetime.date(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day)
    return (d2 - d1).days


@register.simple_tag
def get_totalviews():
    return Post.objects.all().aggregate(Sum('views'))['views__sum']


@register.simple_tag
def days_noupdate():
    recent_date = datetime.date(Post.objects.order_by('-publish')[0].publish.year,
                                Post.objects.order_by('-publish')[0].publish.month,
                                Post.objects.order_by('-publish')[0].publish.day)
    days = (datetime.date(datetime.datetime.now().year,
                          datetime.datetime.now().month,
                          datetime.datetime.now().day) - recent_date).days
    return days


@register.simple_tag
def show_spark():
    spark = Post.objects.filter(tags__name="Spark")
    return spark


@register.simple_tag
def show_otherdatascience():
    hadoop = Post.objects.filter(tags__name="Hadoop")
    tensorflow = Post.objects.filter(tags__name="Tensorflow")
    database = Post.objects.filter(tags__name="Database")
    otherdatascience_list = {hadoop: "Hadoop", tensorflow: "Tensorflow", database: "Database"}

    return otherdatascience_list


@register.simple_tag
def show_java():
    java = Post.objects.filter(tags__name="Java")
    return java


@register.simple_tag
def show_otherprogramming():
    cpp = Post.objects.filter(tags__name="C++")
    python = Post.objects.filter(tags__name="Python")
    scala = Post.objects.filter(tags__name="Scala")
    otherprogramming_list = {cpp: "Cpp", python: "Python", scala: "Scala"}

    return otherprogramming_list


@register.simple_tag
def show_management():
    management = Post.objects.filter(tags__name="管理")
    return management


@register.simple_tag
def get_datascienceurl():
    return Category.objects.get(name="数据科学").get_absolute_url()


@register.simple_tag
def get_programmingurl():
    return Category.objects.get(name="算法编程").get_absolute_url()


@register.simple_tag
def get_talkurl():
    return Category.objects.get(name="杂谈").get_absolute_url()


@register.simple_tag
def news_list():
    return News.objects.all()


@register.simple_tag
def show_lastest_news():
    return News.objects.all().first()
