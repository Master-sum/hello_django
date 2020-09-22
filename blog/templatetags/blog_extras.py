from django import template
from ..models import Article,Category,Tag
from django.db.models.aggregates import Count
register = template.Library()

@register.inclusion_tag('blog/inclusions/_recent_articles.html', takes_context=True)
def show_recent_article(context, num=5):
    return {
        'recent_article_list': Article.objects.all().order_by('creat_time')[:num],
    }
@register.inclusion_tag('blog/inclusions/_archives.html', takes_context=True)
def show_archives(context):
    return {
        'date_list': Article.objects.dates('creat_time', 'month', order='DESC'),
    }
@register.inclusion_tag('blog/inclusions/_categories.html', takes_context=True)
def show_categories(context):
    category_list = Category.objects.annotate(num_articles = Count('article')).filter(num_articles__gt=0)
    return {
        'category_list':category_list,
    }
@register.inclusion_tag('blog/inclusions/_tags.html', takes_context=True)
def show_tags(context):
    tag_list = Tag.objects.annotate(num_articles = Count('article')).filter(num_articles__gt=0)
    return {
        'tag_list': tag_list
    }