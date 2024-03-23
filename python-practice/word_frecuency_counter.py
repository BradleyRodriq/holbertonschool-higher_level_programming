#!/usr/bin/python3

def word_frecuency_counter(string):
    freq_dict = {}
    words = string.split()

    for word in words:
        cleaned_word = ''.join(filter(str.isalnum, word)).lower()
        if cleaned_word in freq_dict:
            freq_dict[cleaned_word] += 1
        else:
            freq_dict[cleaned_word] = 1
    return freq_dict


ex_str = "This is a sample string, sample string example."
print(word_frecuency_counter(ex_str))
