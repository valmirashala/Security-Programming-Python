from elftools.elf.elffile import ELFFile

addr=input('Path of the elf file you want to parse:') #a.out ne rastin tone
with open(addr, 'rb') as f:
    
    elf_file = ELFFile(f)
    zgjedhja=input('Do you wanna explore header or sections?')
    zgjedhja.lower()

    def again():
        x=input('Do you wanna select another section?', )
        if x=='yes':
            seksionet()
        else:
            exit

    #iterimi i headerit
    def headeri():
        header = elf_file.header
        print(f'Header:')
        for part in header:
            print(f'{part}: {header[part]}')

    #iterimi i seksioneve
    def seksionet():
        for section in elf_file.iter_sections():
            print("Section name:", section.name)
        section=input("Which section you want to explore?", )
        text_section = elf_file.get_section_by_name(section)
        text_data = text_section.data()
        print(section,':',text_data)
        again()

    if zgjedhja=='header':
        headeri()
    elif zgjedhja=='sections':
        seksionet()
    else:
        print("Please choose header or sections")



 

    
    
 