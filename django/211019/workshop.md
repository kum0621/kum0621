1. accounts  views.py

``` python

from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import login as auth_login
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:signup')
    else:
        form = CustomUserCreationForm()

    context = {
        'form' : form ,

    }
    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            
            return redirect(request.GET.get('next') or 'todos:index')          
    else:
        form = AuthenticationForm()
 
    context = {
        'form': form

    }
    return render(request, 'accounts/login.html', context)

```

2. accounts forms.py

```python
from django.contrib.auth.forms import(
    UserCreationForm,
)
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fileds = UserCreationForm.Meta.fields
```

3. accounts modles.py

```python
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    pass
```

4. todos views.py

``` python
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from todos.forms import TodoForm
from .models import Todo
# Create your views here.

def index(request):

    todos = Todo.objects.order_by('-pk')
    context = {
        'todos': todos
    }
    return render(request,'todos/index.html', context)

@login_required
def create(request):
    '''
    GET : 투두 작성하는 템플릿
    POST : DB에 투두 정보 생성
    '''
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            # commit 임시저장 => todo 임시로 인스턴스 생성
            todo = form.save(commit=False)
            # 1:N 관계 설정
            todo.author = request.user
            # 진짜 저장하기
            todo.save()
            return redirect('todos:index')
    else:
        form = TodoForm()
    context = {
        'form': form
    }
    return render(request, 'todos/create.html', context)
```



5. todos forms.py

``` python
from django import forms
from .models import Todo
class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        #fields = '__all__' # 1:N
        fields = ('title', 'completed',)
```



6. todos models.py

``` python
from django.db import models
from django.conf import settings
# Create your models here.

class Todo(models.Model):
    # author_id
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)

```

7. 회원가입 구현

![image-20211019225203663](workshop.assets/image-20211019225203663.png)

8. 로그인 구현

![image-20211019225413024](workshop.assets/image-20211019225413024.png)

9. todo 목록

![image-20211019230607791](workshop.assets/image-20211019230607791.png)

10. todo 생성 구현

![image-20211019230220503](workshop.assets/image-20211019230220503.png)



