from django.db import models
from user.models import User
# Create your models here.
#文章点赞数量
class LikeCount(models.Model):
    #点赞文章
    article = models.ForeignKey('blog.Article', verbose_name='文章', on_delete=models.CASCADE)
    # # 点赞者
    # name = models.ForeignKey(User, related_name='comments', verbose_name='用户', on_delete=models.CASCADE)
    #点赞数量
    like_num= models.IntegerField(default=0)
#人员点赞文章
class LikeRecord(models.Model):
    # 点赞文章
    article = models.ForeignKey('blog.Article', verbose_name='文章', on_delete=models.CASCADE)
    # 点赞者
    name = models.ForeignKey(User, related_name='like_uesr', verbose_name='用户', on_delete=models.CASCADE)
    #点赞日期
    like_time = models.DateTimeField(auto_now_add=True)