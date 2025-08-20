汉王e脸通任意文件读取漏洞检测工具



简介

用于检测汉王e脸通综合管理平台 `/manage/resourceUpload/imgDownload.do` 接口任意文件读取漏洞的Python脚本。



使用方法

\# 检测单个目标

python poc.py -u http://example.com

\# 批量检测

python poc.py -f urls.txt



参数说明

-u/--url: 单个目标URL

-f/--file: 包含多个URL的文件



功能

\- 多线程批量检测

\- 自动保存漏洞结果到result.txt

\- 忽略SSL证书验证



输入文件格式

每行一个URL:

http://target1.com/

https://target2.com:8080/

