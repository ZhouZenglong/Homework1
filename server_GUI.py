from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton,  QPlainTextEdit,QMessageBox
from socket import*

def winD():

    IP = '127.0.0.0'
    Port = 50000
    Buflen = 512

    listenSocket = socket(AF_INET,SOCK_STREAM)

    listenSocket.bind((IP,Port))

    istenSocket.listen(8)  
    print(f'服务端启动成功，在｛Port｝端口等待客户连接...')

    dataSocket,addr = listenSocket.accept()
    print('接受一个客户端连接：',addr)

    while True:
        recved = dataSocket.recv(Buflen)
        if not recved:
            break
    info = recved.decode()
    print(f'收到对方信息：｛info｝')

    dataSocket.send(f'服务端接受到了信息｛info｝'.encode())

    dataSocket.close()
    listenSocket.close()

app = QApplication([])

window = QMainWindow()
window.resize(500, 400)
window.move(300, 310)
window.setWindowTitle('服务器')

textEdit = QPlainTextEdit(window)
textEdit.setPlaceholderText("服务器收到信息")
textEdit.move(10,25)
textEdit.resize(300,350)

button = QPushButton('启动服务器', window)
button.move(380,80)

window.show()

button.clicked.connect(winD)

app.exec_()