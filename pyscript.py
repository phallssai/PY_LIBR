def main():
  fo=open('N7TO3_default.ctl','w')
  fo.write('\n')
  fo.write('# default files (these don\'t change)\n')
  fo.write('10301|leapsec.dat|||||1\n')
  fo.write('410100|N7TO3.MCF|../tbl||||1\n')
  fo.write('10250|MCF|||||1\n')
  fo.write('10252|GetAttr.temp|||||1\n')
  fo.write('10254|MCFWrite.temp|||||1\n')
  fo.write('10100|LogPGE|||||1\n')
  fo.write('10101|LogPGE|||||1\n')
  fo.write('10102|LogPGE|||||1\n')
  fo.write('10111|ShmMem|||||1\n')
  fo.write('\n')
  fo.write('# default params (these don\'t change)\n')
  fo.write('10220|Toolkit version string|SCF  TK5.2.16\n')
  fo.write('200100|SMF Verbosity Threshold|2\n')
  fo.write('200110|ProcessingCenter|"TLCF"\n')
  fo.write('200115|ProcessingHost|Linux 2.6.9-89.0.20.ELsmp i686\n')
  fo.write('200135|REPROCESSINGACTUAL|"processed 1 time"\n')
  fo.write('200170|ProcessLevel|"2"\n')
  fo.write('200175|InstrumentName|"TOMS"\n')
  fo.write('200180|OPERATIONMODE|"Test"\n')
  fo.write('200185|AuthorAffiliation|NASA/GSFC\n')
  fo.write('200190|AuthorName|"TOMS Science Team"\n')
  fo.write('200195|LOCALVERSIONID|"RFC1321 MD5 = not yet calculated"\n')
  fo.write('200210|SwathName|"TOMS Column Amount O3"\n')
  fo.write('400091|TERRAINPRESSURESOURCE|"ETOPO-5"\n')
  fo.write('400092|TEMPERATURESOURCE|"Climatology"\n')
  fo.write('400093|SNOWICESOURCE|"Climatology"\n')
  fo.write('400094|APRIORIOZONEPROFILESOURCE|"Climatology"\n')
  fo.write('123456|VERSIONID|1\n')
  fo.write('\n')
  fo.close()
if __name__ == '__main__' :
  main()