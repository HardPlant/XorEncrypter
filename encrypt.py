def get_byte(filename, chunksize = 8192):
    with open(filename, "rb") as f:
        while True:
            word = bytearray(f.read(chunksize))
            enc_word = []
            if word:
                yield word
            else:
                break


def write_byte(filename, byte):
    with open(filename, "wb") as result:
            result.write(byte)

def read_file(filename):
    with open(filename) as f:
        print(bytes(f.read(), 'UTF-8'))

def read_file_xor(filename, key=0x12):
    with open(filename) as f:
        content = bytearray(f.read(), 'UTF-8')
        for i in range(len(content)):
            content[i] ^= key
        print(content)
        print(content.decode('UTF-8'))

def xor_file(destFile, srcFile, key=0x41):
    enc_byte = []
    for byte in get_byte(destFile):
        for i in range(len(byte)):
            byte[i] ^= key
        enc_byte += byte
    enc_byte = bytes(enc_byte)
    write_byte(srcFile, enc_byte)

if __name__ == '__main__':
    xor_file("text.txt", "result.txt", 0x41)
    xor_file("result.txt", "result2.txt", 0x73)
    read_file_xor("result2.txt", 0x12)
    xor_file("result2.txt", "result.txt", 0x73)
    xor_file("result.txt", "result.txt", 0x41)


