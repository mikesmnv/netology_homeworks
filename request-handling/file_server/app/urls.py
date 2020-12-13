from django.urls import path, register_converter
from app import views
import datetime


class DateConverter:
    regex = '[0-9]{4}-[0-9]{2}-[0-9]{2}'
    format = '%Y-%m-d%'

    def to_python(self, value):
        return datetime.strptime(value, self.format)

    def to_url(self, value):
        return value.strftime(self.format)


register_converter(DateConverter, 'dtc')

# Определите и зарегистрируйте конвертер для определения даты в урлах и наоборот урла по датам


urlpatterns = [
    # Определите схему урлов с привязкой к отображениям .views.file_list и .views.file_content
    path('file_list/', views.file_list, name='file_list'),
    path('file_list/dtc:date/', views.file_list, name='file_list'),    # задайте необязательный параметр "date"
                                      # для детальной информации смотрите HTML-шаблоны в директории templates
   # path('file_content/', views.file_content, name='file_content'),
]
