
import pathlib

p = pathlib.Path('./content/posts')

md = list(p.rglob("*.md"))

# changeFigure = lambda s: s.replace("../figures", "../../figures")
changeFormula = lambda s: s.replace("\\", "\\\\").replace("_", "\\_")
# def changeFormula(s: str):
#     ls = s.split("\n$$\n")
#     if len(ls) == 1:
#         return s
    
#     ls[0] = ls[0] + "\n<div>\n$$\n"
#     for i in range(1, len(ls) - 1):
#         if i % 2 == 0:
#             ls[i] = "\n$$\n</div>\n" + ls[i] + "\n<div>\n$$\n"
#     ls[-1] = "\n$$\n</div>\n" + ls[-1]
#     return ''.join(ls)

for i in md:
    text = i.open('r').read()
    # text = changeFigure(text)
    text = changeFormula(text)
    with i.open('w') as f:
        f.write(text)
