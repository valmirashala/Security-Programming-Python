import pyelftools

# Open the COFF file in binary mode
with open('', 'rb') as f:
    # Create an ELF object from the file
    elffile = pyelftools.elffile.ELFFile(f)
    
    # Print the file header information
    print("File header:")
    print(elffile.header)
    
    # Print the program header information
    print("\nProgram headers:")
    for segment in elffile.iter_segments():
        print(segment.header)
    
    # Print the section header information
    print("\nSection headers:")
    for section in elffile.iter_sections():
        print(section.header)
    
    # Print the symbol table information
    print("\nSymbol table:")
    if elffile.has_symbols():
        for symbol in elffile.iter_symbols():
            print(symbol.name)