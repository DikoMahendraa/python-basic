Notes!

Python is a case-sensitive language, so be mindful of capitalization.
Don't forget to enclose the text welcome inside quotation marks.

Common Mistakes (I)

1. Spelling Error
   annual_income = 95000

# error because of a spelling mistake

print(annual_icome)

2.  Adding Spaces at the Beginning
    In Python, indentation has a specific meaning. So, if we add unnecessary spaces at the beginning, we will get an error. For example,

          print("Hello")  # Error

3.  Error because of Quotation Marks
    We have seen many beginners make this mistake. They usually forget to close the string with quotation marks. For example,

4.  Forgetting Commas in the print() Function
    Here, Python interprets "Age:" age as a single item. Since it's neither a string nor a variable, we get an error.

5.  Forgetting to use f in a f-string
    If you forget to include f before the quotation marks, the string is treated as a normal string. As a result, {age} is interpreted as plain text instead of being evaluated as a variable
