import sys 
from bs4 import BeautifulSoup
from urllib import parse
from urllib import request

def GetTitle(question_word):

    url = parse.quote('http://cn.bing.com/search?q='+question_word, safe='/:?=' )

    req = request.Request(
    url, 
    data=None, 
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        }
    )

    htmlpage = request.urlopen(req).read().decode('utf8')

    soup = BeautifulSoup(htmlpage,'html.parser')

    res = soup.find_all('strong')


    NeedAutoCorrection = False

    if htmlpage.find('<div>????? <a') != -1:
        NeedAutoCorrection = True

    return res, NeedAutoCorrection

def CheckCorrectness(res, question_word):

    counter = 0

    for highlightWords in res:
        content = highlightWords.get_text()

        if content.find(question_word) != -1:
            counter += 1

    if counter > 3:
        return True
    else:
        return False
