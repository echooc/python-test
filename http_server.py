import httplib
conn = httplib.HTTPConnection("www.jxust.edu.cn")
conn.request('get', '/')
print conn.getresponse().read()

conn.close()