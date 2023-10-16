from django.db.models import Count, QuerySet
from django.http import HttpResponse, HttpRequest

# Create your views here.
from demo.models import User


def loadexampledata(_: HttpRequest):
    name_list: list[str] = ["Admin", "Staff1", "Staff12"]
    for name in name_list:
        u = User(name=name)
        u.save()
    return HttpResponse("ok")


def users(request: HttpRequest):
    field: str = request.GET.get('field', "demo.name")
    user_amount: QuerySet[User] = User.objects.annotate(**{field: Count("name")})

    html: str = ""
    for u in user_amount:
        html += f"<h3>Amoount of users: {u}</h3>"
    return HttpResponse(html)
