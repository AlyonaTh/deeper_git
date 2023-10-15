from django.shortcuts import render
from django.http import HttpResponse
import random
import logging
from myapp2.models import Coin


logger = logging.getLogger(__name__)


def coin(request, count: int):
    game_list = ['Head','Tail']
    result = []
    for i in range(count):
        response = random.choice(game_list)
        result.append(response)
    context = {
        'result': result
    }
    return render(request, 'myapp/index.html', context=context)


def cube(request):
    cube_value = random.randint(1, 6)
    logger.info(f'Кубик выпал стороной: {cube_value}')
    return HttpResponse(cube_value)


def random_number(request):
    number = random.randint(0, 100)
    logger.info(f'Случайное число: {number}')
    return HttpResponse(number)