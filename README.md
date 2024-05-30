## Sentry 企微机器人插件

 - 发送异常信息至企微机器人
 - 本插件可兼容 Sentry 自身限流功能
 - 可通过 `docker-compose logs -f` 查看插件日志信息 (例如使用 [onpremise](https://github.com/getsentry/onpremise) 部署)

## 安装

```bash
$ pip install sentry_qiwei
```

## 使用

在 `项目` 的`集成(Legacy Integrations)`页面找到 `企微机器人` 插件启用并设置 `Key`

## 参照仓储

 - [sentry-dingding](https://github.com/anshengme/sentry-dingding)
 - [sentry-dingtalk](https://github.com/evilbs/sentry-dingtalk)
