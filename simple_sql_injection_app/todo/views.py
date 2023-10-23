from typing import Any
from django.db.models import QuerySet
from django.http import HttpRequest, JsonResponse
# from django.core import serializers
from django.forms.models import model_to_dict

from todo.models import Todo


def todo_list(request: HttpRequest):
    todo: str = request.GET.get("todo", "")
    todos: QuerySet[Todo] | Any = Todo.objects.all()
    if not todo:
        print("hoge")
        todos = Todo.objects.all()
        return JsonResponse({"todos": [model_to_dict(todo) for todo in todos]})

    sql: str = (
        "SELECT id, id_str, todo, created_date, due_date FROM todo_todo "
        "WHERE todo = '{}';".format(todo)
    )
    todos = Todo.objects.raw(sql)

    # Correct implementation:
    # todos = Todo.objects.filter(todo=todo_str)

    return JsonResponse({"todos": [model_to_dict(todo) for todo in todos]})
