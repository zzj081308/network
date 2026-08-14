import telnetlib3
import time

def 假装进度条():
    time.sleep(0.5)
    print(".", end="")
    time.sleep(0.5)
    print(".", end="")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)

host = '192.168.200.10'
username = 'huawei'
password = 'Zzj123456@'

print("开始登录",end="")
假装进度条()

print("发起telnet请求")
time.sleep(1)
tn = telnetlib3.Telnet(host)
print(f'telnet {host}')
time.sleep(1)

print(f'输入用户名：',end="")
time.sleep(1)
tn.read_until(b'Username:')
tn.write(username.encode('ascii') + b'\n')
print(username)
time.sleep(1)

print("输入密码：",end="")
time.sleep(1)
tn.read_until(b'Password:')    #读取，直到读到Password:为止，b：二进制字节。telnet输出位二进制字节
tn.write(password.encode('ascii') + b'\n')    #写入密码并回车
print(password)
time.sleep(1)

print("新的登录，要修改密码吗[Y/N]：",end="")
time.sleep(1)
tn.read_until(b'[Y/N]:')
tn.write(b'n\n')
print("n")
time.sleep(1)
tn.read_until(b'n')

print("即将进入",end="")
假装进度条()

print(tn.read_until(b'<SW5>').decode('ascii'))    #打印路由器的显示直到出现<SW5>，即路由器输出完了
tn.close()