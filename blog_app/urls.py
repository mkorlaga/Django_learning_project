from django.urls import path
from .views import (PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostDeleteView,
                    PostUpdateView,
                    UserPostListView,
                    AboutView)


# Names are used in *.html instead of hardcoded route
urlpatterns = [
    path('', PostListView.as_view(template_name='blog_app/home.html'), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('user/<str:username>', UserPostListView.as_view(template_name='blog_app/user_posts.html'), name='user-posts'),
    path('about/', AboutView.as_view(template_name='blog_app/about.html'), name='blog-about'),

]
