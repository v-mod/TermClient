import getpass
CUname='vivaan'
CPwd='vivaan123'
def login():
    print('In order to continue you must verify your identity. Please login below:')
    uname=input('UserId: ')
    pwd=getpass.getpass('Pwd: ')
    if uname == CUname and pwd == CPwd:
        print('Access Granted. ')
        return True
    else:
        return False