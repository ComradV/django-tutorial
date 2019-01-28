from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Board

# def home(request):
#     boards = Board.objects.all()
#     boards_names = [board.name for board in boards]

#     response_html = '<br>'.join(boards_names)

#     return HttpResponse(response_html)    

def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})

def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    topics = []
    return render(request, 'topics.html', {'board': board, 'topics': topics})

def new_topic(request, pk):
    # board = get_object_or_404(Board, pk=pk)
    # topics = []
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'new_topic.html', {'board': board})