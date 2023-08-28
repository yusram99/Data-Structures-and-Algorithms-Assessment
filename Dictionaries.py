# Question 3: Implement a function word_frequency(sentence) that takes 
# a sentence and returns a dictionary containing the frequency of each 
# word in the sentence. 

# Ignore punctuation and consider words in a case-insensitive manner. 

# sample input = 

# sentence = "This is a test sentence. This sentence is a test."
# result = word_frequency(sentence)
# print(result)

def word_frequency(sentence):
     # Remove punctuation and convert to lower case
    sentence = ''.join(ch for ch in sentence if ch.isalnum() or ch.isspace()).lower()
    
    # Split the sentence into words
    words = sentence.split()
    
    # Dictionary to hold the frequency of each word
    frequency_dict = {}
    
    # Count the frequency of each word
    for word in words:
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1
    
    return frequency_dict

# Tests
sampleinput = []
sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)