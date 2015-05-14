from facctorial import factorial
def fact_digits (n): 
	n  = str(n)
	numb = 0
	answ = 0
	for i in n :
		numb = int(i)
		answ += factorial(numb)
	return answ