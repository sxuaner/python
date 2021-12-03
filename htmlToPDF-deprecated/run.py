# install: "pip install pdfcrowd"
# https://pdfcrowd.com/user/account/
import sys
import pdfcrowd

html = sys.argv[1]


try:
    # create the API client instance
    client = pdfcrowd.HtmlToPdfClient('Xuan', '1194a5b31b74a41c98425024425798c5')

    # run the conversion and write the result to a file
    client.convertUrlToFile(html, 'output.pdf')
except pdfcrowd.Error as why:
    # report the error
    sys.stderr.write('Pdfcrowd Error: {}\n'.format(why))

    # rethrow or handle the exception
    raise
