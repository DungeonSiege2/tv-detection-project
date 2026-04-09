from openpyxl import Workbook
import json

def generate_excel():
    wb = Workbook()
    ws = wb.active

    ws.append(["Дата", "Файл", "Количество ТВ"])

    with open("data/history.json", "r") as f:
        data = json.load(f)

    for item in data:
        ws.append([item["date"], item["file"], item["tv_count"]])

    wb.save("report.xlsx")