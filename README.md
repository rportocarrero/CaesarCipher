# Substitution Cipher
## rationale
This is a simple program that demonstrates encoding and decoding letters in a substitution cipher.  This is used in conjunction with a series of blog posts about the basics of cryptography.
## Design
The cipher only shifts the letters in the plain and cipher texts,  The numbers, formatting, spacing all remains identical to the original plaintext message.
**Disclaimer**
This is not in any way cryptographically secure and should not be used for any non-educational appliations.
## Usage
This example requires python 3 to run
python3 subCipher.py -i <input file> -o <output file> -s <letter shift> <encrypt/decrypt>
### Example
Encrypt a plaintext file with a -3 shift and store the output in the ciphertext.txt file:
python3 -i plaintext.txt -o ciphertext.txt -s -3 encrypt

Decrypt a ciphertext file with a -3 shift and store the output in the decoded.txt file:
python3 -i ciphertext.txt -o decoded.txt -s -3 encrypt

## Files
subCipher.py : main program
plaintext.txt   : lorem ipsum example plaintext
ciphertext.txt  : lorem ipsum encrypted with a -3 shift
decoded.txt     : ciphertext.txt decrypted 

