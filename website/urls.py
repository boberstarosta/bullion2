from django.contrib import admin
from django.urls import path
from bullion import views


urlpatterns = [
    path('', views.MetalListView.as_view(), name='index'),
    path('coins/', views.CoinListView.as_view(), name='coin_list'),
    path('coins/new', views.CoinCreateView.as_view(), name='coin_new'),
    path('coins/<int:pk>/', views.CoinDetailView.as_view(), name='coin_detail'),
    path('coins/<int:pk>/edit', views.CoinUpdateView.as_view(), name='coin_update'),
    path('coins/<int:pk>/delete', views.CoinDeleteView.as_view(), name='coin_delete'),
    path('admin/', admin.site.urls),
]
