import Armeec
import check_insurance_provider
import two
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename


def main():
    Tk().withdraw()  # Hide the root window of Tkinter
    pdf_path = askopenfilename(
        title="Select a PDF file",
        filetypes=[("PDF files", "*.pdf")]
        )
    if not pdf_path:
            print("No file selected. Exiting.")

    policy_data = check_insurance_provider.check_insurance_provider(pdf_path)
    print(policy_data)

    output_path = os.path.join(os.path.expanduser("~"), "Documents", "Extracted_Data.xlsx")
    two.save_to_excel(policy_data, output_path)

if __name__ == "__main__":
    main()
