import csv
import random
#the function creates random combinations of letters 'A', 'G', 'C', 'T'
#then write the values as a tests.csv file
def selfCombine( list2Combine, length ):
    listCombined = str( ['list2Combine[i' + str( i ) + ']' for i in range( length )] ).replace( "'", '' ) \
                     + 'for i0 in range(len( list2Combine ) )'
    if length > 1:
        listCombined += str( [' for i' + str( i ) + ' in range( i' + str( i - 1 ) + ', len( list2Combine ) )' for i in range( 1, length )] )\
            .replace( "', '", ' ' )\
            .replace( "['", '' )\
            .replace( "']", '' )

    listCombined = '[' + listCombined + ']'
    listCombined = eval( listCombined )

    return listCombined

list2Combine = ['A', 'G', 'C', 'T']
#list2Combine = "A, G, C, T" 
listCombined = selfCombine( list2Combine, 4 )
random.shuffle(listCombined,random.random)

with open('n.csv', 'w') as csvfile:
    wr = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    wr.writerow(listCombined)
