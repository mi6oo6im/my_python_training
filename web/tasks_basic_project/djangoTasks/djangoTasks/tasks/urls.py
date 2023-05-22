from django.urls import path

from djangoTasks.tasks import views

urlpatterns = (
    # localhost:8000/tasks/
    path('', views.index),
    path('it-works/', views.show_bare_minimum),
    path('all/', views.get_all_tasks),
)