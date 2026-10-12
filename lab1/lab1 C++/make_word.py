import docx
import os
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

doc = docx.Document()

# Настройка полей по ГОСТу
for section in doc.sections:
    section.top_margin = Inches(0.78)
    section.bottom_margin = Inches(0.78)
    section.left_margin = Inches(1.18)
    section.right_margin = Inches(0.59)


def format_p(
    p, before=0, after=4, indent=0, size=14, bold=False, align=WD_ALIGN_PARAGRAPH.LEFT
):
    p.alignment = align
    p.paragraph_format.space_before = Pt(before)
    p.paragraph_format.space_after = Pt(after)
    p.paragraph_format.line_spacing = 1.15
    if indent > 0:
        p.paragraph_format.first_line_indent = Inches(indent)
    for run in p.runs:
        run.font.name = "Times New Roman"
        run.font.size = Pt(size)
        run.font.color.rgb = RGBColor(0, 0, 0)
        run.bold = bold


# ==================== ТИТУЛЬНЫЙ ЛИСТ ====================
headers = [
    "МИНОБРНАУКИ РОССИИ",
    "Федеральное государственное бюджетное образовательное учреждение высшего образования",
    "«ВЛАДИВОСТОКСКИЙ ГОСУДАРСТВЕННЫЙ УНИВЕРСИТЕТ»",
    "(ФГБОУ ВО «ВВГУ»)",
    "Институт информационных технологий и анализа данных",
    "Кафедра информационных технологий и систем",
]
for h in headers:
    p = doc.add_paragraph()
    p.add_run(h)
    format_p(p, after=1, size=14, align=WD_ALIGN_PARAGRAPH.CENTER)

# Уменьшили отступы, чтобы Владивосток не улетал
for _ in range(4):
    doc.add_paragraph()

p_title = doc.add_paragraph()
p_title.add_run("ОТЧЕТ ПО ЛАБОРАТОРНОЙ РАБОТЕ")
format_p(p_title, after=12, size=24, align=WD_ALIGN_PARAGRAPH.CENTER)

p_disc = doc.add_paragraph()
p_disc.add_run("по дисциплине «Информатика и основы программирования»")
format_p(p_disc, after=12, size=18, align=WD_ALIGN_PARAGRAPH.CENTER)

p_theme = doc.add_paragraph()
p_theme.add_run("Лабораторная работа 1. Основы программирования на Python")
format_p(p_theme, after=12, size=20, align=WD_ALIGN_PARAGRAPH.CENTER)

for _ in range(3):
    doc.add_paragraph()

# Сетка подписей
table = doc.add_table(rows=3, cols=3)
table.alignment = WD_TABLE_ALIGNMENT.RIGHT
widths = [Inches(1.5), Inches(3.0), Inches(2.0)]
for row in table.rows:
    for idx, w in enumerate(widths):
        row.cells[idx].width = w


def add_cell(cell, text, align=WD_ALIGN_PARAGRAPH.LEFT):
    p = cell.paragraphs[0]
    p.text = ""
    run = p.add_run(text)
    format_p(p, size=12, align=align)


add_cell(table.cell(0, 0), "Студент")
add_cell(table.cell(1, 0), "гр. БИН-26-1")
add_cell(table.cell(1, 2), "Д. Ю. Гембарская", align=WD_ALIGN_PARAGRAPH.RIGHT)
add_cell(table.cell(2, 0), "Преподаватель")
add_cell(table.cell(2, 2), "М. В. Водяницкий", align=WD_ALIGN_PARAGRAPH.RIGHT)

for i in range(1, 3):
    cell_xml = table.cell(i, 1)._tc.get_or_add_tcPr()
    cell_xml.append(
        parse_xml(
            f'<w:tcBorders {nsdecls("w")}><w:bottom w:val="single" w:sz="6" w:color="000000"/></w:tcBorders>'
        )
    )

for _ in range(2):
    doc.add_paragraph()
p_city = doc.add_paragraph()
p_city.add_run("Владивосток 2026")
format_p(p_city, size=12, align=WD_ALIGN_PARAGRAPH.CENTER)

# ==================== ВЫПОЛНЕНИЕ РАБОТЫ ====================
doc.add_page_break()

p_h1 = doc.add_paragraph()
p_h1.add_run("Выполнение работы")
format_p(p_h1, before=12, after=6, size=18, bold=True)

codes = [
    '#include <iostream>\n#include <string>\nusing namespace std;\nint main(){\n    string station_name = "Ocean";\n    int active_sensors = 18;\n    float average_temperature = 21.6;\n    bool is_online = true;\n    cout << station_name << " <class \'str\'>" << endl;\n    return 0;\n}',
    '#include <iostream>\n#include <cmath>\nusing namespace std;\nint main(){\n    int a = 7, b = 4, c = 3;\n    cout << "Результат: " << (a + b) * pow(c, 2) - (a / b) + (a % b);\n    return 0;\n}',
    '#include <iostream>\nusing namespace std;\nint main(){\n    double length, width;\n    cin >> length >> width;\n    cout << "Площадь: " << (length * width);\n    return 0;\n}',
    "#include <iostream>\n#include <iomanip>\nusing namespace std;\nint main(){\n    int total_seconds = 3665;\n    cout << setfill('0') << setw(2) << total_seconds / 3600 << endl;\n    return 0;\n}",
    '#include <iostream>\n#include <iomanip>\nusing namespace std;\nint main(){\n    double rasstoyanie_kilometr = 100, rashod_topliva = 8, stoimost_litr = 55;\n    cout << fixed << setprecision(2) << "Топливо: " << (rasstoyanie_kilometr * rashod_topliva) / 100;\n    return 0;\n}',
]

for i in range(1, 6):
    p_h2 = doc.add_paragraph()
    p_h2.add_run(f"Задание {i}. Работа с переменными" if i == 1 else f"Задание {i}")
    if i == 2:
        p_h2.runs[0].text = "Задание 2. Вычисление выражения"
    if i == 3:
        p_h2.runs[0].text = "Задание 3. Расчет параметров площадки"
    if i == 4:
        p_h2.runs[0].text = "Задание 4. Перевод времени"
    if i == 5:
        p_h2.runs[0].text = "Задание 5. Расчет стоимости поездки"
    format_p(p_h2, before=12, after=4, size=14, bold=True)

    p_text1 = (
        "В первом задании требуется создать четыре переменные разных типов (строка, целое число, вещественное число, логическое значение), присвоить им исходные значения и последовательно вывести в консоль их значения и типы данных."
        if i == 1
        else ""
    )
    if i == 2:
        p_text1 = "Во втором задании необходимо объявить переменные a, b и c и вычислить арифметическое выражение, используя математические операции C++, включая целочисленное деление, остаток от деления (%) и функцию pow() из библиотеки <cmath> для возведения в степень."
    if i == 3:
        p_text1 = "В третьем задании реализуется ввод данных пользователем через поток std::cin. Программа запрашивает длину и ширину прямоугольной площадки (вещественные числа типа double), после чего производит расчет её площади и периметра по геометрическим формулам."
    if i == 4:
        p_text1 = "В четвертом задании осуществляется математический перевод общей продолжительности времени, заданной пользователем в секундах, в формат часов, минут и секунд с помощью операторов деления и остатка. Вывод в консоль форматируется с ведущими нулями с помощью std::setw и std::setfill."
    if i == 5:
        p_text1 = "В пятом задании программа принимает от пользователя расстояние, средний расход топлива автомобиля и его цену за литр. Вычисляется итоговый объем израсходованного горючего и полные денежные затраты. Вывод вещественных чисел настраивается с точностью до двух знаков после запятой с помощью std::fixed и std::setprecision."

    p_txt = doc.add_paragraph()
    p_txt.add_run(p_text1)
    format_p(p_txt, indent=0.49)

    p_ref1 = doc.add_paragraph()
    p_ref1.add_run(f"Алгоритм решения задания представлен на рисунке {i*2-1}.")
    format_p(p_ref1, indent=0.49)

    # Автоматическая вставка блок-схем, если они лежат в папке
    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    img_name = f"blsxm{i}.png"
    if os.path.exists(img_name):
        p_img.add_run().add_picture(img_name, width=Inches(3.0))
    else:
        p_img.add_run(
            f"[Картинка {img_name} не найдена в папке floww]"
        ).font.color.rgb = RGBColor(128, 128, 128)
    format_p(p_img, before=6, after=2)

    p_cap1 = doc.add_paragraph()
    p_cap1.add_run(f"Рисунок {i*2-1} – Блок-схема программы")
    format_p(p_cap1, after=6, align=WD_ALIGN_PARAGRAPH.CENTER)

    p_ref2 = doc.add_paragraph()
    p_ref2.add_run(f"Текст программы представлен на рисунке {i*2}.")
    format_p(p_ref2, indent=0.49)

    # Рамка кода C++
    c_table = doc.add_table(rows=1, cols=1)
    c_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = c_table.cell(0, 0)
    cell.width = Inches(5.5)
    cell._tc.get_or_add_tcPr().append(
        parse_xml(f'<w:shd {nsdecls("w")} w:fill="F2F2F2"/>')
    )
    p_code = cell.paragraphs[0]
    p_code.add_run(codes[i - 1])
    format_p(p_code, size=10)
    p_code.runs[0].font.name = "Courier New"

    p_cap2 = doc.add_paragraph()
    p_cap2.add_run(f"Рисунок {i*2} – Текст программы")
    format_p(p_cap2, before=4, after=6, align=WD_ALIGN_PARAGRAPH.CENTER)

    # Текст-заключение (Размер 12)
    p_desc = doc.add_paragraph()
    p_desc.add_run(
        "В данном задании программа принимает от пользователя расстояние, средний расход топлива автомобиля и его цену за литр. Вычисляется итоговый объем израсходованного горючего и полные денежные затраты. Вывод вещественных чисел настраивается с точностью до двух знаков после запятой с помощью std::fixed и std::setprecision."
    )
    format_p(p_desc, indent=0.49, size=12)

doc.save("report.docx")
print("Готово!")
