import os,sys
import unittest

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.insert(0,parent_dir)

from auth import token_generator


class Test_Auth_Token(unittest.TestCase):

    def test_auth_token(self):
        fullname = "f"
        payload = token_generator.getPayLoad(fullname, 0, 60*60)
        encoded = token_generator.encode_auth_token_HS256(payload)
        isSucc, decoded = token_generator.decode_auth_token_HS256(encoded, fullname)
        isValid = decoded.items() == payload.items()
        self.assertTrue(isSucc)
        self.assertTrue(isValid)
        
    def test_get_auth_token(self):
        fullname = "f"
        isSucc, auth_token_encoded = token_generator.get_auth_token(fullname, 10, 60*60)
        #print(auth_token_encoded)
        isSucc, decoded = token_generator.decode_auth_token_HS256(auth_token_encoded, fullname)
        self.assertTrue(len(decoded.items()) > 0)
        self.assertTrue(isSucc)




if __name__ == '__main__':
    unittest.main()