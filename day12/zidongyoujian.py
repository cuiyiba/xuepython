import smtplib
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# 第一步：连接到smtp服务器
smtp = smtplib.SMTP_SSL (host='smtp.163.com', port=465)

# 第二步：登录smtp服务器
smtp.login (user='fengxuanqi501401@163.com', password='ZITFNMPTMJUMMRCB')

# 第三步构建一封带附件的邮件
# 创建一封多组件的邮件
msg = MIMEMultipart ()
# 添加发件人
msg['From'] = "fengxuanqi501401@163.com"
# 添加收件人
msg['To'] = "2578157471@qq.com>"
# 添加主题
msg['Subject'] = Header ("带附件的测试邮件", charset='utf8')
# 添加邮件文本内容
# 创建邮件文件内容对象
text_content = MIMEText ("这封邮件是崔高升发送的，邮件中添加了测试报告的附件", _charset='utf8')
# 把邮件的文本内容，添加到多组件的邮件中
msg.attach (text_content)

# 添加附件
f_msg = open (r'F:\Python-work\xuepython\hankeruan\day12\测试报告.html', 'rb').read ()
app = MIMEApplication (f_msg)
app.add_header ('content-disposition', 'attachment', filename='计算器报告.html')
msg.attach (app)

# 发送邮件
smtp.send_message (msg=msg, from_addr="fengxuanqi501401@163.com", to_addrs="2578157471@qq.com")
