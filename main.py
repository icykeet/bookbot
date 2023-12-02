def main():
        book_path = "books/frankenstein.txt"
        text = get_book_text(book_path)
        num_words = get_words_num(text)
        chars_dic = get_chars_dic(text)
        chars_sorted_list = get_sorted_list(chars_dic)

        print(f"-- Begin report of {book_path} --")
        print(f"{num_words} words found on the document")
        print()

        for item in chars_sorted_list:
                if not item["char"].isalpha():
                        continue
                print(f"The '{item['char']}' character was found {item['num']} times")
        
        print("-- End of report --")
        
def get_book_text(file_path):
        with open(file_path) as f:
                return f.read()

def get_words_num(text):
        words = text.split()
        return len(words)

def get_chars_dic(text):
        chars = {}
        for c in text:
                lowered = c.lower()
                if lowered in chars:
                        chars[lowered] += 1
                else:
                        chars[lowered] = 1
        return chars
def sort_on(item):
        return item["num"]

def get_sorted_list(dict):
        sorted_list = []
        for ch in dict:
              sorted_list.append({"char": ch, "num": dict[ch]})
        sorted_list.sort(reverse = True, key=sort_on)
        return sorted_list

main()