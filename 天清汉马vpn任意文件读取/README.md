天清汉马VPN任意文件读取漏洞检测工具

本工具用于检测天清汉马VPN设备 /vpn/user/download/client 接口存在的任意文件读取漏洞。通过构造特殊路径遍历Payload尝试读取 /etc/passwd 系统文件来验证漏洞是否存在，支持单目标检测和批量URL检测，测试结果将自动保存至 result.txt。请确保在获得授权后使用，使用者需对测试行为负责。