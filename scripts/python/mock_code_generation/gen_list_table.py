import json

with open('../get_stock_list/dist/nasdaq_list.json') as f:
  entries = json.load(f)['nasdaq_list']

with open('dow_html.txt', 'w') as out_file:
  out_file.write('<table class="table">\n')
  out_file.write('<tbody>\n')
  for entry in entries:
    out_file.write('<tr>\n')
    out_file.write('<td>')
    out_file.write(entry['title']+' ('+ entry['symbol']+')')
    out_file.write('</td>\n')
    out_file.write('<td>')
    out_file.write('<button type="button" class="btn btn-info">More</button>')
    out_file.write('</td>\n')
    out_file.write('</tr>\n')
  out_file.write('</tbody>\n')  
  out_file.write('</table>\n')
