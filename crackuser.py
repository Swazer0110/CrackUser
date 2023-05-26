import itertools
import os
import sys
import argparse
import itertools
import chardet

def apply_rule(path):
    os.system("hashcat --stdout temp -r OneRuleToRuleThemAll.rule > {}".format(path))

def save_data(data,path):
    with open(path,"w")as file:
        file.write("\n".join(data))


def generate_permutations(data, min_words, max_words):
    permutations = []
    
    for r in range(min_words, max_words + 1):
        for combination in itertools.permutations(data, r):
            permutations.append("".join(combination))
    
    return permutations


def allowed(filep, allowed_characters):
    filtered_wordlist = []
    with open(filep, 'r') as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']
        wordlist = raw_data.decode(encoding).splitlines()
    for word in wordlist:
        if re.match(f"^[{allowed_characters}]+$", word):
            filtered_wordlist.append(word)
    with open(filep, 'w') as file:
        for word in filtered_wordlist:
            file.write(word + '\n')


def disallowed(filep, not_allowed_characters):
    filtered_wordlist = []
    with open(filep, 'r') as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']
        wordlist = raw_data.decode(encoding).splitlines()
    for word in wordlist:
        if not re.search(f"[{not_allowed_characters}]", word):
            filtered_wordlist.append(word)
    with open(filep, 'w') as file:
        for word in filtered_wordlist:
            file.write(word + '\n')


def main():
    parser = argparse.ArgumentParser(description='Create wordlist with combinations of given data')
    parser.add_argument('-s', '--strings', type=str, required=False, help='Strings to combine (separated by commas) Ex: -s word1,word2,word3')
    parser.add_argument('-r', '--rule', type=str, required=False, help='Hashcat rule')
    parser.add_argument('-o', '--output', type=str, required=False, help='Output file path')
    parser.add_argument('-max', '--max-combinations', type=str, required=False, help='Max number of combined word together')
    parser.add_argument('-min', '--min-combinations', type=str, required=False, help='Minimun number of combined word together')
    parser.add_argument('-a', '--allowed', type=str, required=False, help='Allowed characters in the wordlist. Ex: -a abcdefghijklmnopqrstxyz-_,')
    parser.add_argument('-d', '--disallowed', type=str, required=False, help='Disallowed characters in the wordlist. Ex: -d *?_:.;,')



    args = parser.parse_args()

    if args.strings:
       data = args.strings.split(",")
    else:
        print("No strings specified")
        exit()


    if args.max_combinations:
        max_comb = args.max_combinations
    else:
        max_comb = len(data)

    if args.min_combinations:
        min_comb = args.min_combinations
    else:
        min_comb = 0


    if args.output:
        path=args.output
    else:
        path="wordlist.txt"

    
    if args.allowed and args.disallowed:
        print("Incompatible flags: -allowed -disallowed")
        exit()
    
    

    combinations = generate_permutations(data,min_comb,max_comb)[1:]
    print(combinations)
    save_data(combinations, "temp")
    apply_rule(path)
    os.system("rm temp")
    if args.allowed:
        allowed(path,args.allowed)
    if args.disallowed:
        disallowed(path,args.disallowed)
if __name__ == "__main__":
    main()