file=r"C:\Python_scripting\log_scripts\ips.txt"

def duplicate():
    try:
        with open(file, 'r') as f:
            ips=f.readlines()  #stroe out put in list format

            for ip in set(ips):
                if ips.count(ip)>1:
                    print(ip.strip())
    except FileNotFoundError:
        print("error")
    finally:
        print("execution completed")
if __name__=="__main__":
    duplicate()