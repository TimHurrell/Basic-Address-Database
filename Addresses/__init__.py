

#!/usr/bin/env python
import sys
import json

for arg in sys.argv:
  print(arg)

#with open('databasenew.json') as f:
  #data = json.load(f)

#for address in data['Addressbook']:
#  print (address)


#with open('databasenew.json', 'w') as f:
#  json.dump = (data,f)

#with open('databasenew.json', 'w', encoding='utf-8') as f:
  #json.dump(data, f, ensure_ascii=False, indent=4)


##print (data['Addressbook'])
#print (type(data))

#list1 = [1,2,3]
#print (type(list1))

#json.dump(data,indent = 4)


# Define JSON data
#JSONData = '{"Java": "3 Credits", "PHP": "2 Credits", "C++": "3 Credits"}'
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
    

# Assign object of the class
p_object = addressbook(JSONData)
p_object.find('Matthew Hurrell')
p_object.add('Prince','Highgrove','GL7')
p_object.remove('Prince')
p_object.amend('Queen','Hotel','NW10')

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




#print(p_object.Addressbook[0])
##for a in p_object.Addressbook:
#  if a['name'] == "Matthew Hurrell":
# print (a['postcode'])
#print (type(p_object.Addressbook))



