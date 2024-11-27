import re 

pattern ="[A-Z]merica"

text = '''
 American singer-songwriter. With Debbi Peterson and Vicki Peterson, she founded the Bangles in 1981. Their second album, Different Light (1986), was warmly received by critics and was certified triple-platinum in 1994. The group's third album, Everything (1988), included the US-top-ten-charting "In Your Room" and number-one "Eternal Flame", both written by Hoffs with Billy Steinberg and Tom Kelly. Following tensions including resentment at Hoffs's perceived leadership of the band and the stress of touring, the band split in 1989, reforming in 1999. Hoffs's first solo album, When You're a Boy (1991), was followed by Susanna Hoffs (1996). Neither of the releases proved to be as popular as the Bangles's albums, although they yielded two US-charting singles. Her most recent solo album is The Deep End (2023), and her first novel, This Bird Has Flown, a romantic comedy about a struggling musician, was published in the same year. (Full article...)


'''
matches = re.finditer(pattern , text)

for match in matches:
    print(match)