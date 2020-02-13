# code for public key encryption
def xor(msg, key):
    encrypted_msg = int(msg,2) ^ int(key,2)
    output = '{0:0{1}b}'.format(encrypted_msg,len(msg))
    return output

def PRNG(seed):
    CONST_A = 533
    CONST_B = 227
    CONST_N = 64
    key_parts = [seed]
    temp = 0
    for i in range(4):
        temp  = (CONST_A*key_parts[i]+CONST_B)%CONST_N
        key_parts.append(temp)
    key_parts.remove(seed)
    key = ''
    for i in key_parts:
        key += '{0:0{1}b}'.format(i,6)
    return key

def PKE(private, CONST_N):
    other_usr_public_key = int(input('What is the public key of the other user?\n'))
    encryption_key = pow(other_usr_public_key, private, CONST_N)
    return encryption_key

def convert_letter_ascii(msg_to_encrypt):
    temp = 0
    msg_binary = ''
    for i in msg_to_encrypt:
        temp = '{0:0{1}b}'.format(ord(i),8)
        msg_binary += temp
    return msg_binary

def convert_binary_letter(msg):
    temp = ''
    output = ''
    for i in range(int(len(msg)/8)):
        temp = msg[i*8:(i+1)*8]
        output += chr(int(temp,2))
    return output
CONST_private_key = 11
CONST_C = 5
CONST_N = 19

print('Public Key is', pow(CONST_C, CONST_private_key, CONST_N))
msg_to_encrypt = input('Give me a message to encrypt:\n')
msg_binary = convert_letter_ascii(msg_to_encrypt)
seed = PKE(CONST_private_key, CONST_N)
binary_key = PRNG(seed)
print('Encrypted msg is\n'+ xor(msg_binary, binary_key))
msg_to_decrypt = input('Give me a message to decrypt:\n')
decrypt_binary = xor(msg_to_decrypt, binary_key)
decrypted_msg = convert_binary_letter(decrypt_binary)
print('The message is "'+ decrypted_msg + '"')
