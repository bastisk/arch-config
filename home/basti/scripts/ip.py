#Gets external IP Adress

import urllib.request
page = urllib.request.urlopen('https://basti-sk.com/php/ip.php')
print(page.read())


