from Logo import logo
print (logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','^','&','*','(',')','-','+','_','=','{','}','[',']','"\"','|',';','"',"'","<",">",",",".","/","?"]

should_end = True
while should_end:
    direction = input("Type 'encrypt' for encode and 'decrypt' for decode \n").lower()
    text=input("Type the word  : ")
    shift=int(input("Type the shift key : "))
    
    def ceasar(text,shift,direction):
        if direction=="encrypt":
            cipher_text=""
            for char in text:
                position = alphabet.index(char)
                new_position = position + shift
                cipher_text  = cipher_text + alphabet[new_position]
            print(f"The Encrypted word is {cipher_text}")
        elif direction=="decrypt":
            cipher_text=""
            for char in text:
                position=alphabet.index(char)
                new_position=position-shift
                cipher_text = cipher_text + alphabet[new_position]
            print(f"The Decrypted word is {cipher_text}")
        else:
            print("Invalid input")

    ceasar(text,shift,direction)

    result = input("Type 'yes' for again and 'no' for Exit\n").lower()
    if result=="yes":
        should_end=True
    else:
        should_end=False
        print("Thank you! Good bye!")








        
        
