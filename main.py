from elftools.elf.elffile import ELFFile
import elf_functions

addr=input('Path of the elf file you want to parse:') #a.out ne rastin tone
with open(addr, 'rb') as f:
    elf_file = ELFFile(f)
    choice=input('Press 1 to explore header, press 2 to explore sections, press 3 to explore symbols, press 4 to explore notes!')
    choice.lower()


    def switchChoice(choice):
        if choice=='1':
            elf_functions.printHeader(elf_file)
        elif choice=='2':
            elf_functions.printSections(elf_file)
        elif choice=='3':
            elf_functions.printSymbolTable(elf_file)
        elif choice=='4':
            elf_functions.printNotesTable(elf_file)
        else:
            print(choice)
            print("We don't provide what you are searching for")

   
switchChoice(choice)



 

    
    
 