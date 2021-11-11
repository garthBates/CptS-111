def cipher_chr(text, offset):
    x = ord(text) - 32
    x += offset
    x = x % 95
    x += 32
    x = chr(x)
    return x

def decipher_chr(text, offset):
    x = ord(text) - 32
    x -= offset
    x = x % 95
    x += 32
    x = chr(x)
    return x


def clear2cipher(text, offset):
    accum = ""
    for i in range(len(text)):
        x = text[i]
        x = cipher_chr(x, offset)
        accum = accum + x
    return accum


def cipher2clear(text, offset):
    accum = ""
    for i in range(len(text)):
        x = text[i]
        x = decipher_chr(x, offset)
        accum = accum + x
    return accum


def log_map(amp, cur_gen):
    return (amp * cur_gen * (1 - cur_gen))


def compare(amp, num_gen, xa, xb):
    print("Gen #", "\t\txa", "\t\t\txb", "\t\t\txa - xb")
    #xa = int(xa * 96)
    print(xa * 96)
    #xb = int(xb * 96)
    print(xb * 96)
    for i in range(num_gen + 1):
        xa = log_map(amp, xa)
        xb = log_map(amp, xb)
        c = xa - xb
        print(i, "\t", (xa * 1), "\t", int(xb * 96), "\t", c)
    
def main():
    amp =  float(input("Enter the amplitude a: "))
    gens = int(input("Enter the numbre of generations n: "))
    pops = input("Enter the two initiaal populations: ")
    xa, xb = pops.split(",")
    xa = float(xa)
    xb = float(xb)

    compare(amp, gens, xa, xb)

main()

    
    
