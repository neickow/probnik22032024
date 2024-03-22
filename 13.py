from ipaddress import *
k=0
ip1='167.77.194.47'
ip2='167.77.194.37'
ip3='167.77.200.25'
for mask in range(33):
    s1 = ip_network(f'{ip1}/{mask}', 0)
    s2 = ip_network(f'{ip2}/{mask}',0)
    s3 = ip_network(f'{ip3}/{mask}' , 0)
    if s1==s2!=s3:
        if ip_address(ip1) in s1.hosts() and ip_address(ip2) in s2.hosts() and ip_address(ip3) in s3.hosts():
              k+=1
print(k)