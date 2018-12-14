import ast
import requests
import urllib

ke = ['갈리시아어', '구자라트어', '그리스어', '네덜란드어', '네팔어', '노르웨이어', '덴마크어', '독일어', '라오어', '라트비아어', '라틴어', '러시아어',
          '루마니아어', '룩셈부르크어', '리투아니아어', '마라티어', '마오리어', '마케도니아어', '말라가시어', '말라얄람어', '말레이어', '몰타어', '몽골어', '몽어',
          '미얀마어 (버마어)', '바스크어', '베트남어', '벨라루스어', '벵골어', '보스니아어', '불가리아어', '사모아어', '세르비아어', '세부아노', '세소토어', '소말리아어',
          '쇼나어', '순다어', '스와힐리어', '스웨덴어', '스코틀랜드 게일어', '스페인어', '슬로바키아어', '슬로베니아어', '신디어', '신할라어', '아랍어', '아르메니아어',
          '아이슬란드어', '아이티 크리올어', '아일랜드어', '아제르바이잔어', '아프리칸스어', '알바니아어', '암하라어', '에스토니아어', '에스페란토어', '영어', '요루바어', '우르두어',
          '우즈베크어', '우크라이나어', '웨일즈어', '이그보어', '이디시어', '이탈리아어', '인도네시아어', '일본어', '자바어', '조지아어', '줄루어', '중국어', '체와어',
          '체코어', '카자흐어', '카탈로니아어', '칸나다어', '코르시카어', '코사어', '쿠르드어', '크로아티아어', '크메르어', '키르기스어', '타갈로그어', '타밀어', '타지크어',
          '태국어', '터키어', '텔루구어', '파슈토어', '펀자브어', '페르시아어', '포르투갈어', '폴란드어', '프랑스어', '프리지아어', '핀란드어', '하와이어', '하우사어',
          '한국어', '헝가리어', '히브리어', '힌디어']


def naver_translate(srch,before,after):
    k = {'한국어': 'ko',
         '영어': 'en',
         '중국어 간체': 'zh-CN',
         '중국어 번체': 'zh-TW',
         '스페인어': 'es',
         '프랑스어': 'fr',
         '베트남어': 'vi',
         '태국어': 'th',
         '인도네시아어': 'id', }
    try:
        client_id = "eBVkHawd8iCnqtm5cSRa"
        client_secret = "giD28l9evC"
        encText = urllib.parse.quote(srch)
        data = "source={0}&target={1}&text=".format(k[before],k[after]) + encText
        url = "https://openapi.naver.com/v1/papago/n2mt"
        request_url = urllib.request.Request(url)
        request_url.add_header("X-Naver-Client-Id", client_id)
        request_url.add_header("X-Naver-Client-Secret", client_secret)
        response_naver = urllib.request.urlopen(request_url, data=data.encode("utf-8"))
        return ast.literal_eval(response_naver.read().decode('utf-8'))['message']['result']['translatedText']
    except:
        return 0

def kakao_translate(srch,before,after):
    k = {'한국어': 'kr',
         '영어': 'en',
         '일본어': 'jp',
         '중국어': 'cn',
         '베트남어':'vi',
         '인도네시아어': 'id'}
    try:
        params = {'query': srch,
                  'src_lang': k[before],
                  'target_lang': k[after]}
        headers = {'Authorization': 'KakaoAK b167b8ee6ae11b188ec88be00166bcd3'}
        res = requests.get('https://kapi.kakao.com/v1/translation/translate', params=params, headers=headers)
        parse = res.json()
        return parse['translated_text'][0][0]
    except:
        return 0

def google_translate(srch,after):
    k={'﻿갈라시아어': 'gl', '구자라트어': 'gu', '그리스어': 'el', '네덜란드어': 'nl', '네팔어': 'ne', '노르웨이어': 'no', '덴마크어': 'da', '독일어': 'de',
     '라오어': 'lo', '라트비아어': 'lv', '라틴어': 'la', '러시아어': 'ru', '루마니아어': 'ro', '룩셈부르크어': 'lb', '리투아니아어': 'lt', '마라티어': 'mr',
     '마오리어': 'mi', '마케도니아어': 'mk', '말라가시어': 'mg', '말라얄람어': 'ml', '말레이어': 'ms', '몰타어': 'mt', '몽골어': 'mn', '몽어': 'hmn',
     '미얀마어': 'my', '바스크어': 'eu', '베트남어': 'vi', '벨라루스어': 'be', '벵골어': 'bn', '보스니아어': 'bs', '불가리아어': 'bg', '사모아어': 'sm',
     '세르비아어': 'sr', '세부아노': 'ceb', '세소토어': 'st', '소말리아어': 'so', '쇼나어': 'sn', '순다어': 'su', '스와힐리어': 'sw', '스웨덴어': 'sv',
     '스코틀랜드 게일어': 'gd', '스페인어': 'es', '슬로바키아어': 'sk', '슬로베니아어': 'sl', '신디어': 'sd', '신할라어': 'si', '아랍어': 'ar',
     '아르메니아어': 'hy', '아이슬란드어': 'is', '아이티 크리올어': 'ht', '아제르바이잔어': 'az', '아프리칸스어': 'af', '알바니아어': 'sq', '암하라어': 'am',
     '에스토니아어': 'et', '에스페란토어': 'eo', '영어': 'en', '요루바어': 'yo', '우르두어': 'ur', '우즈베크어': 'uz', '우크라이나어': 'uk',
     '웨일즈어': 'cy', '이그보어': 'ig', '이디시어': 'yi', '이탈리아어': 'it', '인도네시아어': 'id', '일본어': 'ja', '자바어': 'jw', '조지아어': 'ka',
     '줄루어': 'zu', '중국어(간체)': 'zh', '중국어(번체)': 'zh-TW', '체와어': 'ny', '체코어': 'cs', '카자흐어': 'kk', '카탈로니아어': 'ca',
     '칸나다어': 'kn', '코르시카어': 'co', '코사어': 'xh', '쿠르드어': 'ku', '크로아티아어': 'hr', '크메르어': 'km', '키르기스어': 'ky', '타갈로그어': 'tl',
     '타밀어': 'ta', '타지크어': 'tg', '태국어': 'th', '터키어': 'tr', '텔루구어': 'te', '파슈토어': 'ps', '펀자브어': 'pa', '페르시아어': 'fa',
     '포르투갈어': 'pt', '폴란드어': 'pl', '프랑스어': 'fr', '프리지아어': 'fy', '핀란드어': 'fi', '하와이어': 'haw', '하우사어': 'ha', '한국어': 'ko',
     '헝가리어': 'hu', '히브리어': 'iw', '힌디어': 'h'}
    try:
        key='AIzaSyB9patcZnecbgjkafup0OlwVRvlogKKUak'
        url='https://translation.googleapis.com/language/translate/v2?q={0}&target={1}&key={2}'.format(srch,k[after],key)
        return requests.get(url).json()['data']['translations'][0]['translatedText']
    except:
        return 0