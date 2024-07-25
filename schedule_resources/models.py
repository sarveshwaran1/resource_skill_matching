from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Resource(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ResourceSkill(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

class ResourceAvailability(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

class TaskSkill(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)