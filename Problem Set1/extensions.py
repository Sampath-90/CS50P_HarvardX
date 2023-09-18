def main():
    string = input("File name: ").strip().lower().split(".")
    print(extension(string[-1]))

def extension(s):
    match s:
        case "gif"|"jpg"|"jpeg"|"png":
            if s == "jpg":
                return ("image/"+"jpeg")
            else:
                return ("image/"+s)
        case "pdf"|"zip":
            return ("application/"+s)
        case "txt":
            return ("text/plain")
        case _:
            return ("application/octet-stream")

main()
