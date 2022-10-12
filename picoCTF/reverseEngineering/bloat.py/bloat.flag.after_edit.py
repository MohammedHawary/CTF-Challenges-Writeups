import sys
a = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ"+ \
            "[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~ "

def check_User_Input(get_User_Input):
  if get_User_Input == 'happychance':
    return True
  else:
    print('That password is incorrect')
    sys.exit(0)
    return False

def decode_Flag(flag_Var):
  return decrypt_Flag(flag_Var.decode(), 'rapscallion')

def get_User_Input():
  return input('Please enter correct password for flag: ')

def readFlag():
  return open('flag.txt.enc', 'rb').read()

def prepair_Flag():
  print('Welcome back... your flag, user:')

def decrypt_Flag(get_User_Input, Var_decode_Flag):
    key = Var_decode_Flag
    i = 0
    while len(key) < len(get_User_Input):
        key = key + Var_decode_Flag[i]
        i = (i + 1) % len(Var_decode_Flag)        
    return "".join([chr(ord(arg422) ^ ord(arg442)) for (arg422,arg442) in zip(get_User_Input,key)])

flag_Var = readFlag()
get_User_Input = get_User_Input()
check_User_Input(get_User_Input)
prepair_Flag()
Var_decode_Flag = decode_Flag(flag_Var)
print(Var_decode_Flag)
sys.exit(0)

