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