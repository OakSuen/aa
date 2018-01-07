from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils.html import strip_tags
import markdown
from project_blog import settings


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'

    def get_absolute_url(self):
        return reverse('blog:category', kwargs={'name': self.name})

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()
    img_url = models.CharField(max_length=300, default="")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    publish = models.DateTimeField(default=timezone.now)
    excerpt = models.CharField(max_length=200, blank=True)
    views = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.pk})

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    # def getcomment_num(self):
    #     return self.comment_set.count()

    def save(self, *args, **kwargs):
        if not self.excerpt:
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            # 先将 Markdown 文本渲染成 HTML 文本
            # strip_tags 去掉 HTML 文本的全部 HTML 标签
            # 从文本摘取前 100 个字符赋给 excerpt
            self.excerpt = strip_tags(md.convert(self.body))[:160]
        # 调用父类的 save 方法将数据保存到数据库中
        super(Post, self).save(*args, **kwargs)


class News(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
