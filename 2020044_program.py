# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 15:15:20 2021

@author: SELAB
"""
def encrypt(text,s):
    result = ""
    
    for i in range(len(text)):
       char = text[i]
       
       
       if (char.isupper()):
          result += chr((ord(char) + s-65) % 26 + 65)
       
       else:
          result += chr((ord(char) + s - 97) % 26 + 97)
    return result
    
text = "DEFENDTHEFORT"
s = 7
    
print ("Plain Text : " + text)
print ("Shift pattern : " + str(s))
print ("Decrypted string is " + encrypt(text,s))

text1=encrypt(text,s) 

def decrypt(text,s):
    result = ""
    
    for i in range(len(text)):
       char = text[i]
       
       
       if (char.isupper()):
          result += chr((ord(char) - s-65) % 26 + 65)
       
       else:
          result += chr((ord(char) - s - 97) % 26 + 97)
    return result

print("Decryption of the string is : ",end="")
print(decrypt(text1,s))

#kdhfdkjfghihfiugf
