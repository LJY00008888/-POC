孚盟云CRM SQL注入漏洞检测工具

简介
用于检测孚盟云CRM系统 `/Common/GetIcon.aspx` 接口SQL注入漏洞的Python脚本。

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
- 自动保存漏洞结果到result.txt
- 忽略SSL证书验证

输入文件格式
每行一个URL:
http://target1.com/
https://target2.com:8080/