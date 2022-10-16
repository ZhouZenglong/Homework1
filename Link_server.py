from PySide2.QtWidgets import QApplication,QMainWindow,QPushButton,QPlainTextEdit,QMessageBox,QLineEdit,QLabel
import socket

def link_fun(self):
    IP=line1.text()
    Port=int(line2.text())
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    mysocket.connect((IP, Port))

    cmd = 'GET http://IP/romeo.txt HTTP/1.0\r\n\r\n'.encode()

    mysocket.send(cmd)

    while True:
        data = mysocket.recv(512)
        if (len(data) < 1):
            break
        str = data.decode()

    mysocket.close()
    plain.setPlainText(str)


ap=QApplication([])
window=QMainWindow()
window.setWindowTitle('window')
window.resize(800,800)
window.move(100,100)

plain=QPlainTextEdit(window)
plain.resize(400,300)
plain.move(10,10)
plain.setPlaceholderText('Show info window:')

label1=QLabel(window)
label1.move(420,60)
label1.resize(130,20)
label1.setText('IP：')

label2=QLabel(window)
label2.move(420,100)
label2.resize(130,20)
label2.setText('Port：')

line1=QLineEdit(window)
line1.move(465,60)
line1.setPlaceholderText('Please into IP:')

line2=QLineEdit(window)
line2.move(465,100)
line2.setPlaceholderText("Please input port:")



button=QPushButton(window)
button.resize(120,40)
button.move(300,450)
button.setText('Reset')
button.clicked.connect(link_fun)

window.show()
ap.exec_()