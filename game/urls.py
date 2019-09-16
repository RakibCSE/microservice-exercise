from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('api/categories/', views.CategoryList.as_view(), name='category-list'),
    path('api/games/', views.GameList.as_view(), name='game-list'),
    path('api/game/<int:pk>', views.GameDetail.as_view(), name='game-detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
