import requests

class HttpClient(object):
    def __init__(self, url, port=None, url_suffix=None, timeout=None):
        self.url = self._fix_url(url, port, url_suffix)
        
        self.timeout = timeout
        
        #self.check_connection()
        
    def send_query(self, query):
        headers = {"Content-Type": "application/sparql-query"}
        response = requests.post(self.url, headers=headers, timeout=self.timeout, data=query)
        return response
    
    def _fix_url(self, url, port, suffix):    
        if port is not None:
            url += ":" + str(port)
            
        if suffix is not None:
            url += "/" + suffix
            
        return url

    def check_connection(self):
        if self._probe():
            print("Connection to " + self.url + " is OK")
        else:
            exit("Connection to " + self.url + " is not OK")
        
    def _probe(self):
        try:
            response = requests.get(self.url, timeout=self.timeout)
            return response.status_code == 200
        except:
            return False