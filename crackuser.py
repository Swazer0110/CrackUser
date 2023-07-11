import itertools
import os
import sys
import argparse
import itertools
import chardet
import re

def banner():
    print("""
          _____             __   __  __           
         / ___/______ _____/ /__/ / / /__ ___ ____
        / /__/ __/ _ `/ __/  '_/ /_/ (_-</ -_) __/
        \___/_/  \_,_/\__/_/\_\\____/___/\__/_/                                       
        """)

def apply_rule(rule,path):
    print("!> Applying the rule [{}] to [{}]".format(rule,path))
    os.system("hashcat --hook-threads=24 --stdout temp -r {} > {}".format(rule,path))


def save_data(data,path):
    with open(path,"w")as file:
        file.write("\n".join(data))

def remove_duplicates(path):
    with open(path, 'r', encoding='utf-8', errors='replace') as f:
        wordlist = f.read().splitlines()

    unique_wordlist = list(set(wordlist))

    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(unique_wordlist))


def errors(args):
    if args.strings:
       data = args.strings.split(",")
    else:
        print("No strings specified")
        exit()

    if args.allowed and args.disallowed:
        print("Incompatible flags: -allowed -disallowed")
        exit()

def generate_permutations(data, min_words, max_words):
    print("!> Generating string combinations")
    permutations = []
    
    for r in range(min_words, max_words + 1):
        for combination in itertools.permutations(data, r):
            permutations.append("".join(combination))
    
    return permutations

def filter_word(word, regex, mode):
    if mode == "allowed":
        regex="^[{}]+$".format(regex)
        if re.match(regex, word):
            return word
    elif mode == "disallowed":
        if not re.search(f"[{regex}]", word):
            return word
    elif mode == "regex":
        if re.match(regex, word):
            return word
    return None

def regex_filter(filep, regex, mode):
    print("!> Applying {} regex to [{}]".format(mode, filep))
    filtered_wordlist = []
    with open(filep, 'r', encoding='latin-1') as file:
        wordlist = file.read().splitlines()

    for word in wordlist:
        result = filter_word(word, regex, mode)
        if result is not None:
            filtered_wordlist.append(result)

    with open(filep, 'w', encoding='latin-1') as file:
        file.write('\n'.join(filtered_wordlist))



def main():
    banner()
    parser = argparse.ArgumentParser(description="Create wordlist with combinations of given data")
    parser.add_argument('-s', '--strings', type=str, required=True, help='Strings to combine (separated by commas) Ex: -s word1,word2,word3')
    parser.add_argument('-r', '--rule', type=str, required=False, default="OneRuleToRuleThemAll.rule", help='Hashcat rule')
    parser.add_argument('-o', '--output', type=str, required=False, default="Output/wordlist.txt", help='Output file path')
    parser.add_argument('-max', '--max-combinations', type=int, required=False, default=3, help='Max number of combined word together')
    parser.add_argument('-min', '--min-combinations', type=int, required=False, default=1, help='Minimum number of combined word together')
    parser.add_argument('-a', '--allowed', type=str, required=False, help='Allowed characters in the wordlist. Ex: -a abcdefghijklmnopqrstxyz-_,')
    parser.add_argument('-d', '--disallowed', type=str, required=False, help='Disallowed characters in the wordlist. Ex: -d *?_:.;,')
    parser.add_argument('-re', '--regex', type=str, required=False, help='Custom regex to filter wordlist. Ex: -re "^[{abcdefghijklmnopqrstxyz}]+$"')

    args = parser.parse_args()
    errors(args)

    data = args.strings.split(",")
    rule=args.rule
    path=args.output
    min_comb = args.min_combinations
    max_comb = args.max_combinations
    mode=None
    regex=None
    if args.allowed:
        mode="allowed"
        regex=args.allowed
    if args.disallowed:
        mode="disallowed"
        regex=args.disallowed
    if args.regex:
        mode="regex"
        regex=args.regex
    
    combinations = generate_permutations(data,min_comb,max_comb)
    save_data(combinations, "temp")
    apply_rule(rule,path)
        
    if regex: regex_filter(path, regex, mode)

    remove_duplicates(path)
    
    os.system("rm temp")

if __name__ == "__main__":
    main()