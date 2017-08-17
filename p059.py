def read_cipher():
    file = open("p059_cipher.txt", 'r')
    cipher = file.readline().replace('\n', '')
    codes = cipher.split(',')
    return map(lambda x: int(x), codes)

def asciiToChar(codes):
    return "".join(map(lambda x: chr(x), (codes)))

def expand(message_length, key):
    expanded_key = ""
    for i in range(0,message_length):
        expanded_key += key[i%len(key)]
    return expanded_key

def decode(message, key):
    decoded = ""
    for i in range(0,len(message)):
        value = ord(message[i])^ord(key[i])
        decoded += chr(value)
    return decoded

def main():
    cipher = asciiToChar(read_cipher())
    for a in range(97, 123):
        for b in range(97, 123):
            for c in range(97, 123):
                key = expand(len(cipher), chr(a)+chr(b)+chr(c))
                decoded = decode(cipher,key)
                if isValid(decoded):
                    print("KEY: " + key)
                    print("MESSAGE: " + decoded)
                    print("ASCII SUM: " + str(asciiSum(decoded)))
                    print("________________________________")

def asciiSum(message):
    return sum(map(lambda x: ord(x), message))

def isValid(decoded_message):
    return all(isEnglish(c) for c in decoded_message)

def isEnglish(char):
    ascii = ord(char)
    return (ascii >= 32 and ascii <= 122)

if __name__ == '__main__':
    main()

