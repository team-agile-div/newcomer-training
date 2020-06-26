# coding:utf-8
import requests
import json

# 取得したいBacklogのURL
BACKLOG_URL = "https://aws-plus.backlog.jp/api/v2/issues"

# 課題の内容
BACKLOG_PARAMS = {
    'apiKey': 'un9Zxec8M0HXUARoTBaKoKXQ9mX760fUKZubf5A9dJehUfX2XSAkp3okzJTUi31w',
    'projectId[]': 1073909995,
    # 'statusId[]': {1},  # 1:未対応,2:処理中,3:処理済み,4:完了
    'sort': 'updated',  # 更新日でソート
    'count': 10,       # 100件取得
}

will_do=[]
doing=[]
do=[]
done=[]

# データをリクエスト
backlog_issues = requests.get(BACKLOG_URL, params=BACKLOG_PARAMS).json()

# backlog_list =  json.dumps(backlog_issues, ensure_ascii=False, indent=2)
# # print(type(eval(backlog_list[0])))

for task_object in backlog_issues:
    if task_object["status"]["id"] == 1:
        will_do.append(task_object["summary"])
    elif task_object["status"]["id"] == 2:
        summary = task_object["summary"].encode('utf-8')
        doing.append(summary)
    elif task_object["status"]["id"] == 3:
        summary = task_object["summary"].encode('utf-8')
        do.append(summary)
    elif task_object["status"]["id"] == 4:
        summary = task_object["summary"].encode('utf-8')
        done.append(summary)
    
print("未対応")
for task in will_do:
    print(task)
print("\n処理中")
for task in doing:
    print(task)
print("\n処理済")
for task in do:
    print(task)
# print("\n完了")
# for task in done:
#     print(task)

