scores = {"aoki" : 70, "itou" : 68, "ueda" : 93, "emoto" : 55, "okada" : 86}

# 取得
# print(scores.get("aoki"))
# print(scores["aoki"])

resultName = ""
resultPoint = 0

# for で一個ずつ取得
for key in scores.keys():
    print(f'{key} : {scores.get(key)}')
    point = scores.get(key)
    
    if point > resultPoint :
        resultPoint = point
        resultName = key

print(f'最高得点者 - {resultName} : {resultPoint}')
