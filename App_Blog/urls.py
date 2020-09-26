from django.urls import path
from App_Blog import views

app_name = 'App_Blog'

urlpatterns = [
    path('', views.BlogList.as_view(), name='home'),
    path('write/', views.CreateBlog.as_view(), name='create_blog'),
    path('details/<slug:slug>', views.blog_details, name='blog_details'),
    path('liked/<pk>', views.liked, name='like_post'),
    path('unliked/<pk>', views.disliked, name='dislike'),
    path('my-blog', views.MyBlog.as_view(), name='my_blog'),
    path('edit/<pk>', views.UpdateBlog.as_view(), name='edit_blog'),
    path('blog-author-profile/<username>/', views.blog_author_profile, name='blog-author-profile'),
    path('author-blogs/<username>/', views.author_blogs, name='author-blog'),
    path('blog_ranking/', views.ranking, name='ranking'),
]
