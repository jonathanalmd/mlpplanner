import sys
import plex
import multipparser
import mlpplanner
import re
import time
    
def parse(pinput):
    planning = multipparser.mlpParser()

    if len(pinput) > 1:
        run_parser = True
        in_type = pinput[0].split(".")
        if in_type[-1] not in ["pddl","PDDL"]:
            print("Invalid input for PDDL DOMAIN formalization")
            print("Correct use: python mlpparser.py input.{strips,adl} or python mlpparser.py domain.pddl problem.pddl")
            run_parser = False
        in_type = pinput[1].split(".")
        
        if in_type[-1] not in ["pddl","PDDL"]:
            print("Invalid input for PDDL PROBLEM formalization")
            print("Correct use: python mlpparser.py input.{strips,adl} or python mlpparser.py domain.pddl problem.pddl")
            run_parser = False
        
        if run_parser:
            pmode = "pddl"
            domain, problem = multipparser.parse(pmode,[pinput[0], pinput[1]])
            # print(domain)
            # print(problem)
            planning.setPDDL(domain, problem)
        else:
            sys.exit()

    else: # strips ou adl
        in_type = inputlist[0].split(".")
        pmode = in_type[-1]

        if pmode not in ["adl","strips","ADL","STRIPS"]:
            print(">Invalid input file:",inputlist[0])
            print("Correct use: python mlpparser.py input.{strips,adl} or python mlpparser.py domain.pddl problem.pddl")
            sys.exit()
        else:
            strips_adl = multipparser.parse(pmode, [inputlist[0]])
            if strips_adl:
                # print(strips_adl)
                in_type = inputlist[0].split(".")
                if in_type[-1] in ["strips","STRIPS"]:
                    planning.setSTRIPS(strips_adl)
                else: # adl
                    planning.setADL(strips_adl)

    return planning

def runMlp(inputlist):
    planning = multipparser.mlpParser()

    if len(inputlist) > 1:
        run_parser = True
        in_type = inputlist[0].split(".")
        if in_type[-1] not in ["pddl","PDDL"]:
            print("Invalid input for PDDL DOMAIN formalization")
            print("Correct use: python mlpparser.py input.{strips,adl} or python mlpparser.py domain.pddl problem.pddl")
            run_parser = False
        in_type = inputlist[1].split(".")
        
        if in_type[-1] not in ["pddl","PDDL"]:
            print("Invalid input for PDDL PROBLEM formalization")
            print("Correct use: python mlpparser.py input.{strips,adl} or python mlpparser.py domain.pddl problem.pddl")
            run_parser = False
        
        if run_parser:
            pmode = "pddl"
            domain, problem = multipparser.parse(pmode,[inputlist[0], inputlist[1]])
    
            # print(domain)
            # print(problem)
            planning.setPDDL(domain, problem)
            rmode = "pddl"
        else:
            sys.exit()

    elif len(inputlist) == 1:
        in_type = inputlist[0].split(".")
        pmode = in_type[-1]

        if pmode not in ["adl","strips","ADL","STRIPS"]:
            print(">Invalid input file:",inputlist[0])
            print("Correct use: python mlpparser.py input.{strips,adl} or python mlpparser.py domain.pddl problem.pddl")
            sys.exit()
        else:
            strips_adl = multipparser.parse(pmode, [inputlist[0]])
            if strips_adl:
                # print(strips_adl)
                in_type = inputlist[0].split(".")
                if in_type[-1] in ["strips","STRIPS"]:
                    planning.setSTRIPS(strips_adl)
                    rmode = "strips"
                else: # adl
                    planning.setADL(strips_adl)
                    rmode = "adl"

    return planning,rmode

# @profile
def mlPlanner(inputlist):
    planner_time = 0
    parse_time = 0
    start_time = time.time()   
    parsed_data, rmode = runMlp(inputlist)
    print(parsed_data)
    planner = mlpplanner.BFSPlanner(rmode)
    parse_time = (time.time() - start_time)

    # run planner
    start_time = time.time()
    plan = planner.solve(parsed_data)
    planner_time = (time.time() - start_time)

    if plan:
        print("Plan:")
        for act in plan:
            print(act)
        print("Plan length: %d"%(len(plan)))
    else:
        print("No plan was found")
    # print(planning.getPDDLDomainPredicates())

    print("Parse: %s seconds" % (parse_time))
    print("Planner: %s seconds" % (planner_time))
    print("Total: %s seconds" % (planner_time + parse_time))


def mlParse(inputlist):
    parse_time = 0
    planner_time = 0

    input_parser = inputlist
    # print (input_parser)
    start_time = time.time()   
    parsed_data = parse(input_parser)
    parse_time = (time.time() - start_time)
    # print(parsed_data)    
    
    # print("Parse: %s seconds" % (parse_time))

    return parsed_data, parse_time
