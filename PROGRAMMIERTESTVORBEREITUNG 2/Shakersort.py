
A = [9,2,7,2,4,2,9,5,1]

def shakerSort(A,beginn,ende):
    

    for i in range(beginn+1, ende):

        if A[i] > A[i+1]:
            A[i], A[i+1] = A[i+1], A[i]
            vertauscht = 1
            #ende = ende -1
            shakerSort(A,beginn,ende)

        elif A[i] < A[i+1]:
            vertauscht = 0
            #ende = ende -1
            shakerSort(A,beginn+1,ende)

            if vertauscht == 1:
                shakerSort(A,beginn+1,ende) 

            elif vertauscht == 0:
                shakerSort(A,beginn+1,ende)

        



            
    print(A)
        

beginn = -1
ende = len(A)-2

shakerSort(A, beginn, ende)
        