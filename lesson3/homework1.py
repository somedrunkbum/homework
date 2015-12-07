#!/usr/bin/python
# coding=utf-8
import smtplib, argparse


parser = argparse.ArgumentParser(description='Send mail')
parser.add_argument('-m', '--mail_server', type=str, required=True, help='Mail server URL')
parser.add_argument('-p', '--mail_port', type=int, default=587, help='Mail server port')
parser.add_argument('-f', '--from_addr', type=str, required=True, help='Address to send mail from')
parser.add_argument('-ps', '--passw', type=str, required=True, help='Mail from password')
parser.add_argument('-t', '--to_addr', type=str, required=True, help='Address to send mail to')
parser.add_argument('-s', '--subj', type=str, required=True, help='Mail subject')
parser.add_argument('-txt', '--text', type=str, required=True, help='Mail body')

args = parser.parse_args()

mail_server_url = args.mail_server
mail_server_prot = args.mail_port
from_address = args.from_addr
password = args.passw
to_address = args.to_addr
subject = args.subj
text = args.text

smtp_obj = smtplib.SMTP(mail_server_url, mail_server_prot)

print(smtp_obj.ehlo())

print(smtp_obj.starttls())

print(smtp_obj.login(from_address, password))

print(smtp_obj.sendmail(from_address, to_address,
    'Subject: ' + subject + '\n\n' + text))

print(smtp_obj.quit())
