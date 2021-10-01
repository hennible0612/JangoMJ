# from django.urls import path
# from . import views
#
#
# app_name = 'polls' #하드 코딩된 url제거용가리
# urlpatterns = [
#     # /polls/
#     path('', views.index, name='index'),
#     # /polls/5/
#     path('<int:question_id>/',views.detail, name='detail'),
#     # /polls/5/results/
#     path('<int:question_id>/results/', views.results, name='results'),
#     # /polls/5/vote
#     path('<int:question_id>/vote/', views.vote, name='vote'),
#
# ]

#제너릭 뷰
from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
