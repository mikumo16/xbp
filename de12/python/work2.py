name="aaa"
waist=83
age=45

print(name, "さんは腹囲", waist, "cmで年齢は",age, "才ですね。")

if waist>=85 and age>=40:
    print(name,"さん、内臓脂肪蓄積注意です")
elif waist>=80 and age>=40:
    print(name, "さん、食べすぎに注意してください")
else:
    print(name,"さん、腹囲は問題ありません")

#条件が複数の時の書き方
#if 条件式１ and 条件式２ ...and条件式n:
    # 条件式1、条件式2、… 条件式nがともにTrueの時に実行する処理

#複数の条件のうちいずれか一つを満たせばよい場合の書き方
#if 条件式1 or 条件式2 … or 条件式n :
   # 条件式1、条件式2、… 条件式nのいずれかがTrueの時に実行する処理
