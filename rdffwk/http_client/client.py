

#Build a HTTP client to send requests to the server
import os
import requests
import xml.etree.ElementTree as et


class HttpClient(object):
    
    def __init__(self, url, port, timeout):
        self.url = url
        self.port = port
        self.timeout = timeout
        
    def send_query(self, query):
        headers = {"Content-Type": "application/sparql-query"}
        response = requests.post(self.url, headers=headers, data=query, timeout=self.timeout)
        print(response.status_code)
        self.__handle_http_response(response, "test.csv")
        
        
    
    def __handle_http_response(self, response, export_file, first_query_flag=False):
        data = response.text
        body = data.split("\n", 1)[1]

        if len(body) > 0:
            csv_representation = self.to_csv(body)
            
            if export_file is not None:
                # In order to skip the header line before appending to file
                if os.path.exists(export_file):
                    data = body
                #Translate the response from a XML to CSV format
                self.to_csv(data)
                    
            return response.text
    
    def to_csv(self, response):
        #get all the variables from the header
        vars = []
        root = et.fromstring(response)
        
        for child in root:
            if child.tag == "{http://www.w3.org/2005/sparql-results#}head":
                for var in child:
                    vars.append(var.attrib["name"])
                    
        #get all the values from the body
        values = []
        for child in root:
            if child.tag == "{http://www.w3.org/2005/sparql-results#}results":
                for result in child:
                    res = []
                    for binding in result:
                        res.append(binding[0].text)
                    values.append(", ".join(res))
                    
        print(values)   
              
        #create the csv file
        with open("test.csv", "w") as csv_file:
            csv_file.write(", ".join(vars) + "\n")
            csv_file.write("\n".join(values))
            
            
        