from win32com.client import Dispatch
from os import walk

wdFormatPDF = 17


def doc2pdf(input_file, is_doc=False):
    word = Dispatch('Word.Application')
    doc = word.Documents.Open(input_file)
    if is_doc:
        doc.SaveAs(input_file.replace(".doc", ".pdf"), FileFormat=wdFormatPDF)
    else:
        doc.SaveAs(input_file.replace(".docx", ".pdf"), FileFormat=wdFormatPDF)
    doc.Close()
    word.Quit()


if __name__ == "__main__":
    doc_files = []
    directory = "C:\\Users\\xkw\\Desktop\\destData"
    # directory = r"E:\Learn\已学完\2.1.Fundamental of microelectronic\助教生涯\homework\HW12\homework\new_part"
    for root, dirs, filenames in walk(directory):
        for file in filenames:
            if file.endswith(".docx"):
                doc2pdf(str(root + "\\" + file))
            elif file.endswith(".doc"):
                doc2pdf(str(root + "\\" + file), True)
