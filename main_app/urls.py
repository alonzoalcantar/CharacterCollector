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

    path('items/', views.items_index, name='items_index'),
    path('items/<int:item_id>/', views.item_detail, name='itemdetail'),
    path('items/create/', views.ItemCreate.as_view(), name='items_create'),
    path('items/<int:pk>/update/', views.ItemUpdate.as_view(), name= 'items_update'),
    path('items/<int:pk>/delete/', views.ItemDelete.as_view(), name= 'items_delete'),
    path('characters/<int:character_id>/add_session/', views.add_session, name= 'add_session'),
]
