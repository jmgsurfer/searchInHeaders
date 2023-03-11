import urllib.request as ulr
from sys import argv
#
#
headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
}

def usage():
    print('\nUsage: searchInHeaders <url>\nExample: snip1.py https://google.com\n')
    exit()
    
    
def get_headers(url,headers):
    req = ulr.Request(
    url, 
    data=None, 
    headers= headers
    )
    resp = ulr.urlopen(req)
    return resp.headers
    

def all():
    print('\n')
    print(get_headers(url,headers))
    exit()

    
def select(query):
    a = get_headers(url, headers)
    h= a.as_string().split('\n')
    for i in range(0, len(h)-1):
        if h[i].find(query) >= 0:
            print('\n')
            print(h[i], '\n')
        if i == len(h) - 1:
            print('\nNo ',query, ' header')

if len(argv) == 1 or len(argv) >2:
    usage()
    
url= argv[1]#'https://www.google.com'

print('\nLook for specific word in response headers for:\n==============================================\n','==>',url)
query = input('\nWhich term: ')
if query == "all":
    all()
else:
    select(query)

