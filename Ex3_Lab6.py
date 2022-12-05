import re
import urllib.request

emails = []
with urllib.request.urlopen("https://www.tinthethao.com.vn/") as response:
    body = response.read()
    emails += re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', body.decode('utf-8'))
    urls = re.findall\
            ('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|\
            (?:%[0-9a-fA-F][0-9a-fA-F]))+', body.decode('utf-8'))
    for url in urls:
        try:
            with urllib.request.urlopen(url) as response:
                body = response.read().decode('utf-8')
                emails += re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', body)
        except:
              continue

# Loại bỏ những phần tử giống nhau
print(sorted(set(emails), key=emails.index))