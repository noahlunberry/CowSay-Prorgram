import sys
from heifer_generator import HeiferGenerator


def list_cows(cows):
    #list out the cows abvaioalbel on the smae lines
    print("Cows available:", end=' ')
    for cow in cows:
        print(cow.get_name(), end=' ')


def find_cow(name, cows):
    #iterate through cows and each time looking at one cow
        #if the name of the cow we are looking at is eqal to name
            #return cow
    #return None to indicate we couldnt find the name in cows
    for cow in cows:
        if cow.get_name() == name:
            return cow
    return None


if __name__ == '__main__':
    cows = HeiferGenerator.get_cows()
    #if sys.argv[1] == '-l':
    if sys.argv[1] == '-l':
        # call list_cows(cows)
        list_cows(cows)
    #elif sys.arv[1] == '-n':
    elif sys.argv[1] == '-n':
        #print the messege starting from sys.argv[3]
        message = ' '.join(sys.argv[3:])
        #call cow = find_cow(sys.argv[2], cows]
        cow = find_cow(sys.argv[2], cows)
        if cow:
            # print the cow.image
            print(message)
            print(cow.get_image())
        else:
            print(f'Could not find {sys.argv[2]} cow!')
    else:
        message = ' '.join(sys.argv[1:])
        cow = find_cow("heifer", cows)  # Default to 'heifer' cow
        if cow:
            print(message)
            print(cow.get_image())

