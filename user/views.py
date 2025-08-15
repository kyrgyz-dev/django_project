from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

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
            return render(request, "user/detail.html", {"person": person})
    else:
        return HttpResponse("<h1 style='color:red'>Страница не найдено!</h1>")


def get_all_users(request):
    return render(request, "user/list.html", {"people": PEOPLE})


def add_user(request):
    if request.method == "POST":  # GET
        user_id = len(PEOPLE) + 1
        person = {
            "id": user_id,
            "name": request.POST.get("name", "unknown"),
            "email": request.POST.get("email", "unknown"),
            "age": int(request.POST.get("age", 18)),
            "is_active": request.POST.get("is_active", True),
        }
        PEOPLE.append(person)
        return JsonResponse(person)
    return render(request, "user/create.html")


def edit_user(request, user_id):
    user: dict = {}
    for person in PEOPLE:
        if person["id"] == user_id:
            user = person
            break
    if user == {}:
        return HttpResponse("<h1 style='color:red'>Пользователь не найдено!</h1>")
    if request.method == "POST":
        user['name'] = request.POST.get("name", user['name']),
        user['email'] = request.POST.get("email", user['email']),
        user['age'] = int(request.POST.get("age", user['age'])),
        user['is_active'] = request.POST.get("is_active", user['is_active']),
        PEOPLE.append(user)
        return JsonResponse({"user": user})
    return render(request, "user/edit.html", {"person": user})


def delete_user(request, user_id):
    for person in PEOPLE:
        if person["id"] == user_id:
            PEOPLE.remove(person)
            return JsonResponse({"status": "success"})
    else:
        return HttpResponse("<h1 style='color:red'>Страница не найдено!</h1>")
