def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")

if __name__ == '__main__':
    main()

###
#Exception has occurred: PermissionError
#[Errno 13] Permission denied: 'config.txt'
# File "C:\Users\LaunchX\Desktop\xc\Módulo10 Kata config.py", line 3, in main
#  configuration = open('config.txt')
#File "C:\Users\LaunchX\Desktop\xc\Módulo10 Kata config.py", line 9, in <module>
# main()
###
