import bcrypt
import logging
import os
import jwt

from datetime import datetime, timedelta

from src.repository import TUserRepo


class LoginService():
    def __init__(self, username:str, password:str):
        self.log = logging.getLogger(self.__class__.__name__)

        self.username= username
        self.password= password.encode("utf-8")
    
    def verify(self) -> tuple[int, str]:
        # Query User based on his/her username
        user_obj = TUserRepo().get_by_username(self.username)

        if user_obj:
            # Construct JWT Payload
            DURATION_TOKEN = int(os.getenv("DURATION_TOKEN"))
            DURATION_TOKEN_TYPE = os.getenv("DURATION_TOKEN_TYPE")

            # Check type duration token type (Is it HOURS, MINUTES, SECODNS)
            if DURATION_TOKEN_TYPE.lower() == "hours":
                duration_token = DURATION_TOKEN * 3600
            elif DURATION_TOKEN_TYPE.lower() == "minutes":
                duration_token = DURATION_TOKEN * 60
            else:
                duration_token = DURATION_TOKEN

            dt_now = datetime.now()
            dt_duration = timedelta(seconds=duration_token)
            dt_total = dt_now + dt_duration

            payload = {
                "sub": user_obj.username,
                "name": user_obj.name,
                "nbf": int(dt_now.timestamp()),
                "iat": int(dt_now.timestamp()),
                "exp": int(dt_total.timestamp())
            }

            # Get Hash Password on DB
            stored_hash = user_obj.password.encode("utf-8")

            # Use checkpw() to compare the entered password to the stored hash
            # checkpw() automatically extracts the salt from the stored_hash and performs the comparison.
            if bcrypt.checkpw(self.password, stored_hash):
                self.log.info(f"USER {self.username} SUCCESS LOGIN")
                jwt_token = jwt.encode(payload, os.getenv("SECRET"))
                return (200, "Login Success", jwt_token)
            else:
                self.log.warning(f"USER {self.username} FAILED LOGIN")
                return (401, "Wrong username or password", None)

        else:
            self.log.warning(f"USER {self.username} is NOT FOUND")
            return (401, "Wrong username or password", None)