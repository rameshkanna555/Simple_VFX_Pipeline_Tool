from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


def sendingMail():
    server = smtplib.SMTP_SSL('smtp.gmail.com:465')
    server.login('rameshkanna95@gmail.com','bujji199555')

    ip = "Kanna"
    message = MIMEMultipart('alternative')
    message['Subject'] = 'Internet is down -' + ip
    message['From'] = 'rameshkanna95@gmail.com'
    message['To'] = 'rameshkanna95@gmail.com'
    # message.attach(MIMEText(html, 'html'))
    # html= """"""
    # message.attach(MIMEText(html, 'html'))

    # message.attach(MIMEText('<h1 style="color:red"> No Ping Response on IP: ' + ip + '</h1>', 'html'))
    message.attach(MIMEText('<style> .td_one{background-color:#c9daf8} th{padding:6px} table {border-collapse:collapse;border-spacing:0;border-color:black;border-style:solid;border-width:1px} td {text-align:center;border-color:black;border-style:solid;border-width:1px;overflow:hidden;padding:8px 5px;word-break:normal;} </style> <table> <thead> <tr> <th colspan="12"><b style="text-align:center">Shot Details </b></th> </tr> </thead> <tbody> <tr> <td colspan="10" class="td_one">Shot Owner</td> <td> </td> </tr> <tr> <td colspan="10" class="td_one">Department</td> <td> Department_Name </td> </tr> <tr> <td colspan="10" class="td_one" >Show Name </td> <td>' + ip +  '</td> </tr> <tr> <td colspan="10" class="td_one">Shot Number</td> <td> tun_145_0010</td> </tr> <tr> <td colspan="10" class="td_one"> Version</td> <td> v011</td> </tr> <tr> <td colspan="10" class="td_one"> Frame Range </td> <td> 1001-1075</td> </tr> <tr> <td colspan="10" class="td_one"> Resolution </td> <td> 2048x1108</td> </tr> <tr> <td colspan="10" class="td_one"> Notes to Client </td> <td> NOTE_TO_TYPE</td> </tr> <tr> <td colspan="10" class="td_one">Output Path</td> <td> PATH </td> </tr> <tr> <td colspan="10" class="td_one">Approved By</td> <td> Supervisor </td> </tr> </tbody> </table> ', 'html'))
    server.sendmail('rameshkanna95@gmail.com', 'rameshkanna95@gmail.com', message.as_string())

    server.quit()


