#Build a log parser that reads a file and counts failed login attempts.

file_path=r"C:\Python_scripting\log_scripts\logs.txt"

def error_logs():
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            count = 0
            for line in f:
                
                if "login failed" in line:
                    count+=1
                    print("Login Failed Attempt: " + line.strip())
            print(f"Total {count} failed" )
    except FileNotFoundError:
        print("File Not Found")
    finally:
        print("log parser completed")
    
if __name__=="__main__":
    error_logs()


