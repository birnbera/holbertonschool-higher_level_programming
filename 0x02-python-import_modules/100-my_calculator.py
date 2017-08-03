#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a, operator, b = sys.argv[1:]
    if operator not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    print("{:s} {:s} {:s} = ".format(a, operator, b), end="")
    for sym, op in [('+', add), ('-', sub), ('*', mul), ('/', div)]:
        if operator == sym:
            print("{:d}".format(op(int(a), int(b))))
