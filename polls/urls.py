from django.urls import path

from polls import views
from . import views1

app_name = 'polls'

urlpatterns = [
    # # ex: /polls/
    # path("", views1.index, name="index"),
    # # ex: /polls/5/
    # path("<int:question_id>/", views1.detail, name="detail"),
    # # ex: /polls/5/results/
    # path("<int:question_id>/results/", views1.results, name="results"),
    # # ex: /polls/5/vote/
    # path("<int:question_id>/vote/", views1.vote, name="vote"),


    # Generic views

    path("", views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
