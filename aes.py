from Crypto.Cipher import AES
import binascii, os

# função para criptografar mensagem
def encrypt_AES_GCM(msg, chaveSecreta):
    aesCipher = AES.new(chaveSecreta, AES.MODE_GCM)
    ciphertext, authTag = aesCipher.encrypt_and_digest(msg)
    return (ciphertext, aesCipher.nonce, authTag)

#função para descriptografar mensagem
def decrypt_AES_GCM(criptoMsg, chaveSecreta):
    (ciphertext, nonce, authTag) = criptoMsg
    aesCipher = AES.new(chaveSecreta, AES.MODE_GCM, nonce)
    plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag)
    return plaintext

chaveSecreta = os.urandom(32)  # chave aleatória de criptografia (256-bits)
print("Chave de criptografia:", binascii.hexlify(chaveSecreta))

# uso da chave para criptografar uma mensagem de texto
msg = b'Criptografa-me'
criptoMsg = encrypt_AES_GCM(msg, chaveSecreta)
print("criptoMsg", {
    'ciphertext': binascii.hexlify(criptoMsg[0]),
    'aesIV': binascii.hexlify(criptoMsg[1]),
    'authTag': binascii.hexlify(criptoMsg[2])
})

# em seguida, descriptografa-a de volta à mensagem original
descriptoMsg = decrypt_AES_GCM(criptoMsg, chaveSecreta)
print("descriptoMsg", descriptoMsg)