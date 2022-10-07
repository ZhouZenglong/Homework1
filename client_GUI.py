from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton,  QPlainTextEdit,QMessageBox
from socket import*
def winD():
    IP = '127.0.0.1'
    SERVER_PORT = 50000
    Buflen = 1024

    dataSocket = socket(AF_INET,SOCK_STREAM)

    dataSocket.connect((IP,SERVER_PORT))
    while True:
        toSend =input('>>> ')
        if  toSend == 'exit':
            break
        dataSocket.send(toSend.encode())
        recved = dataSocket.recv(Buflen)
        if not recved:
            break
        print(recved.decode())

    dataSocket.close()

app = QApplication([])

window = QMainWindow()
window.resize(500, 400)
window.move(300, 310)
window.setWindowTitle('客户端')

textEdit = QPlainTextEdit(window)
textEdit.setPlaceholderText("客户端发送信息：")
textEdit.move(10,25)
textEdit.resize(300,350)

button = QPushButton('启动客户端', window)
button.move(380,80)

window.show()

button.clicked.connect(winD)

app.exec_()