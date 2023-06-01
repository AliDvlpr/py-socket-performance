import socket
s = socket.socket()

# IP & Port config
ip = '127.0.0.1'
port = 8801

# Socket
s.bind((ip, port))
s.listen()
print("CONNECTED SUCSSEFULLY")
# پذیرش اتصال از کلاینت
c,addr = s.accept()

while True:
    # دریافت پیام از کلاینت
    request = c.recv(1024)
    # ارسال پیام به کلاینت
    c.send(request)
    print(request)