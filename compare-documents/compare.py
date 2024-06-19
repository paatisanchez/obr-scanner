import argparse
import difflib
from tkinter import Tk, Label, Button, filedialog, Text
from docx import Document

def read_document(path):
    """Reads the content of a document given its path."""
    if path.endswith('.docx'):
        doc = Document(path)
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text)
        return '\n'.join(full_text)
    elif path.endswith('.txt') or path.endswith('.brl'):
        with open(path, 'r', encoding='utf-8') as file:
            return file.read()
    else:
        raise ValueError("Unsupported file format")

def compare_documents(doc1, doc2):
    """Compares the content of two documents and shows the differences."""
    d = difflib.Differ()
    diff = list(d.compare(doc1.splitlines(), doc2.splitlines()))
    return '\n'.join(diff)

def calculate_accuracy(doc1, doc2):
    """Calculates the accuracy percentage between two documents."""
    matcher = difflib.SequenceMatcher(None, doc1, doc2)
    return matcher.ratio() * 100

def truncate_to_match_length(doc1, doc2):
    """Truncates the longer document to match the length of the shorter document."""
    min_length = min(len(doc1), len(doc2))
    return doc1[:min_length], doc2[:min_length], len(doc1) != len(doc2)

def select_file1():
    global file1_path
    file1_path = filedialog.askopenfilename(filetypes=[("Document Files", "*.docx *.txt *.brl")])
    label_file1.config(text="File 1: " + file1_path)

def select_file2():
    global file2_path
    file2_path = filedialog.askopenfilename(filetypes=[("Document Files", "*.docx *.txt *.brl")])
    label_file2.config(text="File 2: " + file2_path)

def run_comparison():
    # Read the documents
    content_doc1 = read_document(file1_path)
    content_doc2 = read_document(file2_path)

    # Truncate documents to match lengths
    content_doc1, content_doc2, truncated = truncate_to_match_length(content_doc1, content_doc2)

    # Notify if the documents were truncated
    if truncated:
        if label_truncated is not None:
            label_truncated.config(text="Note: One or both documents have been truncated for comparison.")
        else:
            print("Note: One or both documents have been truncated for comparison.")

    # Compare the documents and show differences
    differences = compare_documents(content_doc1, content_doc2)
    if text_differences is not None:
        text_differences.delete("1.0", "end")
        text_differences.insert("1.0", "Differences:\n" + differences)
    else:
        print("Differences:\n", differences)

    # Calculate and print the accuracy percentage
    accuracy = calculate_accuracy(content_doc1, content_doc2)
    if label_accuracy is not None:
        label_accuracy.config(text=f"Accuracy: {accuracy:.2f}%")
    else:
        print(f"Accuracy: {accuracy:.2f}%")

def main():
    parser = argparse.ArgumentParser(description="Compare two documents (.docx, .txt, or .brl) and show the differences.")
    parser.add_argument("file1", nargs='?', help="Path to the first document file.")
    parser.add_argument("file2", nargs='?', help="Path to the second document file.")
    args = parser.parse_args()

    global label_truncated, label_accuracy, text_differences
    label_truncated = None
    label_accuracy = None
    text_differences = None

    if args.file1 and args.file2:
        global file1_path, file2_path
        file1_path = args.file1
        file2_path = args.file2
        run_comparison()
    else:
        # Create the main window
        root = Tk()
        root.title("Document Comparison Tool")

        global label_file1, label_file2

        label_instructions = Label(root, text="Select two documents (.docx, .txt, or .brl) to compare")
        label_instructions.pack()

        label_file1 = Label(root, text="File 1: Not selected")
        label_file1.pack()

        button_file1 = Button(root, text="Select File 1", command=select_file1)
        button_file1.pack()

        label_file2 = Label(root, text="File 2: Not selected")
        label_file2.pack()

        button_file2 = Button(root, text="Select File 2", command=select_file2)
        button_file2.pack()

        button_compare = Button(root, text="Compare Documents", command=run_comparison)
        button_compare.pack()

        label_truncated = Label(root, text="")
        label_truncated.pack()

        label_accuracy = Label(root, text="Accuracy: N/A")
        label_accuracy.pack()

        text_differences = Text(root, wrap="word", height=15, width=80)
        text_differences.pack()

        # Run the GUI event loop
        root.mainloop()

if __name__ == "__main__":
    main()
