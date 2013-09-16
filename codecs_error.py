#-*-coding:utf-8-*-
import re,sys,os
import locale,codecs

'''
    open file use the default encoding
    以默认的编码格式打开文件：没有使用binary格式
'''
def print_str(str):
    print(str)

def print_len(str):
    str_len = len(str)
    print(str_len)

def codecs_encode(str,encoding='utf-8'):
    return str.encode(encoding)
    pass

def codecs_decode(b_str,encoding='utf-8'):
    if type(b_str) == str:
        return
    print(b_str.decode(encoding))
    pass

def print_file_info(filename):
    data = open(filename).read()
    print(data)
    codecs_decode(data)
    pass

def print_file_line(filename):
    with open(filename) as file:
        for line in file:
            print(line)    
    pass

def print_file_line_encoding(filename,encoding = 'utf-8'):
    with open(filename,encoding = 'utf-8') as file:
        for line in file:
            print(line)  
    pass

def print_codecs_file_line(filename):
    with codecs.open(filename) as file:
        for line in file:
            print(line)    
    pass

if __name__ == '__main__':
    ch_str = '中文'
    unicode_str = u'中文'
    print('<strong>python中文:')
    print_str(ch_str)
    print_str(unicode_str)
    print('<strong>python encode():')
    print_str(codecs_encode(ch_str))
    print_str(codecs_encode(ch_str,'gbk'))
    print_str(codecs_encode(ch_str,'gb18030'))
    print_str(codecs_encode('1ère'))
    print_str(codecs_encode('1ère','gbk'))
    print('<strong>python decode():')
    codecs_decode(codecs_encode(ch_str))
    codecs_decode(codecs_encode(unicode_str))
    try:
        codecs_decode(codecs_encode(ch_str,'gbk'))
    except Exception:
        print('<strong>utf-8 codec decode error')

    codecs_decode(codecs_encode('1ère Recuérdame Ã©couteur Ã§a'))
    codecs_decode(codecs_encode('1ère Recuérdame Ã©couteur Ã§a'),'gbk')
    try:
        codecs_decode(codecs_encode('1ère','gbk'))
    except Exception:
        print('<strong>utf-8 codec decode error')

    code_str = '中国'
    print(code_str.encode().decode())
    print(code_str.encode().decode('mbcs','ignore'))
    try:
        print(code_str.encode().decode('gbk','strict'))
    except Exception:
        print('<strong>gbk codec decode error')
    print('python长度：')


    print('################################################################')
    print('下面为文件测试数据')
    '''
    encoding = 'utf-8'
    英语目录下，报错；法语目录下，没问题
    否则，恰好相反
    '''
    dir_path = ['languages/english/languages.php']
    #dir_path = ['languages/english/languages.php','languages/france/languages.php']
    for i in range(len(dir_path)):
        print_file_line(dir_path[i])
        #print_codecs_file_line(dir_path[i])

    dir_path = ['languages/france/languages.php']
    #dir_path = ['france.txt']
    #dir_path = ['languages/english/languages.php','languages/france/languages.php']
    for i in range(len(dir_path)):
        print_file_line_encoding(dir_path[i])
        #print_codecs_file_line(dir_path[i])

    dir_path = ['languages/english/languages.php']
    #dir_path = ['languages/english/languages.php','languages/france/languages.php']
    for i in range(len(dir_path)):
        try:
            print_file_line_encoding(dir_path[i])
        except Exception:
            print('<strong>english utf-8 error')
        #print_codecs_file_line(dir_path[i])

    #dir_path = ['languages/france/languages.php']
    dir_path = ['france.txt']
    #dir_path = ['languages/english/languages.php','languages/france/languages.php']
    for i in range(len(dir_path)):
        try:
            print_file_line(dir_path[i])
        except Exception:
            print('<strong>france gbk error')
        #print_codecs_file_line(dir_path[i])

    dir_path = ['languages/english/languages.php','languages/france/languages.php']
    file_output = ['lang/en/aaa.txt','lang/fr/aaa.txt']
    for i in range(len(dir_path)):
        try:
            print_codecs_file_line(dir_path[i])
        except Exception:
            print('<strong>error')

    
