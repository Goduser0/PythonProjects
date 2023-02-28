from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import time

import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


from_addr = '1318917927@qq.com'
password = 'wuwhjhqqecvzhhaf'
all_to_addr = ['noelstallworth@163.com', '1240298579@qq.com']
smtp_server = 'smtp.qq.com'

for to_addr in all_to_addr:
    # 纯文本内容
    msg = MIMEText('hello, send by Python...'+str(time.localtime()), 'plain', 'utf-8')

    # html邮件
    msg = MIMEText('<html><body><h1>Hello</h1>' +
                   '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
                   '</body></html>', 'html', 'utf-8')

    # 带附件

    # 正文中带图片
    msg['From'] = _format_addr('Noel Stallworth <%s>' % from_addr)
    msg['To'] = _format_addr('Guest <%s>' % to_addr)
    msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

    server = smtplib.SMTP_SSL(smtp_server, 465)  # qq邮箱服务器地址和端口
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()
