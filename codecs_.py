#coding: UTF-8
import locale,sys,codecs,os

'''
    所有基于编码的格式都是在py33环境中进行开发
'''

def open_file_text(filename):
    #对于多语言，这里最好别用 encoding = 'utf-8' encoding = 'utf-16_LE'
    #open function : has buffering influnceing
    #open(),codecs class，io class

    '''
       这里的可能解决方式是：
       利用codecs.open;（不好用）
       利用rb，转换成b（unicode）形式，不过在写入的时候需要进行encode操作;（可行）
       把txt文件转换成UTF-8格式，然后在打开文件的时候指定编码格式utf-8(可行)
    ''' 
    with open(filename,'rb') as file:
        for line in file:
            print(line)

def open_file_binary(filename):
    #open状态rb对应的是_io.BufferedReader,r对应的是_io.TextIOWrapper
    data = open(filename,'rb')#.read()
    print(data.name)
    #print(data.encoding)
    print(data.mode)
    print(data)

def write_file(filename):
    #line_list = []
    #with open(filename,'rb') as file:
    #    for line in file:
    #        line_list.append(line)
    with open(filename,'wb') as file:
        file.write('ry dialect: /a/, /ɑ/, /e/, /ɛ/, /ə/, /i/, /o/, /ɔ/, /'.encode())
        
def file_encoding(filename):
    data = open(filename,'r')
    print(data.encoding)

def encode_decode_file(filename):
    data = open(filename,'r')
    de = data.read()

def write_file_append(filename,string):
    line_list = []
    with open(filename,'rb') as file:
        for line in file:
            line_list.append(line)

    with open(filename,'wb') as file:
        for i in range(len(line_list)):
            file.write(line_list[i])

        file.write(string.encode())

if __name__ == '__main__':
    print(locale.getdefaultlocale()) #('zh_CN', 'cp936')
    print(locale.getpreferredencoding()) # cp936
    print(sys.getdefaultencoding()) #utf-8
    print(sys.getfilesystemencoding())#mbcs
    
    print(len('含'))
    print(len(u'含'))

    code_str = u'中国'
    print(code_str.encode())
    print(code_str.encode('gbk'))
    print(code_str.encode().decode())
    print(code_str.encode().decode('mbcs','ignore'))
    #print(code_str.encode().decode('gbk','strict'))

    print(codecs.lookup('utf-8'))

    french = 'ry dialect: /a/, /ɑ/, /e/, /ɛ/, /ə/, /i/, /o/, /ɔ/, /y/, /u/, /œ/, /ø/, '
    print(french.encode())
    print(french.encode().decode())
    print('打开文件：')
    open_file_text('french-unicode.txt')#需特别注意编码问题，在win7中文系统环境中，默认会提示gbk decode error
    open_file_text('french-mscs.txt')#默认的保存格式，会造成字符的丢失
    open_file_text('french-utf8.txt')#不会出问题，但需注意open的encoding格式，否则会出现乱码

    file_encoding('french-unicode.txt')
    file_encoding('french-mscs.txt')
    file_encoding('french-utf8.txt')
    write_file('write_test.txt')#以wb状态写文件，不管文件的格式，最终都正确写入文件，并将txt文件格式修改为UTF-8
    write_file_append('encode_decode_file.txt','zhangasdg')
    encode_decode_file('encode_decode_file.txt')    
    
    path = ['french-utf8.txt']#,'french_mscs.txt']#,'french.txt']
    for i in range(0,len(path)):
        open_file_text(path[i])
    
