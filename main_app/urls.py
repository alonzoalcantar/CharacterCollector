from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home_1'),
    path('about/', views.about, name='about'),
    path('characters/', views.characters_index, name='index'),
    path('characters/<int:character_id>/', views.character_detail, name='detail'),
    path('characters/create/', views.CharacterCreate.as_view(), name='characters_create'),
    path('characters/<int:pk>/update/', views.CharacterUpdate.as_view(), name= 'characters_update'),
    path('characters/<int:pk>/delete/', views.CharacterDelete.as_view(), name= 'characters_delete'),
]