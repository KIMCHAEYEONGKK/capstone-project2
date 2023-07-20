from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Board,Common
from .forms import BoardForm


@login_required(login_url="common:login")
def board_write(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board = Board()  # 모델 클래스 변수 생성
            board.title = form.cleaned_data['title']  # form의 제목을 가져옴
            board.contents = form.cleaned_data['contents']
            board.writer = request.user  # 현재 로그인한 사용자의 id
            board.save()
            return HttpResponseRedirect('/board/board_list/')  # 작성 후 글목록으로 이동
        else:
            return render(request, 'board/board_write.html')
    else:
        form = BoardForm()
    return render(request, 'board/board_write.html', {'form': form})


def board_list(request):
    boards = Board.objects.all().order_by('-id')
    return render(request, 'board/board_list.html', {'boards': boards})


@login_required(login_url="common:login")
def board_detail(request, pk):
    board = Board.objects.get(id=pk)
    return render(request, 'board/board_detail.html', {'board': board})


@login_required(login_url="common:login")
def board_delete(request, pk):
    board = get_object_or_404(Board, id=pk)
    if request.user == board.writer:
        board.delete()
    return redirect('board:board_list')


@login_required(login_url="common:login")
def board_update(request, pk):
    board = Board.objects.get(id=pk)
    if request.method == "POST":
        board.title = request.POST.get('title')
        board.contents = request.POST.get('contents')
        board.writer = request.user
        board.save()
        return redirect('/board/board_list')
    else:
        boardForm = BoardForm()
        return render(request, 'board/board_update.html', {'boardForm': boardForm})


@login_required(login_url="common:login")
def notice(request):
    return render(request, 'board/notice.html')
