import os,sys
from rtlib import flatten
def main(argv) :
        print type(argv)
        if(type(argv) =='list') :
            inp_args = argv
        else:
            inp_args=[]
            inp_args.append(argv)
        inp_args = flatten(inp_args)
        print inp_args
        m= len(argv)
        out_file= 'pyscript.py'
        if m ==0 :
            raise IOError('No input file given')
        else:
            for i,item in enumerate(inp_args) :
                if( i==0):
                    inp_file = item
                if( i==1):
                    out_file =item
        
        print inp_file
        print out_file
        fo=open(out_file,'w')
        fi=open(inp_file,'rU')
        #content = fi.read()
        tab1='  '
        print1='fo.write('

        fo.write('def main():\n')
        fo.write(tab1+"fo=open('"+inp_file+"','w')\n")
        for i in fi.readlines() :
            iq = i.strip()
            iq = str.replace(iq,"'","\\'")
            iq=iq+"\\n"
            fo.write(tab1+print1+"'"+iq+"')\n")
        fo.write(tab1+"fo.close()\n")
        fo.write("if __name__ == '__main__' :\n")
        fo.write(tab1+'main()')
        fi.close()
        fo.close()







if __name__ == '__main__' :
    main(sys.argv[1:])
