from utils_ceb import CEBApi
from utils_my import MyAPI
from utils_pg19 import PG19Api


############################################
# Extract Information about Speakers.
############################################
def get_book_id(v):
    return v.split('_')[0]

# 126_2 The Poison Belt by Arthur Conan Doyle ['Lord John', 'Lord John Roxton'] UNK


# 507_9. Bartle Massey -- The schoolteacher and Adam’s best friend. Unbeknownst to his friends, not only does Mr. Massey care deeply for his students, but he exhibits a patience with them that he seldom shows in the company of friends. Mr. Massey rails against the stupidity of women and says everything twice. During Hetty’s trial, he is a tactful comfort to Adam because he is able to see when it is best not to speak.I
# 139_1 The Lost World by Arthur Conan Doyle ['Summerlee', 'Mr. Summerlee', 'SUMMERLEE'] UNK https://arthurconandoyle.co.uk/character/professor-summerlee-from-the-professor-challenger-stories
# 1257_9 The Three Musketeers by Alexandre Dumas Pere ['Buckingham', 'Duke', 'Lord Duke', 'Lord Buckingham', 'Duke of Buckingham'] https://heroes-and-villain.fandom.com/wiki/Duke_of_Buckingham_(2011)
# 155_21 The Moonstone by Wilkie Collins ['Sergeant', 'Mr. Cuff', 'Sergeant Cuff'] UNK https://www.litcharts.com/lit/the-moonstone/characters/sergeant-cuff#:~:text=A%20%E2%80%9Crenowned%20and%20capable%E2%80%9D%20detective,%2C%20Franklin%20Blake%2C%20and%20Mr.
# 507_3 Soldiers of Fortune by Richard Harding Davis ['MacWilliams', 'Mr. MacWilliams'] https://www.theatlantic.com/magazine/archive/1897/12/mr-daviss-soldiers-of-fortune/636194/

predefined_speakers = [#'763_3', #'547_3',
                       #'538_2',
                       '507_3',
                       '457_4', '433_6', '429_0', '394_0',
                       '369_0', '367_0', '335_3', '330_0', '298_5', '296_0', '283_2', '268_3',
                       '233_2', '203_2', '179_7', '155_21', '1380_0', '1282_3', '126_2', '1259_7',
                       '1259_29', '1257_9', '1257_7', '1235_2', '122_2', '1207_0', '1204_1',
                       '1024_9', '98_2', '960_1', '763_1', '720_0', '604_2', '547_1', '51_2',
                       '507_9', '498_1', '479_1', '457_6', '450_4', '403_5', '403_3', '401_1',
                       '297_0', '293_2', '270_1', '210_2', '203_10', '154_6', '139_1', '135_6',
                       '1327_1', '1294_3', '1283_1', '1282_2', '1259_13', '1258_8', '1223_0', '1188_0', '1056_1',
                       '938_2', '905_0', '903_6', '780_0', '764_7', '72_0', '716_1', '599_1', '599_0', '482_1',
                       '47_1', '479_0', '460_0', '42_2', '403_1', '388_0', '361_1', '335_0', '296_1', '284_0',
                       '153_2', '152_0', '144_4', '144_21', '1380_1', '1363_2', '1348_2', '1343_2', '1314_3',
                       '1303_16', '1299_0', '1284_1', '125_4', '1258_5', '1242_0', '1237_4']

ceb_api = CEBApi()
ceb_api.read_char_map()
pg19 = PG19Api()
pg19.read()
roles = ceb_api.get_meta_role()
for s in predefined_speakers:
    book_id = get_book_id(s)
    if int(book_id) in pg19.book_ids():
        title = pg19.find_book_title(book_id)
        print(s, title, ceb_api.get_char_names(s), roles[s] if s in roles else "UNK")


