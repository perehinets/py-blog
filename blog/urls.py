from django.urls import path

from .views import index, PostDetailView, CommentaryCreateView

urlpatterns = [
    path("blog/", index, name="index"),
    path("blog/post/<int:pk>", PostDetailView.as_view(), name="post-detail"),
    path(
        "blog/post/<int:pk>/comment/",
        CommentaryCreateView.as_view(),
        name="comment-create"
    ),
]

app_name = "blog"
