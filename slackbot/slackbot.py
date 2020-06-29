# coding:utf-8
import os
import sys
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'requests'))
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'slackweb'))
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'vendor'))
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

def lambda_handler(event,context) :
        


    will_do=list()
    doing=list()
    do=list()
    done=list()
    will_do_task=0
    doing_task=0
    do_task=0
    actualHours=0


    # データをリクエスト
    backlog_issues = requests.get(BACKLOG_URL, params=BACKLOG_PARAMS).json()


    for task_object in backlog_issues:
        if task_object["status"]["id"] == 1:
            if task_object["estimatedHours"]:
                will_do_task += task_object["estimatedHours"]
            summary = task_object["summary"].encode('utf-8')
            will_do.append(summary.decode('utf-8'))
        elif task_object["status"]["id"] == 2:
            if task_object["estimatedHours"]:
                doing_task += task_object["estimatedHours"]
            summary = task_object["summary"].encode('utf-8')
            doing.append(summary.decode('utf-8'))
        elif task_object["status"]["id"] == 3:
            if task_object["estimatedHours"]:
                do_task += task_object["estimatedHours"]
            if task_object["actualHours"]:
                actualHours += task_object["actualHours"]
            summary = task_object["summary"].encode('utf-8')
            do.append(summary.decode('utf-8'))
        elif task_object["status"]["id"] == 4:
            summary = task_object["summary"].encode('utf-8')
            done.append(summary.decode('utf-8'))


    id_1 = '\n'.join(will_do)
    id_2 = '\n'.join(doing)
    id_3 = '\n'.join(do)

    result = "未対応\n"+ id_1 +"\n見積もり: " + str(will_do_task) + "\n\n処理中\n" + id_2 + "\n見積もり: "+ str(doing_task) + "\n\n処理済\n" + id_3 + "\n見積もり: " + str(do_task) \
    + "\n累計実績時間: " + str(actualHours) +"  １時間あたりの消化数: " + str(format((do_task/actualHours),'.2f'))


    slack.notify(text= result)


