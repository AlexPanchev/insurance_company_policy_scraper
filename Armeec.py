# import pdfplumber
from datetime import datetime
import re


def extract_policy_data(page_text, data):

        data['Номер на полицата'] = re.search(r'№\s*(\w+/\d+/\d+)', page_text).group(1)
        data['Застраховащ'] = re.search(r'ЗАСТРАХОВАЩ\s*(\S.*?)(?=\s*ЕГН)', page_text).group(1)
        match = re.search(r"(\d+\.\d+)\sлв\.\s(\d+\.\d+)\sлв\.\s(\d+\.\d+)\sлв\.\s(\d+\.\d+)\sлв\.", page_text)
        if match:
            data['Базова премия'] = match.group(1)
            data['Данък'] = match.group(2)
            data['Други'] = match.group(3)
            data['Обща сума'] = match.group(4)
        match = re.search(r'НАЧАЛО: ([\d]+.[\d]+.[\d]+)', page_text).group(1)
        if match:
            date_object = datetime.strptime(match, "%d.%m.%Y")
            formatted_date = date_object.strftime("%d-%m-%y")
        data['Начална дата'] = formatted_date

        match = re.search(r'Дата и място на сключване: ([\d]+.[\d]+.[\d]+)', page_text).group(1)
        if match:
            date_object = datetime.strptime(match, "%d.%m.%Y")
            formatted_date = date_object.strftime("%d-%m-%y")
        data['Дата на издаване'] = formatted_date
        data['ЕГН'] = re.search(r'ЕГН \/ ЕИК ([\d]+)', page_text).group(1)

        pattern = r"ЕГН \/ ЕИК [\d]+\s*(.*?)Тел"
        first_part = re.search(pattern, page_text).group(1)

        pattern = r'\s*(.*?)Им'
        second_part = re.search(pattern, page_text).group(1)

        data['Address'] = first_part + second_part


        return data




