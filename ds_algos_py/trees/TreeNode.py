from collections.abc import MutableSequence
from dataclasses import dataclass

@dataclass
class Skill:
    skill_name: str
    level: int

    def __str__(self):
        return f"{self.skill_name} [{self.level}]"

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
        msg: str = spaces+str(self.data) if self.parent else f"==={str(self.data)}==="
        print(msg)
        if self.children:
            for x in self.children:
                x.print_tree()



if __name__ == "__main__":
    skills = TreeNode("Skills")
    de = TreeNode(Skill("Data Engineer", 6))
    survival = TreeNode(Skill("Survival", 3))
    python = TreeNode(Skill("Python", 3))
    azure = TreeNode(Skill("Azure", 5))
    databricks = TreeNode(Skill("Databricks", 7))
    box = TreeNode(Skill("Boxing", 2))
    jump_row = TreeNode(Skill("Jump Row", 4))
    shotgun = TreeNode(Skill("Shotgun", 1))
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

