from django.urls import path

from . import views

urlpatterns = [
    # ex: /home/
    path('', views.index, name='index'),
    path('update/', views.user_update, name='user_update'),
    path('password/', views.user_password, name='user_password'),
    path('comments/', views.user_comments, name='user_comments'),
    #path('addcomment/<int:id>',views.addcomment,name="addcomment")
    # ex: /home/5/
    #path('<int:question_id>/', views.detail, name='detail'),

    ]
