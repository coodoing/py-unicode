py-unicode
==========

python unicode and encoding code
代码基于python33，深入了解一些关于python3.x中unicode以及encoding方面相应的知识

一些相关的知识点：
#open状态rb对应的是_io.BufferedReader,r对应的是_io.TextIOWrapper
class io.TextIOWrapper(buffer, encoding=None, errors=None, newline=None, 
line_buffering=False)
A buffered text stream over a BufferedIOBase binary stream. It inherits TextIOBase.
encoding gives the name of the encoding that the stream will be decoded or encoded with. It 
defaults to locale.getpreferredencoding().

encode和decode方法
字符串在Python内部的表示是unicode编码，因此，在做编码转换时，通常需要以unicode作为中间编
码，即先将其他编码的字符串解码（decode）成unicode，再从unicode编码（encode）成另一种编码
decode的作用是将其他编码的字符串转换成unicode编码，如str1.decode('gb2312')，表示将gb2312
编码的字符串str1转换成unicode编码。 
encode的作用是将unicode编码转换成其他编码的字符串，如str2.encode('gb2312')，表示将unicode
编码的字符串str2转换成gb2312编码。 
因此，转码的时候一定要先搞明白，字符串str是什么编码，然后decode成unicode，然后再encode成其他编码。
代码中字符串的默认编码与代码文件本身的编码一致。 
如：s='中文'
如果是在utf8的文件中，该字符串就是utf8编码，如果是在gb2312的文件中，则其编码为gb2312。这
种情况下，要进行编码转换，都需要先用decode方法将其转换成unicode编码，再使用encode方法将
其转换成其他编码。通常，在没有指定特定的编码方式时，都是使用的系统默认编码创建的代码文件
