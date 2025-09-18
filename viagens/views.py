from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.core.mail import send_mail
from .models import Foto
from .forms import ContatoForm

def index(request):
    busca = request.GET.get('q','')
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

def sobre_nos(request):
    return render(request, 'viagens/sobre_nos.html')

def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            mensagem = form.cleaned_data['mensagem']

            send_mail(
                f'Mensagem de {nome}',
                f'Mensagem de {nome} ({email}):\n\n{mensagem}',
                email,
                ['seu_email_para_receber@exemplo.com'],
                fail_silently=False,
            )

            return redirect(reverse('sucesso'))
        
    else:
        form = ContatoForm()

    return render(request, 'viagens/contato.html', {'form': form})

def sucesso(request):
    return render(request, 'viagens/sucesso.html')
