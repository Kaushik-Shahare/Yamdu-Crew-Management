# Create your views here.
from django.http import HttpResponse, JsonResponse
# from .models import Crew, Cast
from .models import  User, Crew, Cast, Project
import json

#Delete later
from django.views.decorators.csrf import csrf_exempt

def getCrew(request):
    if request.method == 'GET':
        try:
            crews = Crew.objects.all()
            data = [
                {
                    "id": crew.id,
                    "user": crew.user.name if crew.user else None,
                    "position": crew.position,
                    "project": [project.name for project in crew.projects.all()]
                } for crew in crews
            ]
            return JsonResponse(data, safe=False)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)

def getCrewById(request, crew_id):
    if request.method == 'GET':
        try:
            if crew_id:
                crew = Crew.objects.get(id=crew_id)
                if crew is None:
                    return JsonResponse({"error": "Crew not found"}, status=404)
                data = {
                    "id": crew.id,
                    "user": crew.user.name if crew.user else None,
                    "position": crew.position,
                    "project": [project.name for project in crew.projects.all()]
                }
                return JsonResponse(data, safe=False)
            else:
                return JsonResponse({"error": "Crew ID is required"}, status=400)
            
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

def getCast(request):
    if request.method == 'GET':
        try:
            casts = Cast.objects.all()
            data = [
                {
                    "id": cast.id,
                    "user": cast.user.name if cast.user else None,
                    "role": cast.role,
                    "project": [project.name for project in cast.projects.all()]
                } for cast in casts
            ]
            return JsonResponse(data, safe=False)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)

def getCastById(request, cast_id):
    if request.method == 'GET':
        try:
            if cast_id:
                cast = Cast.objects.get(id=cast_id)
                if cast is None:
                    return JsonResponse({"error": "Cast not found"}, status=404)
                data = {
                    "id": cast.id,
                    "user": cast.user.name if cast.user else None,
                    "role": cast.role,
                    "project": [project.name for project in cast.projects.all()]
                }
                return JsonResponse(data, safe=False)
            else:
                return JsonResponse({"error": "Cast ID is required"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

def assignPost(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        user_id = data.get('user_id')
        project_id = data.get('project_id')
        if project_id is not None:
            try:
                project = Project.objects.get(id=project_id)
            except Project.DoesNotExist:
                return JsonResponse({"error": "Project not found"}, status=404)
        else:
            return JsonResponse({"error": "Project ID is required"}, status=400)

        if 'cast' in data:
            cast = data['cast']
            role = cast.get('role')
            if role:
                cast = Cast.objects.get(user=User.objects.get(id=user_id))
                if cast.projects.filter(id=project_id).exists():
                    return JsonResponse({"error": "User already assigned to project"}, status=409)
                cast.projects.add(project)
                cast.save()
            else:
                return JsonResponse({"error": "Role is required for cast"}, status=400)

        if 'crew' in data:
            crew = data['crew']
            position = crew.get('position')
            if position:
                crew = Crew.objects.get(user=User.objects.get(id=user_id))
                crew.projects.add(project)
                if crew.projects.filter(id=project_id).exists():
                    return JsonResponse({"error": "User already assigned to project"}, status=409)
                crew.save()
            else:
                return JsonResponse({"error": "Position is required for crew"}, status=400)

        return JsonResponse({"message": "User assigned to project successfully"}, status=201)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)

def emptyCrewPosition(request):
    if(request.method == 'POST'):
        try:
            data = json.loads(request.body.decode('utf-8'))
            project_id = data.get('project_id')
            position = data.get('position')

            if not project_id or not position:
                return JsonResponse({"error": "Project ID and position are required"}, status=400)

            project = Project.objects.get(id=project_id)  
            if(project is None):
                return JsonResponse({"error": "Project not found"}, status=404)
            crew = Crew.objects.create(position=position)
            crew.projects.add(project)

            return JsonResponse({"message": "Crew position created successfully", "crew_id": crew.id})
        except Project.DoesNotExist:
            return JsonResponse({"error": "Project not found"}, status=404)
        except KeyError as e:
            return JsonResponse({"error": f"Missing key: {str(e)}"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)

# Just for testing
def cast_and_crew_table(request):
    # Fetch all Crew and Cast objects from the database
    crews = Crew.objects.all()
    casts = Cast.objects.all()
    
    crew_data = [
        {
            "id": crew.user.id,
            "name": crew.user.name,
            "position": crew.position,
            "phoneNo": crew.user.phone,
            "project": [project.name for project in crew.projects.all()]
        } for crew in crews
    ]

    # Prepare data for Cast
    cast_data = [
        {
            "id": cast.user.id,
            "name": cast.user.name,
            "role": cast.role,
            "phoneNo": cast.user.phone,
            "project": [project.name for project in cast.projects.all()]
        } for cast in casts
    ]

    # Prepare data for Projects
    project_data = [
        {
            "id": project.id,
            "name": project.name,
            "description": project.description,
            "start_date": project.start_date,
            "end_date": project.end_date,
            "cast": [cast.user.name for cast in project.cast.all()],
            "crew": [crew.user.name for crew in project.crew.all()]
        } for project in Project.objects.all()
    ]

    # Combine all data into a single dictionary
    data = {
        "crews": crew_data,
        "casts": cast_data,
        "projects": project_data
    }

    # Return JSON response
    return JsonResponse(data)
    
def createProject(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            print(data)

            project = Project.objects.create(
                name=data.get('name'),
                description=data.get('description'),
                start_date=data.get('start_date'),
                end_date=data.get('end_date')
            )
            
            return JsonResponse({"message": "Project created successfully", "project_id": project.id}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)

def getProjectCrew(request, project_id):
    
    if request.method == 'GET':
        try:
            project = Project.objects.get(id=project_id)
            crew = project.crew.all()
            data = [
                {
                    "id": crew_member.user.id if crew_member.user else None,
                    "name": crew_member.user.name if crew_member.user else "Position vacant",
                    "position": crew_member.position
                } for crew_member in crew
            ]
            return JsonResponse(data, safe=False)
        except Project.DoesNotExist:
            return JsonResponse({"error": "Project not found"}, status=404)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)

def getProjectCast(request, project_id):
    
    if request.method == 'GET':
        try:
            project = Project.objects.get(id=project_id)
            cast = project.cast.all()
            data = [
                {
                    "id": cast_member.user.id if cast_member.user else None,
                    "name": cast_member.user.name if cast_member.user else "Position vacant",
                    "role": cast_member.role
                } for cast_member in cast
            ]
            return JsonResponse(data, safe=False)
        except Project.DoesNotExist:
            return JsonResponse({"error": "Project not found"}, status=404)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)

