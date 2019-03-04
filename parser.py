from grab import Grab

g = Grab()
url = 'https://news.yandex.ru/index.rss'
g.go(url)

g.search(u'яндекс'.encode('utf-8'), byte=True)
