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
patt = re.compile("\d*")
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
Use scraped numbers tuple to read through main file line by line, writing each line to output file
closing output file if page number of page break line matches number in the numbers tuple
'''

# Open file for writing
fp = open("/Users/trip/Coding/TextMining/Bozovic-Rosenkranz-S15/dhrees-scraping/number-list.txt", "w")
fp.write(numbers)
fp.close()
