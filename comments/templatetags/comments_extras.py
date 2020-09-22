from django import template
from ..forms import CommentForm

register = template.Library()


@register.inclusion_tag('comments/inclusions/_form.html', takes_context=True)
def show_comment_form(context, article, form=None):
    print(form)
    if form is None:
        form = CommentForm()
    return {
        'form': form,
        'article': article,
        'reply_comment_id': 0,
    }
@register.inclusion_tag('comments/inclusions/_list.html', takes_context=True)
def show_comments(context, article):
    comment_list = article.comment_set.filter(parent=None).order_by('-creat_time')
    comment_count = comment_list.count()
    return {
        'comment_count': comment_count,
        'comment_list': comment_list,
    }