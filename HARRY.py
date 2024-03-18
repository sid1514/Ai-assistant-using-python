from PyQt5 import QtCore, QtGui, QtWidgets
from tabulate import tabulate
import pywhatkit as kt
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyjokes
import pyautogui as  pa
import time
import requests
from ecapture  import ecapture as ec
import keyboard
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton,QVBoxLayout
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import*
from PyQt5.QtGui import QColor, QFont

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',150)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1672, 945)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(-20, 10, 2000, 1020))
        self.label_1.setAutoFillBackground(True)
        self.label_1.setText("")
        self.label_1.setPixmap(QtGui.QPixmap("lib/bg_AI.jpg"))
        self.label_1.setScaledContents(True)
        self.label_1.setObjectName("label_1")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(870, 400, 191, 171))
        self.pushButton.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton.setMaximumSize(QtCore.QSize(341, 16777215))
        self.pushButton.setSizeIncrement(QtCore.QSize(100, 100))
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setAutoFillBackground(True)
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("lib/mic1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(150, 120))
        self.pushButton.setCheckable(False)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(True)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.play_gif)
        self.pushButton.clicked.connect(self.harry)                             
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1800, 30, 50, 51))
        self.pushButton_2.setAutoFillBackground(True)
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("lib/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.closeAS)    

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1170, 220, 211, 121))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setScaledContents(True)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1100, 440, 300, 300))
        self.label_2.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        self.label_2.setFont(font)
        self.label_2.setScaledContents(True)
        self.label_2.setWordWrap(True)
        #self.label_2.setAutoFillBackground(True)
        self.label_2.setObjectName("label_2")
        layout = QVBoxLayout()
        layout.addWidget(self.label_2)
        MainWindow.setLayout(layout)

       

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 100, 170, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.label_3.setFont(font)
        self.label_3.setScaledContents(True)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 130, 130, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.label_4.setFont(font)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setScaledContents(True)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(800, 550, 300, 200))
        

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1672, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1672, 26))
        self.menubar.setObjectName("menubar")
        self.menuHelpful_commands = QtWidgets.QMenu(self.menubar)
        self.menuHelpful_commands.setObjectName("menuHelpful_commands")
        self.menufor_remember_anything = QtWidgets.QMenu(self.menuHelpful_commands)
        self.menufor_remember_anything.setObjectName("menufor_remember_anything")
        self.menucreating_text_file = QtWidgets.QMenu(self.menuHelpful_commands)
        self.menucreating_text_file.setObjectName("menucreating_text_file")
        self.menucreating_table = QtWidgets.QMenu(self.menuHelpful_commands)
        self.menucreating_table.setObjectName("menucreating_table")
        self.menumaths_function = QtWidgets.QMenu(self.menuHelpful_commands)
        self.menumaths_function.setObjectName("menumaths_function")
        self.menufor_clicking_photo = QtWidgets.QMenu(self.menuHelpful_commands)
        self.menufor_clicking_photo.setObjectName("menufor_clicking_photo")
        self.menufor_screenshot = QtWidgets.QMenu(self.menuHelpful_commands)
        self.menufor_screenshot.setObjectName("menufor_screenshot")
        self.menuyoutube_commands = QtWidgets.QMenu(self.menuHelpful_commands)
        self.menuyoutube_commands.setObjectName("menuyoutube_commands")
        self.menusearch_commands = QtWidgets.QMenu(self.menuHelpful_commands)
        self.menusearch_commands.setObjectName("menusearch_commands")
        self.menuchrome_commands = QtWidgets.QMenu(self.menuHelpful_commands)
        self.menuchrome_commands.setObjectName("menuchrome_commands")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_remembar_that_user_voice_input = QtWidgets.QAction(MainWindow)
        self.action_remembar_that_user_voice_input.setObjectName("action_remembar_that_user_voice_input")
        self.action_create_text_file_name = QtWidgets.QAction(MainWindow)
        self.action_create_text_file_name.setObjectName("action_create_text_file_name")
        self.action_create_table = QtWidgets.QAction(MainWindow)
        self.action_create_table.setObjectName("action_create_table")
        self.action_add_two_number = QtWidgets.QAction(MainWindow)
        self.action_add_two_number.setObjectName("action_add_two_number")
        self.action_subtract = QtWidgets.QAction(MainWindow)
        self.action_subtract.setObjectName("action_subtract")
        self.action_multiply = QtWidgets.QAction(MainWindow)
        self.action_multiply.setObjectName("action_multiply")
        self.action_divide = QtWidgets.QAction(MainWindow)
        self.action_divide.setObjectName("action_divide")
        self.action_area_of_tringle_circle_rectangle = QtWidgets.QAction(MainWindow)
        self.action_area_of_tringle_circle_rectangle.setObjectName("action_area_of_tringle_circle_rectangle")
        self.action_take_a_photo = QtWidgets.QAction(MainWindow)
        self.action_take_a_photo.setObjectName("action_take_a_photo")
        self.action_open_camera = QtWidgets.QAction(MainWindow)
        self.action_open_camera.setObjectName("action_open_camera")
        self.action_take_a_screenshot = QtWidgets.QAction(MainWindow)
        self.action_take_a_screenshot.setObjectName("action_take_a_screenshot")
        self.action_open_screensave = QtWidgets.QAction(MainWindow)
        self.action_open_screensave.setObjectName("action_open_screensave")
        self.action_open_youtube = QtWidgets.QAction(MainWindow)
        self.action_open_youtube.setObjectName("action_open_youtube")
        self.action_you_tube_channel_name = QtWidgets.QAction(MainWindow)
        self.action_you_tube_channel_name.setObjectName("action_you_tube_channel_name")
        self.action_tell_me_about_user_input = QtWidgets.QAction(MainWindow)
        self.action_tell_me_about_user_input.setObjectName("action_tell_me_about_user_input")
        self.action_search_user_input = QtWidgets.QAction(MainWindow)
        self.action_search_user_input.setObjectName("action_search_user_input")
        self.action_open_chrome = QtWidgets.QAction(MainWindow)
        self.action_open_chrome.setObjectName("action_open_chrome")
        self.action_open_new_window = QtWidgets.QAction(MainWindow)
        self.action_open_new_window.setObjectName("action_open_new_window")
        self.action_open_new_tab = QtWidgets.QAction(MainWindow)
        self.action_open_new_tab.setObjectName("action_open_new_tab")
        self.action_open_history = QtWidgets.QAction(MainWindow)
        self.action_open_history.setObjectName("action_open_history")
        self.menufor_remember_anything.addAction(self.action_remembar_that_user_voice_input)
        self.menucreating_text_file.addAction(self.action_create_text_file_name)
        self.menucreating_table.addAction(self.action_create_table)
        self.menumaths_function.addAction(self.action_add_two_number)
        self.menumaths_function.addAction(self.action_subtract)
        self.menumaths_function.addAction(self.action_multiply)
        self.menumaths_function.addAction(self.action_divide)
        self.menumaths_function.addAction(self.action_area_of_tringle_circle_rectangle)
        self.menufor_clicking_photo.addAction(self.action_take_a_photo)
        self.menufor_clicking_photo.addAction(self.action_open_camera)
        self.menufor_screenshot.addAction(self.action_take_a_screenshot)
        self.menufor_screenshot.addAction(self.action_open_screensave)
        self.menuyoutube_commands.addAction(self.action_open_youtube)
        self.menuyoutube_commands.addAction(self.action_you_tube_channel_name)
        self.menusearch_commands.addAction(self.action_tell_me_about_user_input)
        self.menusearch_commands.addAction(self.action_search_user_input)
        self.menuchrome_commands.addAction(self.action_open_chrome)
        self.menuchrome_commands.addAction(self.action_open_new_window)
        self.menuchrome_commands.addAction(self.action_open_new_tab)
        self.menuchrome_commands.addAction(self.action_open_history)
        self.menuHelpful_commands.addAction(self.menufor_remember_anything.menuAction())
        self.menuHelpful_commands.addAction(self.menucreating_text_file.menuAction())
        self.menuHelpful_commands.addAction(self.menucreating_table.menuAction())
        self.menuHelpful_commands.addAction(self.menumaths_function.menuAction())
        self.menuHelpful_commands.addAction(self.menufor_clicking_photo.menuAction())
        self.menuHelpful_commands.addAction(self.menufor_screenshot.menuAction())
        self.menuHelpful_commands.addAction(self.menuyoutube_commands.menuAction())
        self.menuHelpful_commands.addAction(self.menuchrome_commands.menuAction())
        self.menuHelpful_commands.addAction(self.menusearch_commands.menuAction())
        self.menubar.addAction(self.menuHelpful_commands.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        day = datetime.datetime.today().weekday() + 1
        Day_dict = {1: 'Monday', 2: 'Tuesday',
                    3: 'Wednesday', 4: 'Thursday',
                    5: 'Friday', 6: 'Saturday',
                    7: 'Sunday'}
        if day in Day_dict.keys():
            day_of_the_week = Day_dict[day]
            #print(day_of_the_week)
        today=datetime.date.today()
        
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", f"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#ffffff;\">HARRY</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#ffffff;\">Commands</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", f"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-style:italic; color:#ffffff;\">{today}</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", f"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">{day_of_the_week}</span></p></body></html>"))
        self.menuHelpful_commands.setTitle(_translate("MainWindow", "Helpful commands"))
        self.menufor_remember_anything.setTitle(_translate("MainWindow", "for remember anything"))
        self.menucreating_text_file.setTitle(_translate("MainWindow", "creating text file"))
        self.menucreating_table.setTitle(_translate("MainWindow", "creating table"))
        self.menumaths_function.setTitle(_translate("MainWindow", "maths function"))
        self.menufor_clicking_photo.setTitle(_translate("MainWindow", "for clicking photo"))
        self.menufor_screenshot.setTitle(_translate("MainWindow", "for screenshot"))
        self.menuyoutube_commands.setTitle(_translate("MainWindow", "youtube commands"))
        self.menusearch_commands.setTitle(_translate("MainWindow", "search commands"))
        self.menuchrome_commands.setTitle(_translate("MainWindow", "chrome commands"))
        self.action_remembar_that_user_voice_input.setText(_translate("MainWindow", "\"remembar that {user voice input}\""))
        self.action_create_text_file_name.setText(_translate("MainWindow", "\"create text {file name}\""))
        self.action_create_table.setText(_translate("MainWindow", "\"create table\""))
        self.action_add_two_number.setText(_translate("MainWindow", "\"add two number\""))
        self.action_subtract.setText(_translate("MainWindow", "\"subtract\""))
        self.action_multiply.setText(_translate("MainWindow", "\"multiply\""))
        self.action_divide.setText(_translate("MainWindow", "\"divide\""))
        self.action_area_of_tringle_circle_rectangle.setText(_translate("MainWindow", "\"area of tringle/circle/rectangle\""))
        self.action_take_a_photo.setText(_translate("MainWindow", "\"take a photo\""))
        self.action_open_camera.setText(_translate("MainWindow", "\"open camera\""))
        self.action_take_a_screenshot.setText(_translate("MainWindow", "\"take a screenshot\""))
        self.action_open_screensave.setText(_translate("MainWindow", "\"open screensave\""))
        self.action_open_youtube.setText(_translate("MainWindow", "\"open youtube\""))
        self.action_you_tube_channel_name.setText(_translate("MainWindow", "\"you tube {channel name}\""))
        self.action_tell_me_about_user_input.setText(_translate("MainWindow", "\"tell me about{user input}\""))
        self.action_search_user_input.setText(_translate("MainWindow", "\"search {user input}\""))
        self.action_open_chrome.setText(_translate("MainWindow", "\"open chrome\""))
        self.action_open_new_window.setText(_translate("MainWindow", "\"open new window\""))
        self.action_open_new_tab.setText(_translate("MainWindow", "\"open new tab\""))
        self.action_open_history.setText(_translate("MainWindow", "\"open history\""))

    def play_gif(self):
        movie = QMovie("lib/waveicon.gif")
        self.label_5.setMovie(movie)
        movie.start()

    def closeAS(self):
        QCoreApplication.instance().quit()

#main code 
    def speak(self,audio):
        print("   ")
        engine.say(audio)
        print(f":{audio}")
        self.label.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#ffffff;\">HARRY:{audio}</span></p></body></html>")
        engine.runAndWait()
        
        

    def takeCommand(self):
        r=sr.Recognizer()
        with sr.Microphone()  as source:
            print("listening...") 
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("recognizing...")
            query = r.recognize_google(audio,language='en-in')
            print(f"you said:{query}\n")
            self.label_2.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#ffffff;\">you said: {query}</span></p></body></html>")
        except Exception as e:
       # print(e)
            print("say that again please..")
            return "None"
        return query
        

    def table(self):
        while True:
            try:
                self.speak("Enter the number of headers:")
                num_headers = int(self.takeCommand())
                self.speak("ok sir!")
                break
            except ValueError:
                self.speak(" say that again sir ")
        headers = []
        for i in range(num_headers):
            self.speak(f"Enter header {i+1}: ")
            header = str(self.takeCommand())
            if header=="None":
                 self.speak("say that again sir!")
                 header=str(self.takeCommand())
            self.speak("ok sir!")
            headers.append(header)
        
        while True:
            try:
                self.speak("Enter the number of rows: ")
                num_rows = int(self.takeCommand())
                self.speak("ok sir!")
                break
            except ValueError:
                self.speak("say that again")
            
        rows = []
        for i in range(num_rows):
            row = []
            for j in range(num_headers):
                self.speak(f"Enter value for {headers[j]} in row {i+1}: ")
                value = self.takeCommand()
                if value=="None":
                    self.speak("say that again sir")
                    value=self.takeCommand()
                self.speak("ok sir")
                
                row.append(value)
            rows.append(row)
        T = tabulate(rows, headers=headers,	showindex='always',tablefmt='simple')
        
        self.label_2.setStyleSheet('color: white')
        self.label_2.setFont(QFont('cambria', 10))
        self.label_2.setText(T)
        engine.runAndWait()
        #return T
        
    def inp(self):
        while True:
            try:
                self.speak("Enter the number: ")
                a = int(self.takeCommand())
                self.speak("ok sir!")
                break
            except ValueError:
                self.speak("say that again")
            return a

              
        
    def wishMe(self):
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            self.speak("good morning sir! ")
    
        elif hour>=12 and hour<18:
            self.speak("good afternoon sir!")
    
        else:
            self.speak("good evening sir!")
        self.speak("hii, i am harry sir!  please tell me how may i help you?")

    def tellDay(self):
        day = datetime.datetime.today().weekday() + 1
        Day_dict = {1: 'Monday', 2: 'Tuesday',
                    3: 'Wednesday', 4: 'Thursday',
                    5: 'Friday', 6: 'Saturday',
                    7: 'Sunday'}
     
        if day in Day_dict.keys():
            day_of_the_week = Day_dict[day]
            print(day_of_the_week)
            self.speak("The day is " + day_of_the_week)

    def harry(self):
        self.wishMe()
        while  True:
            query = self.takeCommand().lower()
            if 'wikipedia' in query:
                self.speak('searching wikipedia...')
                query = query.replace("wikipedia","")
                results = wikipedia.summary(query,sentences=2)
                self.speak("According to wikipedia..")
                print(results)
                self.speak(results)
#conversation----------------------------------------------------------------------------
            elif 'how are you' in query:
                self.speak("i am good sir!")
                self.speak("whats about you?")
                time.sleep(3)
                if '' in query:
                    self.speak('ok sir!')

            elif 'break'  in query:
                self.speak('ok sir good bye!, you can call me anytime!')
                break

            elif "goodbye" in query or"good bye" in query or "ok bye" in query or "stop" in query:
                self.speak('your personal assistant harry is going to shut down ,Good bye')
                break

            elif "who are you" in query:
                self.speak("i am harry , you personal assistant sir! i can able to do basic open app,search on google,telling weather ,time ,news  and more things.. ")
    
#task ------------------------------------------------------------------------------------
            elif 'play music' in query:
                self.speak("playing music....")
                music_dir='D:\study_material\TYIT project\music'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir,songs[0]))
       
            elif 'time' in query:
                strTime = datetime.datetime.now().strftime("%I:%M %p")
                self.speak(f"sir ,the time is{strTime}")
       
            elif 'today date' in query:
                today=datetime.date.today()
                self.speak(f"sir ,today date is {today}")

            elif 'day' in query:
                self.tellDay()

            elif 'screenshot' in query:
                self.speak("ok sir !")
                ss=pa.screenshot()
                ss.save(r"D:\study_material\TYIT project\screenshots by harry\ss_.png")
            
            elif 'show screensave' in query:
                self.speak("wait sir!")
                s_path="D:\study_material\TYIT project\screenshots by harry"
                os.startfile(s_path)

            elif "weather" in query:
                api_key="8ef61edcf1c576d65d836254e11ea420"
                base_url="https://api.openweathermap.org/data/2.5/weather?"
                self.speak("whats the city name")
                city_name=self.takeCommand()
                complete_url=base_url+"appid="+api_key+"&q="+city_name
                response = requests.get(complete_url)
                x=response.json()
                if x["cod"]!="404":
                    y=x["main"]
                    current_temperature = y["temp"]
                    current_humidiy = y["humidity"]
                    z = x["weather"]
                    weather_description = z[0]["description"]
                    self.speak(" Temperature in kelvin unit is " +
                        str(current_temperature) +
                        "\n humidity in percentage is " +
                        str(current_humidiy) +
                        "\n description  " +
                        str(weather_description))
                else:
                    self.speak("city not found")

            elif 'news' in query:
                news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
                self.speak('Here are some news from the Times of India')
                time.sleep(4)

            elif "camera" in query or "photo" in query:
                ec.capture(0,"robo camera","img.jpg")

#keyboard commands

            elif 'restart' in query:
                keyboard.press('0')
                self.speak("done..")

            elif 'mute' in query:
                keyboard.press('m')
                self.speak("done..")

            elif 'skip' in query:
                keyboard.press('1')
                self.speak("done..")

            elif 'back' in query:
                keyboard.press('m')
                self.speak("done..")

            elif 'full screen' in query:
                keyboard.press('f')
                self.speak("done..")

            elif 'file mode' in query:
                keyboard.press('t')
                self.speak("done..")

            elif 'close' in query:
                keyboard.press_and_release('ctrl+W')
                self.speak('done')

        #chrome commands
            elif 'open new tab' in query:
                keyboard.press_and_release('ctrl+t')
                self.speak('done')

            elif 'open new window' in query:
                keyboard.press_and_release('ctrl+n')
                self.speak('done')

            elif 'open history' in query:
                keyboard.press_and_release('ctrl+h')
                self.speak('done')
                

#open apps commands-----------------------------------------------------------------------
            elif 'open google' in query:
                webbrowser.open("google.com")
        
            elif 'open stackoverflow' in query:
                webbrowser.open("stackoverflow.com")

            elif 'open facebook' in query:
                webbrowser.open("facebook.com")

            elif 'open word' in query:
                self.speak("ok sir! wait")
                sf_path="C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word"
                os.startfile(sf_path)


            elif 'open gmail' in query:
                webbrowser.open_new_tab("gmail.com")
                self.speak("gmail is open sir")
                time.sleep(4)
           
            elif 'open chrome' in query:
                self.speak("ok sir! wait")
                sf_path="C:\Program Files\Google\Chrome\Application\chrome"
                os.startfile(sf_path)

            elif 'close chrome' in query:
                self.speak("ok sir, wait a second")
                os.system("TASKKILL/im chrome.exe")

            elif 'open calculator' in query:
                from subprocess import call
                call(["calc.exe"])
            
           
#search commands-----------------------------------------------------------------------
            elif 'search ' in query:
                kt.search(query)

            elif 'google maps' in query:
                webbrowser.open('https://www.google.com/maps/@19.2890698,73.2164396,15z')

            elif 'tell me about' in query:
                l=query.split()
                kt.search(l[3])
            
            elif 'youtube' in query:
                self.speak("ok sir ,this is what i found")
                query=query.replace("youtube","")
                web='https://www.youtube.com/results?search_query='+query
                webbrowser.open(web)
                self.speak('done sir')

            elif 'who is' in query:
                person = query.replace('who the heck is', '')
                info = wikipedia.summary(person, 1)
                print(info)
                self.speak(info)
            
            


#create command-------------------------------------------------------------------------
            elif 'create text' in query:
                query=query.replace('create text',"")
                file_name=query
                text_path=f"D:\study_material\TYIT project\{file_name}"
                f=open(file_name,'w')
                self.speak("file created")
                self.speak("listening text")            
                if file_name==query:
                    f.write(self.takeCommand()) 
                    f.close()
                    os.startfile(text_path)
                    
                else:
                    exit

            elif 'create table' in query:
                self.table()

            elif 'joke' in query:
                self.speak(pyjokes.get_joke())

            elif 'remember that' in query:
                remebermsg=query.replace("remember that","") 
                remembermsg= remebermsg.replace("vision","") 
                self.speak("you tell me to remind you that :"+remebermsg)     
                remeber=open('data.txt','w')
                remeber.write(remebermsg)
                remeber.close()

            elif 'what do you remember' in query:
                remeber = open('data.txt','r')
                self.speak("you tell me that"+remeber.read())

#maths operation----------------------------------------------------------------------------
            elif 'add two number' in query:
                sum=0
                self.speak("tell me first number sir")
                for i in range(2):
                    a=int(self.inp())
                    sum+=a
                
                self.speak(sum)

            elif 'subtract' in query:
                sub=0
                self.speak("tell me first number sir")
                p=int(self.takeCommand())
                self.speak("tell me second number sir")
                q=int(self.takeCommand())
                sub=int(p-q)
                self.speak(sub)
        
            elif 'multiply' in query:
                m=0
                self.speak("tell me first number sir")
                p=int(self.takeCommand())
                self.speak("tell me second number sir")
                q=int(self.takeCommand())
                m=int(p*q)
                self.speak(m)
        
            elif 'divide' in query:
                d=0
                self.speak("tell me first number sir")
                p=float(self.takeCommand())
                self.speak("tell me second number sir")
            
                q=float(self.takeCommand())
                d=float(p/q)
                self.speak(d)

            elif 'area of square' in query:
                self.speak("tell me side of square")
                s=float(self.takeCommand())
                a=s**2
                self.speak(a)

            elif 'area of circle' in query:
                p=3.14
                self.speak("tell me radius of circle")
                r=float(self.takeCommand())
                ac=p*(r**2)
                self.speak(ac)
        
            elif 'area of rectangle' in query:
                self.speak("tell me length of rectangle")
                l=float(self.takeCommand())
                self.speak("tell me breadth of rectangle")
                b=float(self.takeCommand())
                ar=l*b
                self.speak(ar)
    
               
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    MainWindow.show()
    sys.exit(app.exec_())
