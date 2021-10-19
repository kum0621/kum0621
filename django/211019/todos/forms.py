from django import forms
from .models import Todo
class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        #fields = '__all__' # 1:N
        fields = ('title', 'completed',)