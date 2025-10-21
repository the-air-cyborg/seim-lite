from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Alert

def alert_dashboard(request):
    alerts = Alert.objects.all().order_by('-timestamp')[:50]  # show latest 50
    return render(request, 'alerts/dashboard.html', {'alerts': alerts})
