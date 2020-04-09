import phonenumbers

from sys import argv

def format(text):
    diff = 0
    for match in phonenumbers.PhoneNumberMatcher(text, 'RU'):
        num = match.number
        num.country_code = 1
        formatted = phonenumbers.format_number(num, 1)
        text = text[:match.start + diff] + formatted + text[match.end + diff:]
        diff += len(formatted) - len(match.raw_string)
    return text
    
if __name__ == '__main__':
    with open(argv[-1], 'r') as f:
        print(format(f.read()))
