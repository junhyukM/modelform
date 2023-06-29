from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()

    context = {
        'articles': articles
    }

    return render(request, 'articles/index.html', context)

def create(request):
    # method = 어떤 방식으로 들어왔는지
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        article = Article(title=title, content=content)
        article.save()

        return redirect('articles:index')
    
    else:
        return render(request, 'articles/create.html')
    

def create2(request):
    # 경우의수
    # 1. GET 요청이 들어온경우 : Form 만들어서 html 문서 사용자에게 전송
    # 2. POST 요청이 들어온 경우 : 데이터 검증에 실패했을 때(검증된 데이터는 그대로 보여줘야함)
    # 3. POST 요청이 들어온 경우 : 데이터 검증에 성공했을 때()

    if request.method == 'POST':
        form = ArticleForm(request.POST)
        # 3번
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', id=article.id)
        # # 2번
        # else:
        #     context = {
        #         'form': form,
        #     }
        #     return render(request, 'articles/form.html', context)
    # 1번
    else:
        form = ArticleForm()
        
    context = {
        'form': form,
    }

    return render(request, 'articles/form.html', context)



def detail(request, id):
    article = Article.objects.get(id=id)

    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)
