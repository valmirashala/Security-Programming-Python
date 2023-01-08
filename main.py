from pathlib import Path
from elftools.elf.elffile import ELFFile
import elf_functions
import magic
import binary_functions
import os

file=input('Path of the elf file you want to parse:') #a.out ne rastin tone
folder_name = "resources"
path = os.path.join(folder_name, file)
with open(path, 'rb') as f:
    magic_number = f.read(4)
# Check if the magic number matches the ELF magic number
    if magic_number == b'\x7fELF':
        print('The file is an ELF file.')
        elf_file = ELFFile(f)
        elf_functions.analyze_elf_file(elf_file)
    else:
        # The file is not an ELF file, check what file it is
        file_type = magic.from_file(path)
        print(f'The file is not an ELF file. Its type is: {file_type}')
        _, file_extension = os.path.splitext(path)
        if(file_extension)=='.db':
            binary_functions.read_dbfile(path)
        elif(file_extension)=='.bin':
            binary_functions.readBytes(path)
        elif(file_extension)=='.dat':
            binary_functions.read_datfiles(path)

    



 

    
    
 