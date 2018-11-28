#/usr/bin/python
#coding:utf-8
1634044987
import smtplib
import os
def sendMail(body):
    smtp_server = 'smtp.163.com'
#    smtp_server = 'mail.qq.com'
    from_mail = 'm18612884847@163.com'
    mail_pass = 'gushuai110'
    to_mail = ['1634044987111@qq.com', '1353437177@qq.com']
    cc_mail = ['gushuai@shuziguanxing1231.com']
    from_name = 'monitor'
    subject = u'服务监控状态'.encode('gbk')   # 以gbk编码发送，一般邮件客户端都能识别
#     msg = '''\
# From: %s <%s>
# To: %s
# Subject: %s
# %s''' %(from_name, from_mail, to_mail_str, subject, body)  # 这种方式必须将邮件头信息靠左，也就是每行开头不能用空格，否则报SMTP 554
    mail = [
        "From: %s <%s>" % (from_name, from_mail),
        "To: %s" % ','.join(to_mail),   # 转成字符串，以逗号分隔元素
        "Subject: %s" % subject,
        "Cc: %s" % ','.join(cc_mail),
        "",
        body
        ]
    msg = '\n'.join(mail)  # 这种方式先将头信息放到列表中，然后用join拼接，并以换行符分隔元素，结果就是和上面注释一样了
    try:
        s = smtplib.SMTP()
        s.connect(smtp_server, '25')
        s.login(from_mail, mail_pass)
        s.sendmail(from_mail, to_mail+cc_mail, msg)
        s.quit()
    except smtplib.SMTPException as e:
        print "Error: %s" %e
def read_file_as_str(file_path):
    # 判断路径文件是否存在
    if not os.path.isabs(file_path):
        raise TypeError(file_path+"does not exist")
    with open(file_path,"rb+") as f:
        all_the_text=f.read()
        #print type(all_the_text)
        #print all_the_text
        return all_the_text
if __name__ == "__main__":
    a=read_file_as_str('/mptp/config.txt')
    print a
    if a.startswith("t"):
            sendMail("The service was stopped an hour ago, and the service has been restarted successfully now!")
    else:
            sendMail("This service has an exception and failed to start. Please help to fix it before 0 o 'clock the next day")

