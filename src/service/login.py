import bcrypt


class Login():
    def __init__(self, username:str, password:str):
        self.username= username
        self.password= password.encode("utf-8")
    
    def verify(self):
        # Assume this is the hash retrieved from your database
        stored_hash = b'$2y$10$D4zscsSBkSx1xk12qxx.I.fAaEBJSvkLqiejXMI8Fs3vaUGoZD5x.'

        # 2. Use checkpw() to compare the entered password to the stored hash
        # checkpw() automatically extracts the salt from the stored_hash and performs the comparison.
        if bcrypt.checkpw(self.password, stored_hash):
            print("Password matches! User is authenticated.")
        else:
            print("Password does not match. Authentication failed.")