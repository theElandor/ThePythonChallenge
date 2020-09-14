import csv
import  os
import time
os.makedirs('headerRemoved' , exist_ok=True)
for filename in os.listdir():
    if not filename.endswith(".csv"):
        continue

    print("removing header from "+filename)
    time.sleep(1)
    rows = []
    file_obj = open(filename)
    file_reader = csv.reader(file_obj)
    for row in file_reader:
        if file_reader.line_num == 1:
            continue
        rows.append(row)
    file_obj.close()
    file_obj = open(os.path.join('headerRemoved', filename), "w",newline='')
    writer = csv.writer(file_obj)
    for x in rows:
        writer.writerow(x)
    file_obj.close()
