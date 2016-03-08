from django.shortcuts import render

from task.models import Field


def home(request):
    fields = Field.objects.all()
    context = {
        'fields': fields
    }

    if fields.count() == 0:
        Field.objects.create(
            field_data={'field_name': "Имя поля", 'field_text': "Поле"}
        )

    if request.method == 'POST':
        Field.objects.create(
            field_data={'field_name': 'Имя поля', 'field_text': 'Поле'}
        )
    return render(request, 'task/home.html', context)
