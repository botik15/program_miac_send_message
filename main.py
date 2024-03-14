from PyQt5 import *
from PyQt5.QtWidgets import *
import sys
from untitled import *
from ping3 import ping, verbose_ping
import paramiko
from qtwidgets import PasswordEdit

"""Класс, который создает окно и распологает на нем виджеты"""
class Express(QtWidgets.QMainWindow):
    def __init__(self):
        super(Express,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.btn)

    def btn(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        IP = self.ui.lineEdit.text()
        text_message = self.ui.lineEdit_2.text()
        user = self.ui.lineEdit_3.text()
        password = self.ui.lineEdit_4.text()
        if ping(IP) != None:
            ssh.connect(IP, username=user, password=password)
            # ssh.connect('172.20.0.174', username='miac71@med.cap.ru', password='Gfhjkm-1')
            stdin, stdout, stderr = ssh.exec_command('DISPLAY=:0 notify-send "' + str(text_message) + '" -t 6000000')
            print('Сообщение отправлено')
            self.ui.statusbar.showMessage(f'Отправлено сообщение: {text_message} ')
        else:
            self.ui.statusbar.showMessage(f'IP не пингуется')




app = QtWidgets.QApplication([])
application = Express()
application.show()
desktop = QtWidgets.QApplication.desktop()
x = (desktop.width() - application.frameSize().width()) // 4
y = (desktop.height() - application.frameSize().height()) // 2
application.move(x, y)
sys.exit(app.exec())
con.close()