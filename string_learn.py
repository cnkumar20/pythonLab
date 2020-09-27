test_string = ["This is kumar","and his friends","where are you" ,"a tale for the century","and many more to come"]
for x in test_string:
    print(x)



def find_string(search_string):
    result = [s for s in test_string if search_string in s]
    print(result)

def find_string_pos(search_string):
    result = [s.find(search_string) for s in test_string]
    print(result)

def main():
    find_string("and")
    find_string_pos("*")
    find_string_pos("and")
if __name__ == '__main__':
    main()