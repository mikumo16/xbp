import datetime
import schedule#決まった時間に繰り返しプログラムを実行
import time

#再生時間の設定
print("睡眠用BGMを再生する時間を指定してください")
hour = input("時間（hour）：")
minute = input("分（minute）：")
target = f"{hour.zfill(2)}:{minute.zfill(2)}"
print(target+"にセットしました")

#使用する動画の指定
def job():
  import webbrowser#指定したURLを開く
  webbrowser.open("https://youtu.be/XGSSmQiqBl8")
  print("おやすみなさい！")

#毎日指定した時間に実行するという指示
schedule.every().day.at(target).do(job)
  
while True:
  schedule.run_pending()
  time.sleep(60)