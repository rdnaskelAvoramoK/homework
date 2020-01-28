import hashlib, binascii, os

class User:
    def __init__(self, firstname, lastname, password, *args, **kwargs):
        self.firstname = firstname
        self.lastname = lastname
        password = self.hash_password(password)
        #self.password = password
        #__H_password = self.hash_password(self.password)
        #lastname = None
        #adresses = [dict city, country,bibilding_addresses, index]
        #phones = [*args] <= 15 max 3
        print(password)
    def get_fullname(self):
        return f"{self.firstname} {self.lastname}"

    def hash_password(self, password):
        """Hash a password for storing."""
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
        pwdhash = binascii.hexlify(pwdhash)
        return (salt + pwdhash).decode('ascii')

    def verify_password(stored_password, provided_password):
        """Verify a stored password against one provided by user"""
        salt = stored_password[:64]
        stored_password = stored_password[64:]
        pwdhash = hashlib.pbkdf2_hmac('sha512',
                                      provided_password.encode('utf-8'),
                                      salt.encode('ascii'),
                                      100000)
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        return pwdhash == stored_password



User1 = User("dmbclnd", "CSNDJK", "LNDC")
print(User1.get_fullname())
print(User1.password)
User2 = User("Tom", "Soyer", "12qT")
print(User2.get_fullname())