
import sys
import getopt

# This function encrypts a file with a substituion cipher
def encrypt(inName, outName, shift):

    try:
        inFile = open(inName, "r")
        outFile = open(outName, "w")
    except FileNotFoundError as err:
        print(err)
        sys.exit(2)

    for line in inFile:
        for character in line:
            A = ord(character)
            # for uppercase characters
            if(65 <= A <= 90):
                B = (((A + shift) - 65 )% 26) + 65 # Rotate letters according to shift amnt
                outFile.write(chr(B))
            # for lowercase characters
            elif(97 <= A <=122):
                B = (((A + shift) - 97) % 26) + 97 # rotate letters accordingto shift amnt
                outFile.write(chr(B))
            else:
                outFile.write(character)

# This decrypts a file according to a substitution cipher
def decrypt(inName, outName, shift):

    try:
        inFile = open(inName, "r")
        outFile = open(outName, "w")
    except FileNotFoundError as err:
        print(err)
        sys.exit(2)

    for line in inFile:
        for character in line:
            A = ord(character)
            # for uppercase characters
            if(65 <= A <= 90):
                B = (((A - shift) - 65 )% 26) + 65 # This is the cipher encoding
                outFile.write(chr(B))
            # for lowercase characters
            elif(97 <= A <=122):
                B = (((A - shift) - 97) % 26) + 97
                outFile.write(chr(B))
            else:
                outFile.write(character)


def main():
    # Grab command line arguments
    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argv, 'i:o:s:')
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)

    # assign these for scope of the following for loop
    inFileName = ''
    outFileName = ''
    shift = 0

    # parse arguments
    for o, a in opts:
        if o == "-i":
            inFileName = a
        elif o == "-o":
            outFileName = a
        elif o == "-s":
            shift = int(a)
        else:
            print('incorrect options')
            sys.exit(2)

    if(len(args) > 1):
        print("Usage casearCipher.py -i <inputFile> -o <outputFile> <encrypt/decrypt>")
        sys.exit(2)

    # Either encrypt or decrypt the file
    for a in args:
        if a == "encrypt":
            encrypt(inFileName, outFileName, shift)
        elif a == "decrypt":
            decrypt(inFileName, outFileName, shift)
        else:
            print("Usage casearCipher.py -i <inputFile> -o <outputFile> <encrypt/decrypt>")
            sys.exit(2)

if __name__ == '__main__':
    main()