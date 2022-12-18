from django.shortcuts import render, redirect

from .forms import CreateArticle
from .models import Article


# Create your views here.
# Get all articles
def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, '../templates/articles/article_list.html', {'articles': articles, 'title': 'Articles'})


# Get single article
def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, '../templates/articles/article_detail.html', {'article': article, 'title': article.title})


# Create new article
def article_create(request):
    if request.method == 'POST':
        form = CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = CreateArticle()
    return render(request, 'articles/article_create.html', {'title': 'Create Article', 'form': form})


# Update article
def article_update(request, slug):
    article = Article.objects.get(slug=slug)
    if request.method == 'POST':
        form = CreateArticle(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:list')
    else:
        form = CreateArticle(instance=article)
    return render(request, 'articles/article_update.html', {'title': 'Update Article', 'form': form})


# Delete article
def article_delete(request, slug):
    article = Article.objects.get(slug=slug)
    article.delete()
    return redirect('articles:list')
