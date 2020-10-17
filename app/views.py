from django.contrib import messages, auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from app.forms import Student_Form
from app.models import Programming, Maths, Result, Science
from django.core.paginator import Paginator, EmptyPage, InvalidPage



correct_lst = []
wrong_lst = []


def main(request):
    return render(request, 'main.html')

def register(request):
    form = Student_Form()
    if request.method == 'POST':
        form = Student_Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Created Successfully")
            return redirect('login')
    context = {'form': form}
    return render(request, 'register.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Invalid username/password")

    return render(request, 'login.html')


@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('main')


@login_required(login_url='login')
def quiz_test_programming(request):
    obj = Programming.objects.all()
    paginator = Paginator(obj, 1)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        questions = paginator.page(page)
    except(EmptyPage, InvalidPage):
        questions = paginator.page(paginator.num_pages)

    return render(request, 'quiz_test.html', {'obj': obj, 'questions': questions})

@login_required(login_url='login')
def quiz_test_maths(request):
    obj = Maths.objects.all()
    paginator = Paginator(obj, 1)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        questions = paginator.page(page)
    except(EmptyPage, InvalidPage):
        questions = paginator.page(paginator.num_pages)

    return render(request, 'quiz_test.html', {'obj': obj, 'questions': questions})

@login_required(login_url='login')
def quiz_test_science(request):
    obj = Science.objects.all()
    paginator = Paginator(obj, 1)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        questions = paginator.page(page)
    except(EmptyPage, InvalidPage):
        questions = paginator.page(paginator.num_pages)

    return render(request, 'quiz_test.html', {'obj': obj, 'questions': questions})


@login_required(login_url='login')
def result(request):
    correct = len(correct_lst)
    wrong = len(wrong_lst)

    if(correct>5):
        result = "pass"
    else:result = "Fail"

    current_user = request.user
    username = current_user.username

    save_ans = Result(username=username, correct_answers=correct, wrong_answers=wrong, status=result)
    save_ans.save()

    return render(request, 'result.html', {'correct': correct, 'wrong': wrong, 'result': result})


def correctAnswer(request):
    ans = request.GET['ans']
    correct_lst.append(ans)

def wrongAnswer(request):
    ans = request.GET['ans']
    wrong_lst.append(ans)

