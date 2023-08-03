if __name__ == "__main__" :
    import sys
    if len(sys.argv) == 1:
        print("0 arguments")
    elif len(sys.argv) == 2:    
        print("1 argument\n1: {}\n".format(sys.argv[1]))
    else:
        count = 1
        print("{} argument(s)".format(len(sys.argv) -1))
        for i in range(1, len(sys.argv)):
                print("{}: {}".format(count, sys.argv[i]))
                count += 1
