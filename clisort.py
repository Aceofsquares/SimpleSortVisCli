from random import randint, choice
from argparse import ArgumentParser
from sys import exit
from sortalgos.insertsort import insertion
from sortalgos.selsort import selection
from sortalgos.qsort import quicksort
from sortalgos.msort import mergesort
parser = ArgumentParser()

parser.add_argument('amount', type=int, help="Amount of integers in list")
parser.add_argument('-s', '--sortmode', nargs=1, type=str, help="Sort mode. Default: Neither.  Options: quick, merge")
parser.add_argument('-m', '--min', type=int, default=0, help="Minimum value of an integer. Default: 0")
parser.add_argument('-x', '--max', type=int, default=1000, help="Maximum value of an integer. Default: 1000")

args = parser.parse_args()

if args.amount <= 0:
    print("Amount of integers must be greater than 0")
    exit(1)

if args.min > args.max:
    print("Minimum must be greater than maximum")
    exit(2)

values = [randint(args.min, args.max) for _ in range(args.amount)]

sorted_list = []
print(f"\nUnsorted values: {', '.join(map(str, values))}\n")
if args.sortmode:
    if args.sortmode[0] in ("quick", "qui"):
        sorted_list = quicksort(values)
    elif args.sortmode[0] in ("merge", "mer"):
        sorted_list = mergesort(values)
    elif args.sortmode[0] in ("insertion", "ins"):
        sorted_list = insertion(values)
    elif args.sortmode[0] in ("selection", "sel"):
        sorted_list = selection(values)
else:
    sorted_list = sorted(values)

print(f"Sorted values: {', '.join(map(str, sorted_list))}\n")
