from django.urls import path
from . import views

urlpatterns = [
    path('trainers/', views.Trainers.as_view()),
    # path('trainer/<int:id>/',  views.Trainer.as_view()),
    path('doubts/', views.DoubtsView.as_view()),
]
