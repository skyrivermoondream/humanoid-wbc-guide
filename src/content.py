"""All page copy and links. Facts were checked against each paper's arXiv page or
official project page (Oct 2026). Videos are embedded straight from the official
project pages; nothing is re-hosted."""

SONIC = "https://nvlabs.github.io/GEAR-SONIC"
A2A = "https://any2any.top"
SM = "https://supermimic.github.io"
BM = "https://beyondmimic.github.io"
HG = "https://qizekun.github.io/Humanoid-GPT"
BFM = "https://lecar-lab.github.io/BFM-Zero"
OR = "https://omniretarget.github.io"
ASAP = "https://agile.human2humanoid.com"
MO = "https://baai-humanoid.github.io/MOSAIC"
TW = "https://yanjieze.com/projects/TWIST2"
RM = "https://resmimic.github.io"

GROUPS = [
    ("onegs", "ONE-G 正在跟进"),
    ("base", "通用跟踪底座"),
    ("data", "重定向与跨本体数据"),
    ("real", "真机落地"),
    ("tool", "上手工具"),
]

WORKS = [
    dict(
        id="sonic", name="SONIC", group="onegs",
        venue="Science Robotics", org="NVIDIA",
        one="把运动跟踪当作可规模化的基础任务，模型扩到 42M 参数、数据扩到 700 小时动捕，"
            "同一个策略可以接 VR 遥操作、人体视频和 VLA 等多种输入。",
        analogy="像看过 700 小时人体动作的“小脑”：上层不管是遥控器、视频还是大模型，"
                "只需要告诉它下一步做什么动作。",
        inspect="下蹲、跪地、匍匐这些巡检常用姿态都有真机演示，还能直接接 VR 遥操作接管。",
        nums=["42M 参数", "700 小时动捕", "一个策略，多种输入"],
        clips=[
            ("能力集锦", f"{SONIC}/static/videos/teaser_title.mp4", f"{SONIC}/static/images/teaser_poster.png"),
            ("下蹲", f"{SONIC}/static/videos/planner/squat_crawl/planner_squat.mp4", None),
            ("跪地", f"{SONIC}/static/videos/planner/squat_crawl/planner_kneeling.mp4", None),
            ("肘部匍匐", f"{SONIC}/static/videos/planner/squat_crawl/planner_elbow_crawling.mp4", None),
            ("VR 全身遥操作", f"{SONIC}/static/videos/teleop/vr_wholebody/wbt.mp4", None),
            ("抗扰跟踪", f"{SONIC}/static/videos/tracking/robust1.mp4", None),
        ],
        page=f"{SONIC}/",
        links=[("论文", "https://arxiv.org/abs/2511.07820"), ("项目主页", f"{SONIC}/"),
               ("代码", "https://github.com/NVlabs/GR00T-WholeBodyControl")],
    ),
    dict(
        id="any2any", name="Any2Any", group="onegs",
        venue="arXiv 2026", org="逐际动力 LimX Dynamics",
        one="先对齐源、目标人形的运动学接口，再只在动力学敏感的模块上加 LoRA，"
            "用约 1% 的算力和数据，把 G1 上预训练的 SONIC 迁移到 LimX Oli 和 Luna。",
        analogy="像老司机换车：驾驶技术都在，只要重新适应新车油门和刹车的手感。",
        inspect="自家巡检本体不必从零训练；背负设备带来的质量变化，也可以借鉴这种“只调动力学部分”的思路。",
        nums=["约 1% 算力和数据", "只训约 5% 参数", "4 款人形验证"],
        clips=[
            ("迁移效果总览", f"{A2A}/vedio_data/cover_video.mp4", None),
            ("Oli 真机：跑步", f"{A2A}/vedio_data/sim2real-sonic3/sonic_G12oli-7-running.mp4", None),
            ("Oli 真机：移动操作", f"{A2A}/vedio_data/sim2real-sonic3/sonic_G12oli-8-locomanipulation.mp4", None),
            ("多本体同时仿真", f"{A2A}/vedio_data/simulation_multi/multiWBT-window-normal-speed.mp4", None),
        ],
        page=f"{A2A}/",
        links=[("论文", "https://arxiv.org/abs/2605.23733"), ("项目主页", f"{A2A}/"),
               ("代码", "https://github.com/Ming827/any2any_sonic2Oli")],
    ),
    dict(
        id="supermimic", name="SuperMimic", group="onegs",
        venue="CoRL 2026", org="UC Berkeley",
        one="用一个可微世界模型拟合仿真器数据，再对它反传梯度来训练策略；单卡 3 小时就超过了 SONIC "
            "发布版的回报（SONIC 用 128 卡训了 7 天），并零样本部署到 G1 真机。",
        analogy="像体操运动员在脑子里预演：先学会一套“物理直觉”，再在想象里反复练，真实仿真只用来校准。",
        inspect="实验室单卡就能迭代巡检要用的新技能；论文还演示了世界模型对湿滑地面打滑的预测。",
        nums=["1 张 GPU", "约 3 小时", "12.9 万段动作"],
        clips=[
            ("真机短片", f"{SM}/media/real/film-1080.mp4", None),
            ("世界模型预测打滑", f"{SM}/media/world-model/wm_slip.mp4", None),
            ("关掉策略：预测摔倒", f"{SM}/media/world-model/wm_off.mp4", None),
            ("真机翻滚", f"{SM}/media/real/real_grove-roll-wide.mp4", None),
        ],
        page=f"{SM}/",
        links=[("论文", "https://arxiv.org/abs/2610.28480"), ("项目主页", f"{SM}/"),
               ("网页里试玩", f"{SM}/demo/")],
    ),
    dict(
        id="beyondmimic", name="BeyondMimic", group="base",
        venue="Science Robotics 2026", org="UC Berkeley、Stanford",
        one="开源了一套能在真机上稳定做出侧手翻、腾空转体、冲刺等高动态动作的跟踪训练配方，"
            "并用引导扩散把这些动作组合成导航、避障等下游任务。",
        analogy="先把每个高难动作练扎实，再把它们串成一门能完成任务的“动作语言”。",
        inspect="开源配方可以直接复现；引导扩散的思路，适合把“走到点位、蹲下、检查”串成一个任务。",
        nums=["配方全开源", "引导扩散", "真机侧手翻"],
        clips=[
            ("集锦", f"{BM}/static/videos/teaser.mp4", None),
            ("真机动作跟踪", f"{BM}/static/videos/motion_tracking/prep_IMG_2643.mp4", None),
            ("真机动作跟踪 2", f"{BM}/static/videos/motion_tracking/prep_IMG_2669.mp4", None),
            ("扩散策略做任务", f"{BM}/static/videos/diffusion/prep_C1883.mp4", None),
        ],
        page=f"{BM}/",
        links=[("论文", "https://arxiv.org/abs/2508.08241"), ("项目主页", f"{BM}/"),
               ("代码", "https://github.com/HybridRobotics/whole_body_tracking"),
               ("完整视频 YouTube", "https://youtu.be/RS_MtKVIAzY")],
    ),
    dict(
        id="humanoid-gpt", name="Humanoid-GPT", group="base",
        venue="CVPR 2026", org="清华、银河通用、北航等",
        one="在 20 亿帧重定向动作上先训练多个强化学习专家，再蒸馏进一个 GPT 式因果 Transformer，"
            "零样本跟踪训练中没见过的高动态动作，并给出数据与模型规模的 scaling law。",
        analogy="像大语言模型读遍文本：把能找到的人体动作都喂进去，模型越大，越会举一反三。",
        inspect="项目页有安防巡逻、消杀作业等真机演示，和巡检工况很接近。",
        nums=["20 亿帧动作", "Transformer", "4090 上推理 <1.5 ms"],
        clips=[
            ("总览", f"{HG}/videos/home.mp4", None),
            ("安防巡逻", f"{HG}/videos/demo/security.mp4", None),
            ("消杀作业", f"{HG}/videos/demo/disinfection.mp4", None),
            ("平衡动作：对比 SONIC", f"{HG}/videos/conpare_with_sonic/4.mp4", None),
        ],
        page=f"{HG}/",
        links=[("论文", "https://arxiv.org/abs/2606.03985"), ("项目主页", f"{HG}/"),
               ("代码", "https://github.com/GalaxyGeneralRobotics/Humanoid-GPT")],
    ),
    dict(
        id="bfm-zero", name="BFM-Zero", group="base",
        venue="ICLR 2026", org="CMU、Meta",
        one="走无监督强化学习路线，把动作、目标姿态和奖励放进同一个潜空间；"
            "一个策略不用重训，就能做动作跟踪、到达目标姿态和奖励优化。",
        analogy="不背具体动作，而是学一张“身体能力地图”：给它动作、目标或奖励，它都能在地图上找到对应的做法。",
        inspect="演示了躯干负重 4 kg 后的少样本适配，以及被拽倒后的自然恢复，和背负设备、现场磕碰很像。",
        nums=["零样本多任务", "无监督强化学习", "4 kg 负载适配"],
        clips=[
            ("总览", f"{BFM}/resources/head/head_new_firefox_720p.mp4", None),
            ("抗扰与恢复", f"{BFM}/resources/disturbance/disturbance-1_firefox_720p.mp4", None),
            ("负重 4 kg：适配前", f"{BFM}/resources/adaptation/before_adapt_firefox_720p.mp4", None),
            ("负重 4 kg：适配后", f"{BFM}/resources/adaptation/after_adapt_firefox_720p.mp4", None),
        ],
        page=f"{BFM}/",
        links=[("论文", "https://arxiv.org/abs/2511.04131"), ("项目主页", f"{BFM}/"),
               ("代码", "https://github.com/LeCAR-Lab/BFM-Zero"),
               ("完整视频 YouTube", "https://www.youtube.com/watch?v=jYI-LZNvUY4")],
    ),
    dict(
        id="gmr", name="GMR", fullname="Retargeting Matters", group="data",
        venue="ICRA 2026", org="Stanford",
        one="系统评估了重定向质量对跟踪策略的影响；开源的实时重定向工具已支持十几款人形（含轮式人形），"
            "Any2Any 也是用它为各个本体准备训练数据。",
        analogy="给机器人量体裁衣：把人的动作改成机器人身体做得出来的样子。裁得好不好，直接决定后面学得好不好。",
        inspect="同一段巡检动作，可以很快适配到不同本体；还支持从单目视频里提取人体动作。",
        nums=["实时", "十几款人形", "支持视频输入"],
        clips=[
            ("同一段动作，适配多款机器人", f"{TW}/images/GMR.mp4", None),
        ],
        clip_note="视频来自 TWIST2 项目页的相关工作介绍",
        page="https://github.com/YanjieZe/GMR",
        links=[("论文", "https://arxiv.org/abs/2510.02252"), ("代码", "https://github.com/YanjieZe/GMR")],
    ),
    dict(
        id="omniretarget", name="OmniRetarget", group="data",
        venue="ICRA 2026 最佳会议论文", org="Amazon FAR、MIT、UC Berkeley 等",
        one="用交互网格在重定向时保住机器人与物体、地形之间的接触和空间关系，只需很少的奖励设计就能训出"
            "移动操作和场景交互策略，还能把一条示范扩增到不同本体、地形和物体。",
        analogy="不只抄姿势，还要保住“手扶在哪、脚踩在哪”这些接触关系。",
        inspect="爬平台、搬箱子这类带接触的动作数据，是开柜门、跨障碍的基础。",
        nums=["ICRA 最佳论文", "交互网格", "数据集开源"],
        clips=[
            ("集锦", f"{OR}/static/website_videos/flagship.mp4", None),
            ("攀上平台", f"{OR}/static/website_videos/climb_1.mp4", None),
            ("搬箱子", f"{OR}/static/website_videos/box_1.mp4", None),
            ("地形高度扩增", f"{OR}/static/website_videos/terrain_aug_1.mp4", None),
        ],
        page=f"{OR}/",
        links=[("论文", "https://arxiv.org/abs/2509.26633"), ("项目主页", f"{OR}/"),
               ("代码", "https://github.com/amazon-far/holosoma"),
               ("数据集", "https://huggingface.co/datasets/omniretarget/OmniRetarget_Dataset"),
               ("完整视频 YouTube", "https://www.youtube.com/watch?v=5ZYFTfGHH8Q")],
    ),
    dict(
        id="asap", name="ASAP", group="real",
        venue="RSS 2025", org="CMU 等",
        one="先在仿真中预训练，再用真机数据训练一个 delta 动作模型来补偿动力学差异，"
            "把它接回仿真器后再微调策略。",
        analogy="先在模拟器里练，再拿真机录下的“偏差”去修正模拟器，让模拟器越来越像真机。",
        inspect="把真机误差闭环回仿真，是巡检机器人长期稳定运行的必修课。",
        nums=["delta 动作模型", "仿真到真机对齐", "代码开源"],
        clips=[
            ("集锦", f"{ASAP}/static/videos/Hero-ASAP-Video-Website-Hero-16-9-202502031028-1080P.mp4", None),
            ("踢腿：对齐前", f"{ASAP}/static/videos/ASAP-Website-Kick-BeforeASAP-1080P.mp4", None),
            ("踢腿：对齐后", f"{ASAP}/static/videos/ASAP-Website-Kick-AfterASAP-1080P.mp4", None),
            ("侧跳 1.3 m", f"{ASAP}/static/videos/ASAP-Motion-SideJump_level3-1080P.mp4", None),
        ],
        page=f"{ASAP}/",
        links=[("论文", "https://arxiv.org/abs/2502.01143"), ("项目主页", f"{ASAP}/"),
               ("代码", "https://github.com/LeCAR-Lab/ASAP"),
               ("完整视频 YouTube", "https://www.youtube.com/watch?v=tu7LSNYWDTs")],
    ),
    dict(
        id="mosaic", name="MOSAIC", group="real",
        venue="arXiv 2026", org="智源研究院 BAAI 等",
        one="针对通用跟踪器在真机长时间遥操作中不够稳的问题，用少量接口数据做残差适配；"
            "PICO VR 和诺亦腾动捕两套适配模型都已开源。",
        analogy="通用跟踪器是主干，每换一种遥操作设备，就插上一个小小的“适配器”。",
        inspect="现场出现异常、需要远程接管时，可以直接参考；代码、模型和数据集都已开源。",
        nums=["残差适配", "PICO / 诺亦腾", "模型与数据开源"],
        clips=[
            ("总览", f"{MO}/static/website_videos/mosaic.mp4", None),
            ("VR：蹲姿移动", f"{MO}/static/website_videos/VR%20%E5%8E%9F%E5%9C%B0%E8%B9%B2%E5%A7%BF.mp4", None),
            ("动捕服：深蹲", f"{MO}/static/website_videos/noitom%20%E6%B7%B1%E8%B9%B2.mp4", None),
            ("回放：倒地起身", f"{MO}/static/website_videos/off%20lafan%20%E5%80%92%E5%9C%B0.mp4", None),
        ],
        page=f"{MO}/",
        links=[("论文", "https://arxiv.org/abs/2602.08594"), ("项目主页", f"{MO}/"),
               ("代码", "https://github.com/BAAI-Humanoid/MOSAIC"),
               ("数据集", "https://huggingface.co/datasets/BAAI-Humanoid/MOSAIC_Dataset")],
    ),
    dict(
        id="twist2", name="TWIST2", group="real",
        venue="ICRA 2026", org="Amazon FAR、Stanford 等",
        one="用 PICO 4U VR 加一个约 250 美元的二自由度机器人脖子，做到免动捕的便携全身遥操作采数"
            "（15 分钟约 100 条示范），系统和数据集都已开源。",
        analogy="戴上 VR 就能“附身”机器人：成本低、随走随采，攒下大量全身操作示范。",
        inspect="可以用同样的方式在巡检现场批量采示范，为以后的自主策略攒数据。",
        nums=["$250 机器人脖子", "15 分钟 100 条", "系统与数据开源"],
        clips=[
            ("便携采集", f"{TW}/videos/portable/twist2_portable_edit.webm", None),
            ("长程遥操作：叠毛巾", f"{TW}/videos/fold/fold2_16x.webm", None),
            ("自主策略：踢物体", f"{TW}/videos/kickt/kickt_1.webm", None),
        ],
        page=f"{TW}/",
        links=[("论文", "https://arxiv.org/abs/2511.02832"), ("项目主页", f"{TW}/"),
               ("代码", "https://github.com/amazon-far/TWIST2"), ("数据集", "https://twist-data.github.io/"),
               ("B 站视频", "https://www.bilibili.com/video/BV18c1bB5EQp/")],
    ),
    dict(
        id="resmimic", name="ResMimic", group="real",
        venue="arXiv 2025", org="Amazon FAR 等",
        one="以大规模人体动作训出的通用跟踪策略为底座，再学一个轻量的残差策略来处理物体交互，"
            "在 G1 真机上完成搬箱、抬椅等全身移动操作。",
        analogy="老师傅（通用跟踪器）把动作框架定好，徒弟（残差策略）只负责“对准物体、用好力气”的那部分修正。",
        inspect="开柜门、拧阀门、搬工具箱，本质上也是“通用动作 + 精细修正”。",
        nums=["两阶段残差", "全身接触", "代码开源"],
        clips=[
            ("自主连续搬箱", f"{RM}/static/videos/continuous2.mp4", None),
            ("单膝跪地抬箱", f"{RM}/static/videos/kneel.mov", None),
            ("被推之后的反应", f"{RM}/static/videos/reactive.mp4", None),
            ("底座和残差的动作对比", f"{RM}/static/videos/action_viz.mp4", None),
        ],
        page=f"{RM}/",
        links=[("论文", "https://arxiv.org/abs/2510.05070"), ("项目主页", f"{RM}/"),
               ("代码", "https://github.com/amazon-far/ResMimic"),
               ("完整视频 YouTube", "https://www.youtube.com/watch?v=dadOH-TpbRk")],
    ),
    dict(
        id="mjlab", name="mjlab", group="tool",
        venue="arXiv 2026", org="UC Berkeley 等",
        one="沿用 Isaac Lab 的模块化环境 API，底层换成 MuJoCo Warp 的 GPU 仿真；"
            "一条命令就能装好，自带速度跟踪、运动模仿等参考任务。",
        analogy="一个开箱即用的训练场：装好就能让 G1 学走路、学模仿。",
        inspect="新同学第一周就能跑通运动模仿；和 SuperMimic 用的是同一个仿真底座 MuJoCo Warp。",
        nums=["一条命令安装", "MuJoCo Warp", "训练需 NVIDIA GPU"],
        clips=[],
        page="https://mujocolab.github.io/mjlab/",
        links=[("论文", "https://arxiv.org/abs/2601.22074"), ("文档", "https://mujocolab.github.io/mjlab/"),
               ("代码", "https://github.com/mujocolab/mjlab")],
    ),
]

WORK = {w["id"]: w for w in WORKS}

# 1 ── five-minute primer: the pipeline (a real sequence, so it is numbered)
STAGES = [
    ("motion", "人的动作", "教材",
     "动捕、网络视频、VR 遥操作，都能变成机器人的学习素材。", ["humanoid-gpt", "twist2"]),
    ("retarget", "重定向", "量体裁衣",
     "人和机器人身高、关节都不一样，要先把动作改成机器人做得出来的版本。", ["gmr", "omniretarget"]),
    ("sim", "仿真里练", "虚拟训练馆",
     "成千上万个机器人在 GPU 上同时练，摔倒不心疼。关键是练得快、练得像。", ["mjlab", "supermimic"]),
    ("tracker", "通用跟踪器", "机器人的小脑",
     "给它一段目标动作，它负责稳稳做出来。现在的趋势是做大、做通用。",
     ["sonic", "beyondmimic", "humanoid-gpt", "bfm-zero"]),
    ("command", "上层指挥", "大脑和遥控器",
     "VR 遥操作、规划器或 VLA 大模型，告诉小脑下一步做什么；碰到物体时再加一点修正。",
     ["twist2", "mosaic", "resmimic"]),
    ("real", "真机落地", "下场比赛",
     "仿真和现实总有差距，需要对齐和适配；换一台机器人，还要迁移。", ["asap", "any2any"]),
]

# 3 ── inspection needs; 1–6 are the numbered checkpoints in the hero scene
NEEDS = [
    dict(n=1, title="台阶、格栅与湿滑地面", crop="30 250 330 270",
         desc="巡检路线上常有台阶和排水格栅，雨天或冲洗后地面湿滑。走得稳，是一切的前提。",
         ability="稳健行走、抗扰动、仿真到真机对齐", works=["sonic", "supermimic", "asap", "bfm-zero"], topics=["f"]),
    dict(n=2, title="低矮管道与狭窄通道", crop="300 150 330 330",
         desc="管廊、配电房里常有低矮的管架和窄通道，要弯腰、下蹲，甚至匍匐通过。",
         ability="低姿态行进：下蹲、跪姿、匍匐", works=["sonic", "bfm-zero", "omniretarget"], topics=["c", "a"]),
    dict(n=3, title="低位仪表读数", crop="590 220 270 280",
         desc="压力表、油位计常装在低处，机器人要稳稳蹲下或跪下，让相机正对表盘。",
         ability="稳定的蹲姿和跪姿，以及头部视角控制", works=["sonic", "mosaic", "twist2"], topics=["c", "d"]),
    dict(n=4, title="开柜门、按按钮、拧阀门", crop="800 150 330 340",
         desc="这类任务要求“对准物体、用对力气”，是全身移动操作的典型场景。",
         ability="全身移动操作、接触控制", works=["resmimic", "omniretarget", "beyondmimic"], topics=["e"]),
    dict(n=5, title="背负检测设备", crop="330 230 220 200",
         desc="背上加装相机、传感器或工具箱后，质量和重心都会变，原来的控制器可能就不稳了。",
         ability="负载变化下的快速适配", works=["bfm-zero", "any2any", "resmimic"], topics=["a", "f"]),
    dict(n=6, title="异常时远程接管", crop="950 0 250 150",
         desc="遇到自主处理不了的情况，由值班人员戴 VR 或动捕服远程接管，同时把这段操作录成训练数据。",
         ability="全身遥操作、设备适配、数据闭环", works=["mosaic", "twist2", "sonic"], topics=["d"]),
    dict(n=7, title="本体换代、多个型号", crop=None,
         desc="巡检本体会迭代，也会有多个型号，不能每换一次就从头训练一遍。",
         ability="跨本体迁移、通用重定向", works=["any2any", "gmr"], topics=["a"]),
    dict(n=8, title="新技能要训得快", crop=None,
         desc="现场需求常变，新动作、新任务要能在实验室的算力下快速训出来、快速验证。",
         ability="高效训练、快速迭代", works=["supermimic", "mjlab"], topics=["b"]),
]

CHOICES = [("algo", "推公式、改算法"), ("robot", "调真机、跑实验"), ("data", "做数据、建基准"), ("sys", "搭系统、做工具")]

TOPICS = [
    dict(id="a", title="让通用控制器“换身体”", sub="巡检本体迁移与负载适配", level=2, tags=["algo", "robot"],
         one="把 SONIC 这类在 G1 上训好的通用跟踪器，低成本迁移到巡检用的人形本体上，"
             "并适应背负设备带来的质量和重心变化。",
         problem="不同关节构型怎么对齐？负载变化以后，哪些模块需要适配，能不能在线自适应？",
         read=["sonic", "any2any", "gmr", "bfm-zero"],
         month=["跑通 Any2Any 开源代码，复现 SONIC 迁移到新本体的仿真流程",
                "在仿真里给机器人背上不同重量的负载，看跟踪性能怎么变差",
                "对比 LoRA 适配和全参数微调的效果与代价"],
         output="负载和本体感知的迁移方法，以及真机行走、下蹲、跪地的前后对比。"),
    dict(id="b", title="单卡也能训的世界模型跟踪器", sub="沿 SuperMimic 的路线往下走", level=3, tags=["algo"],
         one="用可微世界模型替代大部分仿真采样，让实验室单卡就能训练、迭代巡检要用的新技能。",
         problem="遇到接触和摩擦突变（比如湿滑地面）时，世界模型的误差怎么控制？地形、负载能不能作为条件放进世界模型？",
         read=["supermimic", "beyondmimic", "mjlab", "humanoid-gpt"],
         month=["在 mjlab 里跑通 G1 运动模仿，熟悉 MuJoCo Warp",
                "试玩 SuperMimic 网页 demo，精读方法和算力对比",
                "在一个小动作集上，实现“世界模型 + 短时域反传”的最小版本"],
         output="训练效率明显提升的方法论文，以及单卡训出的巡检动作策略。"),
    dict(id="c", title="巡检动作库与重定向数据引擎", sub="把巡检动作变成可复用的数据", level=1, tags=["data"],
         one="系统整理巡检常用动作，从动捕和视频里采集，用 GMR、OmniRetarget 重定向到自家本体，"
             "做成可复用的数据集和评测基准。",
         problem="怎么评价重定向的质量？手扶柜门、脚踩台阶这类带接触的动作，怎么保住接触关系？",
         read=["gmr", "omniretarget", "humanoid-gpt"],
         month=["用 GMR 把 LAFAN1 里的动作重定向到 G1",
                "录 10 段巡检动作（下蹲读表、跪姿检查、侧身通过等），动捕或单目视频都可以",
                "用跟踪策略检验每段数据能不能做出来，整理失败原因"],
         output="巡检动作数据集与评测基准，适合写数据类论文。"),
    dict(id="d", title="遥操作接管与数据闭环", sub="人兜底，机器人越用越会", level=1, tags=["sys", "robot", "data"],
         one="现场遇到异常时，由人戴 VR 或动捕服远程接管；接管的过程同时变成训练数据。",
         problem="不同遥操作设备的误差怎么快速适配？有延迟时全身怎么保持稳定？接管数据怎么用来训练自主策略？",
         read=["mosaic", "twist2", "sonic"],
         month=["跑通 MOSAIC 开源的跟踪模型和 PICO 适配器",
                "搭一套 VR 全身遥操作链路，测端到端延迟",
                "采 20 条巡检示范，比如蹲下查看、开柜门"],
         output="一套能用的接管系统和示范数据集，偏系统类论文。"),
    dict(id="e", title="巡检中的全身移动操作", sub="开柜门、拧阀门、搬工具箱", level=2, tags=["algo", "robot"],
         one="在通用跟踪器之上学残差策略，完成开柜门、按按钮、拧阀门、搬工具箱这类要“对准物体、用对力气”的动作。",
         problem="怎么加入物体感知和接触，又不破坏原有的通用动作能力？多个动作怎么串成一个完整任务？",
         read=["resmimic", "omniretarget", "beyondmimic", "sonic"],
         month=["复现 ResMimic 的一个搬箱任务",
                "在仿真里搭一个带柜门和把手的环境",
                "设计接触奖励，做出“走近、抓把手、开门”的最小原型"],
         output="巡检操作技能库，方法论文加真机演示。"),
    dict(id="f", title="真机鲁棒性：湿滑、负载与跌倒", sub="让机器人在现场扛得住意外", level=2, tags=["robot", "algo"],
         one="围绕巡检现场最常见的意外，比如湿滑地面、负载变化、被碰撞、摔倒后起身，研究仿真到真机的对齐和恢复能力。",
         problem="怎样用最少的真机数据修正仿真？摔倒后能不能自然起身，继续完成任务？",
         read=["asap", "bfm-zero", "supermimic", "mosaic"],
         month=["复现 ASAP 的 delta 动作模型流程（代码已开源）",
                "设计一套巡检扰动测试：湿滑、推搡、负载",
                "在仿真里量化现有跟踪器的失败模式，挑一个突破口"],
         output="鲁棒性评测基准和改进方法，以及真机长时间运行的数据。"),
]
TOPIC = {t["id"]: t for t in TOPICS}
LEVELS = {1: "入门", 2: "进阶", 3: "挑战"}

WEEKS = [
    ("看懂基本盘", "读 SONIC 和 BeyondMimic；在 mjlab 里跑通 G1 运动模仿；试玩 SuperMimic 的网页 demo。"),
    ("动手做数据", "用 GMR 把 LAFAN1 的动作重定向到 G1；再录一段自己的“下蹲读表”，从视频提取动作后重定向。"),
    ("训练与评测", "在 mjlab 里训练这段动作的跟踪策略，再放到 MuJoCo 里做 sim2sim，记录失败案例；读 ASAP 和 MOSAIC。"),
    ("定课题", "按兴趣精读对应课题的 2–3 篇论文，写一页开题设想：要解决什么问题、方法思路、在巡检场景里怎么验证。"),
]

GLOSSARY = [
    ("全身运控（WBC）", "同时协调腿、躯干和手臂，让机器人既保持平衡、又完成动作。"),
    ("运动跟踪", "给定一段参考动作，策略输出关节指令，让机器人尽量跟着做出来。"),
    ("重定向", "把人体动作转换成机器人关节能执行的动作。"),
    ("强化学习（RL）", "在仿真里不断试错，根据奖励改进策略。"),
    ("sim2real", "把仿真里训好的策略部署到真机，并缩小两者之间的差距。"),
    ("跨本体迁移", "把一台机器人上训好的策略，用到另一台结构不同的机器人上。"),
    ("世界模型", "学一个预测“下一刻会怎样”的模型，可以在里面“想象”着练习。"),
    ("残差学习", "在已有策略的输出上，再学一个小的修正量。"),
    ("LoRA", "只训练少量低秩参数来适配新任务的微调方法，原模型基本不动。"),
    ("VLA", "视觉-语言-动作模型：看图、听指令，然后输出动作。"),
    ("遥操作", "人通过 VR、动捕服等设备实时操控机器人。"),
    ("行为基础模型（BFM）", "预训练好的通用行为策略，可以用不同方式“提示”它完成不同任务。"),
]

RESOURCES = [
    ("先跑起来", [
        ("mjlab 文档", "https://mujocolab.github.io/mjlab/"),
        ("SuperMimic 网页 demo", f"{SM}/demo/"),
        ("GMR 重定向工具", "https://github.com/YanjieZe/GMR"),
    ]),
    ("开源数据", [
        ("TWIST2 遥操作数据", "https://twist-data.github.io/"),
        ("MOSAIC 数据集", "https://huggingface.co/datasets/BAAI-Humanoid/MOSAIC_Dataset"),
        ("OmniRetarget 数据集", "https://huggingface.co/datasets/omniretarget/OmniRetarget_Dataset"),
    ]),
    ("开源代码", [
        ("SONIC（GR00T-WholeBodyControl）", "https://github.com/NVlabs/GR00T-WholeBodyControl"),
        ("BeyondMimic", "https://github.com/HybridRobotics/whole_body_tracking"),
        ("Any2Any", "https://github.com/Ming827/any2any_sonic2Oli"),
        ("BFM-Zero", "https://github.com/LeCAR-Lab/BFM-Zero"),
        ("ASAP", "https://github.com/LeCAR-Lab/ASAP"),
        ("MOSAIC", "https://github.com/BAAI-Humanoid/MOSAIC"),
        ("TWIST2", "https://github.com/amazon-far/TWIST2"),
        ("ResMimic", "https://github.com/amazon-far/ResMimic"),
        ("Humanoid-GPT", "https://github.com/GalaxyGeneralRobotics/Humanoid-GPT"),
    ]),
]
