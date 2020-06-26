# coding:utf-8
import requests
import json
import slackweb

# 取得したいBacklogのURL
BACKLOG_URL = "https://aws-plus.backlog.jp/api/v2/issues"
slack = slackweb.Slack(url="https://hooks.slack.com/services/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")

# 課題の内容
BACKLOG_PARAMS = {
    'apiKey': 'un9Zxec8M0HXUARoTBaKoKXQ9mX760fUKZubf5A9dJehUfX2XSAkp3okzJTUi31w',
    'projectId[]': 1073909995,
    'statusId[]': {1,2,3}, # 1:未対応,2:処理中,3:処理済み,4:完了
    # 'sort': 'updated',  # 更新日でソート
    'count': 20,       # 100件取得
}

will_do=[]
doing=[]
do=[]
done=[]

# データをリクエスト
backlog_issues = requests.get(BACKLOG_URL, params=BACKLOG_PARAMS).json()
backlog_list =  json.dumps(backlog_issues, ensure_ascii=False, indent=2)


for task_object in backlog_issues:
    if task_object["status"]["id"] == 1:
        summary = task_object["summary"].encode('utf-8')
        will_do.append(summary)
    elif task_object["status"]["id"] == 2:
        summary = task_object["summary"].encode('utf-8')
        print(type(summary))
        doing.append(summary)
    elif task_object["status"]["id"] == 3:
        summary = task_object["summary"].encode('utf-8')
        do.append(summary)
    elif task_object["status"]["id"] == 4:
        summary = task_object["summary"].encode('utf-8')
        done.append(summary)
    

id_1 = '\n'.join(will_do)
id_2 = '\n'.join(doing)
id_3 = '\n'.join(do)

result = "未対応\n"+ id_1 + "\n\n処理中\n" + id_2 + "\n\n処理済\n" + id_3

slack.notify(text= result, channel = "#agile-training-2020")


