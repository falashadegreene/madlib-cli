# Create function that takes in a path to text file and returns a stripped string of the files
# content
import re


def read_template(path):
    with open(path) as f:

        return f.read().strip()

# write function that takes in a template string
# returns a string with language parts removed and a separate tuple of those language parts.
def parse_template(words):
    string = ""
    lis = []
    sentence = False
    word_sentence = ""
    for x in words:
        if sentence:
            if x == "}":
                sentence = False
                lis.append(word_sentence)
                word_sentence = ""
                string += x
            else:
                word_sentence += x
        else:
            string += x
            if x == "{":
                sentence = True
    return string, tuple(lis)

# write a function that takes in a bare template list of user entered language parts
# returns a string with the language parts inserted into the template.
def merge(str, tup):
    return str.format(*tup)


if __name__ == '__main__':
    file_name = "Assets/make_me_a_video_game_output.txt"

    final, sent = parse_template(read_template(file_name))

    responses = []
    for x in sent:
        if x.lower() == "adjective":
            print(f"Enter an {x}")
            user_response = input("> ")
            responses.append(user_response)
        else:
            print(f"Enter a {x}")
            user_response = input("> ")
            responses.append(user_response)

    print(merge(final, tuple()))
