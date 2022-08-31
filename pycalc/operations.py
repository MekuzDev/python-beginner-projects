def addition():
    total = 0
    sum_list = []
    num_len = int(input("Enter number of inputs required:\n"))
    for i in range(0,int(num_len)):
        figures =int(input(f"Enter value for number {i + 1}:\n"))
        total+=figures
        sum_list.append(str(figures))
    sum_text = ' + '.join(sum_list)
    print(f"{sum_text} = {total}")


def subtraction():
    subtraction_list = []
    new_sub_list = []
    num_len = int(input("Enter number of inputs required:\n"))#
    for i in range(0,int(num_len)):
        figures = int(input(f"Enter value for number {i + 1}:\n"))
        subtraction_list.append(figures)
        new_sub_list.append(str(figures))
    total = subtraction_list[0]
    for j in range(1,len(subtraction_list)):
        total -= subtraction_list[j]
    addon_text = ' - '.join(new_sub_list)
    print(f"{addon_text} = {total}")


        
        