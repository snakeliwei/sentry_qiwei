# !/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
import sentry_qiwei
from .forms import QiWeiOptionsForm
from sentry.plugins.bases.notify import NotificationPlugin

QI_WEI_API = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={key}'


class QiWeiPlugin(NotificationPlugin):
    author = 'snakeliwei'
    author_url = 'https://github.com/snakeliwei/sentry_qiwei'
    description = 'sentry extension which can send error to qiwei'
    resource_links = [
        ('Source', 'https://github.com/1018ji/sentry_qiwei_xz'),
        ('Bug Tracker', 'https://github.com/snakeliwei/sentry_qiwei/issues'),
        ('README', 'https://github.com/snakeliwei/sentry_qiwei/blob/main/README.md'),
    ]
    version = sentry_qiwei.VERSION

    slug = 'Qi Wei: Robot'
    title = 'Qi Wei: Robot'
    conf_key = slug
    conf_title = title
    project_conf_form = QiWeiOptionsForm

    def is_configured(self, project):
        return bool(self.get_option('key', project))

    def notify_users(self, group, event, *args, **kwargs):
        if not self.is_configured(group.project):
            self.logger.info('qiwei key config error')
            return None

        if self.should_notify(group, event):
            self.logger.info('send msg to qiwei robot yes')
            self.send_msg(group, event, *args, **kwargs)
        else:
            self.logger.info('send msg to qiwei robot no')
            return None

    def send_msg(self, group, event, *args, **kwargs):
        del args, kwargs

        error_title = u'【WARNING】捕获到来自【%s】的异常' % event.project.slug

        data = {
            "msgtype": "markdown",
            "markdown": {
                "content": u'<font color=\"warning\">#### {title}</font> \n \n > <font color=\"comment\">{message}</font> \n \n > <font color=\"comment\">[更多详细信息]({url}</font>'.format(
                    title=error_title,
                    message=event.message,
                    url=u'{url}events/{id}/'.format(
                        url=group.get_absolute_url(),
                        id=event.event_id if hasattr(event, 'event_id') else event.id
                    ),
                )
            }
        }

        requests.post(
            url=QI_WEI_API.format(key=self.get_option('key', group.project)),
            headers={
                'Content-Type': 'application/json'
            },
            data=json.dumps(data).encode('utf-8')
        )
