import sys
def main(argv) :
    file=argv
    f=open(file,'rU')
    content=f.read()
    return content
if __name__ == '__main__':
  main(sys.argv[1:])
