import nayajson
from StatRepair import StatRepair

def test_json1():
    testjson1 = """
        [
            {
                "id": 1,
                "type": "message",
                "content": "Hello!"
            },
            {
                "id": 2,
                "type": "query",
                "user_name": "tarzan",
                "password": "not_jane"
            },
            {
                "id": 3,
                "type": "command",
                "action": "swing"
            }
        ]
    """

    testjson2 = """
        {
            "id": 3,
            "type": "command",
            "action": "swing"
        }
    """

    testjson3 = """
        {
    "glossary": {
        "title": "example glossary",
		"GlossDiv": {
            "title": "S",
			"GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": ["GML", "XML"]
                    },
					"GlossSee": "markup"
                }
            }
        }
    }
}

    """

    testjson4 = """
    [[[[]]}}
    """

    testjson5 = """
    {}
    """

    debugger = StatRepair()

    with debugger.collect_pass():
        obj = nayajson.parse_string(testjson2)
    with debugger.collect_pass():
        obj = nayajson.parse_string(testjson3)
    with debugger.collect_fail():
        obj = nayajson.parse_string(testjson1)
    with debugger.collect_fail():
        try:
            obj = nayajson.parse_string(testjson4)
        except:
            pass
    with debugger.collect_fail():
        try:
            obj = nayajson.parse_string(testjson5)
        except:
            pass



    print(debugger.rank()[:10])

    for idx in range(10):
        print(debugger.suspiciousness(debugger.rank()[idx]))
    # print(debugger.suspiciousness(debugger.rank()[0]))
    # print(debugger.suspiciousness(debugger.rank()[1]))
    # print(debugger.suspiciousness(debugger.rank()[2]))

    line, dist = debugger.mostsimilarstmt(debugger.rank()[0])

    print(line, dist)



if __name__ == '__main__':
    test_json1()
