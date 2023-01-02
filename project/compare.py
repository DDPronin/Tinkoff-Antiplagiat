import ast
import file_read_functions as frf
import analysis_functions as af

paths, score = input().split()
path_pairs, score_path = frf.read_input(paths, score)
with open(score_path, 'w', encoding='utf-8') as file:
    for pair in path_pairs:
        ast_code1 = ast.parse(frf.read_code(pair[0]))
        ast_code2 = ast.parse(frf.read_code(pair[1]))
        result = af.compare(af.make_ngrams(af.make_ast_list(ast_code1)),
                            af.make_ngrams(af.make_ast_list(ast_code2)))
        file.write(str(round(result, 3))+'\n')
