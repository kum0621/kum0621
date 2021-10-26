from django.urls import path
from . import views


urlpatterns = [
    path('artists/', views.artist_create),
    path('artists/<int:artist_pk>/', views.artist_detail_update_delete),
    path('artists/<int:artist_pk>/musics/', views.music_create),
    path('music/', views.music_list),
    path('music/<int:music_pk>/', views.music_detail_update_delete),

]
