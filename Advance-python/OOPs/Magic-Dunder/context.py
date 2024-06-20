class context:
    def __enter__(self):
        print("Entering context")
        return self
    def __exit__(self,exc_type,exc_value,traceback):
        print("Exiting context")
with context():
    print("Inside context")

