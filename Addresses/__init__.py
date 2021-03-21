

####!/usr/bin/env python3
####!/usr/bin/python3
#!c:/Python39/python.exe
import getopt, sys, json

#with open('databasenew.json') as f:
  #data = json.load(f)


#with open('databasenew.json', 'w') as f:
#  json.dump = (data,f)

#with open('databasenew.json', 'w', encoding='utf-8') as f:
  #json.dump(data, f, ensure_ascii=False, indent=4)


# Define JSON data

JSONData = '{"Addressbook": [{"name": "Matthew Hurrell", "address": "5 Willow Green, Knutsford, Cheshire","postcode": "WA16 6AX"},{"name": "Tim Hurrell","address": "5 Cherry Blosson Grove, Leamington, Warwickshire","postcode": "CV31 2RT"},{"name": "Queen","address": "Palace","postcode": "SW1"}]}'
#JSONData = json.dumps(data)



class postaladdress:
  def __init__(self, name, address, postcode):
    self.name = name
    self.address = address
    self.postcode = postcode
  
  def description(self):
    return f"{self.name} has {self.postcode}"

# Declare class to store JSON data into a python dictionary
class addressbook(object):
  def __init__(self, jdata):
    self.__dict__ = json.loads(jdata)

  def find(self, name):
    for a in self.Addressbook:
      if a['name'] == name:
        return (a['postcode'])
        print (a['postcode'])

  
  def add(self, name,address,postcode):
    x1 = postaladdress(name,address,postcode)
    self.Addressbook.append(x1.__dict__)
    return self

  
  def remove(self, name):
    for a in self.Addressbook:
       if a['name'] == name:
          self.Addressbook.remove(postaladdress(a['name'],a['address'],a['postcode']).__dict__)
    return self
  
   
  def amend(self, name,address,postcode):
    for a in self.Addressbook:
       if a['name'] == name:
          a['address'] = address
          a['postcode'] = postcode
    return self


full_cmd_arguments = sys.argv

argument_list = full_cmd_arguments[1:]
#print (argument_list)

short_options = "hf:d:a:u:"
long_options = ["help", "findname=", "delete=", "add=","update="]

try:
    arguments, values = getopt.getopt(argument_list, short_options, long_options)
except getopt.error as err:
    # Output error, and return with an error code
    print (str(err))
    sys.exit(2)

# Evaluate given options
p_object = addressbook(JSONData)
print(arguments)
for current_argument, current_value in arguments:
    if current_argument in ("-f", "--findname"):
        p_object.find(current_value)
        for a in p_object.Addressbook:
            if a['name'] == current_value:
                print ('postcode is' , a['postcode'])
    elif current_argument in ("-d", "--delete"):
        p_object.remove(current_value)
    elif current_argument in ("-a", "--add"):  
        x = current_value.split(", ")
        p_object.add(x[0],x[1],x[2])
    elif current_argument in ("-u", "--update"):
        x = current_value.split(", ")
        p_object.amend(x[0],x[1],x[2])
    elif current_argument in ("-h", "--help"):
        print ("Displaying help")

#p_object.amend('Queen','Hotel','NW10')

print (p_object.Addressbook)



def write_json(data,filename = 'databasenew.json'):
  with open(filename, 'w', encoding='utf-8') as f:
    json.dump(data,f,indent = 4)


#with open('databasenew.json', encoding='utf-8') as json_file:
#  data = json.load(json_file)
#  temp = data['Addressbook']
#  x1 = postaladdress('Queen','Palace','SW1')
#  temp.append(x1.__dict__)
  #print (temp['Addressbook'].)

# write_json(data)



