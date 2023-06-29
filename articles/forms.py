from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    # model = Article 이렇게 하지 않은 이유?
    # 변수에 넣는 것은 어트리뷰트 - 여기에 forms.CharField 와 같은 것들을 넣는것이 올바르지 않다
    class Meta:
        model = Article
        fields = '__all__'

        