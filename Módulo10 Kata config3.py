def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")

if __name__ == '__main__':
    main()

###
#Exception has occurred: PermissionError
#[Errno 13] Permission denied: 'config.txt'
#File "C:\Users\LaunchX\Desktop\xc\Módulo10 Kata config3.py", line 3, in main
#configuration = open('config.txt')
#File "C:\Users\LaunchX\Desktop\xc\Módulo10 Kata config3.py", line 10, in <module>
#main()
###