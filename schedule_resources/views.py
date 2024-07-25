import logging
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Project, Task, Skill, Resource, ResourceSkill, ResourceAvailability, TaskSkill
from .serializers import (
    ProjectSerializer, TaskSerializer, SkillSerializer,
    ResourceSerializer, ResourceSkillSerializer,
    ResourceAvailabilitySerializer, TaskSkillSerializer
)

logger = logging.getLogger(__name__)

class ProjectListCreate(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class SkillListCreate(generics.ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class ResourceListCreate(generics.ListCreateAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer

class ResourceSkillListCreate(generics.ListCreateAPIView):
    queryset = ResourceSkill.objects.all()
    serializer_class = ResourceSkillSerializer

class ResourceAvailabilityListCreate(generics.ListCreateAPIView):
    queryset = ResourceAvailability.objects.all()
    serializer_class = ResourceAvailabilitySerializer

class TaskSkillListCreate(generics.ListCreateAPIView):
    queryset = TaskSkill.objects.all()
    serializer_class = TaskSkillSerializer

@api_view(['GET'])
def match_resources(request, task_id):
    matching_resources = match_resources_for_task(task_id)
    serializer = ResourceSerializer(matching_resources, many=True)
    return Response(serializer.data)

# Function to to find and match suitable resources for each task based
# on their skills and availability
def match_resources_for_task(task_id):
    try:
        # Fetch the task and required skills
        task = Task.objects.get(id=task_id)
        required_skills = set(TaskSkill.objects.filter(task=task).values_list('skill', flat=True))
    except Task.DoesNotExist:
        logger.error(f"Task with id {task_id} does not exist.")
        return []
    except Exception as e:
        logger.error(f"Error retrieving task or skills: {e}")
        return []

    def is_resource_suitable(resource):
        try:
            # Fetch resource skills
            resource_skills = set(ResourceSkill.objects.filter(resource=resource).values_list('skill', flat=True))
            
            # Check if resource has all required skills
            if not required_skills.issubset(resource_skills):
                return False

            # Check resource availability
            availability_periods = ResourceAvailability.objects.filter(resource=resource)
            return any(
                period.start_date <= task.start_date and period.end_date >= task.end_date
                for period in availability_periods
            )
        except Exception as e:
            logger.error(f"Error checking resource suitability for resource {resource.id}: {e}")
            return False

    try:
        # Get all resources and filter suitable ones
        resources = Resource.objects.all()
        matching_resources = list(filter(lambda r: is_resource_suitable(r), resources))
    except Exception as e:
        logger.error(f"Error matching resources: {e}")
        return []

    return matching_resources
# def match_resources_for_task(task_id):
#     task = Task.objects.get(id=task_id)
#     task_skills = TaskSkill.objects.filter(task=task)
#     required_skills = [task_skill.skill for task_skill in task_skills]
    
#     matching_resources = []

#     for resource in Resource.objects.all():
#         resource_skills = ResourceSkill.objects.filter(resource=resource).values_list('skill', flat=True)
#         if all(skill in resource_skills for skill in required_skills):
#             availability_periods = ResourceAvailability.objects.filter(resource=resource)
#             for period in availability_periods:
#                 if period.start_date <= task.start_date and period.end_date >= task.end_date:
#                     matching_resources.append(resource)
#                     break

#     return matching_resources