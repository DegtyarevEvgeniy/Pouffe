from .models import *


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        users = User.objects.all()
        context['users'] = users
        if 'user_selected' not in context:
            context['user_selected'] = 0
        return context



