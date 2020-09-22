from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from user.models import User
from mptt.models import MPTTModel,TreeForeignKey
class Comment(models.Model):

    article = models.ForeignKey('blog.Article', verbose_name='文章', on_delete=models.CASCADE)

    #评论者
    name = models.ForeignKey(User,related_name='comments',verbose_name='用户',on_delete=models.CASCADE)
    text = RichTextField('内容')
    creat_time = models.DateTimeField('创建时间', default=timezone.now)
    #记录某一条评论的开始
    root = models.ForeignKey('self',related_name='root_comment',verbose_name='评论对象',null=True,on_delete=models.DO_NOTHING)
    #评论根目录
    parent = models.ForeignKey('self',related_name='parent_comment',verbose_name='评论开头',null=True,on_delete=models.DO_NOTHING)
    #回复谁
    reply_to = models.ForeignKey(User,related_name='parent_comment',verbose_name='评论者',null=True,on_delete=models.DO_NOTHING)
    #回复内容

    class Mate:
        verbose_name = '评论'
        verbose_name_plural = verbose_name
        ordering = ['creat_time']

    def __str__(self):
        return '{}: {}'.format(self.name, self.text[:20])