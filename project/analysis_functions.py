import ast
import _ast


def make_ast_list(tree):
    if type(tree) != _ast.Module:
        raise TypeError('tree should have type _ast.Module')
    return [node.__class__.__name__ for node in ast.walk(tree)]


def make_ngrams(ast_list, n=2):
    if n < 1:
        raise ValueError('length of ngram should be a positive number')
    ngrams = []
    if type(ast_list) != list:
        raise TypeError('ast_list should have type list')
    extended_ast_list = ['begin'] * (n - 1) + ast_list + ['end'] * (n - 1)
    for i in range(len(extended_ast_list) - (n - 1)):
        ngrams.append(' '.join(extended_ast_list[i:i + n]))
    return ngrams


def compare(ngrams1, ngrams2):
    if type(ngrams1) != list or type(ngrams2) != list:
        raise TypeError('input args should have type list')
    return len(set(ngrams1).intersection(set(ngrams2))) / len(set(ngrams1).union(set(ngrams2)))
