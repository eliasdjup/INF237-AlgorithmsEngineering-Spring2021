# From lecture 12 - Strings
def longest_prefix_suffix(pattern):
    n, k = 0, len(pattern)
    lps = [0] * k
    idx = 1
    while idx < k:
        if pattern[idx] == pattern[n]:
            n += 1
            lps[idx] = n
            idx += 1
        else:
            if n != 0:
                n = lps[n - 1]
            else:
                lps[idx] = 0
                idx += 1
    return lps

def kmp(text, pattern, lps):
    n, k = len(text), len(pattern)
    txt_idx, pat_idx = 0, 0
    while txt_idx < n:
        if pattern[pat_idx] == text[txt_idx]:
            txt_idx += 1 # currently matching
            pat_idx += 1
        if pat_idx == k:
            yield txt_idx - k # end of pattern, success!
            pat_idx = lps[pat_idx - 1]
        elif txt_idx < n and pattern[pat_idx] != text[txt_idx]:
            if pat_idx != 0: # mismatch, jump to lps[i] in pat
                pat_idx = lps[pat_idx - 1]
            else:
                txt_idx += 1 


n = int(input())
c1 = sorted([int(x) for x in input().split()])
c2 = sorted([int(x) for x in input().split()])

c1_angles = []
c2_angles = []

for i in range(n-1):
    c1_angles.append(c1[i+1] - c1[i])
    c2_angles.append(c2[i+1] - c2[i])

c1_angles.append((360000-c1[n-1])+c1[0])
c2_angles.append((360000-c2[n-1])+c2[0])

res = list(kmp(c1_angles+c1_angles, c2_angles, longest_prefix_suffix(c2_angles)))

if res == []:
    print("impossible")
else:
    print("possible")