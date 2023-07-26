from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

from .views import (
    TaskListView,
    TagListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TaskDetailView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView, TaskCompleteStateView,
)

urlpatterns = [
    path(
        "",
        RedirectView.as_view(
            url=reverse_lazy("to_do_list:task_list")
        )
    ),
    path(
        "tasks/",
        TaskListView.as_view(),
        name="task_list",
    ),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/update-state/", TaskCompleteStateView.as_view(), name="task-update-state"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path(
        "tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"
    ),
    path(
        "tags/",
        TagListView.as_view(),
        name="tag_list",
    ),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
]

app_name = "to_do_list"
