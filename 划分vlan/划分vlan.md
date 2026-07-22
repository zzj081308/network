# 划分vlan



## 1.网络拓扑

先拉几台pc，一台交换机：

![](pic\Snipaste_2026-07-22_13-14-29.png)

分别配ip：

10.0.0.1、10.0.0.2、10.0.0.3、10.0.0.4

掩码255.0.0.0

## 2.基于接口划分

### 创建vlan

进入交换机，创建vlan

```shell
sys
vlan batch 10 20
```

![](pic\Snipaste_2026-07-22_13-22-29.png)

当前vlan表：

![](pic\Snipaste_2026-07-22_13-25-11.png)

### 给接口配vlan

使得pc1，pc3在同一个vlan中：

```shell
int g0/0/1
port hybrid pvid vlan 10
port hybrid untagged vlan 10
int g0/0/3
port hybrid pvid vlan 10
port hybrid untagged vlan 10
```

接口类型是hybrid，混合口，兼具access和trunk，既可以打标签，也可以去标签

port hybrid pvid vlan 10	打标签

port hybrid untagged vlan 10	去标签

相关：

- `port link-type hybrid`：将接口设置为 Hybrid 模式。
- `port hybrid pvid vlan X`：设置端口的缺省 VLAN 为 X（处理接收的无标签帧）。
- `port hybrid tagged vlan X Y`：允许 VLAN X、Y 通过，且发送时**保留**标签。
- `port hybrid untagged vlan X Y`：允许 VLAN X、Y 通过，且发送时**剥离**标签。

ping测试：

![](pic\Snipaste_2026-07-22_13-46-44.png)

当前vlan表：
![](pic\Snipaste_2026-07-22_13-48-05.png)

## 3.基于接口划分（trunk和access）

### 网络拓扑图

![](pic\Snipaste_2026-07-22_14-28-02.png)

分别配10.0.0.1、10.0.0.2

掩码255.0.0.0

交换机与交换机之间接口用trunk，带tag转发

接入终端接口用access，去掉tag

### 终端接口配置access

```shell
vlan 10
q
interface
port link-type access
port default vlan 10
```

先创建vlan 10

退出

配置接口类型为access

接口绑定vlan 10

即收到终端发来的不带tag的数据打上vlan 10，收到交换机发来的带tag vlan 10的数据去掉标签

### 交换机之间配置trunk

```shell
vlan 10
q
interface
port link-type trunk
port trunk allow-pass vlan 10
```

创建 vlan 10

退出

配置接口类型为trunk

放行vlan 10的流量

# 实例：

![](pic\Snipaste_2026-07-22_15-55-42.png)

```shell
PC1：
ipv4:192.168.1.1
子网掩码:255.255.255.0
vlan:10
```

```shell
PC2：
ipv4:192.168.1.2
子网掩码:255.255.255.0
vlan:10
```

```shell
PC3：
ipv4:192.168.2.1
子网掩码:255.255.255.0
vlan:20
```

```shell
PC4：
ipv4:192.168.2.2
子网掩码:255.255.255.0
vlan:20
```

```shell
SW1:
system-view
undo info-center enable
sysname SW1
vlan batch 10 20
interface GigabitEthernet 0/0/1
port link-type access
port default vlan 10
quit
interface GigabitEthernet 0/0/2
port link-type access
port default vlan 10
quit
interface GigabitEthernet 0/0/3
port link-type trunk
port trunk allow-pass vlan 10 20
```

```shell
SW2:
system-view
undo info-center enable
sysname SW2
vlan batch 10 20
interface GigabitEthernet 0/0/1
port link-type access
port default vlan 20
quit
interface GigabitEthernet 0/0/2
port link-type access
port default vlan 20
quit
interface GigabitEthernet 0/0/3
port link-type trunk
port trunk allow-pass vlan 10 20
```

SW1的vlan配置：
![](pic\Snipaste_2026-07-22_16-06-58.png)

SW2的vlan配置：
![](pic\Snipaste_2026-07-22_16-33-40.png)

# 配置三层网关互通vlan：

但还需要再加一台交换机SW3

![](pic\Snipaste_2026-07-22_16-35-30.png)

```shell
SW3
system-view
undo info-center enable
sysname SW3
vlan batch 10 20
interface Vlanif 10
ip address 192.168.1.254 24
interface Vlanif 20
ip address 192.168.2.254 24
interface GigabitEthernet 0/0/1
port link-type trunk
port trunk allow-pass vlan 10 20
interface GigabitEthernet 0/0/2
port link-type trunk
port trunk allow-pass vlan 10 20
```

此外，还需要在各个PC上加上网关

PC1，PC2：192.168.1.254

PC3，PC4：192.168.2.254

vlan 10和vlan 20即可互通

SW3路由表：

![](pic\Snipaste_2026-07-22_16-42-13.png)