from lib2to3.fixes.fix_input import context
from random import randint
from django.shortcuts import render

a = randint(0, 9)
b = randint(0, 9)
c = randint(0, 9)
d = randint(0, 9)
first_check = [a, b, c, d]


def posts_create_view(request):
    if request.method == "GET":
        return render(request, 'posts_create.html')
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

    return render(request,'posts_create.html',{'message':message})
