from openpyxl import Workbook

def save_to_excel(data, output_path):
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Extracted Data"

    headers = list(data.keys())
    sheet.append(headers)

    values = list(data.values())
    sheet.append(values)

    workbook.save(output_path)
    print(f"Data saved to {output_path}")