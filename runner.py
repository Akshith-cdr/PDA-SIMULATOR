from lang import Languages
from argparse import ArgumentParser, RawTextHelpFormatter

if __name__ == "__main__":
    l = Languages()
    parser = ArgumentParser(
        description="PushDown Automata Simulator", allow_abbrev=False, formatter_class=RawTextHelpFormatter
    )
    parser.add_argument('-i', "--input", action = 'store', type = str, required = "True",
                        help="""Enter the language you want:
L = {aNbN : N >= 0}             -      1
L = {aNb2N : N >= 0}            -      2
L = {aMbNc(M+N) : M,N >= 0}     -      3
L = {aNbMcMdN : M,N >= 0}       -      4
L = {wcwR : w ∈ (a+b)*}         -      5
L = {wwR : w ∈ (a+b)*}          -      6
L = {a^m b^n : m >= n >= 0}     -      7
L = {balanced parentheses}       -      8
L = {a^n b^n c^m : n,m >= 0}     -      9
L = {w in {a,b}* : #a = #b}      -      10
L = {a^n b^n} U {a^n b^(2n)}     -      11
"""
    )
    args = parser.parse_args()

    maps = {
        '1': 'aNbN',
        '2': 'aNb2N',
        '3': 'aMbNcM+N',
        '4': 'aNbMcMdN',
        '5': 'wcwR',
        '6': 'wwR',
        '7': 'aMbN_mGeN',
        '8': 'balancedParens',
        '9': 'aNbNcM',
        '10': 'equalAsBsAnyOrder',
        '11': 'aNbN_or_aNb2N'
    }

    pda = l.get_lang(maps[args.input])

    pda.exec(input("Enter string to validate: "))