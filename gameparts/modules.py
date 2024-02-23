def save_result(res):
    with open('results.txt', 'a', encoding='utf-8') as f:
        f.write(res)
