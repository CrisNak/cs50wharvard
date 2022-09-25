def announce(f):
    def wrapper():
        print("About ti run the function...")
        f()
        print("Done with the function.")
    return wrapper
#acresta coisas a função

@announce
def hello():
    print("Hello World")

