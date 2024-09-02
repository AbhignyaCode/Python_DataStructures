def rem(str,a):
    string = ''
    for i in range(len(str)):
        if(str[i] != a):
            string = string + str[i]
    return string

string = str(input("enter your string : "))
a = str(input("which char do u want to remove : "))
print(rem(string,a))

