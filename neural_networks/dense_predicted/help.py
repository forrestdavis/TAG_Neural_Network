
def test(arg, l=None):
    if l:
        print l
    print arg

if __name__=="__main__":
    test(1)
    test(1, [2])
