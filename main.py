import json

def columnize(words, sep=" "*4, num_cols=11):
    res = words[0] + sep
    for i, word in enumerate(words[1:]):
        i =+ 1
        res+=word
        if i%num_cols==0:
            res+=f"\n"
        else:
            res+=sep
    return res


def main():
    with open("./five-letter-words.txt", 'r') as fp:
        lines = fp.readlines()
    words = sorted(list(set(line.strip() for line in lines)))

    with open("five-letter-words.json", 'w') as fp:
        json.dump(words, fp, indent=2)
    print_string = columnize(words)
    print(print_string)
    with open("five_letter_words_pretty.txt", 'w') as fp:
        fp.write(print_string)


if __name__=="__main__":
    main()