from optparse import OptionParser

def get_options(args=None):
    """Parse command line options and parameters."""
    parser = OptionParser(usage='%prog -n max number limit till which we need to print prime',
                          description='print prime numbers till a upper range')

    parser.add_option('-n', '--innum', action='store',
                      help='upper range',default=None)

    options, args = parser.parse_args(args)
    return options, args


def printPrime(num, maxNum):
    val = 2
    while((val*val) < maxNum):
        for i in range( val, maxNum):
            if num[i]!= -1:
                if num[i]%val == 0:
                   num[i]=-1
        val+=1

    for i in range(1,len(num)):
        if num[i] != -1:
           print num[i]


def main(args=None):
    options, args = get_options(args)

    try:
        maxNum = int(options.innum)
    except TypeError:
        print 'Please enter a valid integer'

    num = range(1,maxNum +1 )
    printPrime(num, maxNum)

if __name__ == '__main__':
    main()