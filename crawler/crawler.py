import requests 
import traceback

def get_threads():
    proxies = {
    'http': 'http://181.143.124.243:56935'
    }
    URL = "https://2ch.hk/b/threads.json"

    r = requests.get(url = URL, proxies=proxies, timeout=10) 
    return r.json()

try:
    print(get_threads())
except:
    print("An exception occurred")
    traceback.print_exc()
    
print("end")