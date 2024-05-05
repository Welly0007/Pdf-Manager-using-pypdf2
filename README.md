# Pdf-Manager-using-pypdf2

## Overview
This program serves as a PDF manager enabling users to perform various operations such as splitting, merging, and extracting pages from PDF files. It provides a simple command-line interface where users can input the filename of the PDF they want to manipulate. 

## Features
- **Merge PDF Files**: Combine two PDF files into one.
- **Extract PDF Pages**: Extract a specific page from a PDF file.
- **Split PDF Pages**: Split a PDF file into separate pages.

## Authors
- Mohamed Walid Mohamed

## Version
1.0

## Date
March 1, 2024

## Usage
The user is prompted to select an operation by entering the corresponding number:
1. Merge two PDF files.
2. Extract a page from a PDF file.
3. Split a PDF file into separate pages.
4. Exit the program.

## Instructions
1. **Merge PDF Files**: Enter the filenames of the two PDFs to merge. Optionally, specify the name of the new PDF file. If no name is provided, the default name 'Merged' will be used.

2. **Extract PDF Pages**: Enter the filename of the PDF from which you want to extract a page, followed by the page number.

3. **Split PDF Pages**: Enter the filename of the PDF you want to split.

## Dependencies
- `PyPDF2`: Python library for reading and manipulating PDF files.

## Important Notes
- The input PDF files must be located in the same directory as the program.
- Ensure that filenames are correctly spelled and include the '.pdf' extension.
- For extraction and splitting operations, provide valid page numbers within the range of the PDF file.

## How to Run
Ensure that Python and the `PyPDF2` library are installed. Run the program and follow the on-screen instructions to perform the desired PDF management tasks.

