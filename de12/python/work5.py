for i in range(1,4):
    print(i,"人目")

    #for関数で繰り返したい内容をforの下に入れる(tab)

    name=input("お名前は何ですか？")
    waist=float(input("腹囲は何cmですか？"))
    age=int(input("何歳ですか？"))

    print(name, "さんは腹囲", waist, "cmで年齢は",age, "才ですね。")

    if waist>=85 and age>=40:
        print(name,"さん、内臓脂肪蓄積注意です")
    elif waist>=80 and age>=40:
        print(name, "さん、食べすぎに注意してください")
    else:
        print(name,"さん、腹囲は問題ありません")


