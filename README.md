# Tinkoff-Antiplagiat

 Структура:
 
 out_data - папка с результатами эксперимента по подбору n для n-грамм
 
 plagiat - папка с программами, которые проверяюся на антиплагиат\
     - 1) files - исходные программы\
     - 2) plagiat1 - переписанные программы (плагиат)\
     - 3) plagiat2 - переписанные программы (плагиат)
 
 project - папка с проектом:\
     - 1) analysis_functions - функции, осуществляющие анализ кода\
     - 2) file_read_functions - функции для чтения файлов\
     - 3) compare - основная программа. После ее запуска необходимо ввести в строчку ссылки на файлы input и scores, которые должны быть заполнены согласно заданию

Задача решена при помощи метода n-грамм. Сначала код программы парсится библиотекой ast, после чего из формы ast создается список, который разбивается на 2-граммы. 2-граммы программ сравниваются, после чего выводится результат сравнения. Чем ближе скор к 1, тем больше вероятность, что программа является плагиатом.

Размер n-граммы равный 2-м подобран с помощью эксперимента, в котором сравнивались n-граммы размерами от 1 до 5 включительно. Сначала были созданы выборки оценок при разных n для плагиата и не плагиата. Изучались средние и медианные значения оценок для гарантированно сплагиаченных и неслпагиаченных программ, был изучен "коридор недоверия" - программы, попавшие в промежуток между самой высокой оценкой для не плагиата и самой низкой оценкой для плагиата, так как для таких программ есть риск неправильной классификации. Результаты можно увидеть в файле test_data.xlsx. n=2 позволяет достичь минимального числа программ в "коридоре недоверия", поэтому, для данной задачи (цель которой как можно лучше разделить плагиат и не плагиат) такое значение n, предположительно, является лучшим.
