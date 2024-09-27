from django.forms import ModelForm

from .models import Todo


class AddForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'body']