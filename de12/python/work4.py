name=input("お名前は何ですか？")
waist=float(input("腹囲は何cmですか？"))
age=int(input("何歳ですか？"))

#　input を代入するとキーボード入力で代入できるようになる
#キーボード入力するときの質問は()の中に入れる

#inputで入力した数字はそのままだと文字として扱われてしまう
#整数の時は int, 小数の時は float をinput関数の前に加えることで数字として扱われるようになる
#int,floatの後の関数は()で囲む！

print(name, "さんは腹囲", waist, "cmで年齢は",age, "才ですね。")

if waist>=85 and age>=40:
    print(name,"さん、内臓脂肪蓄積注意です")
elif waist>=80 and age>=40:
    print(name, "さん、食べすぎに注意してください")
else:
    print(name,"さん、腹囲は問題ありません")