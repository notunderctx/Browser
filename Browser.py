from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

class WebBrowser(QMainWindow):
      def __init__(self):
            
            self.window = QWidget()
            self.window.setWindowTitle("Chahan Browser")
            self.layout = QVBoxLayout()
            self.horizontal =QHBoxLayout()
            self.Back_Button = QPushButton("⬅️")
            self.Back_Button.setStyleSheet('''
            QPushButton {
                border: none;
                
                text-align: center;
               
                font-size: 16px;
                
                
                border-radius: 5px;
            }
            
            
        ''')
            self.Back_Button.setMinimumHeight(30)
        

            self.Forward_Button = QPushButton("➡️")
            self.Forward_Button.setStyleSheet('''
            QPushButton {
                border: none;
                
                text-align: center;
                
                font-size: 16px;
            
                cursor: pointer;
                border-radius: 5px;
            }
            
            
        ''')
            self.Forward_Button.setMinimumHeight(30)
            self.Url_Bar = QTextEdit()
            self.Url_Bar.setMaximumHeight(30)
            self.Url_Bar.setStyleSheet('''
            QTextEdit {
                border: 1px solid #dcdcdc;
                border-radius: 20px;
                padding: 5px;
                font-size: 12px;
                font-family: Arial, sans-serif;
                background-color: #ffffff;
                color: #333333;
            }
            
            QTextEdit:hover, QTextEdit:focus {
                border-color: #7cb8fd;
                outline: none;
            }
        ''')
        
        
            self.Search_Button = QPushButton("🔍")
            self.Search_Button.setStyleSheet('''
            QPushButton {
                border: none;
              
                text-align: center;
                
                font-size: 16px;
                
                cursor: pointer;
                border-radius: 10px;
            }
            
           
        ''')
            self.Search_Button.setMinimumHeight(30)

            
            self.horizontal.addWidget(self.Url_Bar)
            self.horizontal.addWidget(self.Search_Button)
            self.horizontal.addWidget(self.Back_Button)
            self.horizontal.addWidget(self.Forward_Button)
            self.browser = QWebEngineView()
            self.Search_Button.clicked.connect(lambda:self.navigate(self.Url_Bar.toPlainText()))
            self.Back_Button.clicked.connect(self.browser.back)
            self.Forward_Button.clicked.connect(self.browser.forward)

            self.layout.addLayout(self.horizontal)
            self.browser.page().setDevToolsPage(self.browser.page())
            
            self.layout.addWidget(self.browser)
            self.browser.setUrl(QUrl("https://google.com"))
            
            self.window.setLayout(self.layout)
            self.window.show()
      def navigate(self,url:str):
            if not url.startswith("http"):
                  url = "https://" + url.strip()
                  self.Url_Bar.setText(url)
            self.browser.setUrl(QUrl(url))