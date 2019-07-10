from django.urls import path
from . import views
from blog import views as bviews


urlpatterns = [
    path('', views.project_index, name='project_index'),
    path('<int:pk>/', views.project_detail, name='project_detail'),
    path('blog/', bviews.blog_index, name='blog_index'),
]