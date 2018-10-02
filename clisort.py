from random import randint
from argparse import ArgumentParser
from sys import exit


parser = ArgumentParser()

#parser.add_argument('sortmode', type=str, default="quick", help="Sort mode. Default: quick.  Options: quick, merge")
parser.add_argument('amount', type=int, help="Amount of integers in list")
parser.add_argument('-m', '--min', type=int, default=0, help="Minimum value of an integer. Default: 0")
parser.add_argument('-x', '--max', type=int, default=1000, help="Maximum value of an integer. Default: 1000")

args = parser.parse_args()

if args.amount < 0:
    print("Amount of integers must be greater than 0")
    exit(1)

if args.min > args.max:
    print("Minimum must be greater than maximum")
    exit(2)

values = [randint(args.min, args.max) for _ in range(args.amount)]

print(values)