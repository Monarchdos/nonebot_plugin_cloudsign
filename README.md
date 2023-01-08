<p align="center">
  <a href="https://v2.nonebot.dev/"><img src="https://v2.nonebot.dev/logo.png" width="200" height="200" alt="nonebot"></a>
</p>
<div align="center">
_✨ NoneBot 云签到插件 ✨_
<br><br><a href="./LICENSE">
    <img src="https://img.shields.io/github/license/Monarchdos/nonebot_plugin_cloudsign.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot_plugin_cloudsignx">
    <img src="https://img.shields.io/pypi/v/nonebot_plugin_cloudsignx.svg" alt="pypi">
</a>
<a href="https://www.python.org">
    <img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">
</a>

</div>

## 📖 介绍

**云签到**  

一款数据存放于云端的签到插件,并附有使用积分的小游戏功能,公平的积分系统,数据不会被机器人主人所更改,所有使用本插件的用户积分数据互通,并可参与与所有用户的积分排行


🎇**本插件的数据在所有插件使用者中互通**

## 💿 安装

**使用 nb-cli 安装**  
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装  

```bash
nb plugin install nonebot-plugin-cloudsignx
```

**使用 pip 安装**  
```bash
pip install nonebot-plugin-cloudsignx
```

打开 nonebot2 项目的 `bot.py` 文件, 在其中写入
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
    <td> ♥每日签到 </td>
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
    <td> 将n积分转账给xxx </td>
  </tr>
    <tr align="center">
    <td> 领取积分补助 </td>
    <td> 积分低于10分时每日可领取一次补助 </td>
  </tr>
    </tr>
    <tr align="center">
    <td> 排行榜 </td>
    <td> 查看全部用户的积分排行榜,并显示自己的名次 </td>
  </tr>
</tr>
    <tr align="center">
    <td> 挖矿 </td>
    <td> 消耗10积分进行挖矿 </td>
  </tr>
</tr>
    <tr align="center">
    <td> 我的背包 </td>
    <td> 查看挖到的矿 </td>
  </tr>
  <tr align="center">
    <td> 售出 xxx </td>
    <td> 将挖到的xxx卖出,获得积分 </td>
  </tr>
</tr>
    <tr align="center">
    <td> 钓鱼 </td>
    <td> 消耗10积分进行钓鱼 </td>
  </tr>
</tr>
    <tr align="center">
    <td> 我的鱼篓 </td>
    <td> 查看钓到的鱼🐟 </td>
  </tr>
  <tr align="center">
    <td> 出售 xxx </td>
    <td> 将钓到的xxx卖出,获得积分 </td>
  </tr>
</tr>
    <tr align="center">
    <td> 签到状态 </td>
    <td> 查看服务器的实时负载等信息 </td>
  </tr>
</tr>
    <tr align="center">
    <td> 功能 </td>
    <td> 列出功能的指令, [功能 功能名]可查看功能名使用方法 </td>
  </tr>
  <tr align="center">
    <td> 打劫@xxx </td>
    <td> 打劫xxx的积分,有几率获得对方的部分积分,也可能打劫不到或被反打劫 </td>
  </tr>
<tr align="center">
    <td> @检查更新@ </td>
    <td> 检查插件是否为新版本 </td>
  </tr>
</table>

#### Tip: 指令与参数间的空格不可省略



## 📝 更新日志

<details>
<summary>展开/收起</summary>

## **2023-01-08 V1.3.0**

  * 新增"出售"功能,可将钓到的鱼进行卖出,获取积分
  * 新增"售出"功能,可将挖到的矿进行卖出,获取积分
  * 优化细节~

## **2023-01-07 V1.2.8**

  * 新增"功能"指令查看功能使用方法功能.
  * 新增"检查更新"功能(不会主动提示更新).
  * 若无需要可以不更新~

</details>

