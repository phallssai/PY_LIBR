
import sys,os 

def create_template(pcf_lines_list,inp_lun_str,out_lun_str) :
    template_lines=list()
    inp_found= False
    out_found = False
    for line in pcf_lines_list :
        if line.find(inp_lun)>=0 :
            if not out_found:
                str1=inp_lun_str+'|$INP|/|||$INP|$IDX'
                template_lines.append(str1)
                inp_found = True
                continue
            else:
                continue

        if line.find(out_lun) >=0  :
            if (not out_found) :
                str1=out_lun_str+'|$OUT|/|||$OUT|$IDX'
                template_lines.append(str1)
                out_found = True
                continue
            else:
                continue
            
        template_lines.append(line)
    return template_lines

def dump_pcf(file,template_lines_list,inp_files,out_files) :
    f=open(file,'w')
    for line in template_lines_list :
        if line.find('$INP') >=0 :
            for index,inp_file in enumerated(inp_files) :
                str1=line.replace('$INP',inp_file)
                str2=str1.replace('$IDX',str((inp_files.count)-index) )
                f.write(str2+'\n')
            continue
        if line.find('$OUT') >=0 :
            for index,out_file in enumerated(out_files) :
                str1=line.replace('$OUT',out_file)
                str2=str1.replace('$IDX',str((out_files.count)-index) )
                f.write(str2+'\n')
            continue
        f.write(line+'\n')

    f.close()
    return


def run_L2G(exe_file,pcf_file,path_bin):
    os.environ['PGS_PC_INFO_FILE']=pcf_file
    os.environ['PGSMSG']=path_bin
    try:
        status=subprocess.check_call([exef],env=os.environ,shell=True)
    except :
        status=0
        print "L2_mod : No output files generated "




