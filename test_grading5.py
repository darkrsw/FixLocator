"""Reference: https://github.com/keon/algorithms/blob/master/algorithms/search/jump_search.py"""
from StatRepair import StatRepair
import math

def jump_search(arr,target):
    length = len(arr)
    block_size = int(math.sqrt(length))
    block_prev = 0
    block= block_size

    # return -1 means that array doesn't contain target value
    # find block that contains target value

    if arr[length - 1] < target:
        return -1
    while block <= length and arr[block - 1] < target:
        block_prev = block
        block += block_size

    # find target value in block

    while arr[block_prev] < target :
        block_prev += 1
        if block_prev == min(block, length) :
            return -1

    # if there is target value in array, return it

    if arr[block_prev] == target :
        return block_prev
    return -1

def test_jump_search():
    debugger = StatRepair()

    with debugger.collect_pass():
        jump_search([123456789], 9);

    with debugger.collect_pass():
        jump_search([12345678907654321456789], -1);

    with debugger.collect_pass():
        jump_search([000000000000000000000], 1);

    with debugger.collect_fail():
        try:
            jump_search([], 1);
        except:
            pass

    with debugger.collect_fail():
        try:
            jump_search({}, -1);
        except:
            pass

    with debugger.collect_fail():
        try:
            jump_search(1, -1);
        except:
            pass

    line, dist = debugger.mostsimilarstmt(debugger.rank()[0])
    assert (line == "if arr[length - 1] < target:" and dist == 20) or (line == "return -1" and dist == 14)
