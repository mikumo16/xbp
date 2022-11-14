

print("講義中寝てしまったあなたは目が覚めると教室3007にいた。\n教室の中にはあなた以外にもう一人誰かがいる。")
print("その人、A君の話によると、どうやら学校は既に閉じてしまったらしい。\nつまり、君たちは学校に閉じ込められてしまったのだ！！")

print() #blank line

name=input("A「君の名前は？」")

while True: #ループのスタート地点
    print() #blank line
    print(name, "!これからどうしよう？")

    #質問1
    print("1.周りを見渡す")
    print("2.諦めてまた寝る")
    print("3.扉を無理やりぶち壊す")

    choicea=int(input("どうする？1~3の中から選ぼう"))
    print() #blank line

    if choicea==2:
        print("目が覚めたら家のベッドの上だった。なんだ、夢だったのか！！")
        break #ゲーム終了
    elif choicea==3:
        print("残念！教室は出られたが器物損壊罪で捕まってしまった！\n最初からやり直そう")
        continue #最初に戻る
    elif choicea==1:
        print("机の上に道用先生のパソコンを見つけた！これで何かできるかもしれない")

        print("パソコンにはロックがかかっている!")
        print() #blank line
        print("何度もパスワードを試したが開かない。試せるのはあと一回だ。なんと打つ？")

        #質問3
        print("1.doyo_design")
        print("2.doyodoyodoyo")
        print("3.daisuke_doyo")

        choiceb=int(input("1~3の中から選ぼう"))
        print() #blank line

        if choiceb==1:
            print("残念！脱出失敗！\n最初からやり直そう")
            continue
        elif choiceb==2:
            print("残念！脱出失敗！\n最初からやり直そう")
            continue
        elif choiceb==3:
            print("パソコンが開いた！同時になぜか教室の扉も開いた！")
            print() #blank line
            print("しかし、教室を出てみると3階では火事が起こっていた！火はどんどんこちらに迫ってきている。どうしよう！！")

            #質問3
            print("1.とりあえず火から逃げよう！上に向かう")
            print("2.脱出するには出入口に向かうしかない。火をかいくぐり頑張って下に向かう")


            choicec=int(input("1~2 の中から選ぼう"))
            print() #balnk line

            if choicec==2:
                print("火事に飲み込まれてしまった...\n残念！最初からやり直そう")
                continue
            elif choicec==1:
                print("階段を登って21階まで来た！しばらくは大丈夫そうだ")
                print() #blank line

                print("A君のスマホには3％だけ電池が残っている！")
                print("誰か一人くらいには電話をできそうだ。誰かに電話して助けを求めよう！")

                #質問4
                print("1.A君の友人である大富豪に電話する")
                print("2.消防に連絡")

                choiced=int(input("どちらに電話をかけよう。1~2の中から選ぼう"))
                print() #blank line

                if choiced==2:
                    print("消防は間に合わず火に飲み込まれてしまった\n最初からやり直そう")
                elif choiced==1:
                    print("大富豪の友達がヘリを呼んでくれて助かった！\n",name, "おめでとう！！君は脱出に成功した!")
                    break