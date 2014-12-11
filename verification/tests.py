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
            "input": ['ACGTC', 'TTACTC'],
            "answer": "ACTC",
        },
        {
            "input": ['TTACTC', 'ACGTC'],
            "answer": "ACTC",
        },
        {
            "input": ['CGCTA', 'TACCG'],
            "answer": "CC,CG,TA",
        },
        {
            "input": ['GCTT', 'AAAAA'],
            "answer": "",
        },
        {
            "input": ['CGTCGTCGT', 'CGTACGT'],
            "answer": "CGTCGT",
        },
        {
            "input": ['TGCAAAACGT', 'ACGTAAAATGCA'],
            "answer": "CAAAAC,CAAAAG,CAAAAT,GAAAAC,GAAAAG,GAAAAT,TAAAAC,TAAAAG,TAAAAT",
        },
        {
            "input": ['GGGCCCAAA', 'AAACCCGGGG'],
            "answer": "AAA,CCC,GGG",
        },
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