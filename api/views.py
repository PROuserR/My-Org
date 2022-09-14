from ast import Sub
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *
from oauth2_provider.models import AccessToken

# Create your views here.
@api_view(['POST'])
def registerUser(request):
    username = request.data['username']
    email = request.data['email']
    password = request.data['password']
    
    user = User.objects.create_user(username, email, password)

    if user:
        login(request, user)
        return Response('Register is done')
    else:
        return Response('Register error')


@api_view(['GET'])
def logoutUser(request):
    logout(request)
    return Response('Logout')


@api_view(['POST'])
def createNote(request, token):
    note = Note.objects.create(owner=AccessToken.objects.get(token=token).user,
    title = request.data['title'],
    content = request.data['content'])
    serializer = NoteSerializer(data=note)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


@api_view(['get'])
def getNotes(request, token):
    notes = Note.objects.filter(owner=AccessToken.objects.get(token=token).user.id)
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


@api_view(['get'])
def getNote(request, id):
    note = Note.objects.get(id=id)
    serializer = NoteSerializer(note)
    return Response(serializer.data)


@api_view(['PUT'])
def updateNote(request, id):
    note = Note.objects.get(id=id)
    note.title = request.data['title']
    note.content = request.data['content']
    note.save()
    return Response('Task updated!')


@api_view(['delete'])
def deleteNote(request, id):
    note = Note.objects.get(id=id)
    note.delete()
    return Response('Note deleted!')


@api_view(['POST'])
def createTask(request, token):
    task = Task.objects.create(owner=AccessToken.objects.get(token=token).user,
    reminder = request.data['reminder'],
    title = request.data['title'])
    for subtaskContent in request.data['subtasksContent']:
        subtask = SubTask.objects.create(content=subtaskContent)
        subtask.save()
        task.subtask.add(subtask)
    serializer = TaskSerializer(data=task)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


def getSubTask(task):
    subtasks = []
    for subtask in task['subtask']:
        subTaskData = SubTask.objects.get(id=subtask)
        subtaskDict = {'content': subTaskData.content,
        'checked': subTaskData.checked,
        'id': subTaskData.id}
        subtasks.append(subtaskDict)
    return subtasks


@api_view(['get'])
def getTasks(request, token):
    tasks = Task.objects.filter(owner=AccessToken.objects.get(token=token).user.id)
    serializer = TaskSerializer(tasks, many=True)

    subtasksWithinTasks = [dict(task) for task in serializer.data]
    for subtasksWithinTask in subtasksWithinTasks:
        subtasksWithinTask['subtask'] = getSubTask(subtasksWithinTask)
    return Response(subtasksWithinTasks)


@api_view(['get'])
def getTask(request, id):
    task = Task.objects.get(id=id)
    serializer = TaskSerializer(task)
    return Response(serializer.data)


@api_view(['PUT'])
def updateTask(request, id):
    task = Task.objects.get(id=id)
    task.title = request.data['title']
    for i in range(len(task.subtask.all())):
        subtask = SubTask.objects.get(id=task.subtask.all()[i].id)
        subtask.checked = request.data['subtaskChecked'][i]
        subtask.content = request.data['subtasksContent'][i]
        subtask.save()
    task.save()
    return Response('Task updated!')


@api_view(['PUT'])
def updateSubTask(request, id):
    subtask = SubTask.objects.get(id=id)
    subtask.checked = request.data['checked']
    subtask.save()
    return Response('Subtask updated!')


@api_view(['PUT'])
def checkAllSubTask(request, id):
    task = Task.objects.get(id=id)
    for subtask in task.subtask.all():
        subtask.checked = request.data['checked']
        subtask.save()
    return Response('Subtasks updated!')


@api_view(['delete'])
def deleteTask(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return Response('Task deleted!')