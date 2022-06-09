from django.urls import path
from . import views

urlpatterns = [
    path('trainers/', views.TrainersListCreate.as_view()),
    path('trainer/<int:pk>/',  views.TrainerRetrieveUpdateDestroy.as_view()),
    path('doubts/', views.DoubtsView.as_view()),
]
