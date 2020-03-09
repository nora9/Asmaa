# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 21:51:40 2020

@author: asmaa
"""



import sys

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)
import sys, getopt

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print 'test.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -i <inputfile> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print 'Input file is "', inputfile
   print 'Output file is "', outputfile

if __name__ == "__main__":
   main(sys.argv[1:])



""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#A python program to illustrate Caesar Cipher Technique 

key = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(n, plaintext):
    """Encrypt the string and return the ciphertext"""
    result = ''

    for l in plaintext.lower():
        try:
            i = (key.index(l) + n) % 26
            result += key[i]
        except ValueError:
            result += l

    return result.lower()

def decrypt(n, ciphertext):
    """Decrypt the string and return the plaintext"""
    result = ''

    for l in ciphertext:
        try:
            i = (key.index(l) - n) % 26
            result += key[i]
        except ValueError:
            result += l

    return result

text = "I am coding Python on SoloLearn!"
offset = 5

encrypted = encrypt(offset, text)
print('Encrypted:', encrypted)

decrypted = decrypt(offset, encrypted)
print('Decrypted:', decrypted)

""""""""""""""""""""""""""""""""""""""""""""""""""""""

 

def egcd(a, b): 
    x,y, u,v = 0,1, 1,0
    while a != 0: 
        q, r = b//a, b%a 
        m, n = x-u*q, y-v*q 
        b,a, x,y, u,v = a,r, u,v, m,n 
    gcd = b 
    return gcd, x, y 
  
def modinv(a, m): 
    gcd, x, y = egcd(a, m) 
    if gcd != 1: 
        return None  # modular inverse does not exist 
    else: 
        return x % m 
  
  
# affine cipher encrytion function  
# returns the cipher text 
def affine_encrypt(text, key): 
    ''' 
    C = (a*P + b) % 26 
    '''
    return ''.join([ chr((( key[0]*(ord(t) - ord('A')) + key[1] ) % 26)  
                  + ord('A')) for t in text.upper().replace(' ', '') ]) 
  
  
# affine cipher decryption function  
# returns original text 
def affine_decrypt(cipher, key): 
    ''' 
    P = (a^-1 * (C - b)) % 26 
    '''
    return ''.join([ chr((( modinv(key[0], 26)*(ord(c) - ord('A') - key[1]))  
                    % 26) + ord('A')) for c in cipher ]) 
  
  
# Driver Code to test the above functions 
def main(): 
    # declaring text and key 
    text = 'AFFINE CIPHER'
    key = [17, 20] 
  
    # calling encryption function 
    affine_encrypted_text = affine_encrypt(text, key) 
  
    print('Encrypted Text: {}'.format( affine_encrypted_text )) 
  
    # calling decryption function 
    print('Decrypted Text: {}'.format
    ( affine_decrypt(affine_encrypted_text, key) )) 
  
  
if __name__ == '__main__': 
    main() 

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def encrypt(plaintext, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    plaintext_int = [ord(i) for i in plaintext]
    ciphertext = ''
    for i in range(len(plaintext_int)):
        value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
        ciphertext += chr(value + 65)
    return ciphertext


def decrypt(ciphertext, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]
    plaintext = ''
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
        plaintext += chr(value + 65)
    return plaintext




