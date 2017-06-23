# tg-jalmeida
Parser multilingual (STRIPS, ADL e PDDL) para planejadores automáticos

O comando para executar o protótipo é:

    python mlp.py <form> <runmode>

Em que \<form\> pode ser um arquivo de formalização STRIPS, ADL ou PDDL. Para o caso de PDDL, vão ser dois arquivos: formalização de domínio primeiro e depois a formalização do problema. O argumento \<runmode\> é opcional e serve para informar o modo de execução: parser ou planejador. Se nenhum argumento for passado, será executado no modo planejador. Para esse modo de execução (planejador), o arquivo de formalização será analisado e interpretado. Se a entrada estiver sintaticamente e semanticamente correta, o algoritmo de planejamento será executado. Caso seja passado o argumento '-p', será executado no modo parser, em que não haverá execução do algoritmo de planejamento (módulo de planejamento) e consequentemente não vai haver saída do plano de ação.
