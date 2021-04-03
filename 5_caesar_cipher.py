from art_cipher import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def shiftText(txt,shift_num):
    splitted = list(txt)
    arr = map(lambda x: alphabet[(alphabet.index(x)+ shift_num) % len(alphabet)],splitted)
    return "".join(list(arr))

def encode(txt,shift_num):
    return shiftText(txt,shift_num)

def decode(txt,shift_num):
    return shiftText(txt,-shift_num)

def test():
    print(encode("selman",1))
    print(decode("tfmnbo",1))
    print(f"""The encoded text is {encode("hello",5)}""")
    print(encode("civilization",1))

def main():
    print(logo())
    again = True
    while again:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        if(direction == "encode"):
            print(f"""The encoded text is {encode(text,shift)}""")
        else:
            print(f"""The decoded text is {decode(text,shift)}""")
        restart = input("Type 'yes' if you want to go again. Otherwise type 'no' \n").lower()
        if restart == "no":
            again = False
            print("Goodbye!")
main()