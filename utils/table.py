from terminaltables import SingleTable

def format_table_header(item, headers):
  table_header = {}
  for key in item.keys():
    table_header[key] = headers[key]
  return table_header.values()

def adapt_table (title: str, headers: list[str], rows):
  table_data = [
    headers
  ]
  for row in rows:
    table_data.append(row.values())
  table = SingleTable(table_data, title)
  print('\n' + table.table)