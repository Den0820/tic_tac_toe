def save_result(res):
    file = open('results.txt', 'a')
    file.write(res + '\n')
    file.close()
