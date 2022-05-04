import ipaddress

'''
networkアドレスは、
192.168.1.0/24
192.168.1.0/255.255.255.0
のようなかたち。つまり、どちらで入力しても解釈される。
ワイルドカードは、
192.168.1.0/0.0.0.255　と入力して解釈される。
「/24 と等しい IPv4 のホストマスクは 0.0.0.255 になります。」公式より。
実際入出力↓
ipaddr = ipaddress.ip_network("192.168.1.0/0.0.0.255")
ipaddr
Out[40]: IPv4Network('192.168.1.0/24')
'''
def checknet(ipaddr, network):
    ipaddr = ipaddress.ip_network(ipaddr)
    ipnet = ipaddress.ip_network(network)
    return (ipaddr,ipnet,ipaddr.subnet_of(ipnet))

'''
メモ
subnet_of(other)
このネットワークが other のサブネットの場合に True を返します。

>>>
a = ip_network('192.168.1.0/24')
b = ip_network('192.168.1.128/30')
b.subnet_of(a)
True
バージョン 3.7 で追加.

supernet_of(other)
このネットワークが other のスーパーネットの場合に True を返します。

>>>
a = ip_network('192.168.1.0/24')
b = ip_network('192.168.1.128/30')
a.supernet_of(b)
True
バージョン 3.7 で追加.
```
```
ホストアドレスも32をつけることで、ip_networkオブジェクトとして扱う
それによってホストアドレスとネットワークアドレスの場合分けをスクリプト中不要にする

a = ipaddress.ip_network("192.168.1.1/32")

a
Out[24]: IPv4Network('192.168.1.1/32')



b = ipaddress.ip_network("192.168.1.0/24")

a.subnet_of(b)
Out[26]: True

b.subnet_of(a)
Out[27]: False
'''
