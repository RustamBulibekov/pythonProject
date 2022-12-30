from django.urls import path
from .views import PostListView, PostDetailListView, OwnLoginView

urlpatterns = [
    path('', PostListView.as_view(), name='post'),
    path('<int:pk>/', PostDetailListView.as_view(), name='post_detail'),
    path('accounts/login/', OwnLoginView.as_view(), name='login')
]
