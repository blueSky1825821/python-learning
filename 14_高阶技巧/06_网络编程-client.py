"""
Socket网络编程：
socket（套接字）是进程之间通信的一个工具
服务端：等待其他进程的连接、可接受发来的消息、可以回复消息
客户端：主动连接服务端、可以发送消息、接收回复


"""
import socket
import threading
import time

# 客户端步骤：
# 1、创建socket对象
socket_client = socket.socket()

# 2、连接到服务端
socket_client.connect(("127.0.0.1", 8080))

# 3、发送消息
while True:
    send_msg = input("请输入要发送的消息：")
    if send_msg == "exit":
        break
    # 消息需要编码
    socket_client.send(send_msg.encode("UTF-8"))
    # 4、接收消息
    recv_data = socket_client.recv(1024)
    print("服务端返回：", recv_data.decode("UTF-8"))

# 5、关闭socket
socket_client.close()
