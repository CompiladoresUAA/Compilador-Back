import nltk
from nltk.tree import Tree
from graphviz import Digraph

# Crear un árbol de ejemplo con NLTK
tree = Tree('S', [Tree('NP', ['John']), Tree('VP', ['runs'])])

# Función recursiva para convertir el árbol en un gráfico de Graphviz
#def convert_tree(tree, graph):
#    if isinstance(tree, str):
#        return graph.node(tree)
#    else:
#        label = str(tree.label())
#        graph.node(label)
#        for subtree in tree:
#            child_label = convert_tree(subtree, graph)
#            graph.edge(label, child_label)
#       return label

def convert_tree(tree, graph):
    if isinstance(tree, str):
        return tree  # Devuelve directamente el valor del nodo
    else:
        label = str(tree.label())
        graph.node(label)
        for subtree in tree:
            child_label = convert_tree(subtree, graph)
            if child_label is not None:  # Verifica que child_label no sea None
                graph.edge(label, child_label)
        return label


# Crear el gráfico de Graphviz a partir del árbol de NLTK
dot = Digraph()
convert_tree(tree, dot)

# Mostrar el gráfico utilizando Graphviz
dot.render('tree', format='png', view=True)
