from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Função para exibir a lista de posts
def index(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'posts': posts})

# Função para exibir detalhes de um post específico
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post_detail.html', {'post': post})

# Função para criar um novo post (apenas usuários logados podem acessar)
@login_required  # Protege a view para exigir que o usuário esteja logado
def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:  # Verifica se os campos não estão vazios
            # Criando o post e associando o autor ao usuário logado
            Post.objects.create(title=title, content=content, author=request.user)
            return redirect('index')  # Redireciona para a página principal após criar o post
        else:
            # Se os campos estiverem vazios, retorna um erro ou mensagem
            return render(request, 'create_post.html', {'error': 'Todos os campos são obrigatórios.'})
    return render(request, 'create_post.html')

# Função de registro de usuário
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Faz o login do usuário após o registro
            return redirect('index')  # Redireciona para a página principal após o login
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
