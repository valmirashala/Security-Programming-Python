from elftools.elf.elffile import ELFFile
import elf_functions
import magic
import chardet
import bin_parses
import binary_functions
import os
file=input('Path of the elf file you want to parse:') #a.out ne rastin tone
with open(file, 'rb') as f:
    magic_number = f.read(4)
    data = f.read()
    result = chardet.detect(data)

# Check if the magic number matches the ELF magic number
    if magic_number == b'\x7fELF':
        print('The file is an ELF file.')
        elf_file = ELFFile(f)
        elf_functions.analyze_elf_file(elf_file)
# Check if the file is a binary string
    elif result['encoding'] == None:
        print('The file is an .bin file.')
        bin_parses.readBytes(file)
    else:
        # The file is not an ELF or .bin file, check what file it is
        file_type = magic.from_file(file)
        print(f'The file is not an ELF file. Its type is: {file_type}')
        _, file_extension = os.path.splittext(file)
        if(file_extension)=='.db':
            binary_functions.read_dbfile(file)

    



 

    
    
 