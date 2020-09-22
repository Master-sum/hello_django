from user.models import User
def blog_context(request):
    context = {}
    user = request.session.get('user_id')
    try:
        user = User.objects.filter(pk=user)
        print(user)
        context['form_user'] = user

    except:
        pass
    return context