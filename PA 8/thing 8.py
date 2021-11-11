file = open('zypa8.dat', 'r')
my_dict = {}
for line in file:
    x = line.split(" - ")
    name = x[0]
    y = x[1].split(" million units\n")
    copies = y[0]
    copies = round(float(copies))
    my_dict[name] = copies

file.close()
for key,val in my_dict.items():
    print('{0:<35}{1}'.format(key, (val // 5) * '*'))
    
print("Each asterisk represents approximately 5 million units sold.")
