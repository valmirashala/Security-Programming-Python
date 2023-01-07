import chardet
import codecs

# Open the binary file in read-only mode
with open('a.out', 'rb') as file:
  # Read the contents of the file into a bytes object
  file_contents = file.read()

# Use the chardet library to detect the encoding of the file
detection = chardet.detect(file_contents)

# Get the encoding and confidence of the detection
encoding = detection['encoding']
confidence = detection['confidence']

# If the encoding was detected with high confidence, decode the file and print its contents
if confidence >= 0.8:
  text = file_contents.decode(encoding)
  print(text)
else:
  # If the encoding could not be detected, try to parse the file using other approaches
  
  # Try to parse the file as a CSV file
  try:
    import csv
    reader = csv.reader(file_contents.decode('utf-8').splitlines())
    for row in reader:
      print(row)
  except Exception:
    pass
    
  # Try to parse the file as a JSON file
  try:
    import json
    data = json.loads(file_contents)
    print(data)
  except Exception:
    pass
    
  # If none of the above approaches work, print an error message
  print('Unable to parse file')
# import magic

# # Open the binary file in read-only mode
# with open('binary.bin', 'rb') as file:
#   # Read the first 4 bytes of the file
#   file_header = file.read(4)

# # Use the magic library to identify the file type based on the file header
# file_type = magic.from_buffer(file_header)

# print(f'The file is a {file_type}')
