from urllib.parse import quote


def search(word):
    url = {'네이버': 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=',
           '구글': 'https://www.google.co.kr/search?ei=o-UIXOyzLM3N-Qbf1JjQBQ&q=',
           '다음': 'https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&q=',
           '클리앙': 'https://www.clien.net/service/search?q=',
           '디씨인사이드': 'http://search.dcinside.com/post/q/',
           '나무위키': 'https://namu.wiki/search/',
           '트위터': 'https://twitter.com/search?f=tweets&q=',
           '인스타': 'https://www.instagram.com/explore/tags/',
           '네이트': 'https://search.daum.net/nate?thr=sbma&w=tot&q=',
           '유튜브': 'https://www.youtube.com/results?search_query=',
           '루리웹': 'http://bbs.ruliweb.com/search?q=',
           '뽐뿌': 'http://www.ppomppu.co.kr/search_bbs.php?keyword=',
           '오늘의유머': 'http://www.todayhumor.co.kr/board/list.php?kind=search&keyfield=subject&keyword='}
    engine_list = list(url.keys())
    url_list = [url[i] + quote(word) for i in engine_list]
    return engine_list, url_list


def new_search(word):
    url = {
        '조선일보': 'http://search.chosun.com/search/news.search?query={0}&orderby=&naviarraystr=&kind=&cont1=&cont2=&cont5=&categoryname=&categoryd2=&c_scope=news&sdate=&edate=&premium=',
        '동아일보': 'http://news.donga.com/search?query={0}&x=0&y=0',
        '중앙일보': 'https://search.joins.com/?keyword={0}',
        '한국일보': 'http://search.hankookilbo.com/v2/?sword={0}&stype=&ssort=1&sdate=&edate=&sfield=&cate_str=&PID=dreamwiz&ptn_name=hankookilbo&cddtc=hankookilbo',
        '경향신문': 'http://search.khan.co.kr/search.html?r=3&q={0}',
        '서울신문': 'http://search.seoul.co.kr/index.php?keyword={0}',
        '한겨레': 'http://search.hani.co.kr/Search?keyword={0}',
        '국민일보': 'http://www.kmib.co.kr/search/searchResult.asp?searchWord={0}%20ark',
        '세계일보': 'http://search3.segye.com/?searchWord={0}',
        '문화일보': 'http://search.munhwa.com/main.jsp?q={0}',
        '내일신문': 'https://www.naeil.com/search/?tsearch={0}&x=0&y=0',
        '신아일보': 'http://www.shinailbo.co.kr/engine_yonhap/search.php?picktab=all&searchcont=photo&div_code=&others_cont_type=&orgsearchword={0}&page=1&sort=&cust_div_code=&searchword={0}',
        '아시아투데이': 'http://www.asiatoday.co.kr/kn_search.php?sword={0}',
        '천지일보': 'http://www.newscj.com/news/articleList.html?sc_area=A&view_type=sm&sc_word={0}',
    }
    engine_list = list(url.keys())
    url_list = [url[i].format(quote(word)) for i in engine_list]
    return engine_list, url_list


def music(word):
    url = {
        '네이버 뮤직': 'https://music.naver.com/search/search.nhn?query={0}&x=0&y=0',
        '멜론': 'https://www.melon.com/search/total/index.htm?q={0}&section=&linkOrText=T&ipath=srch_form',
        '벅스': 'https://music.bugs.co.kr/search/integrated?q={0}',
        '엠넷닷컴': 'http://search.mnet.com/search/index.asp?q={0}',
        '올레 뮤직': 'http://www.ollehmusic.com/#/Search_new/f_Total_Search.asp?cate=all&searchQuery={0}',
        '유튜브 뮤직': 'https://music.youtube.com/search?q={0}',
        '지니뮤직': 'http://www.genie.co.kr/search/searchMain?query={0}'
    }
    engine_list = list(url.keys())
    url_list = [url[i].format(quote(word)) for i in engine_list]
    return engine_list, url_list


def shopping(word):
    url = {
        '네이버': 'https://search.shopping.naver.com/search/all.nhn?query={0}&cat_id=&frm=NVSHATC',
        '옥션': 'http://browse.auction.co.kr/search/empty?keyword={0}',
        'G마켓': 'http://search.gmarket.co.kr/search.aspx?selecturl=total&sheaderkey=&gdlc=&SearchClassFormWord=goodsSearch&keywordOrg=&keywordCVT=&keywordCVTi=&keyword={0}',
        '11번가': 'http://search.11st.co.kr/Search.tmall?kwd={0}',
        '인터파크': 'http://isearch.interpark.com/isearch?q={0}',
        '위메프': 'http://search.wemakeprice.com/search?search_cate=top&search_keyword={0}&_service=5&_type=3',
        '쿠팡': 'https://www.coupang.com/np/search?component=&q={0}&channel=user',
        '티몬': 'http://search.ticketmonster.co.kr/search/?keyword={0}&thr=ts',
        '큐텐': 'https://directjapan.qoo10.com/gmkt.inc/GlobalQShop/SpecialShop.aspx?siteid=directjapan&keyword={0}',
        '아마존': 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords={0}',
        '알리익스프레스': 'https://ko.aliexpress.com/wholesale?catId=0&initiative_id=SB_20181211221836&SearchText={0}',
        '다나와': 'http://search.danawa.com/dsearch.php?k1={0}&module=goods&act=dispMain'
    }
    engine_list = list(url.keys())
    url_list = [url[i].format(quote(word)) for i in engine_list]
    return engine_list, url_list


def book(word):
    url = {
        '알라딘': 'https://www.aladin.co.kr/search/wsearchresult.aspx?SearchTarget=All&SearchWord={0}&x=0&y=0',
        'yes24': 'http://www.yes24.com/searchcorner/Search?keywordAd=&keyword=&domain=ALL&qdomain=%C0%FC%C3%BC&Wcode=001_005&query={0}',
        '교보문고': 'http://www.kyobobook.co.kr/search/SearchCommonMain.jsp?vPstrCategory=TOT&vPstrKeyWord={0}&vPplace=top',
        '영풍': 'http://www.ypbooks.co.kr/search.yp?query={0}'
    }
    engine_list = list(url.keys())
    url_list = [url[i].format(quote(word)) for i in engine_list]
    return engine_list, url_list


def video(word):
    url = {
        '유튜브': 'https://www.youtube.com/results?search_query={0}',
        '판도라': 'http://www.pandora.tv/search/searchResult?query={0}',
        '네이버': 'https://search.naver.com/search.naver?where=video&sm=tab_jum&query={0}',
        '다음': 'https://search.daum.net/search?w=vclip&nil_search=btn&DA=NTB&enc=utf8&q={0}',
        '구글': 'https://www.google.co.jp/search?q={0}&source=lnms&tbm=vid&sa=X&ved=0ahUKEwjo-7-m4pnfAhVDdXAKHVNgBkAQ_AUIDigB&biw=1280&bih=579&dpr=2'
    }
    engine_list = list(url.keys())
    url_list = [url[i].format(quote(word)) for i in engine_list]
    return engine_list, url_list


def dictionary(word):
    url = {
        '네이버': 'https://terms.naver.com/search.nhn?query={0}',
        '다음': 'http://100.daum.net/search/entry?q={0}',
        '위키피디아': 'https://ko.wikipedia.org/wiki/{0}'
    }
    engine_list = list(url.keys())
    url_list = [url[i].format(quote(word)) for i in engine_list]
    return engine_list, url_list

