import re

'''


Sort results by numeric value?

Iterate over results
    Write to file

Close files
'''
# Open file for reading
fp = open("/Users/trip/Coding/TextMining/Bozovic-Rosenkranz-S15/"
          "dhrees-scraping/blok_sobranie_sochineny_v_8-mi_tt_tom1_1960__ocr-index.txt")
# Create regex pattern to find all numbers
patt = re.compile("\d+")
# Execute regex into variable
numbers = patt.findall(fp.read())
# close original file
fp.close()

if numbers:
    print 'Matches found: ', len(numbers)
else:
    print 'No matches'


'''
NEXT:
Use scraped numbers tuple to read through main file after page line by line, writing each line to output file
closing output file if page number of page break line matches number in the numbers tuple
'''

# Using OCRed Blok
late_title = False
v = 0
title = ""
with open("/Users/trip/Coding/TextMining/Bozovic-Rosenkranz-S15/"
          "dhrees-scraping/blok_sobranie_sochineny_v_8-mi_tt_tom1_1960__ocr.txt") as blokfile:
    for line in blokfile:
        # if line is blank, skip it
        if line in ['\n', '\r\n']:
            continue

        # how do we get the title?
        # if late_title = False and we've emptied out the title variable
        if late_title is False and title == "":  # NB: This will be True for the first line of the file
            pass
        # if late_title = True use this line as title
        if late_title is True:
            title = line
            # open output file for this poem
            poem_file = open(("/Users/trip/Coding/TextMining/Bozovic-Rosenkranz-S15/"
                             "dhrees-scraping/%s.txt", title), "w")
            late_title = False
            title = ""
        # if the poem uses asterisks for the title line
        if line.find("**") > -1:
            late_title = True
            continue


        # if the line is a page break
        # get the page number
        # test if the number is in our index tuple

        print(line.strip("\n"))


        # if the line is a page break, test if it's a number from the index, then close output file


        # test if we have open file for poem
        # if yes
        #   do nothing
        # if no
        #   open new file for writing
        if v == 40:
            break
        v += 1


# Open file for writing poem
fp = open("/Users/trip/Coding/TextMining/Bozovic-Rosenkranz-S15/dhrees-scraping/number-list.txt", "w")
#fp.write(numbers[])
fp.close()
