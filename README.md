# pdf2txt

This is a script that scrapes text from a PDF into a txt file.

**Note:** Consider using [pdftotext][pdftotext] over pdf2txt. For reasons, see
the README below.

The project uses Tika, because it's a solution recommended by
[SO](https://stackoverflow.com/questions/34837707/how-to-extract-text-from-a-pdf-file),
and I found it to produce a convenient output for my purposes (scraping
payslips). However, Tika is an external dependency. Pdf2txt fetches the Tika
Java package from Internet, which I found to be an error-prone process.

## Alternatives to pdf2txt

I've tried the following alternatives:

* [pdftotext][pdftotext]. This is my preferred tool. I created pdf2txt, because
  I used to think that the resulting output gave me tables' content
  column-by-column, which made understanding the data harder. Since then I
  found out about `-raw` and `-layout` options, which usually give a workable
  output.
* [PyPDF2](https://pypi.org/project/PyPDF2/), but that didn't give me actual
  PDF contents.

[pdftotext]: https://en.wikipedia.org/wiki/Pdftotext
