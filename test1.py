# 豆瓣实战
# 写正则表达式

import re
import requests

url = 'https://movie.douban.com/'
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
}

res = requests.get(url=url, headers=headers)

if res.status_code == 200:
    res_html = res.text
    with open("dou ban.html","w", encoding="utf-8") as fp:
        fp.write(res_html)
    reg_name = 'href="https://movie.douban.com/subject/\d+/">(.*?)</a></td>'
    res = re.findall(reg_name, res_html)
    print(res, sep='\n')
    for i in res:
        print(i, sep='\n')

    reg_url = 'href="(.*?)">(\S+)</a></td>'
    res = re.findall(reg_url, res_html)
    print(res)

