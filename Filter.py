#!/usr/bin/env python3

import re
import linecache

#Let User define path
path = "/home/justin/Documents/"

#Let User define files
source = path+"MySrc"
target = path+"MyTgt"
new_src = path+"NewSrc"
new_tgt = path+"NewTgt"

num = 0
str1 = ""
check = ""


#Gets Line number of current source sentence
def line_no(file, sent):
    with open(file, "r") as myFile:
        for num, line in enumerate(myFile, 1):
            if sent in line:
                return num

#Writes successful sentences to files (args are new src/tgt files and tgt sentence)
def accept_data(dest_src, dest_tgt, src, tgt):
    with open(dest_src, "a+") as output:
        output.write(src)
    with open(dest_tgt, "a+") as tgtout:
        tgtout.write(tgt)

#Checks to see if the source/target sentences don't match each other
def copy_check(src, tgt):


    if src == tgt:
        print("The sentences are the same")
        return False
    else:
        return True

#Check to see if a sentence is already in a file
def duplicate_check(src, tgt):
    if len(re.findall(source, src)) > 1 or len(re.findall(target, tgt)) > 1:
        print("This is a dupicate")
        return False
    else:
        return True


def sentence_ratio(src, tgt, threshold=0.7):
    short, long = sorted([len(x) for x in [src, tgt]])
    print(short/long)
    if short/long < threshold:
        return False
    else:
        return True


def length_check(src, tgt, threshold=25):
    if len(src.split()) or len(tgt.split()) > threshold:
        return False
    else:
        return True


#Check the ratio of sentence characters
def char_ratio_check(src, tgt):
    alpha = r"([A-Z]|[a-z])"
    digits = r"\d"
    whitespace = r"\s"
    total = 0
    iter = 0

    # Count the number of letters, numbers and symbols in a sentence
    for lang in src, tgt:
        num_count = 0
        other_count = 0
        alpha_count = 0
        char_count = 0
        for char in lang:

            if re.match(alpha, char):
                alpha_count += 1
                char_count += 1
            elif re.match(digits, char):
                num_count += 1
                char_count += 1
            elif re.match(whitespace, char):
                pass
            else:
                other_count += 1
                char_count += 1

        # Check to see if 50% or more of the sentence are numbers and letters or if it's all non-letters
        if (alpha_count + num_count) / char_count < 0.5 or num_count + other_count == num_count + alpha_count + other_count:
            print("This sentence has a bad character ratio")
            total += 1
            # print("This sentence is fine")

        iter += 1

        #Checks for the 2nd iteration. Only proceeds with null int Total value
        if iter == 2:
            if not total:
                accept_data(new_src, new_tgt, src, tgt)
                print("sentence {} is ok".format(line_no(source,src)))


if __name__ == '__main__':
    with open(source, "r+") as f:
        for src_sent in f:
            tgt_sent = linecache.getline("/home/justin/Documents/MyTgt", line_no(source, src_sent))
            tgt_sent = str1.join(tgt_sent)
            copy_check(src_sent, tgt_sent)
            if copy_check:
                print("Yes")
                duplicate_check(src_sent, tgt_sent)
            else:
                break

            if duplicate_check:
                sentence_ratio(src_sent, tgt_sent)
            else:
                break

            if sentence_ratio:
                length_check(src_sent, tgt_sent)
            else:
                break

            if length_check:
                char_ratio_check(src_sent, tgt_sent)
            else:
                break
