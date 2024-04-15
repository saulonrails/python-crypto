from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

# geração de chaves de 3072 bits
parChaves = RSA.generate(3072)

# chaves pública e privada
pubChave = parChaves.publickey()
print(f"Chave pública: (n={hex(pubChave.n)}, e={hex(pubChave.e)})")

pubKeyPEM = pubChave.exportKey()
print(pubKeyPEM.decode('ascii'))

print(f"Chave privada: (n={hex(pubChave.n)}, d={hex(parChaves.d)})")
privKeyPEM = parChaves.exportKey()
print(privKeyPEM.decode('ascii'))

# codificação da mensagem usando o esquema de criptografia RSA-OAEP
msg = b'Criptografa-me'
encryptor = PKCS1_OAEP.new(pubChave)
encrypted = encryptor.encrypt(msg)
print("Criptografada:", binascii.hexlify(encrypted))

# decodificação da mensagem com a chave privada RSA:
decryptor = PKCS1_OAEP.new(parChaves)
decrypted = decryptor.decrypt(encrypted)
print('Descriptografada:', decrypted)