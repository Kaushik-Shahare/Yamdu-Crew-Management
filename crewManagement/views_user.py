# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.hashers import make_password
# from .models import Crew, Cast
from .models import User, Crew, Cast, Project
import json


def getUser(request):
    if request.method == 'GET':
        users = User.objects.all()
        data = [
            {
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "password": user.password,
                "age": user.age,
                "phone": user.phone,
                "address": user.address,
                "availability": user.availability
            } for user in users
        ]
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)

def createUser(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            name = data['name']
            email = data['email']
            password = data['password']
            age = data['age']
            phone = data['phone']
            address = data['address']
            availability = data['availability']

            # Password Hash Logic here
            password = make_password(password=password, salt=None, hasher='default')

            user = User.objects.create(name=name, email=email, password=password, age=age, phone=phone, address=address, availability=availability)
            return JsonResponse({'message': 'User created successfully!'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)

def editUser(request, user_id):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body.decode('utf-8'))
            user = User.objects.get(id=user_id)
            user.name = data.get('name', user.name)
            user.email = data.get('email', user.email)

            # Password Hash Logic here
            password = make_password(password=data.get('password'), salt=None, hasher='default')

            user.password = data.get('password', password)
            user.age = data.get('age', user.age)
            user.phone = data.get('phone', user.phone)
            user.address = data.get('address', user.address)
            user.availability = data.get('availability', user.availability)
            user.save()
            return JsonResponse({'message': 'User updated successfully!'}, status=200)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)
