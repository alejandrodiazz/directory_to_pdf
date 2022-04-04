
# taking care of md files
from markdown import markdown
import pdfkit
from PIL import Image
from PyPDF2 import PdfFileMerger, PdfFileReader
import os
from pathlib import Path

# input_filename = '/Users/alejandro/Downloads/computers/computers.md'
# output_filename1 = 'pdfs/1.pdf'

def markdown_to_pdf(input_filename, output_filename):
    with open(input_filename, 'r') as f:
        html_text = markdown(f.read(), output_format='html4')

    pdfkit.from_string(html_text, output_filename)


# taking care of jpg files
# input_filename = '/Users/alejandro/Downloads/computers/network/TopOfNetworkRack.jpg'
# output_filename2 = 'pdfs/2.pdf'


def jpg_to_pdf(input_filename, output_filename):
    image_1 = Image.open(input_filename)
    im_1 = image_1.convert('RGB')
    im_1.save(output_filename)


# # merge pdfs
# # Call the PdfFileMerger
# mergedObject = PdfFileMerger()
 
# # I had 116 files in the folder that had to be merged into a single document
# # Loop through all of them and append their pages
# mergedObject.append(PdfFileReader(output_filename1, 'rb'))
# mergedObject.append(PdfFileReader(output_filename2, 'rb'))
 
# # Write all the files into a file which is named as shown below
# mergedObject.write("mergedfilesoutput.pdf")

def merge_pdfs(pdfs, output_filename):
    # Call the PdfFileMerger
    merger = PdfFileMerger()

    # Loop through all of them and append their pages
    for pdf in pdfs:
        try:
            print(pdf)
            merger.append(pdf, import_bookmarks=False ) # had to add the import bookmarks false for some reason
        except:
            print("unable to merge: " + pdf)
     
    # Write all the files into a file which is named as shown below
    merger.write(output_filename)
    merger.close()



 
# iterate over files in
# that directory
def recurse_directories(starting_directory):
    filenames = list()

    for filename in sorted(os.scandir(starting_directory), key=lambda e: e.name.lower()):
        if filename.is_file():      # check if it's a file
            # if filename.path.lower().endswith(('.png', '.jpg', '.jpeg')):   # check if it's a picture
            #     print("jpg or png: " + filename.path)
            # elif filename.path.lower().endswith(('.md')):                   # check if it's a MD file
            #     print("MD: " + filename.path)
            # else:
            #     print("OTHER: " + filename.path)                            # print what isn't processed
            filenames.append(filename)
        
        if os.path.isdir(filename):                     # check if it's a directory and dive into it
            print("DIRECTORY: " + filename.path)
            filenames = filenames + recurse_directories(filename)
            print("EXIT DIRECTORY")
    return filenames
            

pdfs = []
# assign directory
directory = '/Users/alejandro/Downloads/computers/'
all_files = recurse_directories(directory)
print(all_files)
for count, filename in enumerate(all_files):
    output_filename = "./pdfs/" + filename.path[filename.path.rindex('/')+1:] # gets the file name
    if filename.path.lower().endswith(('.png', '.jpg', '.jpeg')):   # check if it's a picture
        print("jpg or png: " + filename.path)
        output_filename = "./pdfs/" + Path(output_filename).stem + ".pdf"
        jpg_to_pdf(filename.path, output_filename)
        pdfs.append(output_filename)
    elif filename.path.lower().endswith(('.md')):                   # check if it's a MD file
        print("MD: " + filename.path)
        output_filename = "./pdfs/" + Path(output_filename).stem + ".pdf"
        markdown_to_pdf(filename.path, output_filename)
        pdfs.append(output_filename)
    else:
        print("OTHER: " + filename.path)                            # print what isn't processed
text_file = open("pdf_list.txt", "w")
n = text_file.write(str(pdfs))
text_file.close()
merge_pdfs(pdfs, "mergedfilesoutput.pdf")



