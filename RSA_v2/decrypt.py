import rsa
import os
import fnmatch

def loadKeys():
    with open('keys/privateKey.pem', 'rb') as p:
        privateKey = rsa.PrivateKey.load_pkcs1(p.read())
    return privateKey

def decrypt(ciphertext, key):
    try:
        return rsa.decrypt(ciphertext, key).decode('ascii')
    except:
        return False

privateKey = loadKeys()
folder = r'./tmp/'

# iterate all files from a directory
for file_name in os.listdir(folder):
    if fnmatch.fnmatch(file_name, "*.bin"):
        # Construct old file name
        source = folder + file_name
        # leggo il file da decifrare
        f = open(source, "rb")
        message = f.read()

        text = decrypt(message, privateKey)
        print(f'Contenuto del file: {text}')
        if text:
            print(f'Message text: {text}')
        else:
            print(f'Unable to decrypt the message.')

        # New file name and extension
        file_name2 = file_name[:len(file_name) - 4]
        destination = folder + file_name2
        # scrivo il contenuto in chiaro in un nuovo file
        f = open(destination, "w")
        f.write(text)
        f.close()

        os.remove(source)

print('elenco dei file nella cartella:')
res = os.listdir(folder)
print(res)