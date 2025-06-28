import random as rd
pass_cheaker=[]
characters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')','-', '_', '=', '+', '[', ']', '{', '}', '|', '\\',':', ';', '"', "'", '<', '>', ',', '.', '?', '/','`', '~']


print("This Is A Full Customize Passoward Generator App")

length=int(input("Enter The Length of The Passoward (12-chaharacters/numbers/special character  RECOMMENDED)"))

NUM=int(input("How many numbers you want in your passoward"))
CHR=int(input("How many Alphabets you want in your passoward"))
SCHR=int(input("How many special characters you want in your passoward"))

x=NUM+CHR+SCHR


if(x==length):
    for i in range(0,NUM,1):
        f=rd.randint(1,10)
        pass_cheaker.append(f)
    for j in range(0,SCHR,1):
        f=rd.choice(special_chars)
        pass_cheaker.append(f)
    for k in range(0,CHR,1):
        f=rd.choice(characters)
        pass_cheaker.append(f)


    Final_Passoward=rd.sample(pass_cheaker,length)
    print("This is Your Fully Customizes Passoward :",*Final_Passoward)
elif(x!=length):
    print("SORRY!! Given uantities DONOT Match with the total no of passowars")