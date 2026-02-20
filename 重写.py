import pickle
import re
import time
from concurrent.futures import ThreadPoolExecutor
from threading import Thread
import lxml.etree as HTML
import requests

ipPoolNotVerified = []
TrueIp = []


def 八九IP():  # 89ip
    start_time = time.perf_counter()

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Referer": "https://www.89ip.cn/ti.html",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    }
    [ipPoolNotVerified.append(i) for i in re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}:\d+\b',
                                                     requests.get("https://www.89ip.cn/tqdl.html", headers=headers,
                                                                  params={"num": "9999", "address": "",
                                                                          "kill_address": "", "port": "",
                                                                          "kill_port": "", "isp": ""}).text)]
    end_time = time.perf_counter()
    running_time = end_time - start_time
    print("运行时间为：", running_time, "秒")




def 快代理():
    start_time = time.perf_counter()
    headers = {
        "Referer": "https://www.kuaidaili.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    }
    for i in range(1, 8):
        response = requests.get(url=f"https://www.kuaidaili.com/free/intr/{i}/", headers=headers)
        IP = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', re.findall('fpsList = \[(.*?)];', response.text)[0])
        Port = re.findall(r'"port":\s*"(\d+)"', re.findall('fpsList = \[(.*?)];', response.text)[0])
        [ipPoolNotVerified.append(i) for i in [i + ":" + j for i, j in zip(IP, Port)]]
        time.sleep(5)
    for i in range(1, 8):
        response = requests.get(url=f"https://www.kuaidaili.com/free/inha/{i}/", headers=headers)
        IP = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', re.findall('fpsList = \[(.*?)];', response.text)[0])
        Port = re.findall(r'"port":\s*"(\d+)"', re.findall('fpsList = \[(.*?)];', response.text)[0])
        [ipPoolNotVerified.append(i) for i in [i + ":" + j for i, j in zip(IP, Port)]]
        time.sleep(5)
    end_time = time.perf_counter()
    running_time = end_time - start_time

    print("运行时间为：", running_time, "秒")



def 稻壳代理():
    start_time = time.perf_counter()
    [ipPoolNotVerified.append(i['ip']) for i in requests.get(url="https://www.docip.net/data/free.json").json()['data']]

    end_time = time.perf_counter()
    running_time = end_time - start_time

    print("运行时间为：", running_time, "秒")



def 开心代理():
    start_time = time.perf_counter()
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
    }
    for i in range(1, 50):
        response=requests.get(f"http://www.kxdaili.com/dailiip/1/{i}.html", headers=headers)
        response.encoding = 'utf-8'
        response = HTML.HTML(response.text)
        IP = response.xpath('//table/tbody/tr[1]/td[1]/text()')
        Port = response.xpath('//table/tbody/tr[1]/td[2]/text()')
        [ipPoolNotVerified.append(i) for i in [i + ":" + j for i, j in zip(IP, Port)]]
    for i in range(1, 50):
        response = requests.get(f"http://www.kxdaili.com/dailiip/2/{i}.html", headers=headers)
        response.encoding = 'utf-8'
        response = HTML.HTML(response.text)
        IP = response.xpath('//table/tbody/tr[1]/td[1]/text()')
        Port = response.xpath('//table/tbody/tr[1]/td[2]/text()')
        [ipPoolNotVerified.append(i) for i in [i + ":" + j for i, j in zip(IP, Port)]]
    end_time = time.perf_counter()
    running_time = end_time - start_time

    print("运行时间为：", running_time, "秒")

def proxyscrape():
    start_time = time.perf_counter()
    params = {
        "request": "getproxies",
        "country": "",
        "protocol": "http",
        "skip": "30",
        "proxy_format": "protocolipport",
        "format": "json",
        "limit": "150000",
        "timeout": "20000"
    }
    response = requests.get("https://api.proxyscrape.com/v3/free-proxy-list/get", params=params)
    for i in response.json()["proxies"]:
        ipPoolNotVerified.append(str(i['ip']) + ":" + str(i['port']))
    end_time = time.perf_counter()
    running_time = end_time - start_time

    print("运行时间为：", running_time, "秒")


def 小幻代理():
    import requests
    import lxml.etree as HTML
    import re
    headers = {
        "referer": "https://ip.ihuan.me/today.html",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    }
    url = "https://ip.ihuan.me/today.html"
    response = requests.get(url, headers=headers)
    response = HTML.HTML(response.text)
    response = requests.get('https://ip.ihuan.me' + response.xpath("/html/body//div[2]/div/div/div[1]/a/@href")[0],
                            headers=headers)
    pattern = r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d+)"
    matches = re.findall(pattern, response.text)
    for match in matches:
        ipPoolNotVerified.append(match)


def Checking_roxy_servers():
    start_time = time.perf_counter()
    headers = {
        "referer": "https://ip.ihuan.me/today.html",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    }
    url = "https://checkerproxy.net/getAllProxy"
    response = requests.get(url, headers=headers)
    response = HTML.HTML(response.text)
    response = requests.get('https://checkerproxy.net/api/archive/' + str(
        response.xpath('//*[@id="app"]/div[2]/center/div/ul/li[1]/a/@href')[0]).replace('/archive/', '', ),
                            headers=headers)
    for match in response.json():
        ipPoolNotVerified.append(match['addr'])
    end_time = time.perf_counter()
    running_time = end_time - start_time

    print("运行时间为：", running_time, "秒")


def main():
    八九IP()
    快代理()
    稻壳代理()
    开心代理()
    Checking_roxy_servers()
    proxyscrape()#需要科学环境
    #小幻代理()#有cf验证


def verify_proxy(proxy):
    # 代理地址
    pro = proxy
    proxies = {
        'http': f'http://{pro}',
        'https': f'http://{pro}',
    }

    # 初始化代理可用性标志
    http_proxy_available = False
    https_proxy_available = False

    # 尝试通过HTTP代理访问
    try:
        if requests.get('http://4.ipw.cn/', proxies={'http': proxies['http']}, timeout=5).status_code == 200:
            http_proxy_available = True
    except:
        pass

    # 尝试通过HTTPS代理访问
    try:
        if requests.get('https://4.ipw.cn/', proxies={'https': proxies['https']}, timeout=5).status_code == 200:
            https_proxy_available = True
    except:
        pass

    # 根据代理可用性打印结果
    if http_proxy_available and https_proxy_available:
        print(f'HTTP/HTTPS代理均可用')
        TrueIp.append({"http": proxy})
        TrueIp.append({"https": proxy})
    elif http_proxy_available:
        TrueIp.append({"http": proxy})
        print(f'仅HTTP代理可用')
    elif https_proxy_available:
        TrueIp.append({"https": proxy})
        print(f'仅HTTPS代理可用')
    else:
        pass
        #print(f'HTTP/HTTPS代理均不可用')



if __name__ == '__main__':
    main()
    ipPoolNotVerified = list(set(ipPoolNotVerified))

    print(len(ipPoolNotVerified))
    print(ipPoolNotVerified)
    # 创建并启动线程
    threads = []
    for proxy in ipPoolNotVerified:
        thread = Thread(target=verify_proxy, args=(proxy,))
        threads.append(thread)
        thread.start()

    # 等待所有线程完成
    for thread in threads:
        thread.join()
    print(len(TrueIp))
