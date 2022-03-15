# created by -Akshay
import re
from tabnanny import check
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse('''About our website <a href="/">BACK</a> ''')

def modi(request):
    data = request.GET.get('text', 'default')
    result = data
    checkRead = request.GET.get('check', False)
    checkPunc = request.GET.get('removepunc', False)
    checkCapt = request.GET.get('AutoCapt', False)
    if checkRead == 'on':
        param = {'task': 'Read data', 'modata': data}
        return render(request, 'modified.html', param)
    elif checkPunc == 'on':
        result = ''
        s = ''',/;:'"\}{[]!'''
        for a in data:
            if a not in s:
                result += a
    if checkCapt == 'on':
        newstr = ''
        count = 0
        for i in result:
            if count == 0 and i != ' ' :
                newstr += i.upper()
                count += 1
            elif i == '.':
                newstr += i
                newstr += ' '
                count = 0
            elif count==0 and i==' ':
                continue
            else:
                newstr += i.lower()
                count += 1
        result = newstr
    if checkCapt == 'on' or checkPunc == 'on' :
        param = {'task': 'Operation', 'modata': result}
        return render(request, 'modified.html', param)
    else:
        return HttpResponse("welcome to read page")
