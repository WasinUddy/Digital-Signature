import json

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from Crypto.PublicKey import RSA

class User:

    def __init__(self):
        self.db = self.__ConnectDatabase()

    def CreateNewUser(self, Username, PrivateKeySavedLocation):
        GeneratedKey = RSA.generate(bits=1024)

        # Generated Private Key
        PrivateKey = {
            'n' : str(GeneratedKey.n),
            'd' : str(GeneratedKey.d)
        }
        with open(PrivateKeySavedLocation, 'w') as fp:
            json.dump(PrivateKey, fp)
        
        PublicKey = {
            'n' : str(GeneratedKey.n),
            'e' : str(GeneratedKey.e)
        }
        
        doc_ref = self.db.collection(Username).document('PublicKey')
        doc_ref.set(PublicKey)


    def AccountExisted(self, Username):
        ref = self.db.collection(Username).document('PublicKey')
        if ref.get().exists:
            return True
        else:
            return False

    def GetPublicKey(self, Username):
        if self.AccountExisted(Username):
            return self.db.collection(Username).document('PublicKey').get().to_dict()
        else:
            return None
    

    def __ConnectDatabase(self):
        cred = credentials.Certificate('classes/server.json')
        firebase_admin.initialize_app(cred, {'projectId' : 'digital-signature-8f6e3'})
        return firestore.client()

    
