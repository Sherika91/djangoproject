from django.urls import path
from blog.apps import BlogConfig
from blog.views import BlogListView, BlogDetailView, BlogUpdateView, BlogCreateView, BlogDeleteView, toggle_activity

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='list'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('<int:pk>/', BlogDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', BlogUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', BlogDeleteView.as_view(), name='delete'),
    path('activity/<int:pk>/', toggle_activity, name='toggle_activity'),

]
