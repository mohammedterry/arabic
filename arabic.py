def arabicize(words):
    transliteration = words
    for a,b in ab.items():
        transliteration = transliteration.replace(a,b)
    for phon,code in phonetic_code.items():
        words = words.replace(phon,code)
    tokens = words[:-1].split(',')
    return transliteration, ''.join([code_arabic[int(token)] for token in tokens])

phonetic_code = {
    'an ': "31,",
    'in ' : "33,",
    'un ' : "35,",
    'bba': "1,28,30,",
    'bbi': "1,28,32,",
    'bbu': "1,28,34,",
    'ba': "1,30,",
    'bi': "1,32,",
    'bu': "1,34,",
    'jja': "2,28,30,",
    'jji': "2,28,32,",
    'jju': "2,28,34,",
    'ja': "2,30,",
    'ji': "2,32,",
    'ju': "2,34,",
    'dda': "3,28,30,",
    'ddi': "3,28,32,",
    'ddu': "3,28,34,",   
    'da': "3,30,",
    'di': "3,32,",
    'du': "3,34,",
    'HHa': "4,28,30,",
    'HHi': "4,28,32,",
    'HHu': "4,28,34,",    
    'Ha': "4,30,",
    'Hi': "4,32,",
    'Hu': "4,34,",
    'hha': "37,28,30,",
    'hhi': "37,28,32,",
    'hhu': "37,28,34,",    
    'ha': "37,30,",
    'hi': "37,32,",
    'hu': "37,34,",
    'wwa': "5,28,30,",
    'wwi': "5,28,32,",
    'wwu': "5,28,34,",    
    'wa': "5,30,",
    'wi': "5,32,",
    'wu': "5,34,",
    'zza': "6,28,30,",
    'zzi': "6,28,32,",
    'zzu': "6,28,34,",
    'za': "6,30,",
    'zi': "6,32,",
    'zu': "6,34,",
    'XXa': "7,28,30,",
    'XXi': "7,28,32,",
    'XXu': "7,28,34,",    
    'Xa': "7,30,",
    'Xi': "7,32,",
    'Xu': "7,34,",
    'TTa': "8,28,30,",
    'TTi': "8,28,32,",
    'TTu': "8,28,34,",
    'Ta': "8,30,",
    'Ti': "8,32,",
    'Tu': "8,34,",
    'yya': "9,28,30,",
    'yyi': "9,28,32,",
    'yyu': "9,28,34,",
    'ya': "9,30,",
    'yi': "9,32,",
    'yu': "9,32,",
    'kka': "10,28,30,",
    'kki': "10,28,32,",
    'kku': "10,28,34,",
    'ka': "10,30,",
    'ki': "10,32,",
    'ku': "10,34,",
    'lla': "11,28,30,",
    'lli': "11,28,32,",
    'llu': "11,28,34,",
    'la': "11,30,",
    'li': "11,32,",
    'lu': "11,34,",
    'mma': "12,28,30,",
    'mmi': "12,28,32,",
    'mmu': "12,28,34,",
    'ma': "12,30,",
    'mi': "12,32,",
    'mu': "12,34,",
    'nna': "13,28,30,",
    'nni': "13,28,32,",
    'nnu': "13,28,34,",
    'na': "13,30,",
    'ni': "13,32,",
    'nu': "13,34,",
    'ssa': "14,28,30,",
    'ssi': "14,28,32,",
    'ssu': "14,28,34,",
    'sa': "14,30,",
    'si': "14,32,",
    'su': "14,34,",
    'AAa': "15,28,30,",
    'AAi': "15,28,32,",
    'AAu': "15,28,34,",
    'Aa': "15,30,",
    'Ai': "15,32,",
    'Au': "15,34,",
    'ffa': "16,28,30,",
    'ffi': "16,28,32,",
    'ffu': "16,28,34,",
    'fa': "16,30,",
    'fi': "16,32,",
    'fu': "16,34,",
    'SSa': "17,28,30,",
    'SSi': "17,28,32,",
    'SSu': "17,28,34,",
    'Sa': "17,30,",
    'Si': "17,32,",
    'Su': "17,34,",
    'qqa': "18,28,30,",
    'qqi': "18,28,32,",
    'qqu': "18,28,34,",
    'qa': "18,30,",
    'qi': "18,32,",
    'qu': "18,34,",
    'rra': "19,28,30,",
    'rri': "19,28,32,",
    'rru': "19,28,34,",
    'ra': "19,30,",
    'ri': "19,32,",
    'ru': "19,34,",
    'shsha': "20,28,30,",
    'shshi': "20,28,32,",
    'shshu': "20,28,34,",
    'sha': "20,30,",
    'shi': "20,32,",
    'shu': "20,34,",
    'tta': "21,28,30,",
    'tti': "21,28,32,",
    'ttu': "21,28,34,",
    'ta': "21,30,",
    'ti': "21,32,",
    'tu': "21,34,",
    'ththa': "22,28,30,",
    'ththi': "22,28,32,",
    'ththu': "22,28,34,",
    'tha': "22,30,",
    'thi': "22,32,",
    'thu': "22,34,",
    'khkha': "23,28,30,",
    'khkhi': "23,28,32,",
    'khkhu': "23,28,34,",
    'kha': "23,30,",
    'khi': "23,32,",
    'khu': "23,34,",
    'dhdha': "24,28,30,",
    'dhdhi': "24,28,32,",
    'dhdhu': "24,28,34,",
    'dha': "24,30,",
    'dhi': "24,32,",
    'dhu': "24,34,",
    'DDa': "25,28,30,",
    'DDi': "25,28,32,",
    'DDu': "25,28,34,",
    'Da': "25,30,",
    'Di': "25,32,",
    'Du': "25,34,",
    'DhDha': "26,28,30,",
    'DhDhi': "26,28,32,",
    'DhDhu': "26,28,34,",
    'Dha': "26,30,",
    'Dhi': "26,32,",
    'Dhu': "26,34,",
    'ghgha': "27,28,30,",
    'ghghi': "27,28,32,",
    'ghghu': "27,28,34,",
    'gha': "27,30,",
    'ghi': "27,32,",
    'ghu': "27,34,",
    'a': "0,",
    'i': "0,32,",
    'bb': "1,28,",
    'b': "1,29,",
    'jj': "2,28,",
    'j': "2,29,",
    'dd': "3,28,",    
    'd': "3,29,",
    'HH': "4,28,",    
    'H': "4,29,",
    'ww': "5,28,",
    'w': "5,29,",
    'u': "5,29,",    
    'zz': "6,28,",
    'z': "6,29,",
    'XX': "7,28,",
    'X': "7,29,",
    'TT': "8,28,",    
    'T': "8,29,",
    'yy': "9,28,",
    'y': "9,29,",
    'kk': "10,28,",
    'k': "10,29,",
    'll': "11,28,",    
    'l': "11,29,",
    'mm': "12,28,",    
    'm': "12,29,",
    'nn': "13,28,",    
    'n': "13,29,",
    'ss': "14,28,",   
    's': "14,29,",
    'AA': "15,28,",    
    'A': "15,29,",
    'ff': "16,28,",    
    'f': "16,29,",
    'SS': "17,28,",    
    'S': "17,29,",
    'qq': "18,28,",    
    'q': "18,29,",
    'rr': "19,28,",    
    'r': "19,29,",
    'shsh': "20,28,",    
    'sh': "20,29,",
    'tt': "21,28,",    
    't': "21,29,",
    'thth': "22,28,",    
    'th': "22,29,",
    'khkh': "23,28,",    
    'kh': "23,29,",
    'dhdh': "24,28,",    
    'dh': "24,29,",
    'DD': "25,28,",    
    'D': "25,29,",
    'DhDh': "26,28,",    
    'Dh': "26,29,",
    'ghgh': "27,28,",    
    'gh': "27,29,",
    ' ': "36,",
    'hh': "27,37,",
    'h': "37,",
}

code_arabic = {
    0: 'ا',
    1: 'ب',
    2: 'ج',
    3: 'د',
    4: 'ه',
    5: 'و',
    6: 'ز',
    7: 'ح',
    8: 'ط',
    9: 'ي',
    10: 'ك',
    11: 'ل',
    12: 'م',
    13: 'ن',
    14: 'س',
    15: 'ع',
    16: 'ف',
    17: 'ص',
    18: 'ق',
    19: 'ر',
    20: 'ش',
    21: 'ت',
    22: 'ث',
    23: 'خ',
    24: 'ذ',
    25: 'ض',
    26: 'ظ',
    27: 'غ',
    28: 'ّ', #shaddah
    29: 'ْ', #sukoun
    30: 'َ', #fatha
    31: 'ً', #fathatain
    32: 'ِ', #kesra
    33: 'ٍ', #kesratain
    34: 'ُ', #damma
    35: 'ٌ', #dammatain
    36: ' ',
    37: 'ة',
}

ab = {
    ' al': ' l-',
    'Hum ': '-Hum ' ,
    'Him ': '-Him ',
    'Hun ': '-Hun ',
    'Huma ': '-Huma ',
    'Hu ':'-Hu ',
    'Haa ': '-Haa ',
    'k ' : '-k ',
    'ku ': '-ku ',
    'ki ': '-ki ',
    'kum ': '-kum ',
    ' wa' : ' wa-',
    'aa': 'ā',
    'uu': 'ū',
    'ii': 'ī',
    'lll': 'll',
    'X': 'ḥ',
    'H':'h',
    'T': 'ṭ',
    'A': "'a",
    'S': 'ṣ',
    'D': 'ḍ',
    'gh':'ġ',
}
a = ' alsalaamu Aalaykum waraXmahu alllaHi wabarakaatuHu wamaghfiratuHu '
b,c = arabicize(a)
print(a)
print(b)
print(c)

a = ' laa ilaHa illaa alllaHa muXammadun rasuulu alllaH '
b,c = arabicize(a)
print(a)
print(b)
print(c)