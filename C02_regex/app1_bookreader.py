"""
Create python class for object that can load contents of a text file and do:
    - search for a user provided regular expression and return line number an text
    - find all links in the book and return them
    - get all chapters of the book and the first 3 lines of each chapter
    - replace a section of text then open a temporary file for the user preview
"""
import re


class Book:
    def __init__(self, filename: str):
        self.filename = filename
        with open(self.filename, 'r') as fileopen:
            self.fileopen = fileopen.read()

    def search_patter(self, pattern):
        match = re.search(pattern, self.fileopen)
        final = match.regs[0][1]
        all_lines_pattern = re.compile("\n")
        lines = all_lines_pattern.findall(self.fileopen, 0, endpos=final)
        return len(lines), match.group(0)

    def get_chapter(self):
        pattern = r'#{3}.(?P<chapter>\w+)\n(?P<line1>.*\n)(?P<line2>.*\n)(?P<line3>.*\n)'
        match = re.search(pattern, self.fileopen)
        print(match.group('chapter'))


book1 = Book(r"process_text.md")
print(book1.fileopen)
print(book1.search_patter(r"\d\.\d\.\d"))
book1.get_chapter()
