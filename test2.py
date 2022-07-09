scores = {}

def isint(s):  # 整数値を表しているかどうかを判定
    """
    文字列が数値を表し、int／float関数による変換が可能かどうかを判定
    """
    try:
        int(s, 10)  # 文字列を実際にint関数で変換してみる
    except ValueError:
        return False
    else:
        return True


def scan() :
    """
    読み取り
    """

    print("[キー　値]でスペース区切りで入力してください")

    inputText = input()

    arr = inputText.split(" ") # 配列に
    
    # フォーマットチェック（要素数2個以上か）
    if len(arr) > 1 : 
        key = arr[0]
        val = arr[1]

        # valは数値に変換できるか
        if isint(val) :
            # ENDでないか
            if key != "END":
                scores[key] = val
                print("入力完了")
                scan() # 再帰
            else:
                print("終了")
                print(scores)
        else:
            print("2つ目は数値で入力してください")
            scan() # 再帰

    else:
        print("2つデータを入力してください")
        scan() # 再帰

scan() # 呼び出し