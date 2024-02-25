from make_decrypt import decrypt

def gen_graph_dev():
    b = "ten"
    decrypted_token = decrypt(b).replace('\b', '')