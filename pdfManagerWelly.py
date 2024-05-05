# Program:  A pdf manager program to split, merge, and extract pdf pages
#           the user just input the filename.pdf (file must be included in the same program directory)
# Authors : 
#           Author 1: Mohamed Walid Mohamed
# Version: 1.0
# Date:    Mar 1 2024



from PyPDF2 import PdfReader, PdfWriter, PdfMerger  # Reader to read pdf, writer to create new pdf, merger to merge pdf
import os   # to check and deal with inoyt path






#Pdf Merger 
def merge_pdf(pdfPath1, pdfPath2, outname):
    merger = PdfMerger()
    merger.append(pdfPath1)     #add first pdf
    merger.append(pdfPath2)     #add second pdf
    merger.write(f"{outname}.pdf")      # create the merged file with the desired name
    merger.close

#   Pdf page extracter
def extract_pdf_page(pdfpath, pageNum=1):
    with open(pdfpath, 'rb') as file:
        reader = PdfReader(file)    #read pdf
        page = reader.pages[pageNum-1]
        writer = PdfWriter()
        writer.add_page(page)
        filename = os.path.splitext(pdfpath)[0]
        outname = f"{filename}-{pageNum}.pdf"   # make the filename with the number of extracted page
        with open(outname , 'wb') as outfile:
            writer.write(outfile)




#same as extract one page, but it loops on the whole pdf pages and extract it one by one
def split_pdf_pages(pdfPath):
    with open(pdfPath, 'rb') as file:           #rb to read
        reader = PdfReader(file)
        #split every page into different pdf file
        for pageNum in range(0, len(reader.pages)):
            currPage = reader.pages[pageNum]
            # Writing stage
            writer = PdfWriter()
            writer.add_page(currPage)
            filename = os.path.splitext(pdfPath)[0]     # Get filename from the path
            outname = f"{filename}-{pageNum+1}.pdf"     #make the every file name with the number of page beside it
            #save and compile to pdf
            with open(outname, 'wb') as outfile:        # wb to write
                writer.write(outfile)


def get_num_pages(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            pdf_read = PdfReader(file)
            num_pages = len(pdf_read.pages)
            return num_pages
    except FileNotFoundError:
        print("File not found.")
        return False

def check_path(path):               #check path in general for any fucntion
    try:
        if not (path[-3:] == 'pdf'):
            raise ValueError
        else:
            return True
    except ValueError:
        print("\nInput invalid! Try again\n")
        return False


def check_input_extract(path, page_num):            #check path and num of pages for the extract fucntion
    try:
        num_pages = get_num_pages(path)
        if num_pages is None or not ((path[-3:] == 'pdf') and 0 < page_num <= num_pages):
            raise ValueError
        else:
            return True
    except ValueError:
        print("\nInput invalid! Try again\n")
        return False





def main():
    print("Wnelcome to Pdf Manager")
    # choice=0
    while True:
        print("1-Merge two files\n2-Extract a page from file\n3-Split file into seperate pages\n4-Exit")
        print("Enter Your choice from 1 to 4:", end="")
        while True:
            try:
                choice=int(input())
                break
            except ValueError:
                print("Please Enter valid integer from 1 to 4:", end="")

        match choice:
            case 1:
                path1=input("Enter pdf_1 Name like (cslecture.pdf): ",)
                path2=input("Enter pdf_2 Name like (cslecture.pdf): ",)
                
                if not check_path(f"{path1}"):
                    continue
                elif not check_path(f"{path2}"):
                    continue
                else:
                    newPdfName=input("Enter the new pdf name (press Enter for default 'Merged'): ")
                    if not newPdfName:
                        newPdfName = "Merged"
                    merge_pdf(f"{path1}" , f"{path2}" , f"{newPdfName}")
                    print("\nPdf Created\n")
                    continue
            case 2:
                path=input("Enter Pdf Name like (cslecture.pdf): ")
                pageNum=int(input("Enter the number of page you want to extract: "))
                if not check_input_extract(f"{path}", pageNum):
                    continue
                else:
                    extract_pdf_page(f"{path}", pageNum)
                    print("\nPdf Created\n")
                    continue
            case 3:
                path=input("Enter pdf Name like (cslecture.pdf): ")
                if not check_path(f"{path}"):
                    continue
                else:
                    split_pdf_pages(f"{path}")
                    print("\nPdf Created\n")
                    continue
            case 4:
                print("Program Terminated")
                return
            case _:
                print("\nInvalid input Try again\n")
                
main()
