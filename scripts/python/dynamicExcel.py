###############################################################################
#
# Dynamic Excel Sample
#

import xlsxwriter
from xlsxwriter.utility import xl_rowcol_to_cell

for loop in range(1,401,1):
    filename = "loop"+str(loop)+".xlsx"
    workbook = xlsxwriter.Workbook(filename)
    worksheet1 = workbook.add_worksheet()

    # Add a format. Bold
    bold = workbook.add_format({'bold':True})

    # Add a format for header
    header_format = workbook.add_format({'bold':True,'bottom':6,'bottom_color':'green'})

    # Add a format for loop number
    loop_format = workbook.add_format({'font_name':'Arial','font_color':'blue','font_size':18,'align':'center'})
    
    # Add a format. Light red fill with dark red text.
    format1 = workbook.add_format({'bg_color': '#FFC7CE',
                                   'font_color': '#9C0006'})

    # Add a format. Green fill with dark green text.
    format2 = workbook.add_format({'bg_color': '#C6EFCE',
                                   'font_color': '#006100'})

    # Some sample data to run the conditional formatting against.
    data = [
        [34, 72, 38, 30, 75, 48, 75, 66, 84, 86],
        [6, 24, 1, 84, 54, 62, 60, 3, 26, 59],
        [28, 79, 97, 13, 85, 93, 93, 22, 5, 14],
        [27, 71, 40, 17, 18, 79, 90, 93, 29, 47],
        [88, 25, 33, 23, 67, 1, 59, 79, 47, 36],
        [24, 100, 20, 88, 29, 33, 38, 54, 54, 88],
        [6, 57, 88, 28, 10, 26, 37, 7, 41, 48],
        [52, 78, 1, 96, 26, 45, 47, 33, 96, 36],
        [60, 54, 81, 66, 81, 90, 80, 93, 12, 55],
        [70, 5, 46, 14, 71, 19, 66, 36, 41, 21],
    ]

    caption = ('Cells with values >= 50 are in light red. '
               'Values < 50 are in light green.')

    # Write the header
    worksheet1.write('A1','Loop Count', header_format)
    worksheet1.write('A2',loop, loop_format)
    worksheet1.set_column(0, 0, 25)
    worksheet1.set_row(1,21)

    # Write the data.
    worksheet1.write('A4', caption)
    datarow=5

    for row, row_data in enumerate(data):
        worksheet1.write_row(datarow, 1, row_data)
        datarow += 1

    # Write a conditional format over a range.
    worksheet1.conditional_format('B6:K15', {'type': 'cell',
                                             'criteria': '>=',
                                             'value': 50,
                                             'format': format1})

    # Write another conditional format over the same range.
    worksheet1.conditional_format('B6:K15', {'type': 'cell',
                                             'criteria': '<',
                                             'value': 50,
                                             'format': format2})

    # Write total
    worksheet1.write(datarow,0,"Total * Loop Count",bold)

    # Calculate total
    for column_to_sum in range(1, 11, 1): 
        cell1 = xl_rowcol_to_cell(5,column_to_sum)
        cell2 = xl_rowcol_to_cell(14,column_to_sum)
        cell_total = xl_rowcol_to_cell(datarow,column_to_sum)
        worksheet1.write_formula(cell_total,'{=SUM('+ cell1 + ':'+cell2+')*'+str(loop)+'}')
    workbook.close()
