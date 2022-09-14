def octact_identification(mod=5000):
    df = pandas.read_csv("octant_input.csv")
    df.loc[0, "U Avg"] = df["U"].mean()
    df.loc[0, "V Avg"] = df["V"].mean()
    df.loc[0, "W Avg"] = df["W"].mean()
    df["U'=U - U avg"] = df["U"]-df.loc[0, "U Avg"]
    df["V'=V - V avg"] = df["V"]-df.loc[0, "V Avg"]
    df["W'=W - W avg"] = df["W"]-df.loc[0, "W Avg"]
###Code

import pandas
from platform import python_version
ver = python_version()

if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")

mod=5000
octact_identification(mod)