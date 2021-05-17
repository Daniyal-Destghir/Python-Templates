

#WARNING: WHEN WRITING THESE TEXTS I ALWAYS STARTED WITH "#" by doing these it means that python will not read this, so when adding code, Please dont add "#".


#Creating a Mab Lib is easy 
#But I am going to make it even more easy for you!
#With no coding Skilles required!

#First, We need to ask the questions, Here is an example:
# Q1 = input("What is your favorite flower")

#Now, Listen carefully, Q1 = to your questions name, what inside the quotation marks (Where "What is your favorite color")
#That is the question.

#Now, we need to add the questions
#To do so, here is the command:
# print(Q1)

#Now, print is a statement in python used for printing something or displaying something. now in the brackets we have Q1, because that is the name of the Question. So It will print the question.
#But what if you want to add some TEXT.
#To do so, here is the command:
#print(Q1 + " is his favorite flower")

#Now, when adding the questions and and alphabets we use "+". And we should also add "" WHENEVER WE ARE WRITING ALPHABETS (NOT NUMBERS)
#Also notice that after the "" I put a space, This is because python will add them together. But we dont want that, cause they are different words.
#There is also a second way:
# Answer = f"{Q1} is his favorite flower" 
# print(Answer)

#Now, let me first explain what the f means. Inside these types of brackets ({}), you can write the name of the question. And then write everything normally!
#Then, the thing "Answer" is something were we can store this data. It can be anything, and then we have to print this DATA by using the print command. Now, please remember when you are printing these variables, (The piece of data) dont add quotes ("")

#And that is pretty much it!

#Here is an example you can use to make your own Mab Libs
#Keys:
#{custom}: Meaning you can customize the text init

#code:
# {custom} = input("{custom}")
#print({custom} + "{custom}")

#Now here is something I made:


Q1 = input("what is your name: ")
Q2 = input("What is your age: ")

Answer = f"Hello, I am {Q1}, And I am {Q2} years old!"
print(Answer)

#Now that you now how to make your own mab lib, delete all of the text in this file and Start fresh!