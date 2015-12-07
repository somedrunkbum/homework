import urllib2, urllib

api_key = 'bc0917d5-3087-7014-6d26-d5b56f38f655'

phone = '375291439786'

url_template = 'http://sms.ru/sms/send?api_id=%(api_key)s&to=%(phone)s'

url = url_template % {"api_key": api_key, "phone": phone}

text = u'Hello, bear!!'

encoded_text = urllib.urlencode( {"text": text.encode('utf-8') } )

headers = {"Content-type":  "application/x-www-form-urlencoded",}

r = urllib2.Request(url, data=encoded_text, headers=headers)

u = urllib2.urlopen(r)

u.read()