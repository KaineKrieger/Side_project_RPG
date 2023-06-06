import text_blocks


def get_answer(question):
        answer = str(input(question))
        return answer

def exposite(text: tuple):
    for paragraph in text:
        if paragraph != text[-1]:
            input(paragraph +"...")
        else:
            input(paragraph)

def initial_pathway(path):
    if path == "start":
        text = text_blocks.introduction
        question = initial_choice
        exposite(text)
        path = get_answer(question)

        if path == "1":
            print(text_blocks.path_1)
        if path == 2:
            print(text_blocks.path_2)

        if path == 3:
            print(text_blocks.path_3)

        if path == 4:
            print(text_blocks.path_4)

        if path == 5:
            print(text_blocks.path_5)

    else:
        print("error, please restart code.")


if __name__ == "__main__":
    path = "start"
    introduction = text_blocks.introduction
    initial_choice = text_blocks.initial_choice
    answer = 1
    initial_pathway(path)



