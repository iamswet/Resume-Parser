from pyresparser import ResumeParser
data=ResumeParser('ssresume.pdf').get_extracted_data()
print(data)