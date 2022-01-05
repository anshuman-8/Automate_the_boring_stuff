import csv, openpyxl, os

# wb=openpyxl.load_workbook('/home/anshuman/Downloads/automate_online-materials/censuspopdata.xlsx')
# csvFile=csv.open('censuspopdata.csv')

for excelFile in os.listdir('.'):
    # Skip non-xlsx files, load the workbook object.
    if not excelFile.endswith('.xlsx'):
        print(str(excelFile))
        continue
    if excelFile.endswith('.xlsx'):
        wb=openpyxl.Workbook(excelFile)
    # for sheetName in wb.sheetnames():
     # Loop through every sheet in the workbook.
        sheetName=wb.worksheets[0]
        sheet = wb.get_sheet_by_name(sheetName)
        csvFile=csv.open(str(excelFile)+'_'+str(sheetName)+'.csv')
        writer=csv.writer(csvFile)
        # Create the CSV filename from the Excel filename and sheet title.
        # Create the csv.writer object for this CSV file.

        # Loop through every row in the sheet.
        for rowNum in range(1, sheet.max_row + 1):
            rowData = []    # append each cell to this list
            # Loop through each cell in the row.
            for colNum in range(1, sheet.max_column + 1):
                rowData.append(sheet.column[colNum])
                print(sheet.column[colNum])
                # Append each cell's data to rowData.
            writer.writerow(rowData)
            # Write the rowData list to the CSV file.

        csvFile.close()