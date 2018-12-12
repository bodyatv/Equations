def minor_calc(matrix): # matrix = [['1','2','3'],[...],[...]]
    if len(matrix) == 1:
        return float(matrix[0])
    if len(matrix) == 2:
        return float(matrix[0][0])*float(matrix[1][1])-float(matrix[0][1])*float(matrix[1][0])
    result=0
    k=2
    for index in  range(len(matrix[0])):
        element=matrix[0][index]
        new_minor=[]
        for str_list in matrix[1:]:
            new_minor.append(str_list[:index]+str_list[index+1:])
        result+=pow(-1,k)*float(element)*minor_calc(new_minor)
        k+=1
    return result

def print_space(num_list):
        print(' '.join(list(map(str,num_list))))
def convert_matrix(matrix):
    new_matrix=[]
    for string in matrix:
        new_matrix.append(string.split(","))
    return new_matrix

def convert_matrix_to_nums(matrix):
    matrix=convert_matrix(matrix)
    new_matrix=[]
    for str in matrix:
        new_matrix.append(list(map(float,str)))
    return new_matrix

def matrix_has_0str(matrix):
    counter=0
    for index in range(len(matrix)):
        if matrix[index].count(0)==len(matrix[index]):
            counter+=1
    return counter

def swap_matrix_non_zero_strings(matrix,step):
    for index in range(len(matrix)):
        if index<=step: #<=
            continue
        else:
            if matrix[index][step]!=0:
                matrix[index],matrix[step]=matrix[step],matrix[index]
                return matrix
        return matrix

def rank_check(i, matrix,augmented,diagonalized):
    if augmented:
        i+=1
    step=0
    while(step<i-1):
        if matrix[step][step]!=0:
            matrix[step]=[x/matrix[step][step] for x in matrix[step]]
            for index in range(len(matrix)):
                if index<=step:
                    pass
                else:
                    first_el=matrix[index][step]
                    matrix[index]=[a-b for a,b in zip(matrix[index],[x*first_el for x in matrix[step]])]
            #step+=matrix_has_0str(matrix)
            step+=1
        else:
            if matrix==swap_matrix_non_zero_strings(matrix,step):
                matrix=swap_matrix_non_zero_strings(matrix,step)
            else:
                step+=1
    #print(matrix)
    if diagonalized:
        return matrix
    elif augmented:
        return i-1-matrix_has_0str(matrix)
    else:
        return i-matrix_has_0str(matrix)

def cron_kapelli(i,matrix_augmented,matrix_coefficient):
   if rank_check(i,matrix_augmented,True,False)==rank_check(i,matrix_coefficient,False,False):
       return True
   else:
       return False

def unique_solution(i,matrix_coefficient):
    if matrix_has_0str(matrix_coefficient):
        return False
    else:
        return True

def solve_of_diag_matrix(i,matrix_augmented_diagonalized):
    solution=[0 for x in range(i)]
    solution.append(1)
    x=-2
    for string in reversed(matrix_augmented_diagonalized):
        #print(string,"   --- string")
        solution_temp=[a*b for a,b in zip(string,solution)]
        #print(solution_temp,"        --- sol temp")
        #print(sum(solution_temp[:-1]),"     --- sum")
        solution[x]=solution_temp[-1]-sum(solution_temp[:4])
        solution_temp=solution
        #print(solution,"      --- solution")
        x-=1
    solution=solution[:-1]
    print_space(solution)










def equations_solver(i, *num_strings):
        matrix_augmented = []
        matrix_coefficient=[]
        for strings in num_strings:
            matrix_augmented.append(strings)
            matrix_coefficient.append(strings.rsplit(',', 1)[0])

        matrix_coefficient=convert_matrix_to_nums(matrix_coefficient)
        matrix_augmented=convert_matrix_to_nums(matrix_augmented)

        if cron_kapelli(i,matrix_augmented,matrix_coefficient):
            matrix_coefficient_diagonalized=rank_check(i,matrix_coefficient,False,True)
            if unique_solution(i,matrix_coefficient_diagonalized):
                matrix_augmented_diagonalized=rank_check(i,matrix_augmented,True,True)
                solve_of_diag_matrix(i,matrix_augmented_diagonalized)
            else:
                print("Infinite solutions")
        else:
            print(-1)









equations_solver(5,'1,0,0,0,0,0','1,0,-1,1,0,0','1,-2,1,1,1,1','0,1,1,1,1,3','0,1,-1,0,1,-2')
