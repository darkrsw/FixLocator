class StatRepair
    def getStmt(self, tlocation):
        functions = self.covered_functions()

        stmt = ""
        # print(tlocation[0], tlocation[1])

        for func in functions:
            try:
                if func.__name__ == tlocation[0]:
                    source_lines, starting_line_number = inspect.getsourcelines(func)

                    line_number = starting_line_number

                    for line in source_lines:
                        location = (func.__name__, line_number)
                        # print(location)
                        # location_suspiciousness = self.suspiciousness(location)
                        if location == tlocation:
                            stmt = line.strip()
                            break
                        line_number += 1

            except Exception as e:
                continue


        return stmt

    def mostsimilarstmt(self, targetloc):

        target = self.getStmt(targetloc)

        functions = self.covered_functions()

        simmap = {}

        for func in functions:
            try:
                source_lines, starting_line_number = inspect.getsourcelines(func)
            except Exception as e:
                continue

            # if (function.__name__, starting_line_number) in simmap:
            #     continue

            # print(func)

            line_number = starting_line_number

            for line in source_lines:
                location = (func.__name__, line_number)
                location_suspiciousness = self.suspiciousness(location)
                if location_suspiciousness is not None:
                    line = line.strip()
                    dist = levenshtein(target, line)
                    # print(dist, line)
                    simmap[line] = dist
                line_number += 1

        sortedmap = dict(sorted(simmap.items(), key=lambda item: item[1]))

        for k, v in sortedmap.items():
            if v > 0:
                return (k, v)

        return None
