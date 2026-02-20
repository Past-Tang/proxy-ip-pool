import requests
import lxml.etree as HTML
headers = {
    "referer": "https://ip.ihuan.me/today.html",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}
url = "https://checkerproxy.net/getAllProxy"
response = requests.get(url, headers=headers)
response = HTML.HTML(response.text)
response = requests.get('https://checkerproxy.net/api/archive/'+str(response.xpath('//*[@id="app"]/div[2]/center/div/ul/li[1]/a/@href')[0]).replace('/archive/','',), headers=headers)
for match in response.json():
    print(match['addr'])