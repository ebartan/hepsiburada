import gspread
gc = gspread.service_account(filename='creds.json')
sh = gc.open('egedermowebscraping').sheet1

sh.append_row(['ahmet', 'eray', 'mehmet'])