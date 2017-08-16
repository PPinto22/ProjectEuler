def read_cipher():
    file = open("p059_cipher.txt", 'r')
    cipher = file.readline().replace('\n','')
    return cipher.split(',')

if __name__ == '__main__':
    enc_codes = read_cipher()

