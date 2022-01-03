from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import smtplib
import pathlib

class SendEmail:
    """
    #smtp地址，用户名，密码，接收邮件者，邮件标题，邮件内容，邮件附件
    """
    def __init__(self,title,
                 recv="314983713@qq.com",
                 smtp_addr="smtp.qq.com",
                 username="1315270232@qq.com",
                 password="shqwihtlifxojheg",
                 content=None,file=None):
        self.smtp_addr = smtp_addr
        self.username = username
        self.password = password
        self.recv = recv
        self.title = title
        self.content = content
        self.file = file

    def send_mail(self):
        """
        发送邮件方法
        :return:
        """
        try:
            msg = MIMEMultipart()                                                   #MIME
            msg.attach(MIMEText(self.content,_charset="utf-8"))                     #初始化邮件信息
            msg["Subject"] = self.title                                             #标题
            msg["From"] = self.username                                             #发送者账号
            msg["To"] = self.recv                                                   #接受者
            if self.file:                                                           #判断是否附件  #邮件附件
                att = MIMEApplication(open(self.file,"rb").read())
                att.add_header('Content-Disposition', 'attachment', filename =pathlib.Path(self.file).name)
                msg.attach(att)                                                     #将内容附加到邮件主体中
            self.smtp = smtplib.SMTP(self.smtp_addr,port=25)                        #登录邮件服务器
            self.smtp.login(self.username,self.password)
            self.smtp.sendmail(self.username,self.recv,msg.as_string())             #发送邮件
        except:
            pass

if __name__ == "__main__":

    file = "F:\\6_山东--分类\\002 测试用例\\1、四川用例.xlsx"
    SendEmail("test",file=file).send_mail()



