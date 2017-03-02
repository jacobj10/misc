import itertools
import sys

def prep_list(n):
    men = []
    women = []
    for i in range(n):
        men.append('m' + str(i + 1))
        women.append('w' + str(i + 1))
    zipped = [list(zip(x,women))[:] for x in itertools.permutations(men,len(women))]
    return zipped

if __name__ == '__main__':
    print(prep_list(int(sys.argv[1])))
