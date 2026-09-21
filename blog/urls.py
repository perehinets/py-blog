from django.urls import path

from .views import index, PostDetailView, CommentaryCreateView

urlpatterns = [
    path("", index, name="index"),
    path("post/<int:pk>", PostDetailView.as_view(), name="post-detail"),
    path(
        "post/<int:pk>/comment/",
        CommentaryCreateView.as_view(),
        name="comment-create"
    ),
]

app_name = "blog"
