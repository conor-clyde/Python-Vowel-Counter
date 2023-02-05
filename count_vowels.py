#Define function for counting vowels in a piece of text
def count_vowels(msg):
    vowels = "aeiou"    #String of vowels to be compared to the text's characters
    #Dictionary for storing the amount of vowels. Seperate key for lower and upper case vowels
    vowel_dict = {"upper_case_vowels":0, "lower_case_vowels":0}
    
    for char in msg:   #Iterate through each character in the text
        if char.lower() in vowels:     #If character is a vowel
            if char.isupper():     #If character is a vowel and an upper case character
               vowel_dict["upper_case_vowels"]+=1   #Add to upper case vowel count
            elif char.islower():    #If character is a vowel and a lower case character
               vowel_dict["lower_case_vowels"]+=1    #Add to lower case vowel count
               
    #Display output to user: The text checked and information on its vowels
    print ("The following text was checked for vowels:\n", msg, "\n_________________________________")
    print ("Upper Case Vowels: ", vowel_dict["upper_case_vowels"])
    print ("Lower Case Vowels : ", vowel_dict["lower_case_vowels"])
    print ("Total Vowels: ", vowel_dict["upper_case_vowels"] + vowel_dict["lower_case_vowels"])

#The try block will catch and react to errors with file input
try:  
    #Open a stream to a text file containing the text to be checked
    #In this case: Jabberwocky.txt. A text file stored in the same directiory containing a poem
    #Stream opened in read mode (rt)
    #enocing type utf8 is used when working with text files
    stream = open("Jabberwocky.txt", "rt", encoding="utf8")

    #Read the contents of the stream and pass it through to the count_vowels function
    #Set maximum of 4000 characters to prevent reading a file with an unsafe length into memory
    count_vowels(stream.read(4000))

    #Close the stream as it is no longer needed
    stream.close()
    
#Run if file input fails. Provides feeback on why file input failed to the user
except Exception as exc:
    print("Cannot read from the file: ", exc)
