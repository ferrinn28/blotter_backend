import bcrypt
import logging
from src.repository import TUserRepo


class LoginService():
    def __init__(self, username:str, password:str):
        self.username= username
        self.password= password.encode("utf-8")
    
    def verify(self) -> tuple[int, str]:
        # Query User based on his/her username
        user_obj = TUserRepo().get_by_username(self.username)

        if user_obj:
            # Get Hash Password on DB
            stored_hash = user_obj.password.encode("utf-8")

            # Use checkpw() to compare the entered password to the stored hash
            # checkpw() automatically extracts the salt from the stored_hash and performs the comparison.
            if bcrypt.checkpw(self.password, stored_hash):
                logging.info(f"USER {self.username} SUCCESS LOGIN")
                return (200, "Login Success")
            else:
                logging.warning(f"USER {self.username} FAILED LOGIN")
                return (401, "Wrong username or password")

        else:
            logging.warning(f"USER {self.username} is NOT FOUND")
            return (401, "Wrong username or password")