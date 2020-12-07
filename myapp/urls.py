from django.urls import path

from .views import Homeview, Full_view, Creat_view

urlpatterns = [
    path('', Homeview.as_view(), name = 'blog_name'),
    path('blog_post/<int:pk>/', Full_view.as_view(), name= 'full_view'),
    path('create_view/', Creat_view.as_view(success_url='/'), name= 'create_view')

]