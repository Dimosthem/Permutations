'''
Όνομα : ΄Δημοσθένης
Επίθετο: Μπουναρέλης
ΑΕΜ: 9431



'''
import random
import math
import itertools
import sys
import time
def calcLength(length):
	x= 0
	for i in range (1  , length+1):
		x+= math.factorial(i)

	return x
class MyPair :
	pair =[]
	gotUsed = [] 			#Αν εχει χρησιμοποιηθει μια μεταθεση
	numberUsed = 0
	def __init__(self, p=[]):
		self.pair = p
		
	
	
	

	def initializeBool(self):

		for i in range (0 , len(self.pair)):
			self.gotUsed.append(False)

	
	

	def binarySearch(self ,number, offset , num_of_digits):
		
		x = len(self.pair)
		
		middle = int(x/2)
		low = 0
		high = x -1
		found = False
		b= False
		offsetArr = []
		
		for i in range (0, num_of_digits):
			offsetArr.append(math.pow(10, i))
		
		while not found:

			if number == int(self.pair[middle][0]/offsetArr[offset]):
				
				if middle >low and number == int(self.pair[middle-1][0]/offsetArr[offset]) and b == False :
					middle -=1
					
					
				else:
					
					b= True
					
					
					if self.gotUsed[self.pair[middle][1]] == False:
						found = True
						self.numberUsed +=1
						self.gotUsed[self.pair[middle][1]] = True
						return self.pair[middle][1]
					else:

						if int(self.pair[middle][0]/offsetArr[offset])  == int(self.pair[middle + 1][0]/offsetArr[offset]) and middle < high:
							middle +=1
							

						elif int(self.pair[middle][0]/offsetArr[offset]) != int(self.pair[middle + 1][0]/offsetArr[offset]) :

							return -1
			elif number > int(self.pair[middle][0]/offsetArr[offset]) and high !=low:
				
				low = middle + 1
				middle = int((high + low)/2)
			elif number < int(self.pair[middle][0]/offsetArr[offset] )and high !=low:
				
				high = middle - 1
				middle = int((high + low)/2)
			elif high == low and number != int(self.pair[middle][0]/offsetArr[offset]):

				return -1


def listToInt(arr , depth , height=0):
	a = 0
	for i in range (depth , len(arr) - height ):
		
		
		a += math.pow(10, len(arr)-i - height - 1 )*arr[i ]

	return a


class Number:
	number = []
	num_of_digits = 0
	digits = []
	permutation = []
	num_of_perms = 0
	
	nHashArray = MyPair()
	
	def quickCheck(self):

		if (self.nHashArray.numberUsed + 1) == int(self.num_of_perms/2): # Ο έλεγχος αυτός όντως δειχνει αν εχουν τοποθετηθει όλες οι μεταθέσεις γιατί:
			return True													 # πρέπει να εχουν χρησιμοποιηθεί οι μισες μεταθεσεις + 1 , αφού στη συνέχεια λόγω της συμμετρικότητας
		else:															 # του αποτελέσματος , το άλλο μισό αυτού τοποθετείται αυτόματα και αυτομάτως χρησιμοποιούνται οι αλλες μισές -1 μεταθέσεις
			return False
	def createHashArray(self, arr):
		out = []
		
		
		for j in range( 0 ,len(arr) ):
			
			out.append([listToInt(arr[j], 0,1) , j] )
			
				
		
		
			

		return out
			
	def __init__(self, num = 0):
		self.num_of_digits = num

		for X in range (1 , self.num_of_digits+1):
			self.number.append(X)
		
	permutation = []
	num_of_perms = 0


	

	def swapNumber(self):
		arr = list(itertools.permutations(self.number))

		arr2 = []
		for i in range(0, len(arr)):
			arr2.append([])
		for i in range (0 , len(arr) ):
			for j  in range (0 , len(self.number)):
				arr2[i].append(arr[i][j])


		self.permutation = arr2

		self.num_of_perms = int(math.factorial(len(self.number)) / self.factorialCalc())
		
		x = self.createHashArray(self.permutation)
		
		self.nHashArray.pair = x
		
		self.nHashArray.initializeBool()
		

		return self.permutation


					



	

	def factorialCalc(self):
		denom = 1
		for i in range(1 ,len(self.digits) , 2):
			denom *= math.factorial(self.digits[i])

		return denom

		
	
	def findNextDigits(self, arr, offset):
		
		x = self.nHashArray.binarySearch(listToInt(arr, offset ), offset - 1, self.num_of_digits)

		if x!=-1:
			o= []
			for j in range (0, offset):
				o.append(self.permutation[x][self.num_of_digits + j - offset])
			return o
		else:
			return [-1]


		
		




	


	

	def createOutput(self ):
		output = []
		strOutput = ""
		self.nHashArray.gotUsed[0]=True
		if len(output) == 0 :
			for j in range(0  , len(self.number)):
				
				strOutput += str(self.permutation[0][j])


		n  = self.num_of_perms - 1
		whole = calcLength(self.num_of_digits)
		h = int(calcLength(self.num_of_digits)/2)
		outputLength = self.num_of_digits
		
		offset = 1
		
		while outputLength!=(whole + 1):
			if outputLength <= h  :
				auxArr = []

				
				for i in range(len(strOutput) - self.num_of_digits , len(strOutput)):
					auxArr.append(int(strOutput[i]))
				
				x = self.findNextDigits(auxArr, offset)
				
				if x[0] == -1:

					offset +=1

				else:
					
					for i in range(0, len(x)):
						outputLength +=1
						strOutput += str(x[i])
						
					offset =1

					n -=1
			else:
				
				if (whole- outputLength) != h:
					
					strOutput += strOutput[whole-outputLength]
				outputLength +=1
				n-=1

			if (n%500==0):
				print("Loading" , float(self.num_of_perms - 1 - n)/float(self.num_of_perms - 1))
		
		return strOutput



	
def main():
	
	n=int(input("Enter a number "))

	number = Number(n)
	
	number.num_of_perms = int(math.factorial(n) / number.factorialCalc())
	

	
	
	number.swapNumber()
	
	
	

	
	
	
	arr = number.createOutput()

	print ("Output is ")
	print (arr)
	
	print ("It contains all permutations :",number.quickCheck())
	print ("Its length is ",len(arr))
	

main()
	
