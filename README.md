# Multilingual Parser for STRIPS, ADL and PDDL planners

Nowadays, automated planning is widely used to solve multiple problems in different knowledge areas, as in gaming, robotics and dynamic process adaptation. In this context, parsers are a major component in automated planning tools. Hence, in this work, an implementation of a multilingual parser prototype for automatic planners is presented. Python was the language used for the construction of this prototype with the aid of PLY (Python Lex-Yacc), a syntatic analyzer generator. Thus, a independent one-pass parser module was obtained. This tool was design with the purpose of assist the development of automated planners that use one of the following planning languages STRIPS (Stanford Research Institute Problem Solver), ADL (Action Description Language) or PDDL (Planning Domain Definition Language). Besides, to assert the applicability of the module, an open source implementation of the BFS (Breadth-First Search) algorithm was integrated with the module. Lastly, aiming to highlight the advantages of the developed tool, comparative experiments were performed with six other planners/planner parsers (JavaGP, SAPA, pddlparser-pp, STRIPS-Fiddle, Web-Planner and Planning Domains). The experiments were concerned in tests to verify the planners performance solving propositional problems; the efficiency to generate warnings and detect lexic, syntatic and semantic errors from PDDL language; the difference between running time in the supported planning languages. Considering the results obtained from the performed experiments, this work achieved positive results once the developed prototype presented advantages in most of the tests when compared with the other six parsers.

# How to use
Run:
1) (Parser) 

	python3 main.py domain.pddl problem.pddl 

2) (Propositional Planner example - using BFS Algorithm) 

	python3 main.py domain.pddl problem.pddl -p


Examples:

    python3 main.py examples/galaxy/galaxy.pddl examples/galaxy/galaxy-p1.pddl

    python3 main.py examples/galaxy/galaxy.pddl examples/galaxy/galaxy-p1.pddl -p


Obs:
The parser only implements the basic typing/operators (and, not, equals) from PDDL language

Thesis: http://bdm.unb.br/handle/10483/17749
