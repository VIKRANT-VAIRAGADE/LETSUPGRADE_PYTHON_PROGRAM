from cryptography.fernet import Fernet
key = Fernet.generate_key()
new_key =open('mykey.key','wb')
new_key.write(key)
new_key.close()
print(key)

msg = input("enter the msg : ")
msg = msg.encode()

f = Fernet(key)
cipher_text = f.encrypt(msg)
print(cipher_text)

my_pvt_key = open('mykey.key','rb')
f = Fernet(key)
plain_txt = f.decrypt(cipher_text)
plain_txt=plain_txt.decode()
my_pvt_key.close()
print(plain_txt)