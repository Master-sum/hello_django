from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
import markdown
from django.utils.html import strip_tags
#导入summernote
# from django_summernote.fields import SummernoteTextField
from ckeditor.fields import RichTextField
#文章分类
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

#文章标签
class Tag(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
#创建文章
class Article(models.Model):

    title = models.CharField('标题',max_length=60)
    content = RichTextField('内容')
    creat_time = models.DateTimeField('创建时间',default=timezone.now)
    late_time = models.DateTimeField('更新时间',default=timezone.now)

    #文章摘要
    excerpt = models.CharField('摘要',max_length=200,blank=True)
    #外键是分类
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='分类')
    #标签与文章是多对多的关系
    tags = models.ManyToManyField(Tag,blank=True,verbose_name='标签')
    #作者
    author = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='作者')
    #阅读量
    view_num = models.PositiveIntegerField(default=0)

    #每次访问增加1
    def increase_view_num(self):
        self.view_num +=1
        self.save(update_fields=['view_num'])

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['creat_time']
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.creat_time = timezone.now()
        md = markdown.Markdown(extensions=
        [
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ])
        self.late_time = timezone.now()
        self.excerpt = strip_tags(md.convert(self.content))[:100]
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk':self.pk})