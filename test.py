import unittest
import json
from Addresses import addressbook




#how to run one test?
JSONData = '{"Addressbook": [{"name": "Matthew Hurrell", "address": "5 Willow Green, Knutsford, Cheshire","postcode": "WA16 6AX"},{"name": "Tim Hurrell","address": "5 Cherry Blosson Grove, Leamington, Warwickshire","postcode": "CV31 2RT"},{"name": "Queen","address": "Palace","postcode": "SW1"}]}'

class TestString(unittest.TestCase):

    def test_find(self):
        """
        Test filter is true
        
        """
        data = addressbook(JSONData)
        result = data.find('Matthew Hurrell')
        self.assertEqual(result, "WA16 6AX")
    
    def test_add1(self):
        """
        Test filter is true
        
        """
        data = addressbook(JSONData)
        origlen = len(data.Addressbook)
        data2 = data.add('Prince','Highgrove','GL7')
        result = len(data2.Addressbook) - origlen
        self.assertEqual(result, 1)
    
    def test_add2(self):
        """
        Test filter is true
        
        """
        data = addressbook(JSONData)
        data2 = data.add('Prince','Highgrove','GL7')
        len1 = len(data.Addressbook)
        result = data2.Addressbook[len1-1]['name']
        self.assertEqual(result, 'Prince')
    
    def test_remove1(self):
        """
        Test filter is true
        
        """
        data = addressbook(JSONData)
        origlen = len(data.Addressbook)
        data2 = data.remove('Queen')
        result = origlen - len(data2.Addressbook)
        self.assertEqual(result, 1)
    
    def test_remove2(self):
        """
        Test filter is true
        
        """
        data = addressbook(JSONData)
        data2 = data.remove('Queen')
        result = False
        for a in data2.Addressbook:
            if a['name'] == 'Queen':
                result = True
        self.assertIsNot(result, True)

    
    def test_amend(self):
        """
        Test filter is true
        
        """ 
        data = addressbook(JSONData)
        data2 = data.amend('Queen','Hotel','NW10')
        result = data2.find('Queen')
        self.assertNotEqual(result, 'SW1')

if __name__ == '__main__':  
    unittest.main()

 
