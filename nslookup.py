import socket
import struct
import random
def build_query(domain, qtype=1):
    transaction_id = random.randint(0, 65535)
    flags = 0x0100
    qdcount = 1
    ancount = 0
    nscount = 0
    arcount = 0

    header = struct.pack('>HHHHHH', transaction_id, flags, qdcount, ancount, nscount, arcount)
    qname = b''.join((bytes([len(part)]) + part.encode() for part in domain.split('.'))) + b'\x00'
    question = qname + struct.pack('>HH', qtype, 1)

    return transaction_id, header + question

def parse_response(data):
    (transaction_id, flags, qdcount, ancount, nscount, arcount) = struct.unpack(">HHHHHH", data[:12])
    offset = 12
    while data[offset] != 0:
        offset += 1 + data[offset]
    offset += 5
    results = []
    for _ in range(ancount):
        offset += 2
        rtype, rclass, ttl, rdlength = struct.unpack(">HHIH", data[offset:offset+10])
        offset += 10
        rdata = data[offset:offset+rdlength]
        offset += rdlength

        if rtype == 1:
            ip = ".".join(map(str, rdata))
            results.append(("A", ip))
        elif rtype == 28:
            ipv6 = ":".join(f"{rdata[i]<<8 | rdata[i+1]:x}" for i in range(0, rdlength, 2))
            results.append(("AAAA", ipv6))
    return results

def nslookup(domain, qtype=1, dns_server="8.8.8.8"):
    _, query = build_query(domain, qtype)  # only take query (bytes)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(3)
    sock.sendto(query, (dns_server, 53))   # send bytes
    data, _ = sock.recvfrom(512)
    results = parse_response(data)
    for r in results:
        print(f"{r[0]} Record: {r[1]}")

if __name__ == "__main__":
    domain = input("Enter domain: ")
    print("Fetching A (IPv4) Records...")
    nslookup(domain, qtype=1)
    print("\nFetching AAAA (IPv6) Records...")
    nslookup(domain, qtype=28)