 ###############################################
 # firehawk ~~~> 4d!ty@			       #
 # from: INDIAN INSTITUTE OF TECHNOLOGY INDORE #
 # ******************************************* #
 ###############################################

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from subprocess import *
import os

class CGUI(QDialog):
	def __init__(self, parent = None):
		super(CGUI, self).__init__(parent)
		layout = QHBoxLayout
		self.setGeometry(200,200,850,250)
		self.setWindowTitle('Compile and Run C++')

		self.b1 = QPushButton(self)
		self.b1.setText("Close")
		self.b1.move(50,200)
		self.b1.clicked.connect(self.b1_clicked)
		self.b1.setShortcut(QKeySequence("Ctrl+Q"))
		
		self.b2 = QPushButton(self)
		self.b2.setText("Compile")
		self.b2.move(50,50)
		self.b2.setShortcut(QKeySequence("Ctrl+B"))
		self.b2.clicked.connect(self.b2_clicked)
		
		self.b3 = QPushButton(self)
		self.b3.setText("Run")
		self.b3.move(50,100)
		self.b3.setShortcut(QKeySequence("Ctrl+R"))
		self.b3.clicked.connect(self.b3_clicked)
		
		self.b4 = QPushButton(self)
		self.b4.setText("Browse")
		self.b4.move(50,150)
		self.b4.setShortcut(QKeySequence("Ctrl+O"))
		self.b4.clicked.connect(self.b4_clicked)
		
		self.f1 = QLineEdit(self)
		self.f1.setText('Enter File name(current directory)')
		self.f1.move(50,20)
		
		self.f2 = QTextEdit(self)
		self.f2.move(520,20)
		self.f2.setText('Output')
		
		self.f3 = QTextEdit(self)
		self.f3.move(200,20)
		self.f3.setText('Input')
	
	def b1_clicked(self):
		quit()

	def b2_clicked(self):
		filename = str(self.f1.text())
		if filename[-3:] == 'cpp':
			pipe = Popen('g++ ' + filename, shell=True, stderr=PIPE, stdout=PIPE, stdin=PIPE)
			output = pipe.communicate()[1]
			self.f2.setText(output)
		else:
			self.f2.setText("It's not CPP!")                                      

	def b3_clicked(self):
		filename = str(self.f1.text())
		if filename[-3:] =='cpp':
			process = Popen('./a.out', shell=True, stderr=PIPE, stdout=PIPE, stdin=PIPE)
			output = process.communicate(input = str(self.f3.toPlainText()))[0]
			self.f2.setText(output)
		else:
			self.f2.setText("It's not CPP!")

	def b4_clicked(self):
		ff = QFileDialog.getOpenFileName()
		f = str(ff)
		t = ''
		n = len(ff)
		for i in range(n-1,0,-1):
			if f[i] == '/':
				break
			t = f[i] + t
			f = f[:i]
		if t[-3:] != 'cpp':
			self.f2.setText('Choose CPP File')
		self.f1.setText(t)
		if f!='':
			os.chdir(f)

def main():
	app = QApplication(sys.argv)
	ex = CGUI()
	ex.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
