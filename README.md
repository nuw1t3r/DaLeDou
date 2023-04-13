<h2>使用青龙面板在左上角切换到ql分支</h2>


## 概述

因为等级或者战力差异，脚本不一定适合所有人，脚本参考作者等级 `136`

乐斗等级战力不高的玩家使用脚本可能会有一些问题，建议手动提高等级战力后再使用

脚本定时工作时间：
- 第一轮 `13:01` 运行 `daledouone.py` 模块
- 第二轮 `20:01` 运行 `daledoutwo.py` 模块

大乐斗cookie有效期（通过账号密码登录获得时）：
- 脚本每隔30分钟（定时由 `Schedule` 库实现）请求一次来延长cookie有效期
- 当天更换cookie，第二天依然有效，但会在第三天早上8点整左右失效
- 停止脚本超过一个多小时，cookie也会失效
- 一键登录获得的cookie有效期两天

大乐斗已实现的功能：
- [文档](https://www.gaoyuanqi.cn/python-daledou/#more)


## Python版本

```
Python 3.11
```


## 下载脚本

通过git下载：
```sh
$ git clone https://github.com/gaoyuanqi/DaLeDou.git
$ cd DaLeDou
$ ls
```


## settings.py 配置

**添加大乐斗cookie（必须，支持多账号）**

抓包以下链接：
```
https://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk?cmd=index&channel=0
```

将复制的大乐斗Cookie直接填入：
```python
# 大乐斗cookie，比如 'RK=xxx; ptcz=xxx; uin=xxx; skey=xxx'
# 支持多账号，每行对应一个账号
DALEDOU_ACCOUNT = [
    # 'RK=xxx; ptcz=xxx; uin=xxx; skey=xxx',
    # 'RK=xxx; ptcz=xxx; uin=xxx; skey=xxx',
]
```

**添加pushplus微信通知（可选）**

微信公众号 `pushplus` > `pushplus` > `pushplus官网` > `一对一推送` > `一键复制`

将token添加到：
```python
PUSHPLUS_TOKEN = ''
```


## 自定义账号配置（必须）

运行脚本会自动为当前有效cookie在 `./config` 目录下创建以 `QQ` 命名的yaml文件，比如 `123456.yaml`，其内容与 `daledou.yaml` 完全一致

如果文件存在则不做任何操作

一个 `QQ.yaml` 文件对应唯一一个账号，你可以为每个账号独立配置：
- `十二宫`: 选择扫荡，默认 `双鱼宫`
- `幻境`: 选择场景，默认 `鹅王的试炼`
- `深渊之潮`: 选择 `深渊秘境` 副本，默认 `曲镜空洞`
- `竞技场`: 商店兑换，默认兑换10个 `河洛图书`
- `门派邀请赛`: 商店兑换，默认兑换10个 `炼气石`
- `帮派黄金联赛`: 是否参加防守、参战，默认是
- `武林盟主`: 默认报名黄金赛场
- `历练`: 选择场景，默认乐斗掉落佣兵碎片BOSS的所有场景
- `帮派商会`: 交易、兑换物品
- `背包`: `使用` 指定物品id
- `活动`: `企鹅吉利兑` 材料兑换


## 使用教程

- [使用教程](./md/tutorials.md ':include')


## QQ交流群

- 783035662


## 更新日志

- [更新日志](./md/update_log.md ':include')
