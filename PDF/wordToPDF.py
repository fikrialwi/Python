#convert word to pdf
# import argparse
from docx2pdf import convert

# parser = argparse.ArgumentParser(description="convert your word to pdf")

# parser.add_argument(
#     'sc',
#     type=str,
#     help= "enter path directory of your file"
    
# )

# parser.add_argument(
#     '-dn',
#     '--destination',
#     type = str,
#     help = "enter path for new PDF"
# )

# source = parser.parse_args().source
# destination = parser.parse_args().destination


def main(src, des):
    convert(src,des)


src = "D:\Accepted Skripsi\Draf Skripsi\Draf Skripsi-v3.docx"
des = "D:\Accepted Skripsi\Draf Skripsi"
main(src, des)