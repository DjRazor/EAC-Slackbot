import sys

def main(username, password, email):
    # Your badges script logic here
    print(f'Running badges script with {username}, {password}, {email}')

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
