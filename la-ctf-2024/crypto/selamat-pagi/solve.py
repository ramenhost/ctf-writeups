# flag like text taken from message.txt
ct = list("bkvim{wzbkdki_ckse_kckukx_ukdj_wjuk_kfkbewew_mtzujzfwe}")

# flag guessed to start with lactf{selamat_pagi
mapping = dict(zip(ct[:18], "lactf{selamat_pagi"))

# mappings manually inferred to match indonesian words
mapping['f'] = 'n'
mapping['t'] = 'r'
mapping['u'] = 'k'
mapping['j'] = 'u'
mapping['x'] = 'h'
mapping['}'] = '}'

print(''.join(list(map(lambda x: mapping[x] if x in mapping else '-', ct))))