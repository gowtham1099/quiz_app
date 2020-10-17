from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('home', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('quiz_test_programming', views.quiz_test_programming, name='quiz_test_programming'),
    path('quiz_test_maths', views.quiz_test_maths, name='quiz_test_maths'),
    path('quiz_test_science', views.quiz_test_science, name='quiz_test_science'),
    path('result', views.result, name='result'),
    path('correctAnswer', views.correctAnswer, name='correctAnswer'),
    path('wrongAnswer', views.wrongAnswer, name='wrongAnswer'),
]