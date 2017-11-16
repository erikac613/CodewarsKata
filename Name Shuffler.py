def name_shuffler(str_):
    split_str_ = str_.split(" ")
    new_str_ = split_str_[::-1]
    final_str_ = " ".join(new_str_)
    return final_str_
