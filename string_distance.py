def osa_distance(string1, string2, ignore_case=False, return_matrix=False):
    """Returns levenstein distance between the strings"""
    if ignore_case:
        string1 = string1.lower()
        string2 = string2.lower()

    distance_map = [[max(x, y) for x in range(len(string1)+1)]
                    for y in range(len(string2)+1)]
    for i in range(1, len(distance_map[0])):
        for j in range(1, len(distance_map)):
            cost = 1
            if string1[i-1] == string2[j-1]:
                cost = 0
            distance_map[j][i] = min(
                distance_map[j-1][i]+1, distance_map[j][i-1]+1, distance_map[j-1][i-1]+cost)
            if string1[i-1] == string2[j-2] and string1[i-2] == string2[j-1]:
                distance_map[j][i] = min(
                    distance_map[j][i], distance_map[j-2][i-2]+cost)
    if return_matrix:
        return distance_map
    else:
        return distance_map[-1][-1]


def most_freq_k_distance(string1, string2, k=None, max_distance=None):
    if max_distance is None:
        max_distance = max(len(string1), len(string2))*2

    if k is None:
        k = min(len(string1), len(string2))
    freq_list1 = list(set((string1.count(char_), char_) for char_ in string1))
    freq_list1.sort(key=lambda x: x[0], reverse=True)
    freq_list2 = list(set((string2.count(char_), char_) for char_ in string2))
    freq_list2.sort(key=lambda x: x[0], reverse=True)
    return max_distance - sum(i[0]+j[0] for i in freq_list1[:k] for j in freq_list2[:k] if i[1] == j[1])


for i in range(1000):
    pass
