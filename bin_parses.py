def readBytes(filename):
    bytes=''
    with open(filename,'rb') as file:
        while True:
            b=file.read(1)
            if not b:
                break
            bytes=bytes+str((int.from_bytes(b,byteorder='big')))
            print(bytes)






# def readBytes(filename):
#     bytes = ''
#     with open(filename,'rb') as file:
#     while True:
#     b = file.read(1)
# if not b:
# break
# bytes=bytes+str((int.from_bytes(b, byteorder='big')))
# print(bytes)

# readBytes('binary.bin')