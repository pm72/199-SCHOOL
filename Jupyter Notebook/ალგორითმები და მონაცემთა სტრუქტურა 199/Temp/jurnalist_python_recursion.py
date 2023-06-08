def recurs_find_key(key, obj):
  if key in obj:
    return obj.get(key)
  
  for k, v in obj.items():
    if type(v) == dict:
      result = recurs_find_key(key, v)

      if result:
        return result



# ================
data = {
  'url': 'https://clearspending.ge/contract/2772758941200014/',
  'contracts': {'number': 235678, 'date': '2023-04-16'},
  'sum': {'total': 456_000, 'currency': 'GEL'},
}

print(recurs_find_key('total', data))
