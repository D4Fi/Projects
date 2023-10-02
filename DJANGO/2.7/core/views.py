from pathlib import PureWindowsPath
from django.shortcuts import render

def index(request):

    print('====================')
    querydic = request.GET
    print(querydic)


    return render(request, 'core/index.html')
