import sqlite3
import json

from django.http import HttpResponse
from django.shortcuts import render
import urllib.request

sql_insert_task = "SELECT * FROM stars WHERE id='{}'"

db = sqlite3.connect('./stars.db')


def index(request):
    context = {}
    return render(request, 'index.html', context)


def stars(request):
    if request.method == 'GET':
        context = {}
        return render(request, 'stars.html', context)
    elif request.method == 'POST':
        context = {}
        # return render(request, 'index.html', context)

        body = request.body
        result = str(body, 'utf-8')
        # print(result)

        # result = json.loads(request.body)
        # print(result)

        # print(request.body)
        # print(request.body)
        # loads = json.loads(request.body.decode('utf-8'))
        # print(loads)

        # cursor = db.cursor()
        # cursor.execute(sql_insert_task.format(id, star, time, result))
        # db.commit()
        # cursor.close()

        return HttpResponse(result)
