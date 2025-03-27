def count_words(string):
    
    list_words = string.split()
    number_words = len(list_words)
    return number_words


def count_characters(string):
    
    string_lower = string.lower()
    string_list = list(string_lower)
    
    results = {}
    
    for char in string_list:
        if char not in results:
            results[char] = 1
        else:
            results[char] += 1
            
    return results

def sort_function(result_dict):
    
    return_list = []
    for key, value in result_dict.items():
        return_dict = {"name":"", "count":0}
        return_dict["name"] =  key
        return_dict["count"] = value  
        return_list.append(return_dict)
        
    def sort_on(data_dict):
        return data_dict["count"]
    
    return_list.sort(reverse=True, key=sort_on)
    return return_list