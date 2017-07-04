# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 13:27:57 2017

@author: Don Quan
"""

class Computer(object):
    
        #"""A real world problem modelled using OOP"""
 
    #initialising a class variable
    pcCount = 0
    
    #initialization
    def __init__(self, RAM, processor_speed, hardDisk):
        self.RAM = RAM
        #Data hiding(making variable processor_speed private)
        self.__processor_speed = processor_speed
        self.hardDisk = hardDisk
        Computer.pcCount += 1
        
      
        
    def display_specifications(self):
        
        print ('RAM :', self.RAM, 'processor_speed :', self.__processor_speed, 'harddisk :', self.hardDisk)
 
    
    def print_documents(self):
        
        print ('i can print documents')
        
pc1 = Computer('2Gb', '2.4Ghz', '500Gb')
pc2 = Computer('4Gb', '2.3Ghz', '1Tb')
pc3 = Computer('8Gb', '2.7Ghz', '2Tb')

pc1.display_specifications()
pc2.display_specifications()
pc3.display_specifications()

print ("Total PCs %d" %Computer.pcCount)
        
print ("Computer._doc_:", Computer.__doc__)
print ("Computer._name_:", Computer.__name__)
print ("Computer._module_:", Computer.__module__)
print ("Computer._bases_:", Computer.__bases__)
print ("Computer._dict_:", Computer.__dict__) 

class mac(Computer):
    
    def print_document(self, colored):
        
        print ("Am overriding method")
        overriding = mac()
        overriding.print_document() 
            
    def mac_open_documents(self):
        
        print ("Mac can open documents")
        
