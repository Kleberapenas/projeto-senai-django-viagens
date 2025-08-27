from django.shortcuts import render, get_object_or_404
from .models import Foto
from django.db.models import Q

def index(request):
    busca = request.GET.get('q')
    if busca:
        fotos = Foto.objects.filter(
            Q(titulo__icontains=busca) | Q(descricao__icontains=busca)
        )
    else:
        fotos = Foto.objects.all()
    return render(request, 'viagens/index.html', {'fotos': fotos})

def detalhe_foto(request, foto_id):
    foto = get_object_or_404(Foto, pk=foto_id)
    return render(request, 'viagens/detalhe.html', {'foto': foto})
