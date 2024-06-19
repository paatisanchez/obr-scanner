
# Document Comparison Tool

This tool allows you to compare the content of two documents (.docx or .txt) and shows the differences between them. It also calculates an accuracy percentage indicating how similar the two documents are.

## Differences Key

- `-`: Line that is in the first document but not in the second.
- `+`: Line that is in the second document but not in the first.
- `?`: Line that marks the locations of the specific differences in the preceding lines.

## How to Execute

### Command Line Interface

1. **Clone the Repository**

   Clone the repository or download the script to your local machine.

2. **Install Dependencies**

   Ensure you have Python installed. Then, install the required dependencies using pip:

   ```sh
   pip install python-docx
   ```

3. **Run the Script**

   Open the terminal and navigate to the directory where the script is located. Run the script by passing the paths of the documents to compare as arguments:

   ```sh
   python compare.py /path/to/first_document.docx /path/to/second_document.txt
   ```

   Replace `/path/to/first_document.docx` and `/path/to/second_document.txt` with the actual paths to your documents.

### Graphical User Interface

1. **Clone the Repository**

   Clone the repository or download the script to your local machine.

2. **Install Dependencies**

   Ensure you have Python installed. Then, install the required dependencies using pip:

   ```sh
   pip install python-docx tkinter
   ```

3. **Run the Script**

   Open the terminal and navigate to the directory where the script is located. Run the script:

   ```sh
   python compare.py
   ```

4. **Use the GUI**

   A GUI window will open. Click on "Select File 1" and "Select File 2" to choose the `.brl`, `.docx` or `.txt` files you want to compare. After selecting the files, click "Compare Documents" to see the differences and accuracy.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact:

- For any inquiries or issues, feel free to reach out to ic23x001@technikum-wien.at
