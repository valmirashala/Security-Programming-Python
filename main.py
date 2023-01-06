from elftools.elf.elffile import ELFFile
import binascii

with open('a.out', 'rb') as f:
    
    elf_file = ELFFile(f)

    #iterimi i headerit
    header = elf_file.header
    for part in header:
        print(f'Header:')
        print(f'{part}: {header[part]}')

    prog_head_table = elf_file.program_header_table                                      
    for prog_head in prog_head_table:
        print(f'Program Header:')
        print(f'{prog_head}: {prog_head["p_{prog_head}"]}')

    #iterimi i seksioneve
    for section in elf_file.iter_sections():
        print("Section name:", section.name)

    section=input("Which section you want to explore?", )
    text_section = elf_file.get_section_by_name(section)
    text_data = text_section.data()
    print(section,text_data)

 

    
    
 