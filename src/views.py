from django.shortcuts import render,redirect
from .models import Task
from datetime import date

def home(request):
    tasks = Task.objects.all()
    return render(request, 'home.html', {'tasks': tasks})


def add_task(request):
    if request.method == "POST":
        task_name = request.POST['task_name']
        subject = request.POST['subject']
        deadline = request.POST['deadline']
        priority = request.POST['priority']

        Task.objects.create(
            task_name=task_name,
            subject=subject,
            deadline=deadline,
            priority=priority
        )
        return redirect('home')

    return render(request, 'add_task.html')


def mark_completed(request, task_id):
    task = Task.objects.get(id=task_id)
    task.status = "Completed"
    task.save()
    return redirect('home')


def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('home')


def search_by_subject(request):
    query = request.GET.get('subject')
    tasks = Task.objects.filter(subject__iexact=query)

    context = {
        'tasks': tasks,
        'query': query,
        'no_results': not tasks.exists()
    }
    if not query:
        return render(request, 'home.html', {
        'tasks': Task.objects.all(),
        'error': "Please enter a subject to search"
    })

    return render(request, 'home.html', context)


from datetime import date

def overdue_tasks(request):
    today = date.today()
    tasks = Task.objects.filter(deadline__lt=today, status='Pending')

    context = {
        'tasks': tasks,
        'no_overdue': not tasks.exists()
    }

    return render(request, 'home.html', context)