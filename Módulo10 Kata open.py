def main():
    open("/path/to/mars.jpg")
main() #Faltaba main()
if __name__ == '__main__':
    main()

###
#Exception has occurred: FileNotFoundError
#[Errno 2] No such file or directory: '/path/to/mars.jpg'
#File "C:\Users\LaunchX\Desktop\xc\Módulo10 Kata open.py", line 2, in main
# open("/path/to/mars.jpg")
# File "C:\Users\LaunchX\Desktop\xc\Módulo10 Kata open.py", line 3, in <module>
#main()
###