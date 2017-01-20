# -*- coding: utf-8 -*-
# Find the time and value of max load for each of the regions
# COAST, EAST, FAR_WEST, NORTH, NORTH_C, SOUTHERN, SOUTH_C, WEST
# and write the result out in a csv file, using pipe character | as the delimiter.
# An example output can be seen in the "example.csv" file.

import csv
import xlrd

datafile = "2013_ERCOT_Hourly_Load_Data.xls"
outfile = "2013_Max_Loads.csv"


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    data = [['Station', 'Year', 'Month', 'Day', 'Hour', 'Max Load']]

    nameofplace = sheet.row_values(0, start_colx=1, end_colx=None)
    numOfCol = len(nameofplace)

    for i in range(numOfCol-1):
        cv = sheet.col_values(i + 1, start_rowx=1, end_rowx=None)
        maxval = max(cv)
        maxpos = cv.index(maxval) + 1
        maxtime = sheet.cell_value(maxpos, 0)
        realtime = xlrd.xldate_as_tuple(maxtime, 0)
        row = []
        row.append(str(nameofplace[i]))
        row.append(realtime[0])
        row.append(realtime[1])
        row.append(realtime[2])
        row.append(realtime[3])
        row.append(maxval)
        data.append(row)
    return data


def save_file(data, filename):
    with open(outfile, 'wb') as fr:
        f = csv.writer(fr, delimiter="|")
        f.writerows(data)
        fr.close()
        return fr

def test():
    data = parse_file(datafile)
    save_file(data, outfile)

    ans = {'FAR_WEST': {'Max Load': "2281.2722140000024", 'Year': "2013", "Month": "6", "Day": "26", "Hour": "17"}}
    
    fields = ["Year", "Month", "Day", "Hour", "Max Load"]
    with open(outfile) as of:
        csvfile = csv.DictReader(of, delimiter="|")
        for line in csvfile:
            s = line["Station"]
            if s == 'FAR_WEST':
                for field in fields:
                    assert ans[s][field] == line[field]

test()