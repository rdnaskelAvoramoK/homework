from django.shortcuts import render
import random
import string


def index(request):

    rand_num = random.randrange(100, 10000)
    letters = string.ascii_lowercase
    rand_text = ''.join(random.choice(letters) for i in range(5,13))

    return render(request, 'index.html', {'rand_num': rand_num, 'rand_text':rand_text})


def int_page(request):
    return render(request, 'int_page.html')


def srt_page(request):
    return render(request, 'str_page.html')