from socket import*

s = socket(AF_INET,SOCK_STREAM)
s.bind(('127.0.0.1',9999))
s.listen(1) 

print(f'服务端启动成功，在｛Port｝端口等待客户连接...')
conn,addr = s.accept()
print('接受一个客户端连接：',addr)


while True:
	filename = 'c:/test_download.txt'  #文件所在位置
	print('I want to get the file %s!' % filename)
	conn.send(filename.encode('utf8'))
	str1 = conn.recv(1024)
	str2 = str1.decode('utf-8')

	if str2=='no':
		print('To get the file %s is failed!'% filename)
	else:
		conn.send(b'I am ready!')
		temp = filename.split('/')  #过滤文件名中的/
		myname = 'my_'+temp[len(temp)-1]
		size = 1024
		with open(myname,'wb') as f:
			while True:
				data = conn.recv(size)
				f.write(data)
				if len(data)<size:
					break
		print('The download file is %s.'% myname)


conn.close()
s.close()
