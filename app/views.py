import ast
import urllib

from django.shortcuts import render
from requests.utils import quote
from app.item.nkg_translation import google_translate,kakao_translate,naver_translate,ke

# Create your views here.
from app.item.search_all import *


def main(request,division):
    if request.method == 'POST':
        data=None
        word = request.POST['keyword']
        if division == 1:
            data = search(word)
        elif division == 2:
            data = shopping(word)
        elif division == 3:
            data = dictionary(word)
        # elif division == 4:
        #     data = new_search(word)
        # elif division == 5:
        #     data = new_search(word)
        elif division == 6:
            data = book(word)
        elif division == 7:
            data = video(word)
        elif division == 8:
            data = music(word)
        return render(
            request,
            'app/index.html',
            { 'list' : data[0],
              'url' : data[1],
              'word': word,
              'method':request.method,
              'sw':'1',
              'division':division
              }
        )

    else:
        return render(
            request,
            'app/index.html',
            {
            'method':request.method,
            'division': division
             }
        )

def translate(request):

    if request.method == 'POST':
        srch=request.POST['srch']
        before = request.POST['before']
        after = request.POST['after']
        service_list = ['naver','kakao','google']
        naver = naver_translate(srch,before,after)
        print(naver)
        kakao = kakao_translate(srch,before,after)
        google = google_translate(srch,after)
        list = [naver,kakao,google]
        true_list = [(v,service_list[i]) for i,v in enumerate(list) if 0!=v]
        print(true_list)
        return render(
            request,
            'app/translate.html',
            {
                'df':'한국어',
                'df2':'영어',
                'data':true_list,
                'ke':ke,
                'srch':srch,
                'method': request.method,
            }
        )
    else:
        return render(
            request,
            'app/translate.html',
            {
                'df': '한국어',
                'df2': '영어',
                'ke': ke,
                'method': request.method,
            }
        )

def contact(request):
    return render(
        request,
        'app/contact.html',
        {}
    )