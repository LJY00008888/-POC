Geoserver敏感信息泄露漏洞检测工具
简介
用于检测Geoserver Configuration API敏感信息泄露漏洞(CVE-2025-27505)的Python脚本。

使用方法
检测单个目标
python poc.py -u http://example.com

批量检测
python poc.py -f urls.txt

参数说明
-u/--url: 单个目标URL
-f/--file: 包含多个URL的文件

功能
- 多线程批量检测
- 自动保存漏洞结果到`敏感信息泄露漏洞.txt`
- 忽略SSL证书验证

输入文件格式
每行一个URL:
http://target1.com/
https://target2.com:8080/

漏洞说明
Geoserver的`/geoserver/rest.html`接口存在敏感信息泄露漏洞，攻击者可以通过访问此接口获取Geoserver的配置信息，可能导致敏感数据泄露。

免责声明
本POC仅用于安全检测目的，使用者应遵守相关法律法规，不得用于非法用途。使用者应对其行为负责，与作者无关。