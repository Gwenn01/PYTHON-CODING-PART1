# dictionary
# get return the value
def get(dict, key):
    return dict[key]
# return the length
def len(dict):
   count = 0
   for item in dict:
       count += 1
       
   return count       
# add
def add(dict, key, value):
    dict[key] = value
# remove
def remove(dict, key):
     dict[key] = ""
          
dict = {
    "name": "Gwen",
     "course": "BSIT",
     "age": 19
}
print(get(dict, "name"))
print(len(dict))
add(dict, "gender", "male")
print(dict)