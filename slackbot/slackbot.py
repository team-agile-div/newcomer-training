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
        doing.append(task_object["summary"])
        print(type(task_object["summary"].encode('utf-8')))
    elif task_object["status"]["id"] == 3:
        do.append(task_object["summary"])
    elif task_object["status"]["id"] == 4:
        done.append(task_object["summary"])
    
print(will_do)
# print(doing)
print(doing[0].encode('utf-8'))
