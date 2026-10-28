# 人形机器人全身运控：研究生课题地图

在线阅读：https://skyrivermoondream.github.io/humanoid-wbc-guide/

写给联合培养的研究生同学的一页式导读：

1. 五分钟看懂人形全身运控的六站流水线
2. 13 个前沿工作（SONIC、Any2Any、SuperMimic 等）的视频、通俗讲解和与巡检的关系
3. 巡检现场的 8 类需求，对到能力、参考工作和课题
4. 6 个可选课题，含难度、先读论文和第一个月的上手任务
5. 第一个月的上手路线、资源和术语表

页面是单个静态 `index.html`，不依赖外部字体和脚本库。视频直接嵌入各论文官方项目页，点击播放时才加载，版权归原作者所有。

## 修改内容

文字和链接都在 `src/content.py`，插图在 `src/scene.py`，改完后在仓库根目录运行：

```bash
python3 src/build.py
```

会重新生成 `index.html`。只需要 Python 3，无需安装其他依赖。

ONE-G（万机）整理，信息截至 2026 年 10 月。
