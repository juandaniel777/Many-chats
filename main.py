from flask import Flask, jsonify
import base64
import urllib.parse
import html
import hashlib
import re
import unidecode
import jsonpickle
from flask_restful import Resource, Api
from flask import Flask, request
from json import JSONEncoder
import hashlib
from gevent.pywsgi import WSGIServer
import json
from flask import make_response

def intToRoman(num):
  
    # Storing roman values of digits from 0-9
    # when placed at different places
    m = ["", "M", "MM", "MMM"]
    c = ["", "C", "CC", "CCC", "CD", "D",
         "DC", "DCC", "DCCC", "CM "]
    x = ["", "X", "XX", "XXX", "XL", "L",
         "LX", "LXX", "LXXX", "XC"]
    i = ["", "I", "II", "III", "IV", "V",
         "VI", "VII", "VIII", "IX"]
  
    # Converting to roman
    thousands = m[num // 1000]
    hundereds = c[(num % 1000) // 100]
    tens = x[(num % 100) // 10]
    ones = i[num % 10]
  
    ans = (thousands + hundereds +
           tens + ones)
  
    return ans





def jsonDefault(object):
    return object.__dict__



def remove_html_tags(text):
    """Remove html tags from a string"""

    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)
def dictionaryfuction(funct,array1):
        response1=[]
        last=len(array1)
        if funct == 'length': 
           response1=len(array1) 

        elif funct == 'base64': 
            sample_string_bytes = array1 .encode("ascii")
            base64_bytes = base64.b64encode(sample_string_bytes)
            response1 = base64_bytes.decode("ascii")
        elif funct == 'capitalize': 
            response1= array1.capitalize()
        elif funct == 'decodeURL': 
            response1= urllib.parse.unquote(array1)
        elif funct == 'encodeURL': 
            response1= urllib.parse.quote(array1)   
        elif funct == 'escapeHTML': 
            response1= html.escape(array1)  
        elif funct == 'lower': 
            response1= array1.lower()
        elif funct == 'md5': 
            result = hashlib.md5(array1.encode("utf-8"))
            response1= result.hexdigest()
        elif funct == 'stripHTML': 
             response1= remove_html_tags(array1)
        elif funct == 'upper': 
             response1= array1.upper()
        elif funct == 'toString': 
             response1=str(array1)
        elif funct == 'trim': 
             response1=array1.replace(" ", "")
        elif funct == 'startcase': 
             response1=array1.title()
        elif funct == 'ascii': 
             if array1.find(";")>1 and array1[array1.find(";")+1:last] =="true" :
                 response1=unidecode.unidecode(array1[0:array1.find(";")])
             else:
                encoded_string = array1.encode("ascii", "ignore")
                response1 = encoded_string.decode()
        elif funct == 'contains': 
             strx=array1[0:array1.find(";")]
             response1=array1[array1.find(";")+1:last] in strx
        elif funct == 'split': 
            response1 = array1[0:array1.find(";")].split(array1[array1.find(";")+1:last])
        elif funct == 'toBinary': 
               if array1.find(";")>1 and array1[array1.find(";")+1:last] =="base64" :
                 #base64_bytes = array1[0:array1.find(";")].encode('ascii')
                 #response1 = base64.b64decode(base64_bytes)
                  #print(array1[0:array1.find(";")])
                  s=array1[0:array1.find(";")]
                  print(s.encode('utf-8'))
                  t= base64.b64decode(s.encode('utf-8'))
                  print(t)
                  response1=t.hex()
                  print(response1)
               elif array1.find(";")>1 and array1[array1.find(";")+1:last] =="base16" :
                  response1=bin(int(array1[0:array1.find(";")].encode().hex(),16))
                 #response1 = array1[0:array1.find(";")].encode().hex()
               else:
                            
                 response1 = (array1.encode('utf-8')).hex()
        elif funct=='substring':
             to_=array1[array1.find(";")+1 : array1.rfind(";")]
             until_=array1[ array1.rfind(";")+1: len(array1)]
             response1= array1[int(to_):int(until_)]
        elif funct=='replace':
             search_=array1[array1.find(";")+1 : array1.rfind(";")]
             replace_=array1[ array1.rfind(";")+1: len(array1)]
             response1= array1[0:array1.find(";")].replace(search_, replace_)
        elif funct=='indexOf':
             search_1=array1.find(";")
             replace_1= array1.rfind(";") 
             if search_1==replace_1:
                poss_=array1[array1.find(";")+1 : len(array1)]
                response1=array1[0:array1.find(";")].find(poss_)
             else:
               poss_= array1[ search_1+1 : replace_1]
               print( poss_)
               print(array1[0: search_1])
               print(array1[replace_1+1:len(array1)])
               print(len(array1[0: search_1]))
               response1=array1[0: search_1].find(poss_, int(array1[replace_1+1:len(array1)]),len(array1[0: search_1]))
        elif funct=='sha1':       
             hash_object = hashlib.sha1(array1.encode('utf-8'))
             response1 = hash_object.hexdigest()
        elif funct=='sha256':       
             response1 = hashlib.sha256(array1.encode('utf-8')).hexdigest()            
        elif funct=='sha512':       
             response1 = hashlib.sha512( array1.encode("utf-8") ).hexdigest() 
        elif funct=='rept':       
             rept=array1[0:array1.find(",")]
             rept=rept+" "
             print(rept)
             numrept= int(array1[ array1.find(",")+1: len(array1)])
             response1=rept*numrept
             print("rept") 
        elif funct=='roman':       
             nr=int(array1)
             response1=intToRoman(nr)
        elif funct=='right': 
             rigth=array1[0:array1.find(",")]
             until_ = len(rigth)
             from_=int(array1[ array1.find(",")+1: len(array1)])
             response1=rigth[(until_-from_): until_]
        elif funct=='left': 
             left=array1[0:array1.find(",")]
             until_ = len(left)
             from_=int(array1[ array1.find(",")+1: len(array1)])
             response1=left[0: from_] 
        try: 
             return  response1
        except ValueError:  
              result = {"result": "error","status": 0}
              result = make_response(json.dumps(result))
              return result

app = Flask('')
api = Api(app)
result = {}


class Test(Resource):
  def post(self):
      
      request_json = request.get_json() 
      if not request_json:
          result = {"result": "error","status": 0}
          result = make_response(json.dumps(result))
          return result
      print(request_json )
      fuct=request_json["function"]
      result=request_json
      begin=[pos for pos, char in enumerate(fuct) if char == "("]
      end=[pos for pos, char in enumerate(fuct) if char == ")"]
   
      array_=fuct[begin[len(begin)-1]+1:end[0]]
      
      for i in range(len(begin)-1,0,-1):
          funct_=fuct[begin[i-1]+1:begin[i]]
          try:
              array_=dictionaryfuction(funct_,array_)
              print(fuct[begin[i-1]+1:begin[i]])
              print(fuct[0:begin[0]])
              break
          except ValueError:  
               result = {"result": "error","status": 0}
               result = make_response(json.dumps(result))
               return result
            
      try:
          array_=dictionaryfuction(fuct[0:begin[0]],array_) 
          print(array_)  
          try:
            if len(array_) == 2:
               result = {"result": array_,"status":0 }
               result = make_response(json.dumps(result))
               return result
            else:
                result = {"result":array_,"status": 1}
                result = make_response(json.dumps(result))
                #result=str(result)
                #result=json.load(result)
                #result = json.dumps(result  ,sort_keys=True )
                print(result)
                return result
          except :
               result = {"result": array_,"status":0 }
               result = make_response(json.dumps(result))
               return result
      except ValueError:
            result = {"result": "error","status": 0}
            result =make_response(json.dumps(result))
        #result =jsonpickle.encode(result)
      #result =jsonpickle.encode(result)     
      return result
    
      
      #return "Example with Flask-Restful"
  def get(self):
      #return "Example with Flask-Restful"
      return result
    
#creating api endpoint
api.add_resource(Test, '/')

if __name__ == "__main__":
  
  app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False  
  #app.run(host='0.0.0.0', port='8080',debug=True) 
  http_server = WSGIServer(('0.0.0.0', 8080), app) 
  http_server.serve_forever()