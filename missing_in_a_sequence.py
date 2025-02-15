
def find_missing(seq):
    for i in range(1,len(seq)+1):
        if i not in seq:
            return i
    return "nun"

sequence=list(map(int,input("Enter the sequence of numbers separated by spaces: ").split()))
missing_numbers=find_missing(sequence)
print(missing_numbers)