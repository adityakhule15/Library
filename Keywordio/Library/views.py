from django.http import JsonResponse
from Library.models import BookList
from django.http.response import HttpResponse
from rest_framework.views import APIView
import json
from django.views.decorators.csrf import csrf_exempt
from .serializers import BookListSerializer 
 

@csrf_exempt
class BooksList(APIView):

    @csrf_exempt
    def postSave(request):
        prod=BookList()
        prod.Title=request.POST.get('Title')
        prod.Writer=request.POST.get('Writer')
        prod.save()
        return HttpResponse("Success")

    
    @csrf_exempt
    def ListOfBooks(request):
        Books1=BookList.objects.all()
        serializer = BookListSerializer(Books1, many = True)
        total_Books1 = json.dumps(serializer.data)
        total_Books = json.loads(total_Books1)
        data = {'Books':total_Books}
        return JsonResponse(data)
  
    @csrf_exempt
    def update(request):       

        BookList.objects.filter(Id = request.POST.get('Id')).update(
        Title=request.POST.get('Title'),
        Writer=request.POST.get('Writer')
        )
        
        return HttpResponse("Success")  

    @csrf_exempt
    def delete(request):       

        BookList.objects.filter(Id = request.POST.get('Id')).delete()
        
        return HttpResponse("Success") 


        
        