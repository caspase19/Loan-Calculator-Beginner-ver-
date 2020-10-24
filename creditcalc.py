import math
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--principal", type=float)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
parser.add_argument("--payment", type=float)
args = parser.parse_args()

args_list = sys.argv
if len(args_list) != 5 or (not args.type) or (not args.interest) or (args.type == 'diff' and args.payment):
    print("Incorrect parameters.")
elif args.principal != None and args.principal < 0:
    print("Incorrect parameters.")
elif args.periods != None and args.periods < 0:
    print("Incorrect parameters.")
elif args.interest != None and args.interest < 0:
    print("Incorrect parameters.")
elif args.payment != None and args.payment < 0:
    print("Incorrect parameters.")

else:
    if args.type == "diff":
        P = args.principal
        n = args.periods
        i = args.interest / 1200
        total = 0
        for m in range(n):
            overpayment = math.ceil(i * (P - P * m / n))
            dm = P / n + overpayment
            total += overpayment
            print(f"Month {m + 1}: payment is {round(dm)}")
        print(f"\nOverpayment = {total}")

    elif args.type == "annuity":
        P = args.principal
        A = args.payment
        n = args.periods
        i = args.interest / 1200
        if not args.periods:
            n = math.log(A / (A - i * P), i + 1)
            n = math.ceil(n)
            years = n // 12
            sentence1 = f"It will take {years} year" if years else "It will take"
            connect = " and" if n // 12 and n % 12 else ""
            sentence2 = f" {n % 12} month" if n % 12 else ""
            if years > 1:
                sentence1 += "s"
            if n % 12 > 1:
                sentence2 += "s"
            print(sentence1 + connect + sentence2 + " to repay this loan!")
        elif not args.payment:
            A = P * i * pow(i + 1, n) / (pow(1 + i, n) - 1)
            A = math.ceil(A)
            print(f"Your monthly payment = {A}!")
        elif not args.principal:
            P = A * (pow(1 + i, n) - 1) / i / pow(i + 1, n)
            P = math.floor(P)
            print(f"Your loan principal = {P}!")
        Overpayment = round(n * A - P)
        print(f"Overpayment = {Overpayment}")
