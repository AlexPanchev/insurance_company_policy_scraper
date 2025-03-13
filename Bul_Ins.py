# import pdfplumber
from datetime import datetime
import re


def extract_policy_data(page_text, data):

        data['Номер на полицата'] = re.search(r'№ (BG.*) сер', page_text).group(1)
        data['Застраховащ'] = re.search(r'ЗАСТРАХОВАЩ:\s*(\S.*?)(?=\s*ЕИК)', page_text).group(1)
        data['Базова премия'] = re.search(r"премия (\d+,\d+)\s*BGN", page_text).group(1)
        data['Данък'] = re.search(r'2%\s*(\d+,\d+)', page_text).group(1)
        data['Други'] = re.search(r'ОФ\s*(\d+,\d+)', page_text).group(1)
        data['Обща сума'] = re.search(r'що:\s*(\d+,\d+)', page_text).group(1)

        start_date = re.search(r'от 0 0 0 0 (\d \d \d \d \d \d \d \d) до', page_text).group(1)
        if start_date:
                cleaned_date_str = start_date.replace(" ", "")

                day = cleaned_date_str[:2]
                month = cleaned_date_str[2:4]
                year = cleaned_date_str[6:]

                data['Начална дата'] = f"{day}-{month}-{year}"
        issuance_date = re.search(r'вноски ([\d]+\.[\d]+\.[\d]+)г\.', page_text). group(1)
        if issuance_date:
            date_object = datetime.strptime(issuance_date, "%d.%m.%Y")
            formatted_date = date_object.strftime("%d-%m-%y")
        data['Дата на издаване'] = formatted_date

        data['ЕГН'] = re.search(r'ЕИК\s*([\d]+)', page_text).group(1)
        data['Адрес'] = re.search(r'АДРЕС:\s*(гр\.\/с\..*?апте\.л\s.*?0)', page_text).group(1)

        return data




