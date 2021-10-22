1. accounts/views.py

   ```py
   from django.shortcuts import get_object_or_404, redirect, render
   from django.contrib.auth import login as auth_login
   from django.contrib.auth import logout as auth_logout
   from django.contrib.auth.forms import (
       AuthenticationForm, 
       UserCreationForm, 
       PasswordChangeForm
   )
   from django.views.decorators.http import require_http_methods, require_POST
   from django.contrib.auth import update_session_auth_hash
   from django.contrib.auth.decorators import login_required
   
   from accounts.models import User
   from .forms import CustomUserChangeForm, CustomUserCreationForm
   from django.contrib.auth import get_user_model
   
   # Create your views here.
   @require_http_methods(['GET', 'POST'])
   def login(request):
       if request.user.is_authenticated:
           return redirect('articles:index')
   
       if request.method == 'POST':
           form = AuthenticationForm(request, request.POST)
           if form.is_valid():
               auth_login(request, form.get_user())
               return redirect(request.GET.get('next') or 'articles:index')
       else:
           form = AuthenticationForm()
       context = {
           'form': form,
       }
       return render(request, 'accounts/login.html', context)
   
   
   @require_POST
   def logout(request):
       if request.user.is_authenticated:
           auth_logout(request)
       return redirect('articles:index')
   
   
   @require_http_methods(['GET', 'POST'])
   def signup(request):
       if request.user.is_authenticated:
           return redirect('articles:index')
   
       if request.method == 'POST':
           form = CustomUserCreationForm(request.POST)
           if form.is_valid():
               user = form.save()
               auth_login(request, user)
               return redirect('articles:index')
       else:
           form = CustomUserCreationForm()
       context = {
           'form': form,
       }
       return render(request, 'accounts/signup.html', context)
   
   
   @require_POST
   def delete(request):
       if request.user.is_authenticated:
           request.user.delete()
           auth_logout(request)
       return redirect('articles:index') 
   
   
   @login_required
   @require_http_methods(['GET', 'POST'])
   def update(request):
       if request.method == 'POST':
           form = CustomUserChangeForm(request.POST, instance=request.user)
           if form.is_valid():
               form.save()
               return redirect('articles:index')
       else:
           form = CustomUserChangeForm(instance=request.user)
       context = {
           'form': form,
       }
       return render(request, 'accounts/update.html', context)
   
   
   @login_required
   @require_http_methods(['GET', 'POST'])
   def change_password(request):
       if request.method == 'POST':
           form = PasswordChangeForm(request.user, request.POST)
           if form.is_valid():
               form.save()
               update_session_auth_hash(request, form.user)
               return redirect('articles:index')
       else:
           form = PasswordChangeForm(request.user)
       context = {
           'form': form,
       }
       return render(request, 'accounts/change_password.html', context)
   
   
   def profile(request, username):
       person = get_object_or_404(get_user_model(), username=username)
       context = {
           'person': person,
       }
       return render(request, 'accounts/profile.html', context)
   
   @require_POST
   def follow(request, person_pk):
       '''
       POST : 요청한 사람을 중개테이블에 추가하거나 제거
       '''
       if request.user.is_authenticated:
           me = request.user
           you = get_object_or_404(get_user_model(), pk=person_pk)
   
           if me != you:
               # if you in me.followings.all():
               #     me.followiings.remove(you)
               # else:
               #     me.followings.add(you)
               
               if you.followers.filter(pk=me.pk).exists():
                   you.followers.remove(me)
   
               else:
                   you.followers.add(me)
           return redirect('accounts:profile', you.username)
       return redirect('accounts:login')
   ```

   

2. accounts/models.py

```python
from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.conf import settings
# Create your models here.


class User(AbstractUser):
    # followings = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followers')
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
```



3. profile.html

```django
{% extends 'base.html' %}

{% block content %}
<p>{{ person.username }}님의 프로필 페이지입니다.</p>

<p>팔로우 : {{ person.followers.count }}</p>
<p>팔로잉 : {{ person.followings.count }}</p>

{% if user != person %}
    <div>
      <form action="{% url 'accounts:follow' person.pk %}" method="POST">
        {% csrf_token %}
        {% if user in person.followers.all %}
          <input type="submit" value="언팔로우">
        {% else %}
          <input type="submit" value="팔로우">
        {% endif %}

      </form>
    </div>
  
  {% endif %}
<hr>
<p>작성한 글 : {{ person.article_set.count }}</p>
{{ person.article_set.all }}
<hr>
<p>작성한 댓글 : {{ person.comment_set.count }}</p>
{{ person.comment_set.all }}
<hr>
<p>좋아요한 글</p>
{{ person.like_articles.all }}

{% endblock content %}

```

![image-20211021171720462](workshop.assets/image-20211021171720462-16348042417561.png)

![image-20211021171736320](workshop.assets/image-20211021171736320.png)
