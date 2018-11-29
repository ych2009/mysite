import os
from django.core.mail import EmailMultiAlternatives

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

if __name__ == '__main__':

    subject, from_email, to = '来自www.blinkblink.com/index的测试邮件', 'blinkblinksf@sina.com', '1079804535@qq.com'
    text_content = 'blinkblinksf@sina.com'
    html_content = '<p>欢迎访问蛛丝马迹测试网站<a href="http://www.blinkblink.com/index" target=blank>www.blinkblink.com/index</a></p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()