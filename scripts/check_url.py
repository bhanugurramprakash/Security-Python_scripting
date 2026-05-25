urls=[
    "https://enhancv.com/resources/resume-checker/",
    "http://enhancv.com/resources/resume-checker/",
    "http:/enhancv.com/resources/resume-checker/"
    ]


def urlcheck():
    try:
        for url in urls:
            if url.startswith("https://"):
                print(f"This {url} is secure")
            else:
                print(f"This {url} is not secure")
    except:
        print("No URL Found")
if __name__=="__main__":
    urlcheck()
