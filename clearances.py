import sys

def main(username, password, netid_list):
    # Your billing script logic here
    print(f'Running clearances script with {username}, {password}, {netid_list}')

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
