import requests
from threading import Thread

# 代理验证函数
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
        if requests.get('http://4.ipw.cn/', proxies={'http': proxies['http']}, timeout=2).status_code == 200:
            http_proxy_available = True
    except:
        pass

    # 尝试通过HTTPS代理访问
    try:
        if requests.get('https://4.ipw.cn/', proxies={'https': proxies['https']}, timeout=2).status_code == 200:
            https_proxy_available = True
    except:
        pass

    # 根据代理可用性打印结果
    if http_proxy_available and https_proxy_available:
        print(f'HTTP/HTTPS代理均可用')
    elif http_proxy_available:
        print(f'仅HTTP代理可用')
    elif https_proxy_available:
        print(f'仅HTTPS代理可用')
    else:
        print(f'HTTP/HTTPS代理均不可用')


proxies =['117.160.250.138:80', '118.120.209.175:41122', '5.161.50.72:8080', '117.160.250.133:8899', '45.95.203.137:4444', '114.103.80.244:8089', '111.26.177.28:9091', '146.56.154.83:21000', '114.156.77.107:4343', '218.67.30.191:8089', '157.10.80.218:80', '45.90.216.44:4444', '223.100.178.167:9091', '183.166.136.46:41122', '47.74.226.8:5001', '117.1.97.5:4008', '114.106.171.72:8089', '171.250.96.22:4003', '104.129.192.32:8800', '114.106.134.4:8089', '175.10.102.192:7890', '185.247.18.200:8888', '117.1.195.104:4010', '171.234.226.86:4006', '117.69.159.143:41122', '114.106.146.196:8089', '14.103.24.20:8000', '47.243.92.199:3128', '94.182.146.250:8080', '183.166.171.204:41122', '112.3.21.226:8060', '120.37.121.209:9091', '37.1.199.18:80', '114.156.77.107:8080', '180.123.164.205:8089', '117.1.195.104:4007', '185.162.60.6:8080', '120.197.40.219:9002', '102.132.38.71:8080', '52.13.248.29:3128', '104.129.194.46:8800', '117.1.97.5:4005', '66.225.246.238:8080', '114.106.173.207:8089', '117.69.237.203:8089', '207.246.105.172:8899', '45.95.203.129:4444', '120.234.203.171:9002', '27.158.54.230:8089', '117.70.49.223:8089']


# 创建并启动线程
threads = []
for proxy in proxies:
    thread = Thread(target=verify_proxy, args=(proxy,))
    threads.append(thread)
    thread.start()

# 等待所有线程完成
for thread in threads:
    thread.join()