from django.urls import path
from . import views


urlpatterns = [
    path('articles/', views.article_create),
    path('articles/<int:article_pk>/', views.article_detail_update_delete),
    path('articles/<int:article_pk>/comments/', views.comment_create),
    path('comments/', views.comment_list),
]
