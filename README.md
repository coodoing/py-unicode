(py-unicode)基于python33，运行于win7中文环境，主要是关于python3.x中unicode以及encoding方面的深入理解，主要涉及到的知识点包括：
###1 ASCII、UNICODE、GBK、CP936、MSCS
 **1.1 ASCII**

美国信息交换标准码。 在计算机的存储单元中，一个ASCII码值占一个字节(8个二进制位)，但其最高位(b7)用作奇偶校验位。ASCII(American Standard Code for Information Interchange)，是一种单字节的编码。计算机世界里一开始只有英文，而单字节可以表示256个不同的字符，可以表示所有的英文字符和许多的控制符号。不过ASCII只用到了其中的一半（\x80以下），这也是MBCS得以实现的基础。

**1.2 ISO8859-1、EASCII**

EASCII是ASCII的扩充，把第八位也用来存储信息；在Windows中用Alt+小键盘数字输入的就是EASCII码对应字符。ISO8859-1就是EASCII最典型的实现，基本能够覆盖西欧的拉丁字母，所以又叫Latin-1。有些国外程序就要求使用ISO8859-1编码以保证Binary Safe，比如著名的XMB。

**1.3 Unicode、UTF-8**

Unicode是业界的一种标准，它可以使电脑得以呈现世界上数十种文字的系统。
后来，有人开始觉得太多编码导致世界变得过于复杂了，让人脑袋疼，于是大家坐在一起拍脑袋想出来一个方法：所有语言的字符都用同一种字符集来表示，这就是Unicode。

最初的Unicode标准UCS-2使用两个字节表示一个字符，所以你常常可以听到Unicode使用两个字节表示一个字符的说法。但过了不久有人觉得256*256太少了，还是不够用，于是出现了UCS-4标准，它使用4个字节表示一个字符，不过我们用的最多的仍然是UCS-2。

UCS(Unicode Character Set)还仅仅是字符对应码位的一张表而已，比如"汉"这个字的码位是6C49。字符具体如何传输和储存则是由UTF(UCS Transformation Format)来负责。

一开始这事很简单，直接使用UCS的码位来保存，这就是UTF-16，比如，"汉"直接使用\x6C\x49保存(UTF-16-BE)，或是倒过来使用\x49\x6C保存(UTF-16-LE)。但用着用着美国人觉得自己吃了大亏，以前英文字母只需要一个字节就能保存了，现在大锅饭一吃变成了两个字节，空间消耗大了一倍……于是UTF-8横空出世。

UTF-8是一种很别扭的编码，具体表现在他是变长的，并且兼容ASCII，ASCII字符使用1字节表示。然而这里省了的必定是从别的地方抠出来的，你肯定也听说过UTF-8里中文字符使用3个字节来保存吧？4个字节保存的字符更是在泪奔……（具体UCS-2是怎么变成UTF-8的请自行搜索）
Unicode的实现方式不同于编码方式，一个字符的Unicode编码是确定的，但是在实际传输过程中，由于不同系统平台的设计不一定一致，以及出于节省空间的目的，对Unicode编码的实现方式有所不同。于是就有了UTF-8、UTF-16、UTF-32。

UTF-8使用一至四个字节为每个字符编码：

ASCII字符只需一个字节编码（Unicode范围由U+0000至U+007F）。带有附加符号的拉丁文、希腊文、西里尔字母、亚美尼亚语、希伯来文、阿拉伯文、叙利亚文及它拿字母（即以ISO 8859为主的）则需要二个字节编码（Unicode范围由U+0080至U+07FF）。其他基本多文种平面（BMP）中的字符（这包含了大部分常用字，包括汉字）使用三个字节编码。其他极少使用的Unicode 辅助平面的字符使用四字节编码。它唯一的好处在于兼容ASCII。
UTF-16则是以U+10000为分界线，使用两个字节或者四个字节存储。
UTF-32则是全部使用4字节编码，很浪费空间。

**1.4 GB2312、GBK、GB18030**

GB是中国荒谬的国家标准。GB2312、GBK、GB18030各为前一个的扩展。

我从来讨厌GB编码，因为它毫无国际兼容性。更荒谬的是，GBK和GB18030几乎是照着Unicode字符集选取的字库。这样多此一举地弄出一套编码，还强制所有在中国销售的操作系统必须使用它，真是天朝特色。

另外，对于GB编码PHP是不认账的，mb_detect_encoding函数会把GB编码识别成CP936。

**1.5 MSCS**

然而计算机世界里很快就有了其他语言，单字节的ASCII已无法满足需求。后来每个语言就制定了一套自己的编码，由于单字节能表示的字符太少，而且同时也需要与ASCII编码保持兼容，所以这些编码纷纷使用了多字节来表示字符，如GBxxx、BIGxxx等等，他们的规则是，如果第一个字节是\x80以下，则仍然表示ASCII字符；而如果是\x80以上，则跟下一个字节一起（共两个字节）表示一个字符，然后跳过下一个字节，继续往下判断。

这里，IBM发明了一个叫Code Page的概念，将这些编码都收入囊中并分配页码，GBK是第936页，也就是CP936。所以，也可以使用CP936表示GBK。

MBCS(Multi-Byte Character Set)是这些编码的统称。目前为止大家都是用了双字节，所以有时候也叫做DBCS(Double-Byte Character Set)。必须明确的是，MBCS并不是某一种特定的编码，Windows里根据你设定的区域不同，MBCS指代不同的编码，而Linux里无法使用MBCS作为编码。在Windows中你看不到MBCS这几个字符，因为微软为了更加洋气，使用了ANSI来吓唬人，记事本的另存为对话框里编码ANSI就是MBCS。同时，在简体中文Windows默认的区域设定里，指代GBK。

###2 open函数
open状态rb对应的是_io.BufferedReader,r对应的是_io.TextIOWrapper

    class io.TextIOWrapper(buffer, encoding=None, errors=None, newline=None, 
    line_buffering=False)

A buffered text stream over a BufferedIOBase binary stream. It inherits TextIOBase.
encoding gives the name of the encoding that the stream will be decoded or encoded with. It 
defaults to locale.getpreferredencoding().

###3 encode和decode方法
字符串在Python内部的表示是unicode编码，因此，在做编码转换时，通常需要以unicode作为中间编码，即先将其他编码的字符串解码（decode）成unicode，再从unicode编码（encode）成另一种编码decode的作用是将其他编码的字符串转换成unicode编码，如str1.decode('gb2312')，表示将gb2312编码的字符串str1转换成unicode编码。 encode的作用是将unicode编码转换成其他编码的字符串，如str2.encode('gb2312')，表示将unicode编码的字符串str2转换成gb2312编码。 

因此，转码的时候一定要先搞明白，字符串str是什么编码，然后decode成unicode，然后再encode成其他编码。代码中字符串的默认编码与代码文件本身的编码一致。 

如：s='中文'
如果是在utf8的文件中，该字符串就是utf8编码，如果是在gb2312的文件中，则其编码为gb2312。这
种情况下，要进行编码转换，都需要先用decode方法将其转换成unicode编码，再使用encode方法将
其转换成其他编码。通常，在没有指定特定的编码方式时，都是使用的系统默认编码创建的代码文件


###4 相关代码

python默认编码
```
    default encodings in Python are:
    Python 2.x: ASCII
    Python 3.x: UTF-8
```
win7中文环境中对应的系统参数
```
    print('<strong>python系统参数：')
    print(locale.getdefaultlocale()) #('zh_CN', 'cp936')
    print(locale.getpreferredencoding()) # cp936
    print(sys.getdefaultencoding()) #utf-8
    print(sys.getfilesystemencoding())#mbcs
    print(sys.maxunicode)
    print(codecs.lookup('utf-8'))#codeinfo class

```

```
    ('zh_CN', 'cp936')
    cp936
    utf-8
    mbcs
    1114111
```
utf-8, gbk codecs error
```
    ch_str = '中文'
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
```

binary写文件
```

#write french in file
def write_file(filename):
    with open(filename,'wb') as file:
        file.write('ry dialect: /a/, /ɑ/, /e/, /ɛ/, /ə/, /i/, /o/, /ɔ/, /'.encode())

def write_file_append(filename,string):
    line_list = []
    with open(filename,'rb') as file:
        for line in file:
            line_list.append(line)

    with open(filename,'wb') as file:
        for i in range(len(line_list)):
            file.write(line_list[i])

        file.write(string.encode())
```


###5 参考资料
* python unicode howto:(unicode codepoints): http://docs.python.org/3/howto/unicode.html

* python unicode&encoding: http://docs.python.org/3.3/library/codecs.html#encodings-and-unicode

* unicode further reading : http://www.diveinto.org/python3/strings.html#py-encoding

* new in the python3.0:
http://docs.python.org/3.0/whatsnew/3.0.html#text-vs-data-instead-of-unicode-vs-8-bit

* codecs test: http://pymotw.com/2/codecs/

* py33 file (locale.getpreferredencoding()):
http://www.diveinto.org/python3/files.html

* py33 io (buffering):
http://docs.python.org/3.1/library/io.html#io.TextIOWrapper

PEP and ISSUES:


----------
* ISSUES:
 
distutils.commands.bdist_wininst.bdist_wininst.get_inidata use mdcs encoding
http://bugs.python.org/issue10945

bytes.decode('mbcs', 'ignore') does replace undecodable bytes on Windows Vista or later
http://bugs.python.org/issue12281


* PEP393：	

Flexible String Representation
http://www.python.org/dev/peps/pep-0393/#discussion

PEP0263: Defining Python Source Code Encodings
http://www.python.org/dev/peps/pep-0263/
