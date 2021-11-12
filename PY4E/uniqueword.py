'''
Exercise 4: Find all unique words in a file
Shakespeare used over 20,000 words in his works. But how would you determine that? How would
you produce the list of all the words that Shakespeare used? Would you download all his work, read
it and track all unique words by hand?
Let’s use Python to achieve that instead. List all unique words, sorted in alphabetical order, that
are stored in a file romeo.txt containing a subset of Shakespeare’s work.
To get started, download a copy of the file www.py4e.com/code3/romeo.txt
(https://www.py4e.com/code3/romeo.txt). Create a list of unique words, which will contain the final
result. Write a program to open the file romeo.txt and read it line by line. For each line, split the line
into a list of words using the split function. For each word, check to see if the word is already in
the list of unique words. If the word is not in the list of unique words, add it to the list. When the
program completes, sort and print the list of unique words in alphabetical order.

example:
Enter file: romeo.txt
['Arise', 'But', 'It', 'Juliet', 'Who', 'already',
'and', 'breaks', 'east', 'envious', 'fair', 'grief',
'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft',
'sun', 'the', 'through', 'what', 'window',
'with', 'yonder']


流程：
1.打开文件
2.获取每一行
3.检查是否为空
4.获取每个词，重复的词不要
5.结束取词后，排序
6.打印

'''


def uniqueword():
	try:
		fname=input("please enter a file: ")
		fhand=open(fname)
	except:
		print('open file failed: ',fname)
		exit()
	ls=[]
	for line in fhand:
		words=line.split()
		if len(words)==0:
			continue
		for word in words:
			if word in ls:
				continue
			ls.append(word)
	ls.sort()
	print(ls)


uniqueword()

