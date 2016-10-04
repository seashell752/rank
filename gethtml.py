#coding=utf-8
import urllib
import json
from App import App

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

# html = getHtml("https://itunes.apple.com/cn/rss/topfreeapplications/limit=2/json")

# file_object = open('app_rank.txt', 'w')
# file_object.write(html)
# file_object.close()

file_object = open('app_rank.txt', 'r')
html = file_object.read()
file_object.close()


encodedjson = json.loads(html)
# print type(encodedjson)
# print encodedjson

entrys = encodedjson['feed']['entry']

print type(entrys)

# file_object = open('json.txt', 'w')
# file_object.write(str(entrys))
# file_object.close()

# entry = entrys[0]
# print type(entry)

# print str(entry).decode("unicode-escape").encode("utf-8")
apps = []
i = 1
for entry in entrys:
    app = App()
    app.name = entry['im:name']['label']
    print app.name
    app.image = entry['im:image'][0]['label']
    print app.image
    app.summary = entry['summary']['label']
    print app.summary
    app.link = entry['link']['attributes']['href']
    print app.link
    app.bundleId = entry['id']['attributes']['im:bundleId']
    print app.bundleId
    app.category = entry['category']['attributes']['label']
    print app.category
    app.releaseDate = entry['im:releaseDate']['attributes']['label']
    print app.releaseDate
    app.rank = i
    print app.rank
    i = i + 1
    apps.append(app)


