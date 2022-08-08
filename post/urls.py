

from django.urls import path
from post import views

urlpatterns = [
    path('main_posts/', views.MainPostsListView.as_view()),
    path('popular_posts/', views.PopularPostListView.as_view()),
    path('for_you/', views.ForYouListView.as_view()),
    path("<int:id>/", views.ArticleDetailView.as_view()),
    path('read_next/', views.ReadNextListView.as_view()),
    path('post/<int:id>/comment', views.AddCommentView.as_view()),
    
    path("post_create_list/", views.PostCreateListView.as_view()),
    path("posts/", views.ListCreatePostApiView.as_view()),
    path("posts/<int:id>/", views.PostUpdate.as_view()),
    
    
]
