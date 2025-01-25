import socket
import json
import sys
import time

def test_evolink_cmd(evolink_cmd, has_response=False, data_array=[]):
    #========== Init Socket ==========
    evolink_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    evolink_socket.connect(("127.0.0.1", 8063))
    evolink_socket.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 8192)

    #========== Sending command ==========
    print('='*20 +' Sending command ' + '='*20)
    data = bytes(json.dumps(evolink_cmd), encoding='utf-8')
    cmd_len_bytes = len(data).to_bytes(4, sys.byteorder)

    print(f'\nSending {str(len(data))} bytes:\n-----\n{str(data)}\n-----\n')

    evolink_socket.sendall(cmd_len_bytes)
    evolink_socket.sendall(data)

    for sub_data in data_array:
        evolink_socket.sendall(sub_data)

    #========== Receiving Responses ==========
    if (has_response) :
        print('='*20 +' RESPONSE ' + '='*20)
        cmd_len_as_bytes = evolink_socket.recv(4)
        cmd_len = int.from_bytes(cmd_len_as_bytes, sys.byteorder)
        print('message length: ' + str(cmd_len))
        
        cmd_payload_as_bytes = evolink_socket.recv(cmd_len)
        cmd_json_str = str(cmd_payload_as_bytes, 'utf-8')
        print('message response: ' + cmd_json_str + '\n\n')

    evolink_socket.close()