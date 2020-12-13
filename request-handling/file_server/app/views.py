import datetime
import os
from django.shortcuts import render
from django.conf import settings


def file_list(request, date=None):
    template_name = 'index.html'
    files = os.listdir(settings.FILES_PATH)

    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    context = {
        'files': [
            {'name': file + '.txt',
             'ctime': datetime.datetime.fromtimestamp(os.stat(f'{settings.FILES_PATH}/{file}').st_ctime),

             'mtime': datetime.datetime.fromtimestamp(os.stat(f'{settings.FILES_PATH}/{file}').st_mtime)
             }
            for file in files
        ],
        'date': date  # Этот параметр необязательный
    }
    print(context['files'])

    return render(request, template_name, context)

"""
def file_content(request, name):
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    return render(
        request,
        'file_content.html',
        context={'file_name': 'file_name_1.txt', 'file_content': 'File content!'}
    )
"""