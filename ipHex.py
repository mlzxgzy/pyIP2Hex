import ipaddress
import binascii

pyperclip_installed = False


def main():
    ip: str = input("请输入IP：")
    try:
        ip: ipaddress.IPv4Address = ipaddress.ip_address(ip)
    except:
        print("请输入正确的IP地址")
        print("-=-=-=-=-=-=-=-=-=-=-")
        main()
        return
    hex = ip2hex(ip)
    print(hex)
    if pyperclip_installed:
        pyperclip.copy(hex)
    print("-=-=-=-=-=-=-=-=-=-=-")
    pass


def ip2hex(ip):
    return binascii.b2a_hex(ip.packed).decode().upper()


if __name__ == '__main__':
    import sys

    if len(sys.argv) == 1:
        try:
            import pyperclip

            pyperclip_installed = True
            print("[√] pyperclip 已安装，将自动复制转换后的IP地址")
        except:
            print("[×] pyperclip 未安装，将不会自动复制转换后的IP地址")
            print("[×] 如需安装请执行 `pip install pyperclip`")
        while True:
            main()
    else:
        try:
            ip: ipaddress.IPv4Address = ipaddress.ip_address(sys.argv[1])
        except:
            print("请输入正确的IP地址")
            exit(1)
        print(ip2hex(ip))
