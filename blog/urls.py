from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogPostView.as_view(), name='posts_list'),
    path('<int:pk>/', views.BlogPostDetailView.as_view(), name='post_detail'),
    path('create/', views.BlogPostCreateView.as_view(), name='create_post'),
    path('<int:pk>/update/', views.BlogPostUpdateView.as_view(), name='update_post'),
    path('<int:pk>/delete', views.BlogPostDeleteView.as_view(), name='delete_post'),
]
