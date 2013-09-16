#coding: UTF-8
import locale,sys,codecs,os

'''
    所有基于编码的格式都是在py33环境中进行开发
    #codecs/io/file class
    #open() function : has buffering option to use the buffering line  
'''

'''
################################################################
文件操作
    默认使用sys.getfilesystemencoding()编码格式打开文件，在window7中文环境中使用CP936（GBK）打开文件
    所以对于unicode,utf8,mscs的不同编码格式，encoding设置会出问题（utf8 gbk codecs error）
    对于多语言，这里最好别用 encoding = 'utf-8' encoding = 'utf-16_LE' 
       这里的可能解决方式是：
       1 利用codecs.open;这个对于不同的编码格式有问题（不好用）
       2 利用rb，转换成b（unicode）形式，不过在写入的时候需要进行encode操作;（可行）
       3 把txt文件转换成UTF-8格式，然后在打开文件的时候指定编码格式utf-8(可行)
       所以最好的打开方式是以binary方式打开文件，转换成unicode

'''
# codecs.open()打开文件
def open_file_codecs(filename):
    with codecs.open(filename,'rb') as file:
        for line in file:
            print(line)

def open_file_text(filename):  
    with open(filename,'rb') as file:
        for line in file:
            print(line)


#二进制方式打开文件，最有效的方式
def open_file_binary(filename):
    '''
    open状态rb对应的是_io.BufferedReader,r对应的是_io.TextIOWrapper
    '''
    data = open(filename,'rb')#.read()
    print(data.name)
    #print(data.encoding)
    print(data.mode)
    print(data)


#获取文件编码格式  
def file_encoding(filename):
    data = open(filename,'r')
    print(data.encoding)

def encode_decode_file(filename):
    data = open(filename,'r')
    de = data.read()

#write file
def write_file(filename):
    with open(filename,'wb') as file:
        file.write('ry dialect: /a/, /ɑ/, /e/, /ɛ/, /ə/, /i/, /o/, /ɔ/, /'.encode())

#append file
def write_file_append(filename,string):
    line_list = []
    with open(filename,'rb') as file:
        for line in file:
            line_list.append(line)

    with open(filename,'wb') as file:
        for i in range(len(line_list)):
            file.write(line_list[i])

        file.write(string.encode())

'''
################################################################
常用的函数封装
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
'''
################################################################
'''

if __name__ == '__main__':
    print('################################################################')
    print('<strong>python系统参数：')
    print(locale.getdefaultlocale()) #('zh_CN', 'cp936')
    print(locale.getpreferredencoding()) # cp936
    print(sys.getdefaultencoding()) #utf-8
    print(sys.getfilesystemencoding())#mbcs
    print(sys.maxunicode)
    print(codecs.lookup('utf-8'))#codeinfo class

    print('################################################################')
    print('<strong>python长度：')    
    print(len('中文'))
    print(len(u'中文'))
    print_len('中文')
    print_len('1234')
    print_len('我爱中国')

    print('################################################################')
    print('<strong>python中文编码：')
    code_str = u'中国'
    print(code_str.encode())
    print(code_str.encode('gbk'))
    print(code_str.encode().decode())
    print(code_str.encode().decode('mbcs','ignore'))#mbcs 乱码
    #print(code_str.encode().decode('gbk','strict')) #gbk codecs error

    french = 'ry dialect: /a/, /ɑ/, /e/, /ɛ/, /ə/, /i/, /o/, /ɔ/, /y/, /u/, /œ/, /ø/, '
    print(french.encode())
    print(french.encode().decode())
    
    print('################################################################')    
    path = 'encoding'
    french_unicode = path+'/unicode/'+'french-unicode.txt'
    french_utf8 = path+'/utf8/'+'french-utf8.txt'
    french_mscs = path+'/mscs/'+'french-mscs.txt'
    print('<strong>文件操作：')
    print('########################')
    print('<strong>codecs.open方式打开文件：')
    open_file_codecs('french-unicode.txt')
    open_file_codecs('french-mscs.txt')
    open_file_codecs('french-utf8.txt')
    open_file_codecs(path+'/open-test.txt')
    encode_decode_file(path+'/append-test.txt')

    print('########################')
    print('<strong>open方式打开文件：')    
    open_file_text('french-unicode.txt')#需特别注意编码问题，在win7中文系统环境中，默认会提示gbk decode error
    open_file_text('french-mscs.txt')#默认的保存格式，会造成字符的丢失
    open_file_text('french-utf8.txt')#不会出问题，但需注意open的encoding格式，否则会出现乱码

    print('########################')
    print('<strong>file encoding打开文件：')
    file_encoding('french-unicode.txt')
    file_encoding('french-mscs.txt')
    file_encoding('french-utf8.txt')

    print('########################')
    print('<strong>binary写文件：')
    write_file(path+'/write-test.txt')#以wb状态写文件，不管文件的格式，最终都正确写入文件，并将txt文件格式修改为UTF-8
    write_file_append(path+'/append-test.txt','başparmak')        

    print('########################')
    print('<strong>文件遍历：')
    path = ['french-utf8.txt']#,'french_mscs.txt']#,'french.txt']
    for i in range(0,len(path)):
        open_file_text(path[i])

    print('########################')
    codecs.BOM_UTF8.decode( "utf8" )
    s = sys.stdin.read(3)
    if s!=codecs.BOM_UTF8:
        sys.stdout.write(s)
