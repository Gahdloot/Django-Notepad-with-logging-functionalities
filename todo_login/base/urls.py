from django.urls import path

from .views import TaskList, TaskDetail, TaskCreate, TaskUpadate, TaskDelete, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView


app_name = 'base'
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='base:login'), name='logout'),
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task/create/', TaskCreate.as_view(), name='create_task'),
    path('task/<int:pk>/update', TaskUpadate.as_view(), name='update_task'),
    path('task/<int:pk>/delete', TaskDelete.as_view(), name='delete_task')

]