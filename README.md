<h1 align="center">_✨ CloudSign_云签到 ✨_</h1>
<p align="center">
<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/Monarchdos/nonebot_plugin_cloudsign.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot_plugin_cloudsignx">
    <img src="https://img.shields.io/pypi/v/nonebot_plugin_cloudsignx.svg" alt="pypi">
</a>
<a href="https://www.python.org">
    <img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">
</a>
<a href="#">
    <img src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fcloudsign.ayfre.com%2Frelation%2Fusernum%2F&query=num&label=%E7%94%A8%E6%88%B7%E6%95%B0&color=%23f37f40" alt="用户数">
</a>
</p>




## 📖 介绍

**云签到**  

​	一款数据存放于云端的签到积分综合插件,并附有使用积分的小游戏功能,公平的积分系统,数据不会被机器人主人所更改,所有使用本插件的用户积分数据互通,并可参与与所有用户的积分排行。


🎇**本插件的数据在所有插件使用者中互通**

## 💿 安装

**使用 nb-cli 安装** 
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装：

```bash
nb plugin install nonebot-plugin-cloudsignx
```

**使用 pip 安装**  

```bash
pip install nonebot-plugin-cloudsignx
```

打开 nonebot2 项目的 `bot.py` 文件, 在其中写入：
```python
nonebot.load_plugin('nonebot_plugin_cloudsignx')
```

**升级插件**  
```bash
pip install --upgrade nonebot-plugin-cloudsignx
```

## 🎉 使用

<table>
    <tr align="center">
        <th> 指令 </th>
        <th> 说明 </th>
    </tr>
    <tr align="center">
        <td> 签到 </td>
        <td> 🟢每日签到,每日首签与连续签到都将获得额外积分 </td>
    </tr>
    <tr align="center">
        <td> 积分</td>
        <td> 查询现在拥有的积分等数据 </td>
    </tr>
    <tr align="center">
        <td> 抽奖 n</td>
        <td> 消耗n积分,随机获取0-3倍积分 </td>
    </tr>
    <tr align="center">
        <td> 转账 n@xxx </td>
        <td> 将n积分转账给xxx,转账会收取一定手续费 </td>
    </tr>
    <tr align="center">
        <td> 打劫@xxx </td>
        <td> 打劫xxx的积分,有几率获得对方的部分积分,也可能打劫不到或被反打劫 </td>
    </tr>
    <tr align="center">
        <td> #打劫记录 </td>
        <td> 查看打劫统计信息 </td>
    </tr>
    <tr align="center">
        <td> 领取积分补助 </td>
        <td> 积分不足时可领取每日补助 </td>
    </tr>
    <tr align="center">
        <td> 排行榜 </td>
        <td> 查看全部用户的积分排行榜,并显示自己的名次 </td>
    </tr>
    <tr align="center">
        <td> #排行榜 xxx </td>
        <td> 查看积分排行榜第xxx页(xxx∈[1,10]) </td>
    </tr>
    <tr align="center">
        <td> 挖矿 </td>
        <td> 消耗10积分进行挖矿 </td>
    </tr>
    <tr align="center">
        <td> 我的背包 </td>
        <td> 查看挖到的矿 </td>
    </tr>
    <tr align="center">
        <td> 售出 xxx </td>
        <td> 将挖到的xxx卖出,获得积分 </td>
    </tr>
    <tr align="center">
        <td> 钓鱼 </td>
        <td> 消耗10积分进行钓鱼 </td>
    </tr>
    <tr align="center">
        <td> 我的鱼篓 </td>
        <td> 查看钓到的鱼🐟 </td>
    </tr>
    <tr align="center">
        <td> 出售 xxx </td>
        <td> 将钓到的xxx卖出,获得积分 </td>
    </tr>
    <tr align="center">
        <td> 猜数字 xxx </td>
        <td> 消耗xxx积分开始猜数字游戏,猜中则积分翻倍 </td>
    </tr>
    <tr align="center">
        <td> 我猜 xxx </td>
        <td> 在指定次数内进行猜数字游戏,xxx为你所猜的数字 </td>
    </tr>
    <tr align="center">
        <td> 猜拳石头|剪刀|布 xxx </td>
        <td> 消耗xxx积分进行猜拳游戏,胜利则积分翻倍 </td>
    </tr>
    <tr align="center">
        <td> #存入银行 xxx </td>
        <td> 将xxx积分存入银行中,存入将重置存款时长 </td>
    </tr>
    <tr align="center">
        <td> #取出银行 xxx </td>
        <td> 将银行中的xxx积分取出,将根据存款时长计算利息 </td>
    </tr>
    <tr align="center">
        <td> #抢银行 </td>
        <td> 有几率获得系统银行的积分,也可能被罚取积分 </td>
    </tr>
    <tr align="center">
        <td> #扔漂流瓶 xxx </td>
        <td> 将xxx写入漂流瓶,并扔进海里,可以被其他人捞到,只能被捞取一次 </td>
    </tr>
    <tr align="center">
        <td> #捞漂流瓶 </td>
        <td> 从海中捞漂流瓶，无法捞到自己扔的漂流瓶 </td>
    </tr>
    <tr align="center">
        <td> #漂流瓶信息 </td>
        <td> 查看自己的漂流瓶统计信息 </td>
    </tr>
    <tr align="center">
        <td> #等级信息 </td>
        <td> 查看自己的等级以及经验值 </td>
    </tr>
    <tr align="center">
        <td> #邀请码 xxxxx </td>
        <td> 邀请码为对方qq号,视为对方邀请了你,双方积分+50 </td>
    </tr>
    <tr align="center">
        <td> #反馈 xxx </td>
        <td> 反馈xxx问题 </td>
    </tr>
    <tr align="center">
        <td> #反馈信箱 </td>
        <td> 查看反馈 </td>
    </tr>
    <tr align="center">
        <td> #夺宝 </td>
        <td> 宝物每小时整点刷新,宝物只可以被一人夺得,宝物刷新后五分钟未被夺得将消失,夺得宝物将获得大量积分 </td>
    </tr>
    <tr align="center">
        <td> #探险 前/后/左/右 </td>
        <td> 秘境开启后进行探险，有四个方向可以走，每个方向都有不同的事件，事件包括发现宝藏(获得积分),遭遇袭击(失去积分),无事发生,退出秘境(结束探索);随着探索的深入风险也会变大。 </td>
    </tr>
    <tr align="center">
        <td> 签到状态 </td>
        <td> 查看服务器的实时负载等信息 </td>
    </tr>
    <tr align="center">
        <td> 功能 </td>
        <td> 显示功能列表 </td>
    </tr>
    <tr align="center">
        <td> 功能 xxx </td>
        <td> 查看xxx功能的使用方法 </td>
    </tr>
    <tr align="center">
        <td> @检查更新@ </td>
        <td> 检查插件是否为新版本 </td>
    </tr>
</table>


#### 💬 Tip: 指令与参数间的空格不可省略；详细请使用`功能`指令进行查看。

## 📃 配置项

直接在全局配置项`env.dev`后添加即可，配置项修改后重启NoneBot生效。

#### 	cloudsign_reply_quote

类型：Bool

默认值：True

说明：是否在回复时引用用户消息。

```
 cloudsign_reply_quote=true
```

#### 	cloudsign_reply_at

类型：Bool

默认值：False

说明：是否在回复时引用用户消息。

```
 cloudsign_reply_at=false
```

⚠**注：*cloudsign_reply_quote*和*cloudsign_reply_at*不可以同时为*true*；可以同时为*false*表示直接回复消息。**

## 📝 更新日志

<details>
<summary>展开/收起</summary>

## **2024-09-20 V2.1.2**

  * 修复已知问题。
  * 新增机器人回复艾特或引用消息配置项。

## **2024-07-14 V2.1.0**

  * 优化代码结构。
  * 新增机器人回复是否'@用户'的设置。

## **2023-01-10 V2.0.0**

  * 新增 猜数字 小游戏系统,开始游戏后系统将随机生成一个数字,在规定步数内猜对这个数字则获胜,积分翻倍。
  * 新增 猜拳 小游戏系统,在石头、剪刀、布中与系统进行猜拳,胜利则积分翻倍。
  * 优化细节~
  * 后续非重大更新外都将采用热更新。

## **2023-01-08 V1.3.0**

  * 新增"出售"功能,可将钓到的鱼进行卖出,获取积分。
  * 新增"售出"功能,可将挖到的矿进行卖出,获取积分。
  * 优化细节~

## **2023-01-07 V1.2.8**

  * 新增"功能"指令查看功能使用方法功能。
  * 新增"检查更新"功能(不会主动提示更新)。
  * 若无需要可以不更新~

</details>

