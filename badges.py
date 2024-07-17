import sys
import os

def main(username, password, email):
    print(f'Running badges script with {username}, {password}, {email}')
    print(os.getcwd())

if __name__ == '__main__':
    print("reached here in badges!")
    main(sys.argv[1], sys.argv[2], sys.argv[3])