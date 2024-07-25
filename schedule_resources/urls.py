from django.urls import path
from .views import (
    ProjectListCreate, TaskListCreate, SkillListCreate,
    ResourceListCreate, ResourceSkillListCreate,
    ResourceAvailabilityListCreate, TaskSkillListCreate,
    match_resources
)

urlpatterns = [
    path('projects', ProjectListCreate.as_view(), name='project-list-create'),
    path('tasks/', TaskListCreate.as_view(), name='task-list-create'),
    path('skills/', SkillListCreate.as_view(), name='skill-list-create'),
    path('resources/', ResourceListCreate.as_view(), name='resource-list-create'),
    path('resource-skills/', ResourceSkillListCreate.as_view(), name='resource-skill-list-create'),
    path('resource-availability/', ResourceAvailabilityListCreate.as_view(), name='resource-availability-list-create'),
    path('task-skills/', TaskSkillListCreate.as_view(), name='task-skill-list-create'),
    path('match-resources/<int:task_id>/', match_resources, name='match-resources'),

]   

