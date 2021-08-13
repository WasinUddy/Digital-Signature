def CreateMessage(FilePath):
    import hashlib

    file = FilePath
    BLOCK_SIZE = 65536
    file_hash = hashlib.sha512()
    with open(file, 'rb') as f:
        fb = f.read(BLOCK_SIZE)
        while len(fb) > 0:
            file_hash.update(fb)
            fb = f.read(BLOCK_SIZE)

    return int.from_bytes(file_hash.digest(), byteorder='big')

def Sign(message, PrivateKey):
    return pow(message, int(PrivateKey['d']), int(PrivateKey['n']))

def Verify(message, signature, PublicKey):
    return message == pow(signature, int(PublicKey['e']), int(PublicKey['n']))