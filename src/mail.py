#!/usr/bin/env python
#coding=utf-8

import os
import sys
import time
import smtplib
import traceback
from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart

sys.path.append("..")
from etc import default as config
logger = config.logger

def get_mail_content_html(task_name, task_time, status, msg):
    dateNow = time.strftime(config.TIME_FORMAT, time.localtime())
    html = "<html><head><meta http-equiv=\"content-type\" content=\"text/html; charset=UTF-8\"/></head><h1 align='center'>ReMatch New Task Monitor Report</h1>"
    html += "<h3 align='center'>" + dateNow + "</h3>"
    html += "<table align='center' width='1000' border=2 bodercolor=#ffaa00>" + \
            "<tr align='center'>" + \
            "<th>Task Name</th><th>Created At</th><th>Status</th><th>Message</th></tr>"
    html += "<tr align='center'><th>%s</th><th>%s</th><th>%s</th><th>%s</th></tr>" %(task_name, task_time, status, msg)
    html += "</table>"
    html += "</html>"

    return html

def SendMail(content, type = 'text'):
    msg = MIMEMultipart('related')
    msg['Subject'] = config.mail_sub
    msg['From'] = config.mail_from
    msg['To'] = ",".join(config.mail_to)
    body = MIMEText(content, type,  _charset='UTF-8')
    msg.attach(body)

    try:
        server = smtplib.SMTP(config.mail_server)
        server.sendmail(config.mail_from, config.mail_to, msg.as_string())
        server.close()
    except Exception, e:
        logger.error(traceback.format_exc())
        return False

    return True

def send_mail(*args, **kwargs):
    try:
        logger.info("send_mail.")
        task_folder = args[0]
        pro_status = args[1]
        msg = args[2]
        task_name = os.path.basename(task_folder)
        task_time = time.strftime(config.TIME_FORMAT, time.localtime(os.path.getmtime(task_folder)))
        mail_content = get_mail_content_html(task_name, task_time, pro_status, msg)

        return SendMail(mail_content, config.mail_type)
    except Exception, e:
        logger.error(e)

if __name__ == "__main__":
    send_mail("/home/vsftpd/oqm/task1", "success", "finish") 
