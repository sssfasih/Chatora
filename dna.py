import csv
import sys

if len(sys.argv) != 3:
    print("Usage: python dna.py data.csv sequence.txt")
    exit(1)


def main():
    csv_file = open(sys.argv[1])
    csv_reader = csv.reader(csv_file)
    headers = []
    data = []
    # for loop below takes out headers of csv file
    for row in csv_reader:
        headers = row
        break
    # after taking out headers i am zipping rest of data into dictionary
    for rows in csv_reader:
        x = zip(headers, rows)
        data.append(dict(x))

    # txt file is read
    txtfile = open(sys.argv[2])
    DNAString = txtfile.read()

    # here i am zipping 0 to headers so that i can make update this dictionary as pattern matches
    zeros = [x * 0 for x in range(len(headers))]
    dictionary = dict(zip(headers[1:], zeros[1:]))

    # Except names send each heading and iteration of DNA String to Sequence finder
    # where Sequence finder updates the dictionary after matching
    for EachHeading in headers[1:]:
        for EachCharNumber in range(0, len(DNAString)):
            if EachHeading[0] == DNAString[EachCharNumber]:
                SequenceFinder(DNAString[EachCharNumber:], EachHeading, dictionary)

    # For Each Person in Csv Data!
    # compare updated dictionary with each person.
    for EachPerson in data:
        found = Compare(dictionary, EachPerson)
        # Whenever you find any match close the program
        if found:
            return
    # if for Comparision loop ended and still not found then print no match
    # and then end the program
    if (found == False):
        print("No match")
        return


def SequenceFinder(DNASequence, Heading, dictionary):
    # print(Heading,DNASequence)
    counter = 0
    while True:
        if (len(DNASequence) - (counter * len(Heading))) < len(Heading):
            return
        for MatchNumber in range(0, len(Heading)):
            # print("DNA ",DNASequence[MatchNumber + (counter * len(Heading))])
            # print("Heading",Heading[MatchNumber])
            if DNASequence[MatchNumber + (counter * len(Heading))] == Heading[MatchNumber]:
                pass
            else:
                if dictionary[Heading] <= counter:
                    dictionary[Heading] = counter
                    return
                else:
                    return

        counter += 1


def Compare(dictionary, EachPerson):
    for i in EachPerson:
        if i == "name":
            pass
        elif dictionary[i] == int(EachPerson[i]):
            # print("Match!")
            pass
        else:
            return False
    # print(f"DNA Sequence Matches to: {EachPerson['name']}")
    print(EachPerson['name'])
    return True


main()
