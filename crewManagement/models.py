from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=100, null=True)
    availability = models.BooleanField()


class Crew(models.Model):
    # For now set null=True to avoid issues with migrations
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    position = models.CharField(max_length=100)
    projects = models.ManyToManyField("Project", related_name="crew_members")

    
class Cast(models.Model):
    # For now set null=True to avoid issues with migrations
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    role = models.CharField(max_length=100)
    projects = models.ManyToManyField("Project", related_name="cast_members")


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    cast = models.ManyToManyField(Cast, related_name="projects_for_cast")
    crew = models.ManyToManyField(Crew, related_name="projects_for_crew")

    def __str__(self):
        return self.name

    
