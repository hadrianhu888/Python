def hello():
    """Hello function 
    """
    print("Hello, World!")
    
# Path: hello_test.py

def hello1(user_input):
    """Hello1 function
    """
    return "Hello, {}!".format(user_input)

def main(): 
    """Main function
    """
    hello()
    
if __name__ == "__main__":
    main()