import nuke
import os,shutil
import subprocess
import time
import threading
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import SendingMail



############# this class Qt-publisher #################


class ProgressBar(QWidget):

    def __init__(self):
        super(ProgressBar, self).__init__()

        self.setWindowTitle('progress')
        self.setGeometry(500, 500, 400, 150)
        self.setFixedSize(400, 150)

        self.widgets()
        self.show()

    def widgets(self):
        self.mainlayout = QVBoxLayout()
        self.vblayout = QVBoxLayout()
        self.hblayout = QHBoxLayout()
        self.progressbar = QProgressBar()

        self.publishbutn = QPushButton('Publish')
        self.mailbutn = QPushButton('Send-mail')
        self.mailbutn.clicked.connect(self.sendingMail)


        self.timer = QTimer()
        self.timer.setInterval(1000)


        self.vblayout.addWidget(self.progressbar)
        self.hblayout.addWidget(self.publishbutn)

        self.hblayout.addWidget(self.mailbutn)

        self.mainlayout.addLayout(self.vblayout)
        self.mainlayout.addLayout(self.hblayout)

        self.setLayout(self.mainlayout)


    def sendingMail(self):
        self.mail = SendingMail.sendingMail()
        self.close()




class QtPublisher(ProgressBar):

    progressChanged = Signal(int)

    def __init__(self):
        super(QtPublisher, self).__init__()

        #self.converter = Qt_Converter()
        self.publishbutn.clicked.connect(self.converter)
        self.publishbutn.clicked.connect(self.thread)

        self.progressChanged.connect(self.progressbar.setValue)

    def converter(self):

        #os.mkdir(r'C:\FFMPEG\kan')

        ffmpegpath = 'C:/Users/DELL/.nuke/Hulahoop_Pipeline/ffmpeg.exe'

        input = r'F:\Projects\TestinfPipeline\B1_RL_06_SHT_057\input\B1_RL_06_SHT_057_v001\B1_RL_06_SHT_057_%04d.exr'
        output = r'F:\Projects\TestinfPipeline\B1_RL_06_SHT_057\output\qt\B1_RL_06_SHT_057.mov'

        cmd = 'ffmpeg -f image2 -i "{}" -vf scale=1920:1080 -c:v prores_ks -profile:v 3 "{}"'.format(input,output)

        #cmd = [ffmpegpath, '-f', input, '-vf', 'scale=1920:1080', '-r', '15', output]

        print(cmd)

        subprocess.check_output(cmd, shell=True)


    def checker(self):

        self.destination_path = r'F:\Projects\TestinfPipeline\new\kanna.mp4'
        self.source_path = r'F:\Projects\TestinfPipeline\B1_RL_06_SHT_057\output\qt\B1_RL_06_SHT_057.mov'


        # Making sure the destination path exists
        while not os.path.exists(self.destination_path):
            time.sleep(.01)

        # Keep checking the file size till it's the same as source file
        while os.path.getsize(self.source_path) != os.path.getsize(self.destination_path):
            percentage = (int((float(os.path.getsize(self.destination_path)) / float(os.path.getsize(self.source_path))) * 100))

            time.sleep(.01)
            self.progressChanged.emit(percentage)

        percentage = 100
        self.progressChanged.emit(percentage)



    def copyingFile(self):

        self.destination_path = r'F:\Projects\TestinfPipeline\new\kanna.mp4'
        self.source_path = r'F:\Projects\TestinfPipeline\B1_RL_06_SHT_057\output\qt\B1_RL_06_SHT_057.mov'

        #print("Copying....")
        shutil.copyfile(self.source_path, self.destination_path)

        if os.path.exists(self.destination_path):
            #print("Done....")
            return True

        #print("Filed...")
        return False

    def thread(self):

        t = threading.Thread(name='copying', target=self.copyingFile, args=())
        # Start the copying on a separate thread
        t.start()
        # Checking the status of destination file on a separate thread
        b = threading.Thread(name='checking', target=self.checker, args=())
        b.start()


############# this class Final-publisher #################



class FinalPublisher(ProgressBar):


    progressChanged = Signal(int)

    def __init__(self):

        super(FinalPublisher, self).__init__()

        self.publishbutn.clicked.connect(self.thread)

        self.progressChanged.connect(self.progressbar.setValue)


    def checker(self):

        self.source_path = r'F:/Projects/TestinfPipeline/B1_RL_06_SHT_057/input/B1_RL_06_SHT_057_v001/'
        self.destination_path = r'F:/Projects/TestinfPipeline/new/'

        # Making sure the destination path exists
        while not os.path.exists(self.destination_path):
            time.sleep(.01)

        # Keep checking the file size till it's the same as source file
        while os.path.getsize(self.source_path) != os.path.getsize(self.destination_path):
            percentage = (int((float(os.path.getsize(self.destination_path)) / float(os.path.getsize(self.source_path))) * 100))

            time.sleep(.01)
            self.progressChanged.emit(percentage)
        percentage = 100
        self.progressChanged.emit(percentage)



    def copying_file(self):

        self.source_path = r'F:/Projects/TestinfPipeline/B1_RL_06_SHT_057/input/B1_RL_06_SHT_057_v001/'
        self.destination_path = r'F:/Projects/TestinfPipeline/new/'

        for files in os.listdir(self.source_path):
            filename = files
            shutil.copy(self.source_path + filename, self.destination_path)

        if os.path.exists(self.destination_path):
            # print("Done....")
            return True



    def thread(self):

        t = threading.Thread(name='copying', target=self.copying_file, args=())
        # Start the copying on a separate thread
        t.start()
        # Checking the status of destination file on a separate thread
        b = threading.Thread(name='checking', target=self.checker, args=())
        b.start()
