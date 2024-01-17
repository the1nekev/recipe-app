from django.urls import path
from .views import welcome, RecipesListView, RecipesDetailView

app_name = 'recipes'

urlpatterns = [
    path('', welcome),
    path('list/', RecipesListView.as_view(), name='list'),
    path('list/<pk>', RecipesDetailView.as_view(), name='detail'),
]