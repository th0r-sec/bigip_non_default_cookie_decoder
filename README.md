# F5 BIG-IP Non-Default Route Domain Cookie Decoder
Decodes F5 BIG-IP non-default route domain cookie values

This python script will take the value of an F5 BIG-IP persistence cookie that utilizes a non-default route domain and decode the value. This will return the internal IP address, port number, and route domain value.  When a non-default route domain is in use, the cookie is encoded differently (see https://my.f5.com/manage/s/article/K6917).

Example of a BIG-IP Cookie and it's value that does not utilize the default route domain

       BIGipServer_https_pool=rd50o00000000000000000000ffff0a010203o443

Usage

    python3 ./bigip_cookie_decode.py <COOKIE VALUE>

Example Usage

    # python3 ./bigip_cookie_decode.py rd50o00000000000000000000ffff0a010203o443
    ***F5 BIG-IP Non-Default Route Domains Cookie Decoder***
    [*] Route Domain: 50
    [*] IP Address: 10.1.2.3
    [*] Port: 443
