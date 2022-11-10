from socket import*
import os   #用于判断文件是否存在

s = socket(AF_INET,SOCK_STREAM)	#创建套接字
s.connect(('127.0.0.1',9999))		#连接套接字

def sendfile(s):
	str1 = s.recv(1024)            #接收长度1024
	filename = str1.decode('utf-8')   #解码接收到的内容
	print('The server requests my file:',filename)
	if os.path.exists(filename):	  #目录下存在文件
		print('I have %s,begin to download!'% filename)
		s.send(b'yes')   
		s.recv(1024)
		size = 1024
		with open(filename,'rb') as f:   #二进制读文件
			while True:
				data = f.read(size)
				s.send(data)			 #发送读取到的文件
				if len(data) < size:
					break
		print('%s id download successfully!'% filename)
	else:
		print('Sorry,I have no %s'% filename)
		s.send(b'no')
	s.close()


while True:
	sendfile(s)

	
