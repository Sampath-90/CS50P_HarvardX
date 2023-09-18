def main():
    name = input("camelCase: ").strip()
    print(snake_name(name))


def snake_name(n):
    name_list = list(n)
    for i in range(len(name_list)):
        if name_list[i].isupper():
            name_list[i] = name_list[i].replace(name_list[i],"_"+name_list[i].lower())

    updated_name = ''.join(name_list)
    return updated_name

main()
