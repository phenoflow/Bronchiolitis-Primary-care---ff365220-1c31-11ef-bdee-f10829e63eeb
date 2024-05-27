# Chukwuma Iwundu, Clare MacRae, Eleftheria Vasileiou, 2024.

import sys, csv, re

codes = [{"code":"H061.","system":"ctv3"},{"code":"Hyu11","system":"ctv3"},{"code":"H06z.","system":"ctv3"},{"code":"H061z","system":"ctv3"},{"code":"H0616","system":"ctv3"},{"code":"H06..","system":"ctv3"},{"code":"X101l","system":"ctv3"},{"code":"H312300","system":"ctv3"},{"code":"Hyu1100","system":"ctv3"},{"code":"H06z.00","system":"ctv3"},{"code":"H061z00","system":"ctv3"},{"code":"SP08B00","system":"ctv3"},{"code":"H061600","system":"ctv3"},{"code":"Hyu11","system":"ctv3"},{"code":"H06..","system":"ctv3"},{"code":"H06z.","system":"ctv3"},{"code":"X101l","system":"ctv3"},{"code":"H061z","system":"ctv3"},{"code":"H0616","system":"ctv3"},{"code":"H061.","system":"ctv3"},{"code":"H312300","system":"ctv3"},{"code":"Hyu1100","system":"ctv3"},{"code":"H06z.00","system":"ctv3"},{"code":"H061z00","system":"ctv3"},{"code":"H061600","system":"ctv3"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('bronchiolitis-primary-care-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["bronchiolitis-primary-care-bronchitis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["bronchiolitis-primary-care-bronchitis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["bronchiolitis-primary-care-bronchitis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
