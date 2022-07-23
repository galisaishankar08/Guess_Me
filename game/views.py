from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
import sqlite3
import random

from django.template.response import TemplateResponse

conn = sqlite3.connect('./db.sqlite3', check_same_thread=False)


username = ''
password = ''
email = ''


def signin(request):
    global username, password, email

    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['pwd']
    data = conn.execute('select * from game_signin').fetchall()
    flag = False
    for i in range(len(data)):
        if username == data[i][1] and password == data[i][2]:
            flag = True
            break
        else:
            flag = False
    if flag:
        return redirect('/')
    else:
        return render(request, 'signin.html')


def signup(request):
    global username, password, email
    if request.method == 'POST':
        username = request.POST['uname']
        email = request.POST['email']
        password = request.POST['pwd']
        sql1 = f''' INSERT INTO game_signup(username,email,password)
                      VALUES('{username}','{email}','{password}') '''
        sql2 = f''' INSERT INTO game_signin(username,password)
                              VALUES('{username}','{password}') '''
        cur = conn.cursor()
        cur.execute(sql1)
        cur.execute(sql2)
        conn.commit()
        return redirect('/signin')
    return render(request, 'signup.html')


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def profile(request):
    args = {}
    global username, password, email
    email = conn.execute(f"select email from game_signup where username='{username}';").fetchall()
    args['uname'] = username
    try:
        args['email'] = email[0][0]
    except Exception:
        args['email'] = ''
    return TemplateResponse(request, 'profile.html', args)


def logout(request):
    return redirect('/signin')


secret_number = random.randint(0, 100)
turn = 0
success = False


def rookie(request):
    global secret_number, turn, success
    context = {}
    hint = ''
    guessed_number = None

    if request.method == 'POST' and request.POST.get('guess'):
        guessed_number = int(request.POST.get('guess'))
        print(secret_number)
        print(guessed_number)
        turn += 1
        if guessed_number == secret_number:
            success = True
        else:
            if guessed_number < secret_number:
                hint = 'higher'
            else:
                hint = 'lower'

    else:
        secret_number = random.randint(0, 100)
        turn = 0
        success = False
        hint = ''
        guessed_number = None

    context['success'] = success
    context['turn'] = turn
    context['hint'] = hint
    context['guessed_number'] = guessed_number

    if context['turn'] == 10:
        messages.info(request, 'Game Over ❌')
        messages.info(request, 'Secret Number : ' + str(secret_number))
        messages.info(request, 'Please try again...')
        return HttpResponseRedirect(request.path_info)

    elif context['success']:
        messages.info(request, 'Congratulations 🎉')
        messages.info(request, 'Score : ' + str((10 - context['turn'] + 1)*10))
        messages.info(request, 'Play again...')
        return HttpResponseRedirect(request.path_info)

    else:
        messages.info(request, 'Guessed Number : ' + str(context['guessed_number']))
        messages.info(request, 'Success : '+str(context['success']))
        messages.info(request, 'Hint : '+str(context['hint']))
        messages.info(request, 'Remaining turns : ' + str(10-context['turn']))

    return render(request, 'rookie.html')


def intermediate(request):
    global secret_number, turn, success
    context = {}
    hint = ''
    guessed_number = None

    if request.method == 'POST' and request.POST.get('guess'):
        guessed_number = int(request.POST.get('guess'))
        turn += 1
        if guessed_number == secret_number:
            success = True
        else:
            if guessed_number < secret_number:
                hint = 'lower'
            else:
                hint = 'higher'

    else:
        secret_number = random.randint(0, 100)
        turn = 0
        success = False
        hint = ''
        guessed_number = None

    context['success'] = success
    context['turn'] = turn
    context['hint'] = hint
    context['guessed_number'] = guessed_number

    if context['turn'] == 5:
        messages.info(request, 'Game Over ❌')
        messages.info(request, 'Secret Number : ' + str(secret_number))
        messages.info(request, 'Please try again...')
        return HttpResponseRedirect(request.path_info)

    elif context['success']:
        messages.info(request, 'Congratulations 🎉')
        messages.info(request, 'Score : '+str((5 - context['turn'] + 1)*20))
        messages.info(request, 'Play again...')
        return HttpResponseRedirect(request.path_info)

    else:
        messages.info(request, 'Guessed Number : ' + str(context['guessed_number']))
        messages.info(request, 'Success : ' + str(context['success']))
        messages.info(request, 'Remaining turns : ' + str(5 - context['turn']))

    return render(request, 'intermediate.html')


def expert(request):
    number = random.randint(1, 100)
    guess = 0
    print(number)
    if request.method == 'POST':
        guess = int(request.POST.get('guess'))
        if guess < number:
            messages.info(request, 'guess is low')
            messages.info(request, 'Guessed Number : ' + str(guess))
            messages.info(request, 'Secret Number : '+str(number))
        elif guess > number:
            messages.info(request, 'guess is high')
            messages.info(request, 'Guessed Number : ' + str(guess))
            messages.info(request, 'Secret Number : ' + str(number))
        else:
            messages.info(request, 'Congrats, You guessed it!')
            messages.info(request, 'Secret Number : ' + str(number))
    return render(request, 'expert.html')
