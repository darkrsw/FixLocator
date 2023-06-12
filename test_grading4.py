"""Reference: https://github.com/qiwsir/algorithm/blob/050178ada82ef8d5c7ace2eda7ed408aa61e7b90/most_char_num.py"""

from StatRepair import StatRepair
import collections

def most_character_number(one_string):
    static_result = collections.Counter(one_string)
    result = dict(static_result)
    most_number = max([value for value in result.values()])
    most_character = [key for key,value in result.items() if value==most_number]
    return (most_number,most_character)

def test_most_character_number():
    mcnDebugger = StatRepair()

    with mcnDebugger.collect_pass():
        (most_num,most_char) = most_character_number("yyyyyyyyyyyyyyykuuuiii")

    with mcnDebugger.collect_pass():
        (most_num,most_char) = most_character_number("yywwwwwwwwwwwwwwwdddddkuuuiii")

    with mcnDebugger.collect_pass():
        (most_num,most_char) = most_character_number("rrrrrrrrrrrrppppppqpfpfpfpsdpcpspcsnwxjxjxjxjxiw")

    with mcnDebugger.collect_fail():
        try:
            (most_num,most_char) = most_character_number(2345678976534567)
        except:
            pass

    with mcnDebugger.collect_fail():
        try:
            (most_num,most_char) = most_character_number(["3w4e5r67897654"])
        except:
            pass

    with mcnDebugger.collect_fail():
        try:
            (most_num,most_char) = most_character_number({"wertfyghjkhgfdrdewaqAWSEDF"})
        except:
            pass

    line, distance = mcnDebugger.mostsimilarstmt(mcnDebugger.rank()[0])
    assert (line == "result = dict(static_result)" and distance == 28)
