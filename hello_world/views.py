from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from . import models

def hello_world(request):
    table_2 = models.SecondTable.objects.get(id=1)
    table_1 = table_2.second_table.all()
    template = loader.get_template('hello_world/hello_world.html')

    context = {
        'table_1': table_1,
        'table_2': table_2
    }
    return HttpResponse(template.render(context, request))
