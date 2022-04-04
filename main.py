
# taking care of md files
from markdown import markdown
import pdfkit
from PIL import Image
from PyPDF2 import PdfFileMerger, PdfFileReader
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
    # Call the PdfFileMerger
    merger = PdfFileMerger()

    # Loop through all of them and append their pages
    print("PDFs TO BE MERGED")
    for pdf in pdfs:
        print(pdf)
        merger.append(pdf, import_bookmarks=False ) # had to add the import bookmarks false for some reason
     
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
            

pdfs = ['./pdfs/contract_spring17.pdf', './pdfs/contract_summer17.pdf', './pdfs/Bid_Letter.pdf', './pdfs/Advocat.pdf', './pdfs/Cat_History.pdf', './pdfs/Feeding_the_cats.pdf', './pdfs/Majestic_Cat.pdf', './pdfs/afs-zelda-locker.pdf', './pdfs/backup-power.pdf', './pdfs/backups.pdf', './pdfs/cdist.pdf', './pdfs/certificates.pdf', './pdfs/computers.pdf', './pdfs/git.pdf', './pdfs/hostnames.pdf', './pdfs/Mailing-Lists.pdf', './pdfs/musika.pdf', './pdfs/NanoBridges.pdf', './pdfs/Netgear-config.pdf', './pdfs/TopOfNetworkRack.pdf', './pdfs/network.pdf', './pdfs/printing.pdf', './pdfs/README-if-you-are-new-yfncc.pdf', './pdfs/Functional_Kitchen_Tour.pdf', './pdfs/fvuserguide.pdf', './pdfs/Kitchen-Manager.pdf', './pdfs/Inventory-full.pdf', './pdfs/Kitchen-Appliances.pdf', './pdfs/Kitchen_Supplies.pdf', './pdfs/Reimbursement-Caps.pdf', './pdfs/Sterilizer-troubleshooting.pdf', './pdfs/Ministewarding.pdf', './pdfs/new-england-produce-center.pdf', './pdfs/Stewarding.pdf', './pdfs/Sysco.pdf', './pdfs/Kayaks.pdf', './pdfs/New_York_Times.pdf', './pdfs/Take_a_closer_look_at_pika_scavenger_hunt.pdf', './pdfs/2020_GRA_Position_Description.docx.pdf', './pdfs/2020_GRA_Search_Process.pdf', './pdfs/GRA_Search_Candidate_Evaluation_Criteria.pdf', './pdfs/MIT_Housing_Office_GRA_Interview_Rubric.pdf', './pdfs/ailg-plenary-2017.pdf', './pdfs/bay3-office.pdf', './pdfs/Chickens.pdf', './pdfs/House_tour.pdf', './pdfs/IP_addresses.pdf', './pdfs/Reunions_40th_Reunion_Activities.pdf', './pdfs/Roomination.pdf', './pdfs/Summer_dictatorship.pdf', './pdfs/Fire_Prop_Making.pdf', './pdfs/garagetop-garden-plan.pdf', './pdfs/Graywater.pdf', './pdfs/Housecorp_pika-1903-bromley2.pdf', './pdfs/Housecorp_pika-1916-bromley2.pdf', './pdfs/Historical_Maps.pdf', './pdfs/Awesome_Ideas.pdf', './pdfs/Die-in-a-Fire.pdf', './pdfs/Flickr.pdf', './pdfs/Occupy-harvard-dome.pdf', './pdfs/Geodesic_dome_at_occupy_harvard.pdf', './pdfs/headless-squirrel.pdf', './pdfs/network-monitoring.pdf', './pdfs/Rush_Fall_2008_Shirts.pdf', './pdfs/Rush_Room.pdf', './pdfs/1970_09_24_Deed.pdf', './pdfs/1978_10_03_Mortgage.pdf', './pdfs/1978_10_3_FinancingStatement.pdf', './pdfs/1981_06_11_Mortgage.pdf', './pdfs/1984_07_13_Certificate.pdf', './pdfs/1984_07_13_Mortgage.pdf', './pdfs/1984_07_13_MunicipalLien.pdf', './pdfs/1984_07_13_RentAssignment.pdf', './pdfs/1984_08_03_Vote.pdf', './pdfs/1990_07_19_Taking.pdf', './pdfs/1991_09_09_Redemption.pdf', './pdfs/1996_01_19_Discharge.pdf', './pdfs/2007_05_07_Taking.pdf', './pdfs/2008_08_14_Redemption.pdf', './pdfs/2012_06_25_Taking.pdf', './pdfs/2012_08_13_Redemption.pdf', './pdfs/2015_11_04_Discharge.pdf', './pdfs/2015_11_4_Release.pdf', './pdfs/Pantry_Door.pdf', './pdfs/Public_use_computers.pdf', './pdfs/Richard_M_Stallman_at_Dinner.pdf', './pdfs/bluegaloo1.pdf', './pdfs/contract_fall17.pdf', './pdfs/contract_spring18.pdf', './pdfs/Deep-Cleaning-.pdf', './pdfs/Home.pdf', './pdfs/House-Tour.pdf', './pdfs/carrot_wrench.pdf', './pdfs/carrot_wrench_flipped.pdf', './pdfs/logo.pdf', './pdfs/bay-inventory-summer-2018.pdf', './pdfs/Cleaning-Bathrooms.pdf', './pdfs/mopping.pdf', './pdfs/Installing_air_conditioners.pdf', './pdfs/Dysfunctional_house_tour.pdf', './pdfs/electrical-breakers.pdf', './pdfs/Light_Fixtures.pdf', "./pdfs/Steve's-pika-wiring-guide.pdf", './pdfs/bleeding-radiators.pdf', './pdfs/control.pdf', './pdfs/Library.pdf', './pdfs/Barn_bay_doors.pdf', './pdfs/Things_That_Leak_2010.pdf', './pdfs/Deck_permit_situation.pdf', './pdfs/Parking_contract.pdf', './pdfs/Roof_Replacement.pdf', './pdfs/Turn_Off_Outdoor_Faucets.pdf', './pdfs/Contractors_and_their_wisdom.pdf', './pdfs/Dumpster-License.pdf', './pdfs/House_manager_contacts.pdf', './pdfs/Inspections.pdf', './pdfs/Long_Term_Maintenance.pdf', './pdfs/Periodic_Maintenance.pdf', './pdfs/Piano-Tuning-and-Repair.pdf', './pdfs/greasetrap.pdf', './pdfs/Water_Main_Replacement.pdf', './pdfs/SHITS.pdf', './pdfs/Sources-of-common-leaks.pdf', './pdfs/car-battery-charger.pdf', "./pdfs/House_Manager's_Closet.pdf", './pdfs/trash.pdf', './pdfs/Fall-17-Budget-Proposal.pdf', './pdfs/Fall16.pdf', './pdfs/Historical-Expenditures-15-17.pdf', './pdfs/Historical-Expenditures-F13-to-S16.pdf', './pdfs/Spring16.pdf', './pdfs/Spring17.pdf', './pdfs/IRDF_Educational_Operating_Grants.pdf', './pdfs/Treasuring.pdf', './pdfs/Treasuring_Responsibilities.pdf', './pdfs/Treasuring_System_Administration.pdf', './pdfs/AILG.pdf', './pdfs/FIC_Account_Information.pdf', './pdfs/Graduate-Resident-Advisor.pdf', './pdfs/Housecorp_Meeting_2008-07-01.pdf', './pdfs/Housecorp_Meeting_2012-06-16.pdf', './pdfs/Housecorp_Meeting_Minutes.pdf', './pdfs/Housecorp_Search_Committee_2012.pdf', './pdfs/Informal_meeting_to_discuss_Housecorp_on_2012-05-29.pdf', './pdfs/2017-02-23-notes.pdf', './pdfs/2017-02-23.pdf', './pdfs/meeting-2017-04-17-notes.pdf', './pdfs/Official-pika-rules.pdf', './pdfs/Social_Media.pdf', './pdfs/Yanni_Tree.pdf', './pdfs/Email_to_send_to_new_alumni.pdf', './pdfs/yfnac.pdf', './pdfs/pika-ears.pdf', './pdfs/Retreat-Chair.pdf', './pdfs/How-to-Be-Roominator-Chair.pdf', './pdfs/1713.pdf', './pdfs/1714.pdf', './pdfs/1715.pdf', './pdfs/bluegaloo1.pdf', './pdfs/bluegaloo2.pdf', './pdfs/bluegaloo3.pdf', './pdfs/closet1.pdf', './pdfs/closet2.pdf', './pdfs/closet3.pdf', './pdfs/coke1.pdf', './pdfs/coke2.pdf', './pdfs/coke3.pdf', './pdfs/compass1.pdf', './pdfs/compass2.pdf', './pdfs/compass3.pdf', './pdfs/compass4.pdf', './pdfs/compass5.pdf', './pdfs/darkness1.pdf', './pdfs/darkness2.pdf', './pdfs/darkness3.pdf', './pdfs/dragon1.pdf', './pdfs/dragon2.pdf', './pdfs/dragon3.pdf', './pdfs/drug01.pdf', './pdfs/drug02.pdf', './pdfs/drug1.pdf', './pdfs/drug2.pdf', './pdfs/end1.pdf', './pdfs/flower1.pdf', './pdfs/flower2.pdf', './pdfs/flower3.pdf', './pdfs/flower4.pdf', './pdfs/flower5.pdf', './pdfs/flower6.pdf', './pdfs/flower7.pdf', './pdfs/hobbiithole1.pdf', './pdfs/hobbit_hole_1.pdf', './pdfs/hobbit_hole_2.pdf', './pdfs/hobbit_hole_3.pdf', './pdfs/hobbithole2.pdf', './pdfs/hobbithole3.pdf', './pdfs/knot1.pdf', './pdfs/knot2.pdf', './pdfs/knot3.pdf', './pdfs/knot4.pdf', './pdfs/knot5.pdf', './pdfs/loeb2.pdf', './pdfs/loeb3.pdf', './pdfs/loeb4.pdf', './pdfs/maze01.pdf', './pdfs/maze02.pdf', './pdfs/maze1.pdf', './pdfs/maze2.pdf', './pdfs/pirate1.pdf', './pdfs/pirate2.pdf', './pdfs/pirate3.pdf', './pdfs/pirate4.pdf', './pdfs/pirate5.pdf', './pdfs/pirate6.pdf', './pdfs/pirate7.pdf', './pdfs/rainbow1.pdf', './pdfs/rainbow2.pdf', './pdfs/rainbow3.pdf', './pdfs/rainbow4.pdf', './pdfs/rush1.pdf', './pdfs/rush2.pdf', './pdfs/rush3.pdf', './pdfs/rush4.pdf', './pdfs/skylight1.pdf', './pdfs/skylight2.pdf', './pdfs/skylight3.pdf', './pdfs/skylight4.pdf', './pdfs/skylight5.pdf', './pdfs/skylight6.pdf', './pdfs/skylight7.pdf', './pdfs/toastie1.pdf', './pdfs/toastie2.pdf', './pdfs/toastie3.pdf', './pdfs/veggie01.pdf', './pdfs/veggie02.pdf', './pdfs/wood1.pdf', './pdfs/wood2.pdf', './pdfs/wood3.pdf', './pdfs/Room-Descriptions.pdf', './pdfs/roomination-algorithm.pdf', './pdfs/roomination-format.py.pdf', './pdfs/Roomination.pdf', './pdfs/Bid-Letter-Information.pdf', './pdfs/Bid-Letter.pdf', './pdfs/bid-votes.pdf', './pdfs/Bid_Making_and_Delivery.pdf', './pdfs/Cross_Campus_Party_Funding.pdf', './pdfs/cdeweck.pdf', './pdfs/dson32001.pdf', './pdfs/skhaguli.pdf', './pdfs/Rush-Events.pdf', './pdfs/Rush-Meetings.pdf', './pdfs/Rush-Survey.pdf', './pdfs/Rush.pdf', './pdfs/Rush_Chair.pdf', './pdfs/Rushh.pdf', './pdfs/OLD-Summer_Dictator_emails-format.pdf', './pdfs/bids-database.pdf', './pdfs/chromebox-account.pdf', './pdfs/defunct-accounts.pdf', './pdfs/FCI-account.pdf', './pdfs/mailinglist-passwords.pdf', './pdfs/PNG-and-Discomforts.pdf', './pdfs/0-public-wiki.pdf', './pdfs/Directions.pdf', './pdfs/Home.pdf', './pdfs/Cast-Iron.pdf', './pdfs/electromop.pdf', './pdfs/Cleaning-guide.pdf', './pdfs/Cooking-guide.pdf', './pdfs/recipes.pdf', './pdfs/Start-Here.pdf', './pdfs/The Blurred Lines of Trash and Food at a College Co-op.pdf', './pdfs/to-print.pdf', './pdfs/fig1-floorberries.pdf', './pdfs/fig2-graph.pdf', './pdfs/Wiki-TODOs.pdf', './pdfs/MITILGINSP16c.pdf', './pdfs/dumpster_license.pdf']
# assign directory
directory = '/Users/alejandro/Desktop/gitrepos/pika/pikawiki'
all_files = recurse_directories(directory)
print(all_files)
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



