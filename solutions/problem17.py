NAMES = {
    0 : '', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
    6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
    11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
    15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
    19 : 'nineteen', 20 : 'twenty',
    30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty',
    70 : 'seventy', 80 : 'eighty', 90 : 'ninety', 100: 'hundred' 
}

def spell_number(n):
    if n < 21:
        return NAMES[n]
    if n < 100:
        if n % 10 == 0:
            return NAMES[n]
        return NAMES[n // 10 * 10] + '-' + spell_number(n % 10)
    if n % 100 == 0:
        return NAMES[n // 100] + ' ' + NAMES[100]
    return NAMES[n // 100] + ' ' + NAMES[100] + ' and ' + spell_number(n % 100) 
    
        
sum = 0
for i in range(1, 1000):
    print(len(spell_number(i).replace(' ', '').replace('-', '')), spell_number(i))
    sum = sum + len(spell_number(i).replace(' ', '').replace('-', ''))

print(sum)

