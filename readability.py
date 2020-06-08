import cs50

text = cs50.get_string("Text: ")
alphabets = 0
words = 0
sentences = 0
for eachletter in text:
    if eachletter.isalpha():
        # print(f"Alphabet: {eachletter}")
        alphabets += 1
    elif eachletter == " ":
        # print("WhiteSpace",eachletter,"<-")
        words += 1
    elif eachletter in ".!?":
        sentences += 1
        # print("Sentence ends here")
L = (alphabets / (words + 1)) * 100
S = (sentences / (words + 1)) * 100
grade = int(round(0.0588 * L - 0.296 * S - 15.8))
if (grade >= 16):
    print("Grade 16+");
elif (grade < 1):

    print("Grade Before Grade 1");

else:
    print("Grade {0}".format(grade));
