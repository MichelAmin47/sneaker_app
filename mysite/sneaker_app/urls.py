from django.urls import path

from . import views

urlpatterns = [
    # ex: /sneaker_app/
    path('', views.index, name='index'),
    # ex: /sneaker_app/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /sneaker_app/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /sneaker_app/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

    # ex: /sneaker_app/5/
    path('shoe_model/<int:shoe_id>/', views.shoe_model, name='shoe model'),
]