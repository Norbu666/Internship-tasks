import socket
import struct

def parse_packet(packet):
    # Unpack IP header
    ip_header = packet[0:20]
    iph = struct.unpack('!BBHHHBBH4s4s', ip_header)

    version_ihl = iph[0]
    version = version_ihl >> 4
    ihl = version_ihl & 0xF

    protocol = iph[6]
    src_ip = socket.inet_ntoa(iph[8])
    dst_ip = socket.inet_ntoa(iph[9])

    print(f"\nProtocol: {protocol}, Source IP: {src_ip}, Destination IP: {dst_ip}")

def packet_sniffer():
    # Create raw socket and bind
    try:
        sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
        sniffer.bind(("192.168.93.5", 0))
        sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    except Exception as e:
        print("Socket creation failed:", e)
        return

    print("Sniffing packets... Press Ctrl+C to stop.\n")

    try:
        while True:
            packet, _ = sniffer.recvfrom(65565)
            parse_packet(packet)
    except KeyboardInterrupt:
        print("\nSniffing stopped.")

packet_sniffer()
