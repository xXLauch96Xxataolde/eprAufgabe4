'''
Created on 27.11.2017

@author: Robert
'''



def testing():
    liste = []
    liste.append("1")
    liste.append(12)
    liste.append(67)
    liste.append(3)
    
    print(liste)
    print(len(liste))
    liste.insert(2, "here")
    
    print(liste)
    print(len(liste))

if __name__ == '__main__':
    testing()