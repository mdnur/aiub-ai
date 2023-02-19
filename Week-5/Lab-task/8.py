"""Take a character as input and determine whether it is a vowel or not. Therefore, print an appropriate message (vowel/not vowel)."""


print()

x = input("Enter a character: ")

vowels =['a','e','i','o','u']

match x:
    case 'a':
        print(x+" is vowel")
    case'e':
        print(x + " is vowel")
    case 'i':
        print(x + " is vowel")
    case 'o':
        print(x + " is vowel")
    case 'u':
        print(x + " is vowel")
    case __:
        print(x + " is not vowel")


for i in vowels:
    if (i ==x):
        print("Vowels")
        break;
    else:
        print("not vowels")

        
        
        
