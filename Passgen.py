import  string
import random
def passwd(length):
    characters=string.ascii_letters+string.digits+'@'+'#'+'$'+'&'
    return "".join(random.choice(characters) for i in range(length))
length=int(input("Enter the password length:"))
print("generated password is:",passwd(length))