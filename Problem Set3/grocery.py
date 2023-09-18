from collections import Counter
def main():
    grocery_list = []
    sort_list(get_input(grocery_list))

def get_input(l):
    while True:
        try:
            item = input("").casefold()
            l.append(item)
        except EOFError:
            break
    return l

def sort_list(l1):
    counts = Counter(l1)
    sorted_counts = sorted(counts.items(), key=lambda x: x[0])  # Sort by item's name
    for item, count in sorted_counts:
        print(f"{count} {item.title().upper()}")

main()
