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

def get_pref_list(filename, n):
    f = open(filename,"r")
    pref_list = [[int(num) for num in line.split()] for line in f.readlines()]
    f.close()
    pref_dict = {}
    for i,line in enumerate(pref_list):
        if i<n:
            pref_dict["m{}".format(i+1)] = line
        else:
            pref_dict["w{}".format(i-n+1)] = line
    return pref_dict
 
 
def verify(matching, pref_dict):
    for male,female in matching:
        m_prefs = pref_dict[male]
        for new_f in m_prefs[:m_prefs.index(int(female[1:]))]:
            new_f = "w"+str(new_f)
            new_f_prefs = pref_dict[new_f]
            new_fs_male = find_current(matching,new_f)
            for new_m in new_f_prefs[:new_f_prefs.index(int(new_fs_male[1:]))]:
                new_m = 'm' + str(new_m)
                if new_m == male:
                    return False
    return True
 
 
def find_current(matching,female):
    for couple in matching:
        if couple[1] == female:
            return couple[0]

if __name__ == '__main__':
    pref_dict = get_pref_list(sys.argv[1], int(sys.argv[2]))
    matchings = prep_list(int(sys.argv[2]))
    match_list = []
    for matching in matchings:
        if verify(matching, pref_dict):
            match_list.append(True)
            print(matching)
    print(len(match_list))
