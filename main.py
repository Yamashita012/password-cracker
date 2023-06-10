import hashlib
import pyfiglet
from termcolor import colored


#CREATING A BANNER
def create_stylish_banner(text):
    banner = pyfiglet.figlet_format(text)
    return banner

# Example usage:
banner_text = "     Pass -- CRACKER! \n"
banner = create_stylish_banner(banner_text)
print(colored(text=banner, color='green', attrs=['bold']))




def hashCracker(hash_pass):
    print('\n\n')
    try:
        password_list = open(pass_file, 'r')
    
    except:
        print('File Not Found.')

    for password in password_list:
        encrypt_pass = password.encode('utf-8')
        processed = hashlib.md5(encrypt_pass.strip()).hexdigest()

        if processed == hash_pass:
            print(f'[+] Password Found:     [{password}]')
        
        else:
            print(f'[-] {password}')


if __name__ == '__main__':
    pass_file = str(input('[<>] Enter Password List File(with-extension): '))
    the_hash = str(input('[<>]  Paste Hash Here: '))
    hashCracker(the_hash)