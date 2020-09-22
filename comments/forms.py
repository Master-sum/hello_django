from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):

    reply_comment_id = forms.IntegerField(widget=forms.HiddenInput(attrs={'id':'reply_comment_id'}))
    print(1111111111111)
    print(reply_comment_id)
    def clean_reply_comment_id(self):
        reply_comment_id = self.cleaned_data['reply_comment_id']
        print(1111111111111)
        print(reply_comment_id)
        if reply_comment_id < 0:
            raise forms.ValidationError('回复出错11111111')
        elif reply_comment_id ==0:
            self.cleaned_data['parent']=None
        elif Comment.objects.filter(pk=reply_comment_id).exists():
            self.cleaned_data['parent'] = Comment.objects.get(pk=reply_comment_id)
        else:
            raise forms.ValidationError('回复出错')
        return reply_comment_id
    class Meta:
        model = Comment
        fields = ['text']
        exclude=['root','parent','reply_to']
