from itertools import permutations
from nltk import ParentedTree


class Phrase_mixer:
    def __init__(self, based_parse_trees):
        self.based_parse_trees = based_parse_trees
        self.tree_to_str = ParentedTree.fromstring(based_parse_trees)
        self.list_new_tree = []
        self._list_NPs = []

    def __str__(self):
        str(self.tree_to_str.leaves())

    def create_list_NPs(self) -> None:
         for subtree in self.tree_to_str.subtrees():
            if subtree.label() == "NP":
                check_rules = self._counter_NPs(subtree)  # check that children consist of "NP", "CC" and ",".   "NP" >= 2
                if check_rules:
                    index_of_np, list_of_np = check_rules
                    self._list_NPs.append((index_of_np, list_of_np))  # add found np

    @staticmethod
    def _counter_NPs(trees: ParentedTree) -> None | tuple:
        index_np: list = []
        list_np: list = []
        for tree in trees:
            if tree.label() == "NP":
                index_np.append(tree.treeposition())
                list_np.append(tree)
            elif tree.label() == "," or tree.label() == "CC":
                pass
            else:
                return
        return (index_np, list_np) if len(index_np) > 1 else False

    def mix_phrase(self) -> None:
        for index_np, list_np in self._list_NPs:
            for permutation in list(permutations(list_np))[1:]:  # run for every permutation without original position
                new_ptree: ParentedTree = self.tree_to_str.copy(deep=True)
                for position in range(len(index_np)):
                    part_of_tree = permutation[position]
                    new_ptree[index_np[position]] = ParentedTree.fromstring(str(part_of_tree))  # replace old NP to new
                self.list_new_tree.append(new_ptree)

    def create_list_dicts_tree(self, limit: int = 20) -> list:
        return [{"tree": paraphrase.pformat()}for paraphrase in self.list_new_tree[:limit]
                ]

def create_list_tree(tree_in, limit):
    list_tree = tree_in.split('=')
    mix = Phrase_mixer(list_tree[1])
    mix.create_list_NPs()
    mix.mix_phrase()
    return mix.create_list_dicts_tree(limit)

