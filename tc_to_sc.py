from opencc import OpenCC

# Traditional Chinese to Simplified Chinese
cc = OpenCC("t2s")
tc_string = "繁體中文"
sc_string = cc.convert(tc_string)

print(sc_string)
# 繁体中文


# Simplified Chinese to Traditional Chinese
cc = OpenCC("s2t")
sc_string = "简体中文"
tc_string = cc.convert(sc_string)

print(tc_string)
# 簡體中文
