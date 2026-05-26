file=r"C:\Python_scripting\log_scripts\read_Write.txt"

def read_write():
    try:
        with open(file, 'w') as f:
            f.write("Hi This Pyhton scripting\n")
            f.write("Learning for cyber security\n")
            f.write("Welcome")
        with open(file,'r') as f:
                    print(f.read().strip())
    except FileNotFoundError:
        print("File not found")
    finally:
        print("Execution completed")
if __name__=="__main__":
    read_write()
    
