import re

'''


Sort results by numeric value?

Iterate over results
    Write to file

Close files
'''
# Open file for reading
fp = open("/Users/trip/Coding/TextMining/Bozovic-Rosenkranz-S15/dhrees-scraping/blok_sobranie_sochineny_v_8-mi_tt_tom1_1960__ocr-index.txt")
# Create regex pattern to find all numbers
patt = re.compile("\d*")
# Execute regex into variable
numbers = patt.match(fp.read)
# Open file for writing
fp = open("/Users/trip/Coding/TextMining/Bozovic-Rosenkranz-S15/dhrees-scraping/number-list.txt", "w")