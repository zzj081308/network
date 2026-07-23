# stp生成树协议

## 网络拓扑图

![](pic/Snipaste_2026-07-23_23-41-50.png)

华为交换机默认使用mstp协议

```shell
system-view
display stp
```

![](pic/Snipaste_2026-07-23_23-44-29.png)

可以修改为stp模式

```shell
stp mode stp
```

![](pic/Snipaste_2026-07-23_23-46-39.png)

可以自定义主/备根桥：
主根桥优先级0，备根桥优先级4096

```shell
stp root primary
stp root secondary
```

也可手动修改优先级：优先级默认32768，但已经设为主备根桥的设备不能修改优先级

```shell
stp priority 4096
```

![](pic/Snipaste_2026-07-24_00-03-28.png)

设置接口路径开销：

![](pic/Snipaste_2026-07-24_00-07-47.png)

```shell
interface GigabitEthernet 0/0/1
stp cost 123
```

![](pic/Snipaste_2026-07-24_00-11-40.png)

设置接口优先级：

需为16倍数

```shell
interface GigabitEthernet 0/0/1
stp port priority 16
display stp interface GigabitEthernet 0/0/1
```

![](pic/Snipaste_2026-07-24_00-16-32.png)

开启/关闭生成树协议：默认开启，可全局开关，也可进到接口开关

```shell
stp enable
stp disable
```

最后查看接口状态：

```shell
display stp brief
```

![](pic/Snipaste_2026-07-24_00-25-31.png)

![](pic/Snipaste_2026-07-24_00-26-10.png)

![](pic/Snipaste_2026-07-24_00-26-46.png)