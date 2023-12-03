from rdffwk.http_client.http_client import HttpClient
import xml.etree.ElementTree as et
import os

class ExportFormat:
    CSV = "csv"
    XML = "xml"
    JSON = "json"

class SparqlClient(HttpClient):
    def __init__(self, url, port=None, timeout=None):
        super(SparqlClient, self).__init__(url, port, "sparql", timeout)
        
    def send_and_parse(self, query, export_file=None, export_format=ExportFormat.CSV):
        response = self.send_query(query)
        return self.parse_response(response, export_file, export_format)
        
    def send_query(self, query):
        super(SparqlClient, self).send_query(query)
    
    def parse_response(self, response, export_file=None, export_format=ExportFormat.CSV):
        data = response.text
        body = data.split("\n", 1)[1]
        
        if len(body) == 0:
            return None
        
        match export_format:
            case ExportFormat.CSV:
                data = self._to_csv(body)
                if export_file:
                    self.write_csv(data, export_file)
            case _:
                raise Exception("Unsupported export format")
                
        return data
        
    
    def write_csv(self, response, export_file):
        variables, values = self._to_csv(response)
        self._write_csv(variables, values, export_file)
        
    def _write_csv(self, variables, values, export_file):
        with open(export_file, "w") as csv_file:
            csv_file.write(", ".join(variables) + "\n")
            csv_file.write("\n".join(values))
            
    def _to_csv(self, response):
        variables = []
        root = et.fromstring(response)
        
        for child in root:
            if child.tag == "{http://www.w3.org/2005/sparql-results#}head":
                for var in child:
                    variables.append(var.attrib["name"])
                    
        #get all the values from the body
        values = []
        for child in root:
            if child.tag == "{http://www.w3.org/2005/sparql-results#}results":
                for result in child:
                    res = []
                    for binding in result:
                        res.append(binding[0].text)
                    values.append(", ".join(res))
        
        return variables, values     