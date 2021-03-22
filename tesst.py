import re
def compare(file1, file2):
    pattern = r'\w+'
    with open(file1) as f1:
        words1 = []
        for line in f1:
            ans = re.findall(pattern, line)
            words1.extend(ans)
    with open(file2) as f2:
        words2 = []
        for line in f2:
            ans = re.findall(pattern, line)
            words2.extend(ans)
    print(set(words1).intersection(words2))
compare("unit6_testinput_02.txt","unit6_testinput_03.txt")