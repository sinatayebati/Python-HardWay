import sys
script, input_encoding, error = sys.argv

def main(languages_file, encoding, errors):
    line = languages_file.readline()
    if line:
        print_line(line, encoding,errors)
        return main(language_file, encoding, error)
    
def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", encoding="utf-8")

languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)
    