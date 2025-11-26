import sys

def add(a,b): return a+b
def sub(a,b): return a-b
def mul(a,b): return a*b
def div(a,b):
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a/b

def main():
    if len(sys.argv) != 4:
        print("Usage: python app.py <op> <num1> <num2>")
        exit(1)

    op = sys.argv[1]
    a = float(sys.argv[2])
    b = float(sys.argv[3])

    if op == "add": print(add(a,b))
    elif op == "sub": print(sub(a,b))
    elif op == "mul": print(mul(a,b))
    elif op == "div": print(div(a,b))
    else:
        print("Invalid op")
        exit(1)

if __name__ == "__main__":
    main()
