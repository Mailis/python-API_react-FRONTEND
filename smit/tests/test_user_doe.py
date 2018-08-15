import os,sys
import unittest
import random

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.insert(0,parent_dir)

from models import user_doe
from auth import password_utils


class Test_User_Doe(unittest.TestCase):
    
    def test_select_user_by_id(self):
        try:
            user = user_doe.User()
            isSuccess, result = user.get_user_by_id(1)
            print(result)
            self.assertTrue(isSuccess) 
            self.assertTrue(len(result) >= 0) 
        except Exception as e:
            print(e)

    
    def test_delete_user_by_id(self):
        try:
            r = random.randint(6, 120)
            fullname = "test_full_name" + str(r)
            username = "test_user_name"
            phone = "56745678"

            user = user_doe.User()
            isSuccess, result= user.insert_user(fullname, username, phone)
            self.assertTrue(isSuccess) 

            #test insertion of same the user
            user = user_doe.User()
            isSuccess, result= user.insert_user(fullname, username, phone)
            self.assertFalse(isSuccess) 

            user = user_doe.User()
            isSuccess, result = user.get_user_by_fullname(fullname)
            self.assertTrue(isSuccess) 

            testUserID = result[0]
            test_fullname = result[1]
            test_username = result[2]
            test_phone = result[3]
            decoded_username = password_utils.check_if_username_is_safe(username, test_username)
            self.assertTrue(decoded_username)
            self.assertEqual(fullname, test_fullname)
            self.assertEqual(phone, test_phone)

            user = user_doe.User()
            isSuccess, result = user.delete_user_by_id(testUserID)
            print(result)
            self.assertTrue(isSuccess) 
        
        except Exception as e:
            print(e)


if __name__ == '__main__':
    unittest.main()