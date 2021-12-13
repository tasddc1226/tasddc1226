import feedparser, datetime

tistory_blog_url = "https://tasddc.tistory.com"
feed = feedparser.parse(tistory_blog_url+"/rss")

markdown_text = """

## PS Boj Tier
[![Solved.ac Profile](http://mazassumnida.wtf/api/v2/generate_badge?boj=tasddc)](https://solved.ac/tasddc/)

## My Github Status
<img src="https://github-readme-stats.vercel.app/api?username=tasddc1226&show_icons=true&hide_border=true&theme=tokyonight"/>
 
### Total Visitor
![](https://komarev.com/ghpvc/?username=tasddc1226&color=red&style=plastic)

<hr/>  

## Recent My Posts
"""

lst = []

for i in feed['entries']:
    dt = datetime.datetime.strptime(i['published'], "%a, %d %b %Y %H:%M:%S %z").strftime("%b %d, %Y")
    markdown_text += f"[{i['title']}]({i['link']}) - {dt}</br>\n"
    print(i['link'], i['title'])

f = open("README.md", mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
