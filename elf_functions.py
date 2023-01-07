from elftools.elf.elffile import ELFFile

def switchChoice(choice,elf_file):
        if choice=='1':
            printHeader(elf_file)
        elif choice=='2':
            printSections(elf_file)
        elif choice=='3':
           printSymbolTable(elf_file)
        elif choice=='4':
            printNotesTable(elf_file)
        else:
            print(choice)
            print("We don't provide what you are searching for")
def analyze_elf_file(f):
    choice=input('Press 1 to explore header, press 2 to explore sections, press 3 to explore symbols, press 4 to explore notes!')
    choice.lower()
    switchChoice(choice,f)

#iterimi i headerit
def printHeader(elf_file):
        header = elf_file.header
        print(f'Header:')
        for part in header:
            print(f'{part}: {header[part]}')

    #iterimi i seksioneve
def chooseSectionAgain(elf_file):
        x=input('Do you wanna select another section?', )
        x.lower()
        if x=='yes':
            printSections(elf_file)
        else:
            exit

def printSections(elf_file):
        for section in elf_file.iter_sections():
            print("Section name:", section.name)
        section=input("Which section you want to explore?", )
        text_section = elf_file.get_section_by_name(section)
        text_data = text_section.data()
        print(section,':',text_data)
        chooseSectionAgain(elf_file)
    
def printSymbolTable(elf_file):
        print('Symbol Tables:')
        print('-' * 30)
        symbol_table = elf_file.get_section_by_name('.symtab')
        if symbol_table is not None:
            for symbol in symbol_table.iter_symbols():
                print(symbol)
        else:
            print("Couln't find a symbol table")
        print()

def printNotesTable(elf_file):
        print('Note Tables:')
        print('-' * 30)
        note_table = elf_file.get_section_by_name('.note')
        if note_table is not None:
            for note in note_table.iter_notes():
                print(note)
        else:
            print("Couldnt find a note table")
        print()