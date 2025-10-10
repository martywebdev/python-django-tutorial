from django.urls import path

from polls import views2
from . import views

app_name = 'polls'

urlpatterns = [
    # # ex: /polls/
    # path("", views.index, name="index"),
    # # ex: /polls/5/
    # path("<int:question_id>/", views.detail, name="detail"),
    # # ex: /polls/5/results/
    # path("<int:question_id>/results/", views.results, name="results"),
    # # ex: /polls/5/vote/
    # path("<int:question_id>/vote/", views.vote, name="vote"),


    # Generic views

    path("", views2.IndexView.as_view(), name='index'),
    path('<int:pk>/', views2.DetailView.as_view(), name='detail'),
    path("<int:pk>/results/", views2.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views2.vote, name="vote"),
]
