"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": ['ACGGCATAACCCTCGA', 3],
            "answer": "ACGCCCTAATCGGCA"},
        {
            "input": ['ACGTTGCAACGTAGCT', 4],
            "answer": "ACGTACGTAGCTTGCA"},
        {
            "input": ['CGTAGCA', 1],
            "answer": "CGTAGCA"},
        {
            "input": ['GCTACGG', 7],
            "answer": "GCTACGG"},
        {
            "input": ['GGGCCCTTTAAA', 4],
            "answer": "CCTTGGGCTAAA"},
        {
            "input": ['GCATCTAGCAGCATGCATCGTAGCATCGATCTAGTCAGATCGATGTATAGGCCGCG', 10],
            "answer": "CGATGTATAGGCATGCATCGTAGCATCGATCTAGTCAGATGCATCTAGCA"},
        {
            "input": ['A', 1],
            "answer": "A"},
        {
            "input": ['GGGGGGGGGGG', 2],
            "answer": "GGGGGGGGGG"},
    ],
    "Extra": [
        {
            "input": ['AAAGATCTGATTGCATAGGAAGCATGCCATCATACGACCCTGCCGGAAGTTACCGGTGGGACGTGACCTTCAACGGTTTGTGTTTCCGC', 46],
            "answer": "AAAGATCTGATTGCATAGGAAGCATGCCATCATACGACCCTGCCGG"},
        {
            "input": ['CGCACTGCCCGCGCGTTATTGCTATGAAGCTAGTGGTCGCCGCCCGCGCTTGGGTTGGATAGTTCATACCCCGGAC', 18],
            "answer": "TCGCCGCCCGCGCTTGGGCGCACTGCCCGCGCGTTATTGCTATGAAGCTAGTGGTTGGATAGTTCATACCCC"},
        {
            "input": ['CGGGCAGGCATTCTTAACGCATTTCAAGCAGCGACTTG', 4],
            "answer": "CGGGATTTCAGGCATTACGCCAAGCAGCGACTCTTA"},
        {
            "input": ['AGACAGACGAGGACCCGTCCAGGGATGGCAAAAGTTCCTCTACGGTCTCGATACCATTAGTTATACGGAGTAT', 1],
            "answer": "AGACAGACGAGGACCCGTCCAGGGATGGCAAAAGTTCCTCTACGGTCTCGATACCATTAGTTATACGGAGTAT"},
        {
            "input": ['GCTCTAGGATCCCGCGCGTTGGAGTCTCCTCCAAATGGGGCACACGGGACACTGCTTCTGA', 12],
            "answer": "ACACTGCTTCTGCGCGCGTTGGAGGGGGCACACGGGGCTCTAGGATCCTCTCCTCCAAAT"},
        {
            "input": ['TAACATGTACGTGCCTCTTTTAGCCTTTACGCTAGATTGCTACATAAGTGCGCAAAACTCGGATGGAGTCTCTA', 13],
            "answer": "CAAAACTCGGATGTAACATGTACGTGCCTCTTTTAGCCTCTACATAAGTGCGTTACGCTAGATTG"},
        {
            "input": ['TTGTGCGCGGTAAAGAACATTTTATCGAGATCTGCCACCGTTGACCCGGCTATTATCGTGATCTCCGGCGGGACACACCAGCTAATCAGTTGA',
                      19],
            "answer": "CGTTGACCCGGCTATTATCGTGATCTCCGGCGGGACACTTTTATCGAGATCTGCCACTTGTGCGCGGTAAAGAACA"},
        {
            "input": ['CAGGGGCGCCTCGCGAAACCGGAGTTTACGTCTGATTGTGTAGCGGCAACCCAGGCTCCGTTGATA', 4],
            "answer": "AACCACCCCAGGCCTCGGCGGGAGCGTCAGGCTTTATGATTGTGTCCGGCGATAGCGGCATTGA"},
        {
            "input": ['AAGCTGCTGCCACCCATGTCTCGTGTTTGCTTCTACCAGACTGGTCCAGCCAA', 10],
            "answer": "CACCCATGTCAAGCTGCTGCTCGTGTTTGCCTGGTCCAGCTTCTACCAGA"},
    ],
    "Random": [

    ]
}

import random


def count_inversion(line):
    result = 0
    for i, el in enumerate(line):
        for sel in line[i + 1:]:
            result += int(el > sel)
    return result


def golf(sequence, partition_number):
    subs = [sequence[i * partition_number:(i + 1) * partition_number]
            for i in range(len(sequence) // partition_number)]
    sorted_subs = sorted(subs, key=count_inversion)
    return "".join(sorted_subs)


LETTERS = "ACGT"

for __ in range(10):
    s = "".join(random.choice(LETTERS) for _ in range(random.randint(1, 100)))
    n = random.randint(1, len(s) // 2)
    t = [s, n]
    ans = golf(*t)
    TESTS["Random"].append({
        "input": t,
        "answer": ans})