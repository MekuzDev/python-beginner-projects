sample_text = input('Enter sample Text here:\n').lower()
program_ended = False
while not program_ended:
    if(len(sample_text) < 6):
        print('Please enter an actual sentence')
        sample_text = input('Enter sample Text here:\n').lower()
    else:
        word_to_be_replaced = input("word to be replaced:\n").lower()
        to_replaced_with = input('To be replaced with: \n').lower()
        if not word_to_be_replaced in sample_text:
            print("Word not found in text")


        elif word_to_be_replaced in sample_text:
            new_text = sample_text.replace(word_to_be_replaced,to_replaced_with)
            sample_text  = new_text
            print(sample_text.capitalize())
        choice_to_quit = input('You wish to quit program (Y or N) ?\n ')

        if choice_to_quit == 'Y' or choice_to_quit == 'y':
            print('Ok Bye, see ya later!')
            program_ended = True

        elif choice_to_quit == 'N' or choice_to_quit == 'n':
             print('Ok nice') 
               
        else:
            print('Invalid Input: Program ended due to error')
            program_ended = True



