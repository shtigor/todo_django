from django.http import JsonResponse
from django.shortcuts import redirect, render
from .models import Task
from .forms import TODOForm

import json


def show_list(request):
    """ Show all task """
    context = {}
    if request.method == 'POST':
        form = TODOForm(request.POST)

        if form.is_valid():
            description = form.cleaned_data.get('description')
            Task.objects.create(description=description)

        return redirect('/')
    else:
        form = TODOForm()
        context = {
            'form': form,
            'tasks': Task.objects.all()}

    return render(request, 'todo/main.html', context=context)


def update_task(request):
    data = json.load(request)
    instrument = data['instrument']
    task_id = int(data['task_id'])
    new_description = data['new_description']

    task = Task.objects.get(pk=task_id)

    if instrument == 'delete':
        description = task.description
        task.delete()
        return JsonResponse({'message': f'Task is deleted {description}.'})
    else:
        task.description = new_description
        task.save()
        return JsonResponse({'message': 'Task is updated.'})
