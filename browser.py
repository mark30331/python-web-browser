#######################################################################
# This imports all the necessary features to help build this application
#
#######################################################################
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

#######################################################################
# Description of project: GreatMJ Browser is a windows application which is
# used to access the World Wide Web. When a user follows the URL of a web
# page from a particular website, the GreatMJ browser retrieves the necessary
# content from the website's web server and then displays the page on the
# user's device.
#
# Purpose , Scope: This browser would have the fastest load time for websites
# and requires low RAM to operate. This browser is primarily designed to 
# provide users with standard Web browsing experience, while degrading
# their system performance to minimal. This browser would require less
# storage,  provide a simple User interface and require less load time for websites.
#
#
# Overview: Typically,  GreatMJ Browser would utilize less space on a 
# disk, require fewer computing resources and are easy to operate and 
# manage. My project is specifically designed to operate on low-end 
# computers and mobile devices and for general end-users, which are 
# those having lesser or no need for advanced browser features.#

#######################################################################


class GreatMJ_browser(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(GreatMJ_browser, self).__init__(*args, **kwargs)

        self.window = QWidget()

        #this sets my browser's title or name 
        self.window.setWindowTitle("GreatMJ Browser")

        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        # creating an empty space to edit for url
        self.url_bar  = QTextEdit()

        #This sets the maximum height to 35
        self.url_bar.setMaximumHeight(35)

        # to perform go action
        self.go_button = QPushButton("GO")

        #This sets the maximum height to 35
        self.go_button.setMinimumHeight(35)

        # to perform homepage action
        self.home_button = QPushButton("Home")

        #This sets the maximum height to 35
        self.home_button.setMinimumHeight(35)

        # to perform forward action
        self.forward_button = QPushButton("Forward")

        #This sets the maximum height to 35
        self.forward_button.setMinimumHeight(35)

        # to perform back action
        self.back_button = QPushButton("Back")

        #This sets the maximum height to 35
        self.back_button.setMinimumHeight(35)

        # to perform refresh action
        self.refresh_button = QPushButton("Refresh")

        #This sets the maximum height to 35
        self.refresh_button.setMinimumHeight(35)

        #this adds all buttons to the widgets created
        self.horizontal.addWidget(self.back_button)
        self.horizontal.addWidget(self.forward_button)
        self.horizontal.addWidget(self.refresh_button)
        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.go_button)   
        self.horizontal.addWidget(self.home_button)     
        

        self.browser = QWebEngineView()

        #this modifies the view of the web browser
        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        #this line of code sets up my url to google
        self.browser.setUrl(QUrl("https://www.google.com"))

        # this lambda functon calls the navigation function and pass the url to check if
        # it starts with "https"
        self.go_button.clicked.connect(lambda:self.navigation(self.url_bar.toPlainText()))
        
        #this lambda function calls the home functon which automatically sets triggers the 
        # homepage
        self.home_button.clicked.connect(lambda:self.home())

        #this would be able to navigate to a previously visited page
        self.back_button.clicked.connect(self.browser.back)

        #navigate forwardly to a previously visited page.
        self.forward_button.clicked.connect(self.browser.forward)

        #this would reload the page 
        self.refresh_button.clicked.connect(self.browser.reload)
        

        self.window.setLayout(self.layout)
  
        # showing all the components
        self.window.show()

        
    #######################################################################
    #this function is responsible for adding the https the url if not added 
    #
    #######################################################################
    def navigation(self, url):
        if not url.startswith("http"):
            url = "http://" + url
            self.url_bar.setText(url)
        self.browser.setUrl(QUrl(url))

    #######################################################################
    # This function sets the home_button to google which is the homepage
    #######################################################################
    def home(self):
        #set homepage to google
        self.browser.setUrl(QUrl("http://www.google.com"))

# creating a PyQt5 application
app = QApplication([])

# creating MainWindow object
window = GreatMJ_browser()

#this starts the execution of the loop and the browser
app.exec_()
