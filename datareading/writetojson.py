import json

# Read data from the existing JSON file
old_f=open("data.json", "r")
data = json.load(old_f)


# Write to a new JSON file
new_f=open("new_file.json", "w")
json.dump(data, new_f, indent=4)

print("Data copied with modifications!")

old_f.close()
new_f.close()
