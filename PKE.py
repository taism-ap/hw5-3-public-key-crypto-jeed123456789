#Runs XOR function on a pair of binary intergers!
def xor(msg, key):
    encrypted_msg = int(msg,2) ^ int(key,2)
    output = '{0:0{1}b}'.format(encrypted_msg,len(msg))
    return output

#runs a psudo randon number generator to output a key from the seed (as made using
#the XOR function above) and the message in binary (in order to find the key length
def PRNG(seed, msg_binary):
    CONST_A = 533
    CONST_B = 227
    CONST_N = 64
    key_parts = [seed]
    temp = 0
    for i in range(int(len(msg_binary)/8 + 1)):
        temp  = (CONST_A*key_parts[i]+CONST_B)%CONST_N
        key_parts.append(temp)
    key_parts.remove(seed)
    key = ''
    for i in key_parts:
        key += '{0:0{1}b}'.format(i,6)
    return key

#Uses private key and N constant, and the other users public key to create the key to use
#in encryption, result is used C in PRNG() 
def PKE(private, CONST_N):
    other_usr_public_key = int(input('What is the public key of the other user?\n'))
    encryption_key = pow(other_usr_public_key, private, CONST_N)
    return encryption_key

#converts ascii messsage to binary!
def convert_letter_ascii(msg_to_encrypt):
    temp = 0
    msg_binary = ''
    for i in msg_to_encrypt:
        temp = '{0:0{1}b}'.format(ord(i),8)
        msg_binary += temp
    return msg_binary

#converts binary to ascii 
def convert_binary_letter(msg):
    temp = ''
    output = ''
    for i in range(int(len(msg)/8)):
        temp = msg[i*8:(i+1)*8]
        output += chr(int(temp,2))
    return output

#Input private key
CONST_private_key = int(input("Enter your private key!\n"))

#Set constants
CONST_C = 5
CONST_N = 19

#Performs math to find user public key
print('Public Key is', pow(CONST_C, CONST_private_key, CONST_N))
msg_to_encrypt = input('Give me a message to encrypt:\n') #input message
msg_binary = convert_letter_ascii(msg_to_encrypt) #runs all the functions!
seed = PKE(CONST_private_key, CONST_N)
binary_key = PRNG(seed, msg_binary)

#prints final encrypted message in binary
encrypted_msg_binary = xor(msg_binary,binary_key)
encrypted_msg_ascii = convert_binary_letter(encrypted_msg_binary)
print('Encrypted msg is\n'+ '"' +encrypted_msg_ascii+'"')
msg_to_decrypt_initial = input('Give me a message to decrypt:\n') #input a message to decrypt
msg_to_decrypt = convert_letter_ascii(msg_to_decrypt_initial) # converts encrypted message to binary
decrypt_binary = xor(msg_to_decrypt, binary_key) #Perform XOR on message (encrypt message)
decrypted_msg = convert_binary_letter(decrypt_binary) #Perfoms convert_binary_letter()
print('The message is\n'+ decrypted_msg)#prints final decrypted message
