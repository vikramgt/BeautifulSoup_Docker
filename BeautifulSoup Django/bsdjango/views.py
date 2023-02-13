from django.shortcuts import redirect, render, get_object_or_404
from .models import Data

def list_scrap(request):
    queryset = Data.objects.all().order_by('loc')
    context = {
        'queryset': queryset
    }
    return render(request, 'List_Scrap.html', context)

