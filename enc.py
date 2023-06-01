import base64

def encrpt_pass(password):
    encoded_bytes = base64.b64encode(password.encode())
    print(encoded_bytes)



def decrpt_pass(passwor):

    d = base64.b64decode(passwor)
    d_data = d.decode()
    print(f"decoded data {d_data}")



user_pass = input("password")
encrpt_pass(user_pass)

user_decode = input("enter hash")
decrpt_pass(user_decode)








