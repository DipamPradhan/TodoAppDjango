from django.urls import path
from . import views

app_name = "todo"
urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("todopage/", views.todopage, name="todopage"),
    path("signout/", views.signout, name="signout"),
    path("deleteTodo/<int:srno>", views.deleteTodo, name="deleteTodo"),
    path("editTodo/<int:srno>", views.editTodo, name="editTodo"),
]
