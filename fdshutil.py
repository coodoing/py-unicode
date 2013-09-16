#-*-coding:utf-8-*-

import codecs,os,sys
from shutil import copytree, rmtree, ignore_patterns

class FileBak(object):

    input_path = ''
    output_path = ''
    def __init__(self,input_path,output_path):
        self.input_path = input_path
        self.output_path = output_path
        pass

    def copy(self):
        copytree(self.input_path, self.output_path, ignore=ignore_patterns('*.pyc', 'tmp*'))            
        pass

    def rm(self):
        rmtree(self.output_path)
    
    pass



src = 'encoding/languages/'
dst = 'encoding/tmp/'

#if __name__ == '__main__':
#    print()
#    bak = FileBak(src,dst)
#    bak.copy()
    
