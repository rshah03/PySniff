import socket
import struct
import textwrap

#Unpacking ethernet frame
def ethernet_Frame(data):							  #14 bytes total: 6s > 6 bytes x2 + H (2 Bytes)
	dest_macAddr, src_macAddr, proto = struct.unpack('! 6s 6s H', data[:14])
	return get_macAddr(dest_macAddr), get_macAddr(src_macAddr), socket.htons(proto), data[:14]

#Formet mac address to readable format
def get_macAddr(bytes_addr):
	bytes_str = map('{:02x}'.format, bytes_addr) #Split to two decimal places
	#mac_addr = ':'.join(bytes_str).upper()
	return ':'.join(bytes_str).upper()


