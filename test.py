from elftools.elf.elffile import ELFFile

# Open the ELF file
with open('a.out', 'rb') as f:
    # Create an ELFFile object from the file
    elffile = ELFFile(f)
    
    # Print the ELF header
    print('ELF Header:')
    print('-' * 30)
    print(elffile.header)
    print()
    
    # Print the program header table
    print('Program Header Table:')
    print('-' * 30)
    for segment in elffile.iter_segments():
        print(segment)
    print()
        
        # Print the section header table
    print('Section Header Table:')
    print('-' * 30)
    for section in elffile.iter_sections():
            print(section)
    print()
        
        # Print the symbol tables
    print('Symbol Tables:')
    print('-' * 30)
    symbol_table = elffile.get_section_by_name('.symtab')
    if symbol_table is not None:
        for symbol in symbol_table.iter_symbols():
            print(symbol)
    else:
        print("Couln't find a symbol table")
    print()
        
        # Print the note tables
    print('Note Tables:')
    print('-' * 30)
    note_table = elffile.get_section_by_name('.note')
    if note_table is not None:
        for note in note_table.iter_notes():
            print(note)
    else:
        print("Couldnt find a note table")
    print()