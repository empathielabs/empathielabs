# empathielabs/test.py
import argparse

def test():
    """
    run-test --name Alice --age 30
    """
    parser = argparse.ArgumentParser(description="Description of your script.")
    parser.add_argument('--name', type=str, help='Name of the person to greet')
    parser.add_argument('--age', type=int, help='Age of the person')

    args = parser.parse_args()

    name = args.name if args.name else "World"
    age = args.age if args.age else "unknown"
    
    print(f"Hello, {name}! Your age is {age}.")