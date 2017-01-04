from pyzillow.pyzillow import ZillowWrapper, GetDeepSearchResults

address = '2114 Bigelow Ave'
zipcode = 'Seattle, WA'

myAPI = ''


zillow_data = ZillowWrapper(myAPI)
deep_search_response = zillow_data.get_deep_search_results(address, zipcode)
result = GetDeepSearchResults(deep_search_response)

print(result)

result.zillow_id # zillow id, needed for the GetUpdatedPropertyDetails