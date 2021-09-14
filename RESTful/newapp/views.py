from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from newapp.models import NewUser
from newapp.serializers import UserSerializer

# The root of our API is going to be a view that supports listing all the existing newusers, or creating a new newuser.

@csrf_exempt
def newuser_list(request):
    """
    List all code newusers, or create a new newuser.
    """
    if request.method == 'GET':
        newusers = NewUser.objects.all()
        serializer = UserSerializer(newusers, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def newuser_detail(request, pk):
    """
    Retrieve, update or delete a code newuser.
    """
    try:
        newuser = NewUser.objects.get(pk=pk)
    except NewUser.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserSerializer(newuser)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(newuser, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        newuser.delete()
        return HttpResponse(status=204)