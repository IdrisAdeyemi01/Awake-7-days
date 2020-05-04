def name(first_name, last_name, middle_name= ''):
	first_name= str(first_name).capitalize()
	last_name= str(last_name).capitalize()
	middle_name= str(middle_name).capitalize()
	return print(first_name, middle_name, last_name)
	
name('Musa', 'Abdullah')