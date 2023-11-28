
# taking care of md files
from markdown import markdown
import pdfkit
from PIL import Image
from PyPDF2 import PdfMerger, PdfFileReader
import os
from pathlib import Path
import shutil
from fpdf import FPDF


# take care of markdown files
def markdown_to_pdf(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as f:
            html_text = markdown(f.read(), output_format='html4')

        pdfkit.from_string(html_text, output_filename)
    except:
        print("ERRROR: " + input_filename)
    return True


# taking care of jpg files
def jpg_to_pdf(input_filename, output_filename):
    image_1 = Image.open(input_filename)
    im_1 = image_1.convert('RGB')
    im_1.save(output_filename)


def txt_to_pdf(input_filename, output_filename):
    # from https://www.geeksforgeeks.org/convert-text-and-text-file-to-pdf-using-python/
    # save FPDF() class into 
    # a variable pdf
    pdf = FPDF()   
       
    # Add a page
    pdf.add_page()
       
    # set style and size of font 
    # that you want in the pdf
    pdf.set_font("Arial", size = 15)
      
    # open the text file in read mode
    f = open("myfile.txt", "r")
      
    # insert the texts in pdf
    for x in f:
        pdf.cell(200, 10, txt = x, ln = 1, align = 'C')
       
    # save the pdf with name .pdf
    pdf.output("mygfg.pdf")   


# merge_pdfs
def merge_pdfs(pdfs, output_filename):
    # Call the PdfMerger
    merger = PdfMerger()

    # Loop through all of them and append their pages
    print("PDFs TO BE MERGED")
    for pdf in pdfs:
        print(pdf)
        # NEW LINE import_outline=False may not be necessary
        merger.append(pdf, import_outline=False ) # had to add the import bookmarks false for some reason
        # OLD LINE: merger.append(pdf, import_bookmarks=False ) # had to add the import bookmarks false for some reason
     
    # Write all the files into a file which is named as shown below
    merger.write(output_filename)
    merger.close()



# iterate over files in
# that directory
def recurse_directories(starting_directory):
    filenames = list()

    for filename in sorted(os.scandir(starting_directory), key=lambda e: e.name.lower()):
        if filename.is_file():      # check if it's a file
            filenames.append(filename)
        
        if os.path.isdir(filename):                     # check if it's a directory and dive into it
            print("DIRECTORY: " + filename.path)
            filenames = filenames + recurse_directories(filename)
            print("EXIT DIRECTORY")
    return filenames
            

pdfs = []
directory = '/Users/alejandro/Desktop/gitrepos/pika/pikawiki' # ASSIGN DIRECTORY
all_files = recurse_directories(directory)
for count, filename in enumerate(all_files):
    output_filename = "./pdfs/" + filename.path[filename.path.rindex('/')+1:] # gets the file name
    if filename.path.lower().endswith(('.png', '.jpg', '.jpeg, .svg')):   # check if it's a picture
        print("jpg or png: " + filename.path)
        output_filename = "./pdfs/" + Path(output_filename).stem + ".pdf"
        jpg_to_pdf(filename.path, output_filename)
        pdfs.append(output_filename)
    elif filename.path.lower().endswith(('.md')):                   # check if it's a MD file
        print("MD: " + filename.path)
        output_filename = "./pdfs/" + Path(output_filename).stem + ".pdf"
        if markdown_to_pdf(filename.path, output_filename):
            pdfs.append(output_filename)
    elif filename.path.lower().endswith(('.pdf')):                  # check if it's a PDF file
        print("PDF: " + filename.path)
        output_filename = "./pdfs/" + Path(output_filename).stem + ".pdf"
        shutil.copyfile(filename.path, output_filename)
        pdfs.append(output_filename)
    elif filename.path.lower().endswith(('.tex')):                  # check for tex files
        print("TEX: " + filename.path)
        output_filename = "./pdfs/" + Path(output_filename).stem + ".pdf"
        os.system("pdflatex"+ " " + filename.path)
        os.system("mv " +Path(output_filename).stem + ".pdf " + output_filename)
        pdfs.append(output_filename)
    else:
        print("OTHER: " + filename.path)                            # print what is just processed as text


text_file = open("pdf_list.txt", "w")
n = text_file.write(str(pdfs))
text_file.close()
merge_pdfs(pdfs, "mergedfilesoutput.pdf")



