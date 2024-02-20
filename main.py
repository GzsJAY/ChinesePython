ch = [
    "输入",
    "输出"
    "假",
   	"无",
	"真",
	"和",
	"作为",
	"断言",
	"中断",
	"类",
	"继续",
	"定义",
	"删除",
    "否则如果",
    "否则",
    "异常",
	"最终",
	"循环",
	"从",
	"全局",
	"如果",
    "导入",
	"在",
	"是",
	"匿名",
    "非局部",
	"非",
	"或",
	"跳过",
	"抛出",
	"返回",	    
	"尝试",
	"当",
	"带",
	"生成",
]
en = [
    "print"
    "input"
    "False",
    "None",
    "True",
    "and",
    "as",
    "assert",
    "break",
    "class",
    "continue",
    "def",
    "del",
    "elif",
    "else",
    "except",
    "finally",
    "for",
    "from",
    "global",
    "if",
    "import",
    "in",
    "is",
    "lambda",
    "nonlocal",
    "not",
    "or",
    "pass",
    "raise",
    "return",
    "try",
    "while",
    "with",
    "yield",
]
def replace_words_in_file(file_path, words_to_replace, replacement_words):
    with open(file_path, "r") as file:      #读取文件
        content = file.read()
    for index in range(len(words_to_replace)):     #循环更改文件中的中文代码变为python代码
        word = words_to_replace[index]
        replacement = replacement_words[index]
        content = content.replace(word, replacement)
    with open(file_path, "w") as file:       #重新写入
        file.write(content)
filepath = input()
replace_words_in_file(filepath, ch, en)
