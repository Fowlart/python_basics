from collections.abc import MutableSequence

class TreeNode:

    def __init__(self, data):
        self.data = data
        self.children: MutableSequence[TreeNode] = []
        self.parent = None

    def get_level(self) -> int:
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self):
        spaces = self.get_level()*3*" "
        preffix = spaces+"|__"  if self.parent else ""
        print(preffix+self.data)
        if self.children:
            for x in self.children:
                x.print_tree()



if __name__ == "__main__":
    skills = TreeNode("Skills")
    de = TreeNode("Data Engineer")
    survival = TreeNode("Survival")
    python = TreeNode("Python")
    azure = TreeNode("Azure")
    databricks = TreeNode("Databricks")
    box = TreeNode("Boxing")
    jump_row = TreeNode("Jump Row")
    shotgun = TreeNode("Shotgun")
    jump_row_ex = TreeNode("3 hrs weekly")
    boxing_ex = TreeNode("3 hrs weekly")

    survival.add_child(box)
    survival.add_child(jump_row)
    survival.add_child(shotgun)

    de.add_child(python)
    de.add_child(azure)
    de.add_child(databricks)
    skills.add_child(de)
    skills.add_child(survival)

    box.add_child(boxing_ex)
    jump_row.add_child(jump_row_ex)

    skills.print_tree()
    survival.print_tree()

