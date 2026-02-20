<div align="center">
  <img src="assets/logo.svg" alt="Proxy IP Pool Crawler" width="680"/>

  # Proxy IP Pool Crawler

  **多源免费代理 IP 爬取与验证工具**

  [![Python](https://img.shields.io/badge/Python-3.8+-3776ab?style=flat-square&logo=python&logoColor=white)](https://python.org)
  [![Requests](https://img.shields.io/badge/Requests-HTTP-green?style=flat-square)](https://docs.python-requests.org)
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)
</div>

---

## 项目概述

Proxy IP Pool Crawler 是一个多源免费代理 IP 爬取与验证工具。系统从 6 个公开代理源（89IP、快代理、稻壳代理、开心代理、CheckerProxy、ProxyScrape）批量抓取免费代理 IP，去重后通过多线程并发验证每个代理的 HTTP/HTTPS 可用性（使用 `4.ipw.cn` 作为测试目标），最终输出可用代理池。

## 技术栈

- **Python**: 核心编程语言
- **requests**: HTTP 请求与代理验证
- **lxml**: HTML/XML 解析（XPath 提取）
- **threading**: 多线程并发代理验证
- **re**: 正则表达式提取 IP:Port

## 功能特性

- **6 大代理源** -- 从 89IP、快代理、稻壳代理、开心代理、CheckerProxy、ProxyScrape 批量抓取
- **自动去重** -- 使用 `set()` 对所有来源的代理进行去重
- **多线程验证** -- 为每个代理创建独立线程，并发验证 HTTP 和 HTTPS 可用性
- **双协议检测** -- 分别测试 HTTP 和 HTTPS 代理，区分仅 HTTP、仅 HTTPS、双协议可用
- **超时控制** -- 验证请求设置 5 秒超时，快速淘汰不可用代理
- **耗时统计** -- 每个代理源记录爬取耗时，方便性能分析

## 代理源详情

| 代理源 | 函数名 | 类型 | 说明 |
|:---|:---|:---|:---|
| 89IP | `八九IP()` | API | 批量获取免费代理，支持数量参数 |
| 快代理 | `快代理()` | 网页爬取 | 国内高匿 + 国内普通，各 7 页 |
| 稻壳代理 | `稻壳代理()` | JSON API | `docip.net` 免费代理接口 |
| 开心代理 | `开心代理()` | 网页爬取 | XPath 解析，国内高匿 + 普通各 50 页 |
| CheckerProxy | `Checking_roxy_servers()` | JSON API | 国际代理源，获取最新归档 |
| ProxyScrape | `proxyscrape()` | JSON API | 大规模代理列表（需科学上网） |

> 注：`小幻代理` 因 Cloudflare 验证已注释禁用。

## 安装说明

1. 克隆仓库到本地：
   ```bash
   git clone https://github.com/Past-Tang/proxy-ip-pool.git
   cd proxy-ip-pool
   ```

2. 安装依赖：
   ```bash
   pip install requests lxml
   ```

## 使用方法

### 完整流程（爬取 + 验证）
```bash
python main.py
```

运行后系统会：
1. 依次从 6 个代理源爬取免费代理 IP
2. 对所有代理去重
3. 多线程并发验证每个代理的 HTTP/HTTPS 可用性
4. 输出可用代理数量

### 单独验证已有代理列表
```bash
python verify_proxy.py
```

### 测试 CheckerProxy 源
```bash
python test_checker.py
```

## 项目结构

```
proxy-ip-pool/
├── main.py              # 主程序（223行）：6 源爬取 + 多线程验证
│   ├── 八九IP()          # 89IP 代理源
│   ├── 快代理()          # 快代理网页爬取
│   ├── 稻壳代理()        # 稻壳代理 JSON API
│   ├── 开心代理()        # 开心代理网页爬取
│   ├── proxyscrape()    # ProxyScrape API
│   ├── Checking_roxy_servers()  # CheckerProxy API
│   └── verify_proxy()   # 多线程代理验证
├── verify_proxy.py      # 独立代理验证脚本（54行）
├── test_checker.py      # CheckerProxy 测试脚本（12行）
├── assets/
│   └── logo.svg         # 项目 Logo
├── LICENSE              # MIT 许可证
└── README.md
```

## 核心流程

```
启动 -> 依次爬取 6 个代理源:
        ├── 89IP (API 批量获取)
        ├── 快代理 (网页爬取 14 页)
        ├── 稻壳代理 (JSON API)
        ├── 开心代理 (网页爬取 100 页)
        ├── CheckerProxy (JSON 归档)
        └── ProxyScrape (JSON API)
     -> 去重 (set)
     -> 多线程并发验证:
        ├── HTTP 测试 (http://4.ipw.cn/, 5s 超时)
        ├── HTTPS 测试 (https://4.ipw.cn/, 5s 超时)
        └── 分类存储 (HTTP/HTTPS/双协议)
     -> 输出可用代理池
```

## 验证机制

每个代理通过两个独立测试判断可用性：

| 测试 | 目标 URL | 超时 | 判断标准 |
|:---|:---|:---|:---|
| HTTP | `http://4.ipw.cn/` | 5 秒 | HTTP 200 |
| HTTPS | `https://4.ipw.cn/` | 5 秒 | HTTP 200 |

验证结果分为四类：
- **双协议可用**: HTTP + HTTPS 均通过
- **仅 HTTP 可用**: 仅 HTTP 测试通过
- **仅 HTTPS 可用**: 仅 HTTPS 测试通过
- **不可用**: 两项测试均失败（丢弃）

## 依赖项

| 包 | 用途 |
|:---|:---|
| requests | HTTP 请求与代理验证 |
| lxml | HTML 解析（XPath） |

## 常见问题

### ProxyScrape 源获取失败？
ProxyScrape 需要科学上网环境才能访问。如果无法访问，可以在 `main()` 函数中注释掉 `proxyscrape()` 调用。

### 快代理爬取速度慢？
快代理有反爬机制，每页请求间隔 5 秒。14 页共需约 70 秒。

### 验证后可用代理很少？
免费代理可用率通常较低（5%-15%），这是正常现象。可以增加代理源或降低超时阈值来调整。

### 如何使用验证后的代理？
可用代理存储在 `TrueIp` 列表中，格式为 `{"http": "ip:port"}` 或 `{"https": "ip:port"}`，可直接传递给 `requests.get(proxies=...)` 使用。

## 安全注意事项

- 免费代理的安全性无法保证，不建议通过免费代理传输敏感数据
- 部分代理源网站可能有访问频率限制，请合理设置爬取间隔
- 使用代理时请遵守目标网站的 robots.txt 和服务条款

## 许可证

[MIT License](LICENSE)

## 免责声明

本工具仅供学习研究使用，请遵守相关法律法规。使用免费代理存在安全风险，使用者需自行承担所有责任。