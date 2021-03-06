from django.shortcuts import render
import random
from datetime import datetime
from django.http import JsonResponse


def index(request):

    return render(request, 'index.html')

def game(request):
    request.session['win']=request.POST['win']
    request.session['counter'] = 0
    request.session['display'] = ""
    return render(request, 'game.html')


def process_money(request, op):
    temp=time()
    request.session['count_2'] += 1
    if op == 'farm':
        gold=round(random.random()*(20-10)+10)
        request.session['counter'] += gold
    elif op == 'cave':
        gold=round(random.random()*(10-5)+5)
        request.session['counter'] += gold
    elif op == 'house':
        gold=round(random.random()*(5-2)+2)
        request.session['counter'] += gold
    elif op == 'casino':
        gold=round(random.random()*100-50)
        request.session['counter'] += gold
    else:
        print('No válido')

    if gold>0:
        request.session['display'] += f'<div class="gano">Ha ganado {gold} desde {op}!'
    elif gold == 0:
        request.session['display'] += f'Ha entrado a {op}. Su saldo se mantiene igual!'
    else:
        request.session['display'] += f'<div class="perdio">Ha entrado a {op} y ha pérdido {abs(gold)}... Ouch..'



    context={
        'array':{'id':100, 'id':200, 'asd':300}
    }

    request.session['display'] += f"({temp[0]} {temp[1]},  {temp[2]} - {temp[3]}:{temp[4]})</div>\n"
    ruta ='game.html'

    return render(request, ruta, context)


def time():
    now = datetime.now()
    mes = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sept', 'Oct', 'Nov', 'Dic']
    mes_final = mes[now.month - 1]
    if int(now.minute == 0):
        minute = '00'
    elif int(now.minute) < 10:
        minute = str(f"0{now.minute}")
    else:
        minute = now.minute
    return [mes_final, now.day, now.year, now.hour, minute]