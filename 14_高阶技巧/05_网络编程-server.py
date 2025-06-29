"""
Socket网络编程：
socket（套接字）是进程之间通信的一个工具
服务端：等待其他进程的连接、可接受发来的消息、可以回复消息
客户端：主动连接服务端、可以发送消息、接收回复


"""
import socket
import threading
import time

# 服务端步骤：
# 1、创建socket对象
socket_server = socket.socket()

# 2、绑定ip和端口
socket_server.bind(("127.0.0.1", 8080))

# 3、监听
socket_server.listen(10)

# 4、接收客户端连接 阻塞
conn, addr = socket_server.accept()

# 5、接收客户端消息
while True:
    data: str = conn.recv(1024).decode("UTF-8")
    # recv方法的返回值是字节数组，decode解码
    # buffSize缓冲区大小
    if data == "exit":
        break
    print(f"收到客户端消息：{data}")
    # 6、发送消息给客户端
    msg = input("发送的消息：").encode("UTF-8")
    conn.send("send".encode("UTF-8") + msg)
# 持续和客户端进行数据交互，exit退出循环

# 7、关闭连接
conn.close()
# 8、关闭服务端
socket_server.close()