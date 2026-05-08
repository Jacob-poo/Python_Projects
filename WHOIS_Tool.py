import socket

def whois_lookup(domain: str):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("whosis.iana.org", 43))
    s.send((f"{domain}\r\n").encode())
    response = s.receive(4096).decode()
    s.close()
    return response