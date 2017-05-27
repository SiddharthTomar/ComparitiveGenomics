with open(r'11.fa', 'r') as infile, open(r'11', 'w') as outfile:
    data = infile.read()
    data = data.replace("*", "")
    outfile.write(data)