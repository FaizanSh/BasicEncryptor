from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

with open("E:\\Assignment\\public_key.pem", "rb") as key_file_2:
    public_key = serialization.load_pem_public_key(
       key_file_2.read(),
       backend=default_backend()
    )


with open("E:\\Assignment\\Message.txt", "rb") as M:
    message = M.read()

print(message)

encrypted = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

with open('E:\\Assignment\\Message.encrypted', 'wb') as f:
    f.write(encrypted)
