import pdfplumber
import Armeec
import Bul_Ins
import re

def check_insurance_provider(pdf_path):
    data = {}
    with pdfplumber.open(pdf_path) as pdf:
        page_text = pdf.pages[0].extract_text()
        match_armeec = re.findall(r"АРМЕЕЦ", page_text)
        match_bulins = re.findall(r"www\.bulins\.com", page_text)

        if match_armeec:
            data['Застраховател'] = 'Армеец'
            data = Armeec.extract_policy_data(page_text, data)
            return data

        elif match_bulins:
            data['Застраховател'] = 'Бул Инс'
            data = Bul_Ins.extract_policy_data(page_text, data)
            return data

        else:
            return 'Coming Soon'




