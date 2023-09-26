from emoji import emojize

def convert_to_emoji(text):
    return emojize(text,language='alias')

if __name__ == '__main__':
    input_text = str(input("Input: ").strip())
    output_text = convert_to_emoji(input_text)
    print(f"Output: {output_text}")
