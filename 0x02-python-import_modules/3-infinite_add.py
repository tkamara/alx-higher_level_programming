#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    count = len(argv)
    sum = 0
    i = 1
    while i <= count:
        sum += int(sys.argv[i])
        i += 1
    print("{:d}".format(sum))
