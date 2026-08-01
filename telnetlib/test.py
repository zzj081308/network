import telnetlib3

host = '192.168.100.10'
password = 'huawei@123'

tn = telnetlib3.Telnet(host)
tn.read_until(b'Password:')    #读取，直到读到Password:为止，b：二进制字节。telnet输出位二进制字节
tn.write(password.encode('ascii') + b'\n')    #写入密码并回车
print(tn.read_until(b'<Huawei>').decode('ascii'))    #打印路由器的显示直到出现<Huawei>，即路由器输出完了
tn.close()
