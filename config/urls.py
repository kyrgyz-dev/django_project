from django.contrib import admin
from django.http import HttpResponse, JsonResponse
from django.urls import path

PEOPLE = [
    {
        "id": 1,
        "name": "Arnas",
        "email": "arnas@gmail.com",
        "age": 15,
        "is_active": True
    },
    {
        "id": 2,
        "name": "Meerim",
        "email": "meerim@gmail.com",
        "age": 24,
        "is_active": False
    },
    {
        "id": 3,
        "name": "Islam",
        "email": "islam@gmail.com",
        "age": 22,
        "is_active": True
    },
    {
        "id": 4,
        "name": "Elnura",
        "email": "elnura@gmail.com",
        "age": 26,
        "is_active": True
    }
]


def get_user(request, user_id):
    for person in PEOPLE:
        if person["id"] == user_id:
            return JsonResponse(person)
    else:
        return HttpResponse(404)


def get_all_users(request):
    return JsonResponse({"people": PEOPLE})

def add_user(request):
    user_id = len(PEOPLE) + 1
    person = {
        "id": user_id,
        "name": request.GET.get("name", "Unknown"),
        "email": request.GET.get("email", "Unknown"),
        "age": request.GET.get("age", 18),
        "is_active": True
    }
    PEOPLE.append(person)
    return JsonResponse(person)

def edit_user(request, user_id):
    for person in PEOPLE:
        if person["id"] == user_id:
            person["name"] = request.GET.get("name", person["name"])
            person["email"] = request.GET.get("email", person["email"])
            person["age"] = request.GET.get("age", person["age"])
            person["is_active"] = request.GET.get("is_active", person["is_active"])
            return JsonResponse(person)
    else:
        return HttpResponse(404)

def delete_user(request, user_id):
    for person in PEOPLE:
        if person["id"] == user_id:
            PEOPLE.remove(person)
            return JsonResponse({"status": "success"})
    else:
        return HttpResponse(404)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', get_all_users),
    path('users/<int:user_id>/', get_user),
    path('users/add/', add_user),
    path('users/edit/<int:user_id>/', edit_user),
    path('users/delete/<int:user_id>/', delete_user),
]
