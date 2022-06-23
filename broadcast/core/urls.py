from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.IndexPage.as_view(), name='index_page'),
    path('playlist/', views.PlaylistView.as_view(), name='playlist'),
    path('add-to-favorite/', views.AddToFavorite.as_view(), name='add_to_favorite'),
    path('broadcast/', views.BroadcastView.as_view(), name='broadcast'),

]
