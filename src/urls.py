"""
URL configuration for GUI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from basics.views import home, add_task, mark_completed, delete_task, search_by_subject, overdue_tasks

urlpatterns = [
    path("admin/", admin.site.urls),
    path('home/', home, name='home'),
    path('add/',add_task, name='add_task'),
    path('complete/<int:task_id>/',mark_completed, name='complete'),
    path('delete/<int:task_id>/', delete_task, name='delete'),
    path('search/', search_by_subject, name='search'),
    path('overdue/',overdue_tasks, name='overdue'),
]
