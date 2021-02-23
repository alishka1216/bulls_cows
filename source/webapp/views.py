from lib2to3.fixes.fix_input import context
from random import randint
from django.shortcuts import render


first_check = [4, 6, 7, 2]

save_step = {}

count_turn = 0

def posts_create_view(request):
    if request.method == "GET":
        return render(request, 'posts_create.html')
    elif request.method == "POST":
        second_check = request.POST.get("numbers")
        try:
            second_check = list(map(int, second_check.split(" ")))
            bulls = 0
            cows = 0
            message = ''
            if len(second_check) == 4:
                for b in range(4):
                    if second_check[b] in second_check[b+1:]:
                        message ='числа повторяются'
                        break
                    if second_check[b]<1 or second_check[b]>10:
                        message = 'числа не входят в промежуток'
                        break
                    if first_check[b] == second_check[b]:
                        bulls += 1
                    elif second_check[b] in first_check:
                        cows += 1
                if not message:
                    if bulls == 4:
                        message = 'вы угадали'
                    else:
                        message = f"bulls: {bulls} cows: {cows}"
            else:
                message = 'введите 4 числа'

        except ValueError:
            message = "не блатуй! так нельзя"
        except IndexError:
            message ='введите больше чисел'
        global count_turn
        count_turn+=1
        save_step[f'ход номер: {count_turn}']=message
        print(save_step)
        return render(request,'posts_create.html',{'message':message})


def stats(request):
    return render(request, 'stats.html', {'save_step':save_step})