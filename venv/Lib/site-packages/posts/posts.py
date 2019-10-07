# -*- coding: utf-8 -*-

import smtplib
import socket
from contextlib import contextmanager
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


class PostSMTP(smtplib.SMTP):

    def __init__(self, sender, alias=None, host='', port=0,
                 local_hostname=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT):
        smtplib.SMTP.__init__(self, host, port, local_hostname, timeout)
        self._sender = sender
        self._sender_alias = alias if alias else sender.split('@')[0]
        self._attachments = {}
        self._mails = []

    def attach(self, attachments):
        """Add attachments.

        Args:
            attachments (dict): attachments
                example: {'alias_name': 'path/to/filename'}
        Returns:
            obj to support chain calling.
        """
        try:
            iteritems = attachments.iteritems()
        except AttributeError:
            iteritems = attachments.items()
        for k, v in iteritems:
            self._attachments[k] = v
        return self

    def _header(self, msg, recipient, subject):
        msg['Subject'] = subject
        msg['From'] = '{} <{}>'.format(self._sender_alias, self._sender)
        msg['To'] = ', '.\
            join(recipient) if isinstance(recipient, list) else recipient
        return msg

    def _mount(self, mail, files):
        for _ in files:
            mail['msg'].attach(_)
        return mail

    def _load_files(self):
        files = []
        try:
            iteritems = self._attachments.iteritems()
        except AttributeError:
            iteritems = self._attachments.items()
        for k, v in iteritems:
            with open(v, 'rb') as f:
                part = MIMEApplication(f.read())
            part.add_header('Content-Disposition', 'attachment', filename=k)
            part.add_header('Content-ID', '<{}>'.format(k))
            files.append(part)
        return files

    def text(self, recipient, subject, content, charset='us-ascii'):
        _text = MIMEText(content, _subtype='plain', _charset=charset)
        _msg = MIMEMultipart()
        _msg = self._header(_msg, recipient, subject)
        _msg.attach(_text)
        self._mails.append({
            'recipient': recipient,
            'msg': _msg
        })
        return self

    def html(self, recipient, subject, content, charset='utf-8'):
        _html = MIMEText(content, _subtype='html', _charset=charset)
        _msg = MIMEMultipart()
        _msg = self._header(_msg, recipient, subject)
        _msg.attach(_html)
        self._mails.append({
            'recipient': recipient,
            'msg': _msg
        })
        return self

    def _send(self):
        files = self._load_files()
        for mail in self._mails:
            self._mount(mail, files)
            self.sendmail(
                self._sender,
                mail['recipient'],
                mail['msg'].as_string())


class Posts(object):

    def __init__(self, host, usermame, password, port=25):
        self._host = host
        self._port = port
        self._username = usermame
        self._password = password

    @contextmanager
    def __call__(self, sender=None, alias=None, ssl=False):
        sender = sender if sender else self._username
        self._smtp = PostSMTP(sender, alias)
        self._smtp.connect(self._host)
        if ssl:
            self._smtp.ehlo()
            self._smtp.starttls()
            self._smtp.ehlo()
        self._smtp.login(self._username, self._password)
        try:
            yield self._smtp
            self._smtp._send()
        finally:
            self._smtp.quit()
