def announce(f):
    def wrapper():
        print("About to run the function")
        f()
        print("done with the function")