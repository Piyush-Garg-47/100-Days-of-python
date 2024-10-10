def greet(fx):
    def mfx(*args , **kwargs):
        print("happy navratri !!")
        fx(*args , **kwargs)
        print("you are writing this code in sardiya navratri !!")
    return mfx

@greet
def hello():
    print("hello piyush , how are you !!")

hello()
@greet
def add(a,b):
    print(a+b)

add(4,5)