#- IMPORTS 
from random import choice
from string import ascii_letters
from argparse import ArgumentParser

#- PARSER
def parseargs(parser):    
    parser.add_argument("-l", "--length",default=30,type=int)
    parser.add_argument("-o","--output")
    
    args = parser.parse_args()
    return args

#- PWGEN
def genpw(length):
    chars = ascii_letters + "1234567890"
    password = ""

    for i in range(length):
        password += choice(chars)

    return password

#- MAIN
def main():
    parser = ArgumentParser(
        prog="simplepwgen.py",
        description="Create secure Passwords fast."
    )

    args = parseargs(parser) 

    password = genpw(args.length)
    print(f"Password : {password}")

    if args.output:
        output = args.output + ".txt" if ".txt" not in args.output else args.output
        with open(output, "a+") as of:
            of.write(password)

if __name__ == "__main__":
    main()