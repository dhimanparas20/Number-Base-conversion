from flask_restful import Resource, Api
from flask import render_template
from os import system,path
from flask import *
import json,time
import requests

system("clear")

# converts any base to decimal base     
def conv_decimal(num,base):
  ln = len(str(num))
  i,dec = 0,0
  while ln > 0:
    rem = num%10
    num = int(num/10) 
    dec = dec + rem*(base**i)
    ln -= 1
    i += 1     
  return dec

# converts decimal number to any base  
def conv_n(num,base):
    base_num = ""
    while num>0:
        dig = int(num%base)
        if dig<10:
            base_num += str(dig)
        else:
            base_num += chr(ord('A')+dig-10)  #Using uppercase letters
        num //= base

    base_num = base_num[::-1]  #To reverse the string
    return base_num

# converts from any base to any base
def convert(num,frm,to):
  if to == 10:
      return conv_decimal(num,frm)
  else:
    print("")
    return (conv_n(conv_decimal(num,frm),to))

#staring web app
app = Flask(__name__)
api = Api(app)

class Home(Resource):
  def get(self):
    print("--------------------------")
    print("Home Page loaded") 
    frm = request.args.get('frm')
    to = request.args.get('to')
    v1 = request.args.get('value1')
    # from
    if frm  == "binary":
      f = 2
    elif frm  ==  "octal":
      f = 8
    elif frm  ==  "decimal":
      f = 10
    elif frm  ==  "hexa":
      f = 16 
    else:
      f = 10  
    # To  
    if to  == "binary":
      t = 2
    elif to  ==  "octal":
      t = 8
    elif to  ==  "decimal":
      t = 10
    elif to  ==  "hexa":
      t = 16  
    else:
      t = 10  
    
    # Set v1 initially when site loads  
    if v1 == None:
      v1 = "0"

    output = convert(int(v1),f,t)
    if output == 0:
      output,v1,f,t= None,None,0,0 

    return make_response(render_template('index.html',output=output,v1=v1,base1=f,base2=t))

api.add_resource(Home, '/',methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run()

