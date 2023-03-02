import rsa
def generateKeys():
    (publicKey, privateKey) = rsa.newkeys(1024)
    with open('keys/publcKey.pem', 'wb') as p:
        p.write(publicKey.save_pkcs1('PEM'))
    with open('keys/privateKey.pem', 'wb') as p:
        p.write(privateKey.save_pkcs1('PEM'))

def loadKeys():
    with open('keys/publcKey.pem', 'rb') as p:
        publicKey = rsa.PublicKey.load_pkcs1(p.read())
    with open('keys/privateKey.pem', 'rb') as p:
        privateKey = rsa.PrivateKey.load_pkcs1(p.read())
    return privateKey, publicKey


def encrypt(message, key):
    return rsa.encrypt(message.encode('ascii'), key)


def decrypt(ciphertext, key):
    try:
        return rsa.decrypt(ciphertext, key).decode('ascii')
    except:
        return False

def sign(message, key):
    return rsa.sign(message.encode('ascii'), key, 'SHA-1')

def verify(message, signature, key):
    try:
        return rsa.verify(message.encode('ascii'), signature, key,) == 'SHA-1'
    except:
        return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    privateKey, publicKey = loadKeys()

    #leggo il file da cifrare e lo cifro
    f = open("dati.txt", "r")
    message = f.read()
    ciphertext = encrypt(message, publicKey)

    #scrivo il contenuto cifrato in un nuovo file binario
    f = open("testoCifrato.bin", "wb")
    f.write(ciphertext)
    f.close()

    #firmo il contenuto del file con la chiave privata
    signature = sign(message, privateKey)

    #decifro il file binario
    f = open("testoCifrato.bin", "rb")
    message = f.read()
    text = decrypt(message, privateKey)

    print(f'Cipher text: {ciphertext}')
    print(f'Signature: {signature}')

    if text:
        print(f'Message text: {text}')
    else:
        print(f'Unable to decrypt the message.')

    #verifico la validità della firma
    if verify(text, signature, publicKey):
        print('Successfully verified signature')
    else:
        print('The message signature could not be verified')
