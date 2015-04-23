import re
import sys
import os

class Data():
    '''Class to print and display the data of the given items'''

    def __init__(self, name):
        '''constructor to display the name and location of the person'''
        self.name = name
        self.list = ['gipson', 'bobby', 'ricky', 'karthi']
        if self.name in self.list:
            print("The name is present in the given list")

        else:
            print("There is no such name in the list")
    def location(self, name):
        self.location = {'Telangana': 'gipson', 'UP': 'bobby', 'Delhi': 'ricky', 'Chennai': 'karthi'}
        for key, value in self.location.items():
            #print (key, value)
            if value == self.name:
                print(self.name)
                break
            else:
                print('failure') 
        

gip = Data('gipson')
gip.location('gipson')
