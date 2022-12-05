student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    print(key)
    print(value)
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():

    print(f"Below index is  \n {index}")
    print(f"Row data is \n {row}")
    print(f"Student is {row.student} and marks are {row['score']}")
    pass

df = pandas.read_csv("nato_phonetic_alphabet.csv")
print(df)

#TODO 1. Create a dictionary in this format:
nato_dict = {row.letter:row.code for (index, row) in df.iterrows()}
print(nato_dict)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = input("Enter your name")
nato_list_of_your_name = [nato_dict[letter.upper()] for letter in name]
print(nato_list_of_your_name)
