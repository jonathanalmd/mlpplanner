import mlp
import sys


if sys.argv[-1] == "-p": # prop planner
    mlp.mlPlanner(sys.argv[1:-1])

else: # parse
    # parsed_data = object from mlpParser() class (multiparser.py)
    parsed_data, parse_time = mlp.mlParse(sys.argv[1:])

    # python class data pretty printer
    print(parsed_data) 

    # ================= GETTER METHODS ==================
    # get all PDDL info
    # returns 2 objects: pddlDomain and pddlProblem from 
    #      class PDDLDomainInfo() (pddldomain.py) and class PDDLProblemInfo() (pddlproblem.py)
    print(parsed_data.getPDDL())

    # ===================== DOMAIN ======================
    # get only PDDL domain info
    # returns one object from class PDDLDomainInfo() (pddldomain.py)
    print(parsed_data.getPDDLDomain())

    # get only PDDL domain name
    # returns a string (domain name)
    print(parsed_data.getPDDLDomainName())

    # get only PDDL domain predicates
    # returns a list of objects from PDDLPredicate class (pddldomain.py)
    # print structure:
    # [pred_name {'type':[var1,var2], 'type2':[var1,var2]}, pred_name2 {'type3':[var1,var2]}]
    print(parsed_data.getPDDLDomainPredicates())

    # get only PDDL domain defined types (simple typing)
    # returns a list of strings
    # print structure:
    # [type1, type2, type3]
    print(parsed_data.getPDDLDomainTypes())

    # get only PDDL domain constants
    # returns a dictionary
    # print structure:
    # {'type' : [constant1, constant2], 'type2' : [constant3]}
    print(parsed_data.getPDDLDomainConstants())

    # get only PDDL domain functions
    # returns a list of PDDLFunction class (pddldomain.py)
    # print structure:
    # ['' '' {'':['']}]
    # [string string {string:list of strings}]
    # [function_name function type {'type':[var1,var2]}]
    print(parsed_data.getPDDLDomainFunctions())

    # get only PDDL domain actions
    # returns a list of PDDLActions class (pddldomain.py)
    print(parsed_data.getPDDLDomainActions())

    # ===================== PROBLEM =====================
    # get only PDDL problem 
    # returns a object from PDDLProblem() class (pddlproblem.py)
    print(parsed_data.getPDDLProblem())

    # get only PDDL problem name
    # returns a string (problem name)
    print(parsed_data.getPDDLProblemName())

    # get only PDDL problem domain
    # returns a string (domain name)
    print(parsed_data.getPDDLProblemDomain())

    # get only PDDL problem objects
    # returns a dictionary
    # structure:
    # {'type':[var1,var2], 'type2':[var1]}
    print(parsed_data.getPDDLProblemObjects())

    # get only PDDL problem init predicates
    # returns a list of objects from PDDLProblemPredicate class (pddlproblem.py)
    # structure
    # string list of strings
    # pred_name ['var1','var2']
    print(parsed_data.getPDDLProblemInit())

    # get only PDDL problem goal predicates
    # returns a list of objects from PDDLProblemPredicate class (pddlproblem.py)
    # structure
    # string list of strings
    # pred_name ['var1','var2']
    print(parsed_data.getPDDLProblemGoal())


    print("Parse: %s seconds" % (parse_time))
