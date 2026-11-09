#maximium number of rules applied to reach result
MAX_ITERATIONS = 6

#returns [new_string, solution_sequence]
def expand_node(my_string, iteration_num, goal_string, solution_sequence):
    
    print(my_string)

    if my_string == goal_string:
        solution_sequence.append(my_string)
        return my_string, solution_sequence

    if iteration_num == MAX_ITERATIONS:
        return my_string, solution_sequence
    
    my_string_length = len(my_string)
    #applies rule 1 (if last item is I, adds U)
    new_string = []
    if my_string[-1] == "I":
        new_string = my_string.copy()
        new_string.append("U")
        new_string, solution_sequence = expand_node(new_string, iteration_num+1, goal_string, solution_sequence)
        if new_string == goal_string:
            solution_sequence.append(my_string)
            return new_string, solution_sequence

    #applies rule 2 (doubles any size string after M)
    for i in range(1, my_string_length-1):
        new_string = ["M"] + my_string[1:i+1] + my_string[1:1+1]
        if i != my_string_length-1:
            new_string += my_string[i+1:]
        new_string, solution_sequence = expand_node(new_string, iteration_num+1, goal_string, solution_sequence)
        if new_string == goal_string:
            solution_sequence.append(my_string)
            return new_string, solution_sequence

    #applies rule 3 (if III, converts to U)
    if my_string_length>=4:
        for i in range(3, my_string_length-1, 1):
            if my_string[i]=="I" and my_string[i-1]=="I" and my_string[i-2]=="I":
                new_string = my_string[0:i-2]+["U"]
                if i!=my_string_length-1:
                    new_string += my_string[i+1:]
                    new_string, solution_sequence = expand_node(new_string, iteration_num+1, goal_string, solution_sequence)
                    if new_string == goal_string:
                        solution_sequence.append(my_string)
                        return new_string, solution_sequence

    #applies rule 4 (if UU, removes)
    if my_string_length >=3:
        for i in range(2, my_string_length-1, 1):
            if my_string[i]=="U" and my_string[i-1]=="U":
                new_string = my_string[0:i-1]
                if i!=my_string_length-1:
                    new_string += my_string[i+1:]
                    new_string, solution_sequence = expand_node(new_string, iteration_num+1, goal_string, solution_sequence)
                    if new_string == goal_string:
                        solution_sequence.append(my_string)
                        return new_string, solution_sequence

    return my_string, solution_sequence

my_string, solution_sequence = expand_node(["M","I"], 0, ["M","U"],[])

solution_sequence.reverse()
print(solution_sequence)