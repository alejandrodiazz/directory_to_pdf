
# taking care of md files
from markdown import markdown
import pdfkit

input_filename = '/Users/alejandro/Downloads/computers/computers.md'
output_filename = 'pdfs/1.pdf'

with open(input_filename, 'r') as f:
    html_text = markdown(f.read(), output_format='html4')

pdfkit.from_string(html_text, output_filename)


# taking care of jpg files
from PIL import Image
input_filename = '/Users/alejandro/Downloads/computers/network/TopOfNetworkRack.jpg'
output_filename = 'pdfs/2.pdf'
image_1 = Image.open(input_filename)
im_1 = image_1.convert('RGB')
im_1.save(output_filename)


