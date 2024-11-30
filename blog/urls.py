from django.urls import path

from .views import(
PostListView, 
PostDetailView,
PostCreateView,
PostUpdateView,
PostDeleteView
 )
from . import views
urlpatterns = [
    #app/model_list.html
    path('', view=PostListView.as_view(),name='blog-home'),
    path('post/new/', view=PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/update/', view=PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/', view=PostDeleteView.as_view(),name='post-delete'),
    path('post/<int:pk>/', view=PostDetailView.as_view(),name='post-detail'),
    path('about', view=views.about,name='blog-about'), 
]