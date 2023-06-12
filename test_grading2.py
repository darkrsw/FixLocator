from StatRepair import StatRepair
import yaml


def test_yaml1():
    testyaml1 = """
                  a: 1
                  b:
                    c: 3
                    d: 4
                """

    testyaml2 = """
---
foo: 12345
bar: 0x12d4
plop: 023332
     """

    testyaml3 = """
---
foo: 1230.15
bar: 12.3015e+05
        """

    testyaml4 = """
---
items: [ 1, 2, 3, 4, 5 ]
names: [ "one", "two", "three", "four" ]
---
foo:
  bar:
    - bar
    - rab
    - plop
        """

    testyaml5 = """
      ---
      items:
        - 1
        - 2
        - 3
        - 4
        - 5
      names:
        - "one"
        - "two"
        - "three"
        - "four"
    """

    testyaml6 = """
    ---
foo: { thing1: huey, thing2: louie, thing3: dewey }
    """

    testyaml7 = """
---
bar: foo
foo: bar
---
one: two
three: four
  """

    debugger = StatRepair()

    with debugger.collect_pass():
        yaml.dump(yaml.load(testyaml1, Loader=yaml.FullLoader))
    with debugger.collect_pass():
        yaml.dump(yaml.load(testyaml2, Loader=yaml.FullLoader))
    with debugger.collect_pass():
        yaml.dump(yaml.load(testyaml3, Loader=yaml.FullLoader))
    with debugger.collect_fail():
        try:
            yaml.dump(yaml.load(testyaml4, Loader=yaml.FullLoader))
        except:
            pass

    with debugger.collect_fail():
        try:
            yaml.dump(yaml.load(testyaml5, Loader=yaml.FullLoader))
        except:
            pass

    with debugger.collect_fail():
        try:
            yaml.dump(yaml.load(testyaml6, Loader=yaml.FullLoader))
        except:
            pass

    with debugger.collect_pass():
        try:
            yaml.dump(yaml.load_all(testyaml7, Loader=yaml.FullLoader))
        except:
            pass

    line, dist = debugger.mostsimilarstmt(debugger.rank()[0])

    assert (line == "self.column = 0" and dist == 5) or (line == "def fetch_document_start(self):" and dist == 4)
