import argparse
import nmap
import socket

def argument_parser():
    parser = argparse.ArgumentParser(
        description="TCP Port Scanner. Accepts hostname/IP and port list."
    )

    parser.add_argument("-o", "--host", nargs="?", help="Host IP address or domain")
    parser.add_argument("-p", "--ports", nargs="?", help="Comma-separated ports like 25,80,443")

    args = vars(parser.parse_args())
    return args


def nmap_scan(host_id, port_num):
    nm_scan = nmap.PortScanner()

    ip = socket.gethostbyname(host_id)

    nm_scan.scan(ip, port_num)

    state = nm_scan[ip]['tcp'][int(port_num)]['state']

    result = "[*] {} tcp/{} {}".format(ip, port_num, state)

    return result


if __name__ == "__main__":
    try:
        user_args = argument_parser()

        host = user_args["host"]
        ports = user_args["ports"].split(",")

        for port in ports:
            print(nmap_scan(host, port))

    except Exception as e:
        print("Error:", e)