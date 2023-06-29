import sys

# ファイルを読み込み、"silent"、"sounding"、"silnet"が含まれている行を除外する

fname = sys.argv[1]
with open(fname, "r") as file:
    lines = file.readlines()
    lines = [line for line in lines if "silent" not in line and "sounding" not in line and "silnet" not in line]

# 結果を別のファイルに書き込む
with open(fname[0:-4] + "_a.utt", "w") as file:
    file.writelines(lines)

