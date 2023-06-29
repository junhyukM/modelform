# project

## 0. setting

1. django-admin startproject <project name>
2. vscode로 열기
3. .gitignore 설정
4. python -m venv venv
5. source venv/Scripts/activate
6. pip install django


## 1. project setting

1. django-admin startapp <app name>
2. 앱 등록 (setting.py) - `INSTALLED_APPS` 에서 APP 명 추가
3. 최상단 templates 폴더 만들기
4. templates 경로 등록 (setting.py) - `TEMPLATES` 의 `DIRS` 에 `[BASE_DIR / 'templates']` 추가

## 2. model

1. models.py 작성
```python
class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    # auto_now_add - 생성시 자동으로 현재시간 추가 
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now - 자동으로 현재시간 추가
    updated_at = models.DateTimeField(auto_now=True)
```    
2. python manage.py makemigrations
3. python manage.py migrate



## admin 페이지 들어가기
admin.py 에서
```python
from django.contrib import admin
from .models import Article

# Register your models here.
admin.site.register(Article)
```
- python manage.py createsuperuser




