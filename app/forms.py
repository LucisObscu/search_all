from django import forms

class SearchForm(forms.Form):
    search_word = forms.CharField()
#Forms.py 캐릭터필드가 인풋테그로 변환
