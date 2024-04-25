'''

Definiti o funcție care primește un string și printează pe ecran:
Numărul de caractere lower case este x
Numărul de caractere upper case exte y

'''

# def numar_caractere(text):
# 		nr_lowercase = 0
# 		nr_uppercase = 0
# 		for i in range(len(text)):
# 				if text[i].islower():
# 						nr_lowercase+=1
# 				elif text[i].isupper():
# 						nr_uppercase += 1
# 				else:
# 						raise Exception
# 	print(f"Numarul de caractere lowercase este {nr_lowercase} si numarul de caractere"
# 					f" uppercase este {nr_uppercase}")


# def numar_caractere(text):
# 		nr_lowercase = 0
# 		nr_uppercase = 0
# 		for i in range(len(text)):
# 				if text[i].islower():
# 						nr_lowercase += 1
# 				elif text[i].isupper():
# 						nr_uppercase += 1
# 				elif text[i].isnumeric():
# 						print("The number is not a string")
# 				else:
# 						raise Exception
# 		print(f"Numarul de caractere lowercase este {nr_lowercase} si numarul de caractere"
# 							f" uppercase este {nr_uppercase}")

def numar_caractere(text):
    nr_upper_case= 0
    nr_lower_case= 0
    for i in range(len(text)):
        if text[i].islower():
            nr_lower_case+=1
        else:
            nr_upper_case+=1
    print(f"Lowercase: {nr_lower_case}, uppercase :{nr_upper_case}")

numar_caractere("Buna ziua imi pare foarte bine ca sunteti aici")
