# pdf2txt

This is a script that scrapes text from a PDF into a txt file.

The project uses Tika, because it's a solution recommended by
[SO](https://stackoverflow.com/questions/34837707/how-to-extract-text-from-a-pdf-file),
and I found it to produce a convenient output for my purposes (scraping payslips).


I've tried the following alternatives:

* PyPDF2, but that didn't give me actual PDF contents.
* `pdftotext`, but the resulting output gave me tables' content
  column-by-column, which made understanding the data harder.
