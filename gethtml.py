#coding=utf-8
import urllib
import json

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

html = getHtml("https://itunes.apple.com/cn/rss/topfreeapplications/limit=2/json")

# file_object = open('app_rank.txt', 'w')
# file_object.write(html)
# file_object.close()

encodedjson = json.loads(html)
# print type(encodedjson)
# print encodedjson

entrys = encodedjson['feed']['entry']

# print type(entrys)

# file_object = open('json.txt', 'w')
# file_object.write(str(entrys))
# file_object.close()
entry = entrys[0]
print type(entry)

print str(entry).decode("unicode-escape").encode("utf-8")

