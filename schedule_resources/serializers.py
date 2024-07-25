from rest_framework import serializers
from .models import Project, Task, Skill, Resource, ResourceSkill, ResourceAvailability, TaskSkill

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'

class ResourceSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceSkill
        fields = '__all__'

class ResourceAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceAvailability
        fields = '__all__'

class TaskSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskSkill
        fields = '__all__'