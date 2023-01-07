from elftools.elf.elffile import ELFFile
import elf_functions
import magic

file=input('Path of the elf file you want to parse:') #a.out ne rastin tone
with open(file, 'rb') as f:
    magic_number = f.read(4)

# Check if the magic number matches the ELF magic number
    if magic_number == b'\x7fELF':
        print('The file is an ELF file.')
        elf_file = ELFFile(f)
        elf_functions.analyze_elf_file(elf_file)
        
        
    else:
        # The file is not an ELF file, check what file it is
        file_type = magic.from_file(file)
        print(f'The file is not an ELF file. Its type is: {file_type}')
        #TODO: create methods thar parse other binary files

    



 

    
    
 