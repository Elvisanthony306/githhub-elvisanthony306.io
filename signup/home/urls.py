
from django.urls import include, path
from .views import authView, home, post, posts, editPost #, default
#from.views import 

urlpatterns = [
    #path("", default, name="default"),
    path("", home, name="home"),
    path("posts", post, name="post"),
    path("post<int:id>", posts, name="posts"),
    path("edit<int:id>", editPost, name="edit"),
    path("signup/", authView, name="authView"),
    path("accounts/", include("django.contrib.auth.urls")),
]
