'''
Exercise 5: Take the following Python code that stores a string:

str = 'X-DSPAM-Confidence:0.8475'

Use find and string slicing to extract the portion of the string after the colon character and then use the float function to convert the extracted string into a floating point number.

'''

text='X-DSPAM-Confidence:0.8475'
begin=text.find(":")
aimstr=text[begin+1:]
aminum=float(aimstr)
print(aminum)