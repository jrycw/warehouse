import httpx


def cleanup(content, f_out):
    skip_rows = set.union(set(range(34)), set([35]))  # keep header line
    with open(f_out, newline="\n", encoding="utf-8", mode="w") as fw:
        for i, row in enumerate(content.splitlines()):
            if i in skip_rows:
                continue
            print("".join(row), file=fw)


url = "https://raw.githubusercontent.com/jrycw/datasets/master/data/dirtydevil.txt"
content = httpx.get(url).text
f_out = "dirtydevil.txt"
cleanup(content, f_out)
