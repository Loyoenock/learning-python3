import sys

if len(sys.argv) < 2:
    print('Too few arguements')
elif len(sys.argv) > 2:
    print('Too many arguements')

print('Hello my name is', sys.argv[1])
