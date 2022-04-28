# directory_to_pdf
Convert a directory of nested files and folders to one long pdf to print

I had to install a lot of the dependencies using "pip3 install"

make sure to run "pip3 install pdflatex"

In order to merge a large quantity of pdfs you may need to increase the max open file size of your shell. First check the limit by running "ulimit -n" Then increase it if necessary by running "ulimit -n 10240". The number specifies the max.

Can Handle .tex, .pdf, .jpg (most image type files), and .md files!
