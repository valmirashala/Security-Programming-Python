from elftools.elf.elffile import ELFFile

with open('a.out', 'rb') as f:
    elf = ELFFile(f)
    for section in elf.iter_sections():
        print("Section name:", section.name)
    section = elf.get_section_by_name('.text')
    print(section.data())