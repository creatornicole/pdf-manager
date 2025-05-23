# pdf-manager

This Python script offers essential PDF functionalities, without relying on untrustworthy online services. Many websites claim to delete your files after processing, but when it comes to sensitive documents or internal work, why take the risk?

With this tool, you can handle PDF operations locally on your machine, ensuring your data stays private and secure.

---

Functions that can be executed using the command line:
- remove pages from the PDF
- merge several PDFs together
- add a blank page to the PDF

To run the Python script:
```cmd
python pdf_manager.py [function] [other params]
```

Where `function` is a placeholder, that should be replaced with the desired action you would like to perform:
- `-r`... remove
- `-m`... merge
- `-a`... add
- `-h`... help (provides details and instructions how to use each function to modify the PDF file)

and `other params` represent function-specific parameters that vary depending on the function you are executing.
- `-r`... remove
    - 1st: filepath to the PDF file
    - 2nd: page specification
        - single number (e.g.: 7) - removes the specified page
        - comma-separated numbers (e.g.: 42,187,360) - removes all specified pages
        - two numbers with a dash in between (e.g.: 41-47) - removes all pages within the specified range, including both the start and end pages (i.e., 41 and 48 will also be removed)
        - leading dash followed by a number (e.g. -10) - removes all pages *before* the specified page (the specified page itself is not removed)
        - number followed by a dash (e.g. 10-) - removes all pages *after* the specified page (the specified page itself is not removed)
- `-m`... merge
    - specify the filepaths of the PDF files that should be merged together
    - the order in which you specify the files will determine the order in which they are merged
- `-a`... add
    - 1st: filepath to the PDF file
    - 2nd: page *after* which the blank page will be added
- `-h`... help
    - 1st: abbreviation of the function to be explained
        - for example, use `r` to get an explanation of the remove function

Each function creates a new version of the original PDF with the specified changes applied. This ensures that the original file remains untouched, preventing any accidental, irreversible modifications.