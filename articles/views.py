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

    # 5) POST 요청이 들어온 경우(데이터가 잘못된 경우)
    # 10) POST 요청이 들어온 경우(데이터가 잘 들어온 경우)
    if request.method == 'POST':
        # 6) Form에 사용자가 입력한 정보(X)를 담아서
        # 11) Form에 사용자가 입력한 정보(o)를 담아서
        form = ArticleForm(request.POST)
        # 3번
        # 7) 검증단계 실패
        # 12) 검증단계 성공
        if form.is_valid():
            # 13) form을 저장하고 저장한 데이터를 article 변수에 담기
            article = form.save()
            # 14) 방금 생성된 article detail 페이지로 redirect
            return redirect('articles:detail', id=article.id)
        # # 2번
        # else:
        #     context = {
        #         'form': form,
        #     }
        #     return render(request, 'articles/form.html', context)
    # 1) GET 요청이 들어온 경우
    else:
        # 2) 비어있는 Form 만들어서
        form = ArticleForm()
    # 3) context dict에 담고
    # 8) 검증 실패한 Form을 context dict에 담고
    context = {
        'form': form,
    }
    # 4) form.html을 랜더링
    # 9) form.html을 랜더링
    return render(request, 'articles/form.html', context)



def detail(request, id):
    article = Article.objects.get(id=id)

    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

def update(request, id):
    article = Article.objects.get(id=id)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.id)
    else:
        form = ArticleForm(instance=article)

    context = {
        'form': form,
    }    

    return render(request, 'articles/form.html', context)

def delete(request, id):
    article = Article.objects.get(id=id)
    article.delete() 
    return redirect('articles:index')