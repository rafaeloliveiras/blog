from django.urls import path


from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.PostList, name='post_list'),
    path('category/', views.CategoryList, name='category_name'),
    path('post/<slug:slug>', views.PostUnique, name='post_unique'),
]