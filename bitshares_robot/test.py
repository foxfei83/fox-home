quote = 11
my_usd = 222
print([my_usd, quote][my_usd > quote])

def foo():
    global v
    if "v" in globals():
        print("foo:", v)
    v = 2

foo()
foo()
