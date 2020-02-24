PATSK = ['ā', 'ē', 'ī', 'o', 'ū', 'a', 'e', 'i', 'o', 'u']
DIVSKANI = ['ai', 'au', 'ie', 'ei', 'ui', 'iu', 'oi', 'eu', 'ou']

def convert_beens(txt):
    output = ""
    zilbe = ""
    index = 0
    while index < len(txt):
        zilbe = txt[index] + txt[index + 1] if index < len(txt)-1 else txt[index]
        if any(txt[index] in s for s in PATSK):
            if any(zilbe in s for s in DIVSKANI):
                output += zilbe + "p" + zilbe
                index += 1
            else: 
                output += txt[index] + "p" + txt[index]
        else:
            output += txt[index]
        index += 1
    return output

