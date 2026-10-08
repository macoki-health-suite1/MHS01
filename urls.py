from django.http import JsonResponse
from django.urls import path

def health(request):
    return JsonResponse({'status': 'ok', 'service': 'MHS API'})

urlpatterns = [path('health/', health, name='health')]
