from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import QuestionForm, UserForm
from questions.models import Question
from questions.models import Answer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from qrcodegame.models import Leaderboard
from core.utils import signer

def get_user_position_leaderboard(request, all_scores):
    j = 0
    username = request.user.username
    for i in all_scores:
        j = j + 1
        if str(username) == str(i.adam):
            return j
        else:
            pass


def home(request):
    leaderboard = Leaderboard.objects.order_by('-score')
    your_place = get_user_position_leaderboard(request, leaderboard)
    leaderboard = leaderboard[:10]
    if request.user.is_authenticated:
        your_place = get_user_position_leaderboard(request, leaderboard)
        answers = Answer.objects.filter(adam=request.user)
        answers = answers.order_by('-date_created')
    else:
        your_place = 'not'
        answers = None
    return render(request, 'home.html', {'leaderboard':leaderboard, 'your_place':your_place, 'answers':answers})


# Create your views here.
def index(request, secret):
    leaderboard = Leaderboard.objects.order_by('-score')
    string = signer.sign(1)
    print(string)
    id = signer.unsign(secret)
    if request.user.is_authenticated:
        question = Question.objects.get(id=id)
        if request.method == 'POST':
            form = QuestionForm(request.POST)
            if form.is_valid():
                answer = form.cleaned_data['answer']
                adam = User.objects.get(username=request.user.username)
                if question.answer.lower() in answer.lower() or question.secondary_answer.lower() in answer.lower():
                    leaderboard_place = Leaderboard.objects.get(adam=adam)
                    current_score = leaderboard_place.score
                    correct = True
                    if Answer.objects.filter(adam=adam, question=question, correct=True).exists():
                        new_score = current_score
                    else: 
                        new_score = current_score + 1
                    entry = Leaderboard(
                        adam = adam,
                        score = new_score    
                    )
                    entry.save()
                else:
                    correct = False
                answer = Answer(
                    question = question,
                    correct = correct,
                    answer = form.cleaned_data['answer'],
                    adam = adam
                )
                answer.save()
                if answer == question.answer:
                    print(answer)
                    print(question.answer)
                    print(question.solvecount)
                    question.solvecount =+ 1
                    question.save()
                score = Leaderboard.objects.get(adam=adam)
                your_place = get_user_position_leaderboard(request, leaderboard)
                leaderboard = leaderboard[:10]
                return render(request, 'success.html', {'correct': correct, 'score':score.score, 'id':secret, 'leaderboard':leaderboard, 'your_place':your_place})
        else: 
            form = QuestionForm()
        return render(request, 'question.html', {'form': form, 'id':id, 'question':question.riddle,'type':question.question_type,})
    else:
        return redirect('/registeruser/'+str(secret))
        
        

def new_user(request, secret):   
    id = signer.unsign(secret)
    password = 'nopassword'
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            slackhandle = form.cleaned_data['slackhandle']
            slackhandle = slackhandle.lower()
            print(slackhandle)
            if slackhandle == 'pvandoorn':
                print("Was pvandoorn")
                return redirect('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
            if User.objects.filter(username=slackhandle).exists():
                new_user = User.objects.get(username=slackhandle)
            else:
                new_user = User(
                    username = slackhandle,
                    password = password
                )
                new_user.set_password(password)
                new_user.save()
                leaderboard_entry = Leaderboard(
                    adam=new_user,
                    score=0
                )
                leaderboard_entry.save()
                new_user = authenticate(request, username=slackhandle, password=password)
            login(request, new_user)
            return redirect('/qr/'+str(secret))
        else:
            redirect('/registeruser/'+str(secret))
    else:
        if request.user.is_authenticated:
            return redirect('/dashboard')
        else:
            form = UserForm()
            return render(request, 'slackhandle.html', {'form':form})
        

def random(request):
    leaderboard = Leaderboard.objects.order_by('-score')[:10]
    return render(request, 'random.html', {'leaderboard':leaderboard})