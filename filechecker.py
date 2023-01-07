import magic

# Open the file
file='binary.bin'
with open(file, 'rb') as f:
    # Read the first 4 bytes of the file
    magic_number = f.read(4)

# Check if the magic number matches the ELF magic number
if magic_number == b'\x7fELF':
    print('The file is an ELF file.')
else:
    # The file is not an ELF file, check what file it is
    file_type = magic.from_file(file)
    print(f'The file is not an ELF file. Its type is: {file_type}')