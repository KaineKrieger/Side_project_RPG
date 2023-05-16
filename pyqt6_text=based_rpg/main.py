import text_blocks


# just gunna do a lot of psudo code for now to shape it

path = "start"
introduction = text_blocks.introduction
initial_choice = text_blocks.initial_choice
answer = 1

def menu_basics(event, question):
    print(event)
    return answer == int(input(question))

if __name__ == "__main__":

    if path == "start":
        event = introduction
        question = initial_choice
        path == menu_basics(event, question)

        if path == 1:
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



