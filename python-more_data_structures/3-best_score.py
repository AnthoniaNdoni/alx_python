#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    
    max_key = max(a_dictionary,key=a_dictionary.get)
    print("Best score: {}".format(None))
    return max_key


a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'David': 16, 'Adam': 10}
result = best_score(a_dictionary)
print("Best score:", result)