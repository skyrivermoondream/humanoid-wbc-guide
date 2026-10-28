"""All page copy and links, in English and Chinese.

Every translatable string is written as T("English", "中文") so both languages sit side by
side; edit them together. Facts were checked against each paper's arXiv page or official
project page (Oct 2026). Videos are embedded straight from the official project pages;
nothing is re-hosted.
"""


def T(en, zh):
    return {"en": en, "zh": zh}


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

LINK = {
    "paper": T("Paper", "论文"),
    "page": T("Project page", "项目主页"),
    "code": T("Code", "代码"),
    "data": T("Dataset", "数据集"),
    "yt": T("Full video (YouTube)", "完整视频 YouTube"),
    "bili": T("Video (Bilibili)", "B 站视频"),
    "demo": T("Try it in the browser", "网页里试玩"),
    "docs": T("Docs", "文档"),
}

GROUPS = [
    ("onegs", T("ONE-G focus", "ONE-G 正在跟进")),
    ("base", T("Tracking foundations", "通用跟踪底座")),
    ("data", T("Retargeting and data", "重定向与跨本体数据")),
    ("real", T("Real-robot deployment", "真机落地")),
    ("tool", T("Starter tools", "上手工具")),
]

WORKS = [
    dict(
        id="sonic", name="SONIC", group="onegs",
        venue=T("Science Robotics", "Science Robotics"), org=T("NVIDIA", "NVIDIA"),
        one=T("Treats motion tracking as a foundation task that scales: the policy grows to 42M parameters "
              "and learns from 700 hours of motion capture, and the same policy takes VR teleoperation, "
              "human video and VLA models as input.",
              "把运动跟踪当作可规模化的基础任务，模型扩到 42M 参数、数据扩到 700 小时动捕，"
              "同一个策略可以接 VR 遥操作、人体视频和 VLA 等多种输入。"),
        analogy=T("A cerebellum that has watched 700 hours of human movement. Whatever sits on top, "
                  "a joystick, a video or a large model, only has to say which motion comes next.",
                  "像看过 700 小时人体动作的“小脑”：上层不管是遥控器、视频还是大模型，"
                  "只需要告诉它下一步做什么动作。"),
        inspect=T("Squatting, kneeling and crawling, all common on inspection rounds, are shown on the real "
                  "robot, and an operator can take over through VR.",
                  "下蹲、跪地、匍匐这些巡检常用姿态都有真机演示，还能直接接 VR 遥操作接管。"),
        nums=[T("42M parameters", "42M 参数"), T("700 h of motion capture", "700 小时动捕"),
              T("One policy, many inputs", "一个策略，多种输入")],
        clips=[
            (T("Highlights", "能力集锦"), f"{SONIC}/static/videos/teaser_title.mp4", f"{SONIC}/static/images/teaser_poster.png"),
            (T("Squat", "下蹲"), f"{SONIC}/static/videos/planner/squat_crawl/planner_squat.mp4", None),
            (T("Kneel", "跪地"), f"{SONIC}/static/videos/planner/squat_crawl/planner_kneeling.mp4", None),
            (T("Elbow crawl", "肘部匍匐"), f"{SONIC}/static/videos/planner/squat_crawl/planner_elbow_crawling.mp4", None),
            (T("VR whole-body teleop", "VR 全身遥操作"), f"{SONIC}/static/videos/teleop/vr_wholebody/wbt.mp4", None),
            (T("Robust tracking", "抗扰跟踪"), f"{SONIC}/static/videos/tracking/robust1.mp4", None),
        ],
        page=f"{SONIC}/",
        links=[("paper", "https://arxiv.org/abs/2511.07820"), ("page", f"{SONIC}/"),
               ("code", "https://github.com/NVlabs/GR00T-WholeBodyControl")],
    ),
    dict(
        id="any2any", name="Any2Any", group="onegs",
        venue=T("arXiv 2026", "arXiv 2026"), org=T("LimX Dynamics", "逐际动力 LimX Dynamics"),
        one=T("First aligns the kinematic interfaces of the source and target humanoids, then adds LoRA "
              "only to the modules most sensitive to dynamics. With about 1% of the compute and data, it "
              "moves SONIC from the Unitree G1 to the LimX Oli and Luna.",
              "先对齐源、目标人形的运动学接口，再只在动力学敏感的模块上加 LoRA，"
              "用约 1% 的算力和数据，把 G1 上预训练的 SONIC 迁移到 LimX Oli 和 Luna。"),
        analogy=T("An experienced driver switching cars: the skill stays, they only need to get used to "
                  "the new throttle and brakes.",
                  "像老司机换车：驾驶技术都在，只要重新适应新车油门和刹车的手感。"),
        inspect=T("Your own inspection humanoid doesn't have to be trained from scratch, and the same idea, "
                  "adapting only the dynamics part, could absorb the extra mass of a gear backpack.",
                  "自家巡检本体不必从零训练；背负设备带来的质量变化，也可以借鉴这种“只调动力学部分”的思路。"),
        nums=[T("~1% of compute and data", "约 1% 算力和数据"), T("Trains ~5% of parameters", "只训约 5% 参数"),
              T("Tested on 4 humanoids", "4 款人形验证")],
        clips=[
            (T("Transfer overview", "迁移效果总览"), f"{A2A}/vedio_data/cover_video.mp4", None),
            (T("Oli, real robot: running", "Oli 真机：跑步"), f"{A2A}/vedio_data/sim2real-sonic3/sonic_G12oli-7-running.mp4", None),
            (T("Oli, real robot: loco-manipulation", "Oli 真机：移动操作"), f"{A2A}/vedio_data/sim2real-sonic3/sonic_G12oli-8-locomanipulation.mp4", None),
            (T("Many robots in one simulation", "多本体同时仿真"), f"{A2A}/vedio_data/simulation_multi/multiWBT-window-normal-speed.mp4", None),
        ],
        page=f"{A2A}/",
        links=[("paper", "https://arxiv.org/abs/2605.23733"), ("page", f"{A2A}/"),
               ("code", "https://github.com/Ming827/any2any_sonic2Oli")],
    ),
    dict(
        id="supermimic", name="SuperMimic", group="onegs",
        venue=T("CoRL 2026", "CoRL 2026"), org=T("UC Berkeley", "UC Berkeley"),
        one=T("Fits one differentiable world model to simulator data and trains the policy by "
              "backpropagating through it. On a single GPU it beats the return of the released SONIC "
              "checkpoint in about 3 hours (SONIC trained for 7 days on 128 GPUs), and it runs zero-shot "
              "on a real G1.",
              "用一个可微世界模型拟合仿真器数据，再对它反传梯度来训练策略；单卡 3 小时就超过了 SONIC "
              "发布版的回报（SONIC 用 128 卡训了 7 天），并零样本部署到 G1 真机。"),
        analogy=T("A gymnast rehearsing in their head: first build a feel for the physics, then practise "
                  "in imagination, and use the real simulator only to keep that feel calibrated.",
                  "像体操运动员在脑子里预演：先学会一套“物理直觉”，再在想象里反复练，真实仿真只用来校准。"),
        inspect=T("A lab with one GPU can iterate on new inspection skills. The paper also shows the world "
                  "model predicting a slide when the floor turns slippery.",
                  "实验室单卡就能迭代巡检要用的新技能；论文还演示了世界模型对湿滑地面打滑的预测。"),
        nums=[T("1 GPU", "1 张 GPU"), T("~3 hours", "约 3 小时"), T("129k motions", "12.9 万段动作")],
        clips=[
            (T("Real-robot film", "真机短片"), f"{SM}/media/real/film-1080.mp4", None),
            (T("World model predicts a slip", "世界模型预测打滑"), f"{SM}/media/world-model/wm_slip.mp4", None),
            (T("Policy off: predicting the fall", "关掉策略：预测摔倒"), f"{SM}/media/world-model/wm_off.mp4", None),
            (T("Real-robot roll", "真机翻滚"), f"{SM}/media/real/real_grove-roll-wide.mp4", None),
        ],
        page=f"{SM}/",
        links=[("paper", "https://arxiv.org/abs/2610.28480"), ("page", f"{SM}/"),
               ("demo", f"{SM}/demo/")],
    ),
    dict(
        id="beyondmimic", name="BeyondMimic", group="base",
        venue=T("Science Robotics 2026", "Science Robotics 2026"), org=T("UC Berkeley, Stanford", "UC Berkeley、Stanford"),
        one=T("Open-sources a training recipe that reliably runs highly dynamic motions such as cartwheels, "
              "jumping spins and sprints on real hardware, and uses guided diffusion to compose those "
              "motions into tasks like navigation and obstacle avoidance.",
              "开源了一套能在真机上稳定做出侧手翻、腾空转体、冲刺等高动态动作的跟踪训练配方，"
              "并用引导扩散把这些动作组合成导航、避障等下游任务。"),
        analogy=T("Master each hard move first, then string the moves into a motion language that can "
                  "carry out a task.",
                  "先把每个高难动作练扎实，再把它们串成一门能完成任务的“动作语言”。"),
        inspect=T("The open recipe can be reproduced as is, and guided diffusion fits chaining “walk to the "
                  "checkpoint, crouch, inspect” into one task.",
                  "开源配方可以直接复现；引导扩散的思路，适合把“走到点位、蹲下、检查”串成一个任务。"),
        nums=[T("Fully open recipe", "配方全开源"), T("Guided diffusion", "引导扩散"),
              T("Real-robot cartwheels", "真机侧手翻")],
        clips=[
            (T("Highlights", "集锦"), f"{BM}/static/videos/teaser.mp4", None),
            (T("Real-robot tracking", "真机动作跟踪"), f"{BM}/static/videos/motion_tracking/prep_IMG_2643.mp4", None),
            (T("Real-robot tracking 2", "真机动作跟踪 2"), f"{BM}/static/videos/motion_tracking/prep_IMG_2669.mp4", None),
            (T("Diffusion policy on tasks", "扩散策略做任务"), f"{BM}/static/videos/diffusion/prep_C1883.mp4", None),
        ],
        page=f"{BM}/",
        links=[("paper", "https://arxiv.org/abs/2508.08241"), ("page", f"{BM}/"),
               ("code", "https://github.com/HybridRobotics/whole_body_tracking"),
               ("yt", "https://youtu.be/RS_MtKVIAzY")],
    ),
    dict(
        id="humanoid-gpt", name="Humanoid-GPT", group="base",
        venue=T("CVPR 2026", "CVPR 2026"), org=T("Tsinghua, Galbot, Beihang, et al.", "清华、银河通用、北航等"),
        one=T("Trains many RL experts on 2 billion frames of retargeted motion, then distills them into "
              "one GPT-style causal Transformer. It tracks unseen, highly dynamic motions zero-shot and "
              "reports scaling laws for data and model size.",
              "在 20 亿帧重定向动作上先训练多个强化学习专家，再蒸馏进一个 GPT 式因果 Transformer，"
              "零样本跟踪训练中没见过的高动态动作，并给出数据与模型规模的 scaling law。"),
        analogy=T("A large language model for movement: feed it all the human motion you can find, and the "
                  "bigger it gets, the better it generalizes.",
                  "像大语言模型读遍文本：把能找到的人体动作都喂进去，模型越大，越会举一反三。"),
        inspect=T("The project page has real-robot demos of security patrol and disinfection work, both "
                  "close to inspection duty.",
                  "项目页有安防巡逻、消杀作业等真机演示，和巡检工况很接近。"),
        nums=[T("2B frames of motion", "20 亿帧动作"), T("Transformer", "Transformer"),
              T("<1.5 ms inference on an RTX 4090", "4090 上推理 <1.5 ms")],
        clips=[
            (T("Overview", "总览"), f"{HG}/videos/home.mp4", None),
            (T("Security patrol", "安防巡逻"), f"{HG}/videos/demo/security.mp4", None),
            (T("Disinfection", "消杀作业"), f"{HG}/videos/demo/disinfection.mp4", None),
            (T("Balance: compared with SONIC", "平衡动作：对比 SONIC"), f"{HG}/videos/conpare_with_sonic/4.mp4", None),
        ],
        page=f"{HG}/",
        links=[("paper", "https://arxiv.org/abs/2606.03985"), ("page", f"{HG}/"),
               ("code", "https://github.com/GalaxyGeneralRobotics/Humanoid-GPT")],
    ),
    dict(
        id="bfm-zero", name="BFM-Zero", group="base",
        venue=T("ICLR 2026", "ICLR 2026"), org=T("CMU, Meta", "CMU、Meta"),
        one=T("Uses unsupervised RL to put motions, goal poses and rewards into one shared latent space, "
              "so a single policy can track motions, reach goal poses and optimize rewards without "
              "retraining.",
              "走无监督强化学习路线，把动作、目标姿态和奖励放进同一个潜空间；"
              "一个策略不用重训，就能做动作跟踪、到达目标姿态和奖励优化。"),
        analogy=T("Instead of memorizing moves, it learns a map of what the body can do. Give it a motion, "
                  "a goal or a reward, and it finds the matching spot on the map.",
                  "不背具体动作，而是学一张“身体能力地图”：给它动作、目标或奖励，它都能在地图上找到对应的做法。"),
        inspect=T("It shows few-shot adaptation to a 4 kg payload on the torso and a natural recovery after "
                  "being pulled to the ground, much like carrying gear and getting bumped on site.",
                  "演示了躯干负重 4 kg 后的少样本适配，以及被拽倒后的自然恢复，和背负设备、现场磕碰很像。"),
        nums=[T("Zero-shot, many tasks", "零样本多任务"), T("Unsupervised RL", "无监督强化学习"),
              T("4 kg payload adaptation", "4 kg 负载适配")],
        clips=[
            (T("Overview", "总览"), f"{BFM}/resources/head/head_new_firefox_720p.mp4", None),
            (T("Disturbance and recovery", "抗扰与恢复"), f"{BFM}/resources/disturbance/disturbance-1_firefox_720p.mp4", None),
            (T("4 kg payload: before adaptation", "负重 4 kg：适配前"), f"{BFM}/resources/adaptation/before_adapt_firefox_720p.mp4", None),
            (T("4 kg payload: after adaptation", "负重 4 kg：适配后"), f"{BFM}/resources/adaptation/after_adapt_firefox_720p.mp4", None),
        ],
        page=f"{BFM}/",
        links=[("paper", "https://arxiv.org/abs/2511.04131"), ("page", f"{BFM}/"),
               ("code", "https://github.com/LeCAR-Lab/BFM-Zero"),
               ("yt", "https://www.youtube.com/watch?v=jYI-LZNvUY4")],
    ),
    dict(
        id="gmr", name="GMR", fullname="Retargeting Matters", group="data",
        venue=T("ICRA 2026", "ICRA 2026"), org=T("Stanford", "Stanford"),
        one=T("Measures how retargeting quality affects tracking policies. Its open-source real-time "
              "retargeter supports more than a dozen humanoids, including wheeled ones, and Any2Any uses "
              "it to prepare training data for each robot.",
              "系统评估了重定向质量对跟踪策略的影响；开源的实时重定向工具已支持十几款人形（含轮式人形），"
              "Any2Any 也是用它为各个本体准备训练数据。"),
        analogy=T("Tailoring for robots: rework a human motion into something the robot's body can actually "
                  "do. How well it fits decides how well everything downstream learns.",
                  "给机器人量体裁衣：把人的动作改成机器人身体做得出来的样子。裁得好不好，直接决定后面学得好不好。"),
        inspect=T("One inspection motion can be adapted to different robots quickly, and it can pull human "
                  "motion out of ordinary monocular video.",
                  "同一段巡检动作，可以很快适配到不同本体；还支持从单目视频里提取人体动作。"),
        nums=[T("Real time", "实时"), T("Over a dozen humanoids", "十几款人形"), T("Video input", "支持视频输入")],
        clips=[
            (T("One motion, many robots", "同一段动作，适配多款机器人"), f"{TW}/images/GMR.mp4", None),
        ],
        clip_note=T("Video from the related-work section of the TWIST2 project page",
                    "视频来自 TWIST2 项目页的相关工作介绍"),
        page="https://github.com/YanjieZe/GMR",
        links=[("paper", "https://arxiv.org/abs/2510.02252"), ("code", "https://github.com/YanjieZe/GMR")],
    ),
    dict(
        id="omniretarget", name="OmniRetarget", group="data",
        venue=T("ICRA 2026 Best Paper", "ICRA 2026 最佳论文"), org=T("Amazon FAR, MIT, UC Berkeley, et al.", "Amazon FAR、MIT、UC Berkeley 等"),
        one=T("Uses an interaction mesh to keep the contacts and spatial relations between robot, objects "
              "and terrain during retargeting. With very little reward design it trains loco-manipulation "
              "and scene-interaction policies, and it can expand one demonstration across robots, terrains "
              "and objects.",
              "用交互网格在重定向时保住机器人与物体、地形之间的接触和空间关系，只需很少的奖励设计就能训出"
              "移动操作和场景交互策略，还能把一条示范扩增到不同本体、地形和物体。"),
        analogy=T("Copy more than the pose: keep where the hand rests and where the foot lands.",
                  "不只抄姿势，还要保住“手扶在哪、脚踩在哪”这些接触关系。"),
        inspect=T("Contact-rich data such as climbing onto platforms and carrying boxes is the groundwork for "
                  "opening cabinets and getting over obstacles.",
                  "爬平台、搬箱子这类带接触的动作数据，是开柜门、跨障碍的基础。"),
        nums=[T("ICRA Best Conference Paper", "ICRA 最佳论文"), T("Interaction mesh", "交互网格"),
              T("Open dataset", "数据集开源")],
        clips=[
            (T("Highlights", "集锦"), f"{OR}/static/website_videos/flagship.mp4", None),
            (T("Climbing a platform", "攀上平台"), f"{OR}/static/website_videos/climb_1.mp4", None),
            (T("Carrying a box", "搬箱子"), f"{OR}/static/website_videos/box_1.mp4", None),
            (T("Terrain-height augmentation", "地形高度扩增"), f"{OR}/static/website_videos/terrain_aug_1.mp4", None),
        ],
        page=f"{OR}/",
        links=[("paper", "https://arxiv.org/abs/2509.26633"), ("page", f"{OR}/"),
               ("code", "https://github.com/amazon-far/holosoma"),
               ("data", "https://huggingface.co/datasets/omniretarget/OmniRetarget_Dataset"),
               ("yt", "https://www.youtube.com/watch?v=5ZYFTfGHH8Q")],
    ),
    dict(
        id="asap", name="ASAP", group="real",
        venue=T("RSS 2025", "RSS 2025"), org=T("CMU, et al.", "CMU 等"),
        one=T("Pre-trains in simulation, then trains a delta action model on real-robot data to make up "
              "for the dynamics gap, and fine-tunes the policy with that model plugged back into the "
              "simulator.",
              "先在仿真中预训练，再用真机数据训练一个 delta 动作模型来补偿动力学差异，"
              "把它接回仿真器后再微调策略。"),
        analogy=T("Practise in the simulator, then use what the real robot recorded about its own errors to "
                  "correct the simulator until it behaves like the real thing.",
                  "先在模拟器里练，再拿真机录下的“偏差”去修正模拟器，让模拟器越来越像真机。"),
        inspect=T("Feeding real-robot errors back into simulation is essential for an inspection robot that "
                  "has to run reliably for a long time.",
                  "把真机误差闭环回仿真，是巡检机器人长期稳定运行的必修课。"),
        nums=[T("Delta action model", "delta 动作模型"), T("Sim-to-real alignment", "仿真到真机对齐"),
              T("Open code", "代码开源")],
        clips=[
            (T("Highlights", "集锦"), f"{ASAP}/static/videos/Hero-ASAP-Video-Website-Hero-16-9-202502031028-1080P.mp4", None),
            (T("Kick: before ASAP", "踢腿：对齐前"), f"{ASAP}/static/videos/ASAP-Website-Kick-BeforeASAP-1080P.mp4", None),
            (T("Kick: after ASAP", "踢腿：对齐后"), f"{ASAP}/static/videos/ASAP-Website-Kick-AfterASAP-1080P.mp4", None),
            (T("Side jump, 1.3 m", "侧跳 1.3 m"), f"{ASAP}/static/videos/ASAP-Motion-SideJump_level3-1080P.mp4", None),
        ],
        page=f"{ASAP}/",
        links=[("paper", "https://arxiv.org/abs/2502.01143"), ("page", f"{ASAP}/"),
               ("code", "https://github.com/LeCAR-Lab/ASAP"),
               ("yt", "https://www.youtube.com/watch?v=tu7LSNYWDTs")],
    ),
    dict(
        id="mosaic", name="MOSAIC", group="real",
        venue=T("arXiv 2026", "arXiv 2026"), org=T("BAAI (Beijing Academy of AI), et al.", "智源研究院 BAAI 等"),
        one=T("Generalist trackers often get shaky during long teleoperation sessions on a real robot. "
              "MOSAIC adds a residual adapter trained on a small amount of device-specific data, and the "
              "adapters for PICO VR and Noitom motion capture are both open-source.",
              "针对通用跟踪器在真机长时间遥操作中不够稳的问题，用少量接口数据做残差适配；"
              "PICO VR 和诺亦腾动捕两套适配模型都已开源。"),
        analogy=T("The generalist tracker is the trunk; each new teleoperation device just plugs in a small "
                  "adapter.",
                  "通用跟踪器是主干，每换一种遥操作设备，就插上一个小小的“适配器”。"),
        inspect=T("A direct reference for remote takeover when something goes wrong on site. Code, models "
                  "and dataset are all open.",
                  "现场出现异常、需要远程接管时，可以直接参考；代码、模型和数据集都已开源。"),
        nums=[T("Residual adapter", "残差适配"), T("PICO and Noitom", "PICO / 诺亦腾"),
              T("Open models and data", "模型与数据开源")],
        clips=[
            (T("Overview", "总览"), f"{MO}/static/website_videos/mosaic.mp4", None),
            (T("VR: moving in a squat", "VR：蹲姿移动"), f"{MO}/static/website_videos/VR%20%E5%8E%9F%E5%9C%B0%E8%B9%B2%E5%A7%BF.mp4", None),
            (T("Mocap suit: deep squat", "动捕服：深蹲"), f"{MO}/static/website_videos/noitom%20%E6%B7%B1%E8%B9%B2.mp4", None),
            (T("Replay: fall and get up", "回放：倒地起身"), f"{MO}/static/website_videos/off%20lafan%20%E5%80%92%E5%9C%B0.mp4", None),
        ],
        page=f"{MO}/",
        links=[("paper", "https://arxiv.org/abs/2602.08594"), ("page", f"{MO}/"),
               ("code", "https://github.com/BAAI-Humanoid/MOSAIC"),
               ("data", "https://huggingface.co/datasets/BAAI-Humanoid/MOSAIC_Dataset")],
    ),
    dict(
        id="twist2", name="TWIST2", group="real",
        venue=T("ICRA 2026", "ICRA 2026"), org=T("Amazon FAR, Stanford, et al.", "Amazon FAR、Stanford 等"),
        one=T("Pairs a PICO 4U VR headset with a robot neck that costs about $250 for portable, mocap-free "
              "whole-body teleoperation and data collection, about 100 demonstrations in 15 minutes. The "
              "system and the dataset are open-source.",
              "用 PICO 4U VR 加一个约 250 美元的二自由度机器人脖子，做到免动捕的便携全身遥操作采数"
              "（15 分钟约 100 条示范），系统和数据集都已开源。"),
        analogy=T("Put on the headset and you are inside the robot: cheap, portable, and quick to pile up "
                  "whole-body demonstrations.",
                  "戴上 VR 就能“附身”机器人：成本低、随走随采，攒下大量全身操作示范。"),
        inspect=T("The same setup could collect demonstrations on an inspection site in bulk, building up the "
                  "data for future autonomous policies.",
                  "可以用同样的方式在巡检现场批量采示范，为以后的自主策略攒数据。"),
        nums=[T("$250 robot neck", "$250 机器人脖子"), T("100 demos in 15 min", "15 分钟 100 条"),
              T("Open system and data", "系统与数据开源")],
        clips=[
            (T("Portable collection", "便携采集"), f"{TW}/videos/portable/twist2_portable_edit.webm", None),
            (T("Long-horizon teleop: folding towels", "长程遥操作：叠毛巾"), f"{TW}/videos/fold/fold2_16x.webm", None),
            (T("Autonomous policy: kicking an object", "自主策略：踢物体"), f"{TW}/videos/kickt/kickt_1.webm", None),
        ],
        page=f"{TW}/",
        links=[("paper", "https://arxiv.org/abs/2511.02832"), ("page", f"{TW}/"),
               ("code", "https://github.com/amazon-far/TWIST2"), ("data", "https://twist-data.github.io/"),
               ("bili", "https://www.bilibili.com/video/BV18c1bB5EQp/")],
    ),
    dict(
        id="resmimic", name="ResMimic", group="real",
        venue=T("arXiv 2025", "arXiv 2025"), org=T("Amazon FAR, et al.", "Amazon FAR 等"),
        one=T("Starts from a general motion-tracking policy trained on large-scale human motion and learns a "
              "lightweight residual policy for object interaction, carrying boxes and lifting chairs with "
              "the whole body on a real G1.",
              "以大规模人体动作训出的通用跟踪策略为底座，再学一个轻量的残差策略来处理物体交互，"
              "在 G1 真机上完成搬箱、抬椅等全身移动操作。"),
        analogy=T("The master, a general tracker, sets the overall movement; the apprentice, a residual "
                  "policy, only corrects how to line up with the object and how hard to push.",
                  "老师傅（通用跟踪器）把动作框架定好，徒弟（残差策略）只负责“对准物体、用好力气”的那部分修正。"),
        inspect=T("Opening a cabinet, turning a valve or carrying a toolbox is also general motion plus a fine "
                  "correction.",
                  "开柜门、拧阀门、搬工具箱，本质上也是“通用动作 + 精细修正”。"),
        nums=[T("Two-stage residual", "两阶段残差"), T("Whole-body contact", "全身接触"), T("Open code", "代码开源")],
        clips=[
            (T("Lifting boxes autonomously, one after another", "自主连续搬箱"), f"{RM}/static/videos/continuous2.mp4", None),
            (T("Kneel and lift a box", "单膝跪地抬箱"), f"{RM}/static/videos/kneel.mov", None),
            (T("Reacting to a push", "被推之后的反应"), f"{RM}/static/videos/reactive.mp4", None),
            (T("Base and residual actions", "底座和残差的动作对比"), f"{RM}/static/videos/action_viz.mp4", None),
        ],
        page=f"{RM}/",
        links=[("paper", "https://arxiv.org/abs/2510.05070"), ("page", f"{RM}/"),
               ("code", "https://github.com/amazon-far/ResMimic"),
               ("yt", "https://www.youtube.com/watch?v=dadOH-TpbRk")],
    ),
    dict(
        id="mjlab", name="mjlab", group="tool",
        venue=T("arXiv 2026", "arXiv 2026"), org=T("UC Berkeley, et al.", "UC Berkeley 等"),
        one=T("Keeps Isaac Lab's modular environment API but runs on MuJoCo Warp GPU simulation underneath. "
              "It installs with one command and ships reference tasks for velocity tracking and motion "
              "imitation.",
              "沿用 Isaac Lab 的模块化环境 API，底层换成 MuJoCo Warp 的 GPU 仿真；"
              "一条命令就能装好，自带速度跟踪、运动模仿等参考任务。"),
        analogy=T("A ready-to-use training ground: install it and a G1 can start learning to walk and "
                  "imitate.",
                  "一个开箱即用的训练场：装好就能让 G1 学走路、学模仿。"),
        inspect=T("New students can run motion imitation in their first week, on MuJoCo Warp, the same "
                  "simulator SuperMimic uses.",
                  "新同学第一周就能跑通运动模仿；和 SuperMimic 用的是同一个仿真底座 MuJoCo Warp。"),
        nums=[T("One-command install", "一条命令安装"), T("MuJoCo Warp", "MuJoCo Warp"),
              T("Training needs an NVIDIA GPU", "训练需 NVIDIA GPU")],
        clips=[],
        page="https://mujocolab.github.io/mjlab/",
        links=[("paper", "https://arxiv.org/abs/2601.22074"), ("docs", "https://mujocolab.github.io/mjlab/"),
               ("code", "https://github.com/mujocolab/mjlab")],
    ),
]

WORK = {w["id"]: w for w in WORKS}

# 1 ── five-minute primer: the pipeline (a real sequence, so it is numbered)
STAGES = [
    ("motion", T("Human motion", "人的动作"), T("a textbook", "教材"),
     T("Motion capture, online video and VR teleoperation can all become learning material for the robot.",
       "动捕、网络视频、VR 遥操作，都能变成机器人的学习素材。"), ["humanoid-gpt", "twist2"]),
    ("retarget", T("Retargeting", "重定向"), T("tailoring", "量体裁衣"),
     T("Humans and robots differ in size and joints, so a motion first has to be reworked into a version the "
       "robot can perform.",
       "人和机器人身高、关节都不一样，要先把动作改成机器人做得出来的版本。"), ["gmr", "omniretarget"]),
    ("sim", T("Practice in simulation", "仿真里练"), T("a virtual gym", "虚拟训练馆"),
     T("Thousands of robots practise at once on a GPU, and falling costs nothing. The goal is training that "
       "is fast and true to life.",
       "成千上万个机器人在 GPU 上同时练，摔倒不心疼。关键是练得快、练得像。"), ["mjlab", "supermimic"]),
    ("tracker", T("General tracker", "通用跟踪器"), T("the robot's cerebellum", "机器人的小脑"),
     T("Give it a target motion and it performs it steadily. The trend is to make it bigger and more general.",
       "给它一段目标动作，它负责稳稳做出来。现在的趋势是做大、做通用。"),
     ["sonic", "beyondmimic", "humanoid-gpt", "bfm-zero"]),
    ("command", T("High-level commands", "上层指挥"), T("the brain and the remote", "大脑和遥控器"),
     T("VR teleoperation, a planner or a VLA model tells the cerebellum what to do next, with a small "
       "correction added when it touches objects.",
       "VR 遥操作、规划器或 VLA 大模型，告诉小脑下一步做什么；碰到物体时再加一点修正。"),
     ["twist2", "mosaic", "resmimic"]),
    ("real", T("Real robot", "真机落地"), T("game day", "下场比赛"),
     T("Simulation and reality never match exactly, so you align and adapt. A new robot also means "
       "transferring the policy.",
       "仿真和现实总有差距，需要对齐和适配；换一台机器人，还要迁移。"), ["asap", "any2any"]),
]

# 3 ── inspection needs; 1–6 are the numbered checkpoints in the hero scene
NEEDS = [
    dict(n=1, crop="10 208 360 270",
         title=T("Steps, gratings and wet floors", "台阶、格栅与湿滑地面"),
         desc=T("Inspection routes are full of steps and drainage gratings, and floors get slippery after rain "
                "or washing. Walking steadily comes before everything else.",
                "巡检路线上常有台阶和排水格栅，雨天或冲洗后地面湿滑。走得稳，是一切的前提。"),
         ability=T("Robust walking, disturbance rejection, sim-to-real alignment", "稳健行走、抗扰动、仿真到真机对齐"),
         works=["sonic", "supermimic", "asap", "bfm-zero"], topics=["f"]),
    dict(n=2, crop="262 190 388 291",
         title=T("Low pipes and narrow passages", "低矮管道与狭窄通道"),
         desc=T("Utility tunnels and switch rooms often have low pipe racks and tight passages, so the robot "
                "has to bend, crouch or even crawl through.",
                "管廊、配电房里常有低矮的管架和窄通道，要弯腰、下蹲，甚至匍匐通过。"),
         ability=T("Low-posture locomotion: crouching, kneeling, crawling", "低姿态行进：下蹲、跪姿、匍匐"),
         works=["sonic", "bfm-zero", "omniretarget"], topics=["c", "a"]),
    dict(n=3, crop="586 262 286 214",
         title=T("Reading low-mounted gauges", "低位仪表读数"),
         desc=T("Pressure gauges and oil-level indicators are often mounted low. The robot has to crouch or "
                "kneel steadily and point its camera straight at the dial.",
                "压力表、油位计常装在低处，机器人要稳稳蹲下或跪下，让相机正对表盘。"),
         ability=T("Stable squatting and kneeling, plus head and camera control", "稳定的蹲姿和跪姿，以及头部视角控制"),
         works=["sonic", "mosaic", "twist2"], topics=["c", "d"]),
    dict(n=4, crop="780 165 420 315",
         title=T("Opening cabinets, pressing buttons, turning valves", "开柜门、按按钮、拧阀门"),
         desc=T("These tasks need the robot to line up with an object and push with the right force, the classic "
                "case of whole-body loco-manipulation.",
                "这类任务要求“对准物体、用对力气”，是全身移动操作的典型场景。"),
         ability=T("Whole-body loco-manipulation, contact control", "全身移动操作、接触控制"),
         works=["resmimic", "omniretarget", "beyondmimic"], topics=["e"]),
    dict(n=5, crop="330 230 220 200",
         title=T("Carrying inspection gear", "背负检测设备"),
         desc=T("Once a camera, sensors or a toolbox go on the robot's back, its mass and center of mass change, "
                "and the original controller may no longer be stable.",
                "背上加装相机、传感器或工具箱后，质量和重心都会变，原来的控制器可能就不稳了。"),
         ability=T("Fast adaptation to payload changes", "负载变化下的快速适配"),
         works=["bfm-zero", "any2any", "resmimic"], topics=["a", "f"]),
    dict(n=6, crop="960 0 240 180",
         title=T("Remote takeover when things go wrong", "异常时远程接管"),
         desc=T("When autonomy can't handle a situation, an operator takes over remotely with VR or a mocap suit, "
                "and the session is recorded as training data.",
                "遇到自主处理不了的情况，由值班人员戴 VR 或动捕服远程接管，同时把这段操作录成训练数据。"),
         ability=T("Whole-body teleoperation, device adaptation, a data loop", "全身遥操作、设备适配、数据闭环"),
         works=["mosaic", "twist2", "sonic"], topics=["d"]),
    dict(n=7, crop=None,
         title=T("New robot generations and models", "本体换代、多个型号"),
         desc=T("Inspection robots get upgraded and come in several models; retraining from scratch each time "
                "is not an option.",
                "巡检本体会迭代，也会有多个型号，不能每换一次就从头训练一遍。"),
         ability=T("Cross-embodiment transfer, general retargeting", "跨本体迁移、通用重定向"),
         works=["any2any", "gmr"], topics=["a"]),
    dict(n=8, crop=None,
         title=T("Training new skills fast", "新技能要训得快"),
         desc=T("Requirements on site keep changing, so new motions and tasks must be trainable and testable "
                "quickly on a lab's compute budget.",
                "现场需求常变，新动作、新任务要能在实验室的算力下快速训出来、快速验证。"),
         ability=T("Efficient training, fast iteration", "高效训练、快速迭代"),
         works=["supermimic", "mjlab"], topics=["b"]),
]

CHOICES = [
    ("algo", T("Math and algorithms", "推公式、改算法")),
    ("robot", T("Real robots and experiments", "调真机、跑实验")),
    ("data", T("Data and benchmarks", "做数据、建基准")),
    ("sys", T("Systems and tools", "搭系统、做工具")),
]

TOPICS = [
    dict(id="a", level=2, tags=["algo", "robot"],
         title=T("Give a general controller a new body", "让通用控制器“换身体”"),
         sub=T("Transfer to inspection robots and adapt to payloads", "巡检本体迁移与负载适配"),
         one=T("Transfer a general tracker trained on the G1, such as SONIC, to an inspection humanoid at low "
               "cost, and adapt it to the mass and center-of-mass shift a gear backpack brings.",
               "把 SONIC 这类在 G1 上训好的通用跟踪器，低成本迁移到巡检用的人形本体上，"
               "并适应背负设备带来的质量和重心变化。"),
         problem=T("How do you align different joint layouts? When the payload changes, which modules need "
                   "adapting, and can the policy adapt online?",
                   "不同关节构型怎么对齐？负载变化以后，哪些模块需要适配，能不能在线自适应？"),
         read=["sonic", "any2any", "gmr", "bfm-zero"],
         month=[T("Run the open-source Any2Any code and reproduce the simulated transfer of SONIC to a new robot",
                  "跑通 Any2Any 开源代码，复现 SONIC 迁移到新本体的仿真流程"),
                T("Load the robot with backpacks of different weights in simulation and measure how tracking degrades",
                  "在仿真里给机器人背上不同重量的负载，看跟踪性能怎么变差"),
                T("Compare LoRA adaptation with full fine-tuning on quality and cost",
                  "对比 LoRA 适配和全参数微调的效果与代价")],
         output=T("A payload- and embodiment-aware transfer method, plus before-and-after results for walking, "
                  "squatting and kneeling on the real robot.",
                  "负载和本体感知的迁移方法，以及真机行走、下蹲、跪地的前后对比。")),
    dict(id="b", level=3, tags=["algo"],
         title=T("A world-model tracker you can train on one GPU", "单卡也能训的世界模型跟踪器"),
         sub=T("Push further along the SuperMimic route", "沿 SuperMimic 的路线往下走"),
         one=T("Replace most simulator sampling with a differentiable world model, so a lab can train and "
               "iterate on new inspection skills with a single GPU.",
               "用可微世界模型替代大部分仿真采样，让实验室单卡就能训练、迭代巡检要用的新技能。"),
         problem=T("How do you keep world-model error in check when contact and friction change suddenly, as on "
                   "a wet floor? Can terrain and payload become inputs to the world model?",
                   "遇到接触和摩擦突变（比如湿滑地面）时，世界模型的误差怎么控制？地形、负载能不能作为条件放进世界模型？"),
         read=["supermimic", "beyondmimic", "mjlab", "humanoid-gpt"],
         month=[T("Run G1 motion imitation in mjlab and get familiar with MuJoCo Warp",
                  "在 mjlab 里跑通 G1 运动模仿，熟悉 MuJoCo Warp"),
                T("Try the SuperMimic web demo and read the method and compute comparison closely",
                  "试玩 SuperMimic 网页 demo，精读方法和算力对比"),
                T("Implement a minimal “world model plus short-horizon backprop” on a small motion set",
                  "在一个小动作集上，实现“世界模型 + 短时域反传”的最小版本")],
         output=T("A methods paper with a clear gain in training efficiency, plus inspection-motion policies "
                  "trained on one GPU.",
                  "训练效率明显提升的方法论文，以及单卡训出的巡检动作策略。")),
    dict(id="c", level=1, tags=["data"],
         title=T("An inspection motion library and retargeting data engine", "巡检动作库与重定向数据引擎"),
         sub=T("Turn inspection motions into reusable data", "把巡检动作变成可复用的数据"),
         one=T("Catalogue the motions inspection needs, capture them from mocap and video, retarget them to "
               "your robot with GMR and OmniRetarget, and package the result as a reusable dataset and "
               "benchmark.",
               "系统整理巡检常用动作，从动捕和视频里采集，用 GMR、OmniRetarget 重定向到自家本体，"
               "做成可复用的数据集和评测基准。"),
         problem=T("How do you judge retargeting quality? For contact-heavy motions, like a hand on a cabinet "
                   "door or a foot on a step, how do you keep the contacts?",
                   "怎么评价重定向的质量？手扶柜门、脚踩台阶这类带接触的动作，怎么保住接触关系？"),
         read=["gmr", "omniretarget", "humanoid-gpt"],
         month=[T("Retarget LAFAN1 motions to the G1 with GMR", "用 GMR 把 LAFAN1 里的动作重定向到 G1"),
                T("Record 10 inspection motions, such as squatting to read a gauge, kneeling to inspect and "
                  "side-stepping through a gap, with mocap or monocular video",
                  "录 10 段巡检动作（下蹲读表、跪姿检查、侧身通过等），动捕或单目视频都可以"),
                T("Check whether a tracking policy can perform each clip, and work out the cause of each failure",
                  "用跟踪策略检验每段数据能不能做出来，整理失败原因")],
         output=T("An inspection motion dataset and benchmark, a good fit for a dataset paper.",
                  "巡检动作数据集与评测基准，适合写数据类论文。")),
    dict(id="d", level=1, tags=["sys", "robot", "data"],
         title=T("Teleoperated takeover and a data loop", "遥操作接管与数据闭环"),
         sub=T("People handle the hard cases, and the robot learns from each one", "人兜底，机器人越用越会"),
         one=T("When something unusual happens on site, an operator takes over remotely with VR or a mocap suit, "
               "and every takeover becomes training data.",
               "现场遇到异常时，由人戴 VR 或动捕服远程接管；接管的过程同时变成训练数据。"),
         problem=T("How do you adapt quickly to the errors of different teleoperation devices? How does the whole "
                   "body stay stable under latency? How do you train autonomous policies from takeover data?",
                   "不同遥操作设备的误差怎么快速适配？有延迟时全身怎么保持稳定？接管数据怎么用来训练自主策略？"),
         read=["mosaic", "twist2", "sonic"],
         month=[T("Run MOSAIC's open-source tracker and PICO adapter", "跑通 MOSAIC 开源的跟踪模型和 PICO 适配器"),
                T("Build a VR whole-body teleoperation pipeline and measure end-to-end latency",
                  "搭一套 VR 全身遥操作链路，测端到端延迟"),
                T("Collect 20 inspection demonstrations, such as crouching to look and opening a cabinet",
                  "采 20 条巡检示范，比如蹲下查看、开柜门")],
         output=T("A working takeover system and a demonstration dataset, leaning toward a systems paper.",
                  "一套能用的接管系统和示范数据集，偏系统类论文。")),
    dict(id="e", level=2, tags=["algo", "robot"],
         title=T("Whole-body loco-manipulation for inspection", "巡检中的全身移动操作"),
         sub=T("Opening cabinets, turning valves, carrying toolboxes", "开柜门、拧阀门、搬工具箱"),
         one=T("Learn residual policies on top of a general tracker for tasks that need lining up with an "
               "object and pushing with the right force: opening cabinets, pressing buttons, turning valves "
               "and carrying toolboxes.",
               "在通用跟踪器之上学残差策略，完成开柜门、按按钮、拧阀门、搬工具箱这类要“对准物体、用对力气”的动作。"),
         problem=T("How do you add object perception and contact without breaking the general motion skills? How "
                   "do you chain several motions into one complete task?",
                   "怎么加入物体感知和接触，又不破坏原有的通用动作能力？多个动作怎么串成一个完整任务？"),
         read=["resmimic", "omniretarget", "beyondmimic", "sonic"],
         month=[T("Reproduce one box-carrying task from ResMimic", "复现 ResMimic 的一个搬箱任务"),
                T("Build a simulated scene with a cabinet door and handle", "在仿真里搭一个带柜门和把手的环境"),
                T("Design contact rewards and build a minimal “approach, grab the handle, open the door” prototype",
                  "设计接触奖励，做出“走近、抓把手、开门”的最小原型")],
         output=T("A library of inspection manipulation skills: a methods paper plus real-robot demos.",
                  "巡检操作技能库，方法论文加真机演示。")),
    dict(id="f", level=2, tags=["robot", "algo"],
         title=T("Real-robot robustness: wet floors, payloads and falls", "真机鲁棒性：湿滑、负载与跌倒"),
         sub=T("Help the robot cope with surprises on site", "让机器人在现场扛得住意外"),
         one=T("Study sim-to-real alignment and recovery around the most common surprises on an inspection "
               "route: wet floors, payload changes, bumps, and getting up after a fall.",
               "围绕巡检现场最常见的意外，比如湿滑地面、负载变化、被碰撞、摔倒后起身，研究仿真到真机的对齐和恢复能力。"),
         problem=T("How do you correct the simulator with as little real-robot data as possible? Can the robot get "
                   "up naturally after a fall and finish the task?",
                   "怎样用最少的真机数据修正仿真？摔倒后能不能自然起身，继续完成任务？"),
         read=["asap", "bfm-zero", "supermimic", "mosaic"],
         month=[T("Reproduce ASAP's delta action model pipeline (the code is open)",
                  "复现 ASAP 的 delta 动作模型流程（代码已开源）"),
                T("Design an inspection disturbance test covering slippery floors, pushes and payloads",
                  "设计一套巡检扰动测试：湿滑、推搡、负载"),
                T("Quantify how current trackers fail in simulation and pick one failure to attack",
                  "在仿真里量化现有跟踪器的失败模式，挑一个突破口")],
         output=T("A robustness benchmark and an improved method, plus data from long real-robot runs.",
                  "鲁棒性评测基准和改进方法，以及真机长时间运行的数据。")),
]
TOPIC = {t["id"]: t for t in TOPICS}
LEVELS = {1: T("starter", "入门"), 2: T("intermediate", "进阶"), 3: T("challenging", "挑战")}

WEEKS = [
    (T("Learn the basics", "看懂基本盘"),
     T("Read SONIC and BeyondMimic, run G1 motion imitation in mjlab, and try the SuperMimic web demo.",
       "读 SONIC 和 BeyondMimic；在 mjlab 里跑通 G1 运动模仿；试玩 SuperMimic 的网页 demo。")),
    (T("Make some data", "动手做数据"),
     T("Retarget LAFAN1 motions to the G1 with GMR, then film yourself squatting to read a gauge, extract the "
       "motion from the video and retarget it.",
       "用 GMR 把 LAFAN1 的动作重定向到 G1；再录一段自己的“下蹲读表”，从视频提取动作后重定向。")),
    (T("Train and evaluate", "训练与评测"),
     T("Train a tracking policy for that motion in mjlab, run a sim-to-sim check in MuJoCo and log the failure "
       "cases. Read ASAP and MOSAIC.",
       "在 mjlab 里训练这段动作的跟踪策略，再放到 MuJoCo 里做 sim2sim，记录失败案例；读 ASAP 和 MOSAIC。")),
    (T("Choose a topic", "定课题"),
     T("Read the 2–3 papers behind the topic you like, then write a one-page proposal: the problem, the "
       "approach, and how you would test it in an inspection setting.",
       "按兴趣精读对应课题的 2–3 篇论文，写一页开题设想：要解决什么问题、方法思路、在巡检场景里怎么验证。")),
]

GLOSSARY = [
    (T("Whole-body control (WBC)", "全身运控（WBC）"), "全身运控",
     T("Coordinating the legs, torso and arms at once, so the robot keeps its balance while it moves.",
       "同时协调腿、躯干和手臂，让机器人既保持平衡、又完成动作。")),
    (T("Motion tracking", "运动跟踪"), "运动跟踪",
     T("Given a reference motion, the policy outputs joint commands so the robot follows it as closely as "
       "possible.", "给定一段参考动作，策略输出关节指令，让机器人尽量跟着做出来。")),
    (T("Retargeting", "重定向"), "重定向",
     T("Converting human motion into motion the robot's joints can execute.", "把人体动作转换成机器人关节能执行的动作。")),
    (T("Reinforcement learning (RL)", "强化学习（RL）"), "强化学习",
     T("Improving a policy by trial and error in simulation, guided by rewards.", "在仿真里不断试错，根据奖励改进策略。")),
    (T("Sim-to-real", "sim2real"), "仿真到真机",
     T("Deploying a policy trained in simulation on a real robot, and closing the gap between the two.",
       "把仿真里训好的策略部署到真机，并缩小两者之间的差距。")),
    (T("Cross-embodiment transfer", "跨本体迁移"), "跨本体迁移",
     T("Reusing a policy trained on one robot on another robot with a different body.",
       "把一台机器人上训好的策略，用到另一台结构不同的机器人上。")),
    (T("World model", "世界模型"), "世界模型",
     T("A model that predicts what happens next, so a policy can practise inside it, in imagination.",
       "学一个预测“下一刻会怎样”的模型，可以在里面“想象”着练习。")),
    (T("Residual learning", "残差学习"), "残差学习",
     T("Learning a small correction on top of an existing policy's output.", "在已有策略的输出上，再学一个小的修正量。")),
    (T("LoRA", "LoRA"), "低秩适配",
     T("A fine-tuning method that trains a few low-rank parameters and leaves the original model mostly "
       "untouched.", "只训练少量低秩参数来适配新任务的微调方法，原模型基本不动。")),
    (T("VLA", "VLA"), "视觉-语言-动作模型",
     T("Vision-language-action model: it looks, takes an instruction, then outputs actions.",
       "视觉-语言-动作模型：看图、听指令，然后输出动作。")),
    (T("Teleoperation", "遥操作"), "遥操作",
     T("A person controls the robot in real time through VR, a mocap suit or a similar device.",
       "人通过 VR、动捕服等设备实时操控机器人。")),
    (T("Behavior foundation model (BFM)", "行为基础模型（BFM）"), "行为基础模型",
     T("A pre-trained general behavior policy that can be prompted in different ways to do different tasks.",
       "预训练好的通用行为策略，可以用不同方式“提示”它完成不同任务。")),
]

RESOURCES = [
    (T("Run something first", "先跑起来"), [
        (T("mjlab docs", "mjlab 文档"), "https://mujocolab.github.io/mjlab/"),
        (T("SuperMimic web demo", "SuperMimic 网页 demo"), f"{SM}/demo/"),
        (T("GMR retargeting tool", "GMR 重定向工具"), "https://github.com/YanjieZe/GMR"),
    ]),
    (T("Open data", "开源数据"), [
        (T("TWIST2 teleoperation data", "TWIST2 遥操作数据"), "https://twist-data.github.io/"),
        (T("MOSAIC dataset", "MOSAIC 数据集"), "https://huggingface.co/datasets/BAAI-Humanoid/MOSAIC_Dataset"),
        (T("OmniRetarget dataset", "OmniRetarget 数据集"), "https://huggingface.co/datasets/omniretarget/OmniRetarget_Dataset"),
    ]),
    (T("Open code", "开源代码"), [
        (T("SONIC (GR00T-WholeBodyControl)", "SONIC（GR00T-WholeBodyControl）"), "https://github.com/NVlabs/GR00T-WholeBodyControl"),
        (T("BeyondMimic", "BeyondMimic"), "https://github.com/HybridRobotics/whole_body_tracking"),
        (T("Any2Any", "Any2Any"), "https://github.com/Ming827/any2any_sonic2Oli"),
        (T("BFM-Zero", "BFM-Zero"), "https://github.com/LeCAR-Lab/BFM-Zero"),
        (T("ASAP", "ASAP"), "https://github.com/LeCAR-Lab/ASAP"),
        (T("MOSAIC", "MOSAIC"), "https://github.com/BAAI-Humanoid/MOSAIC"),
        (T("TWIST2", "TWIST2"), "https://github.com/amazon-far/TWIST2"),
        (T("ResMimic", "ResMimic"), "https://github.com/amazon-far/ResMimic"),
        (T("Humanoid-GPT", "Humanoid-GPT"), "https://github.com/GalaxyGeneralRobotics/Humanoid-GPT"),
    ]),
]

# ── interface text
UI = dict(
    title=T("Humanoid Whole-Body Control: A Topic Map for Graduate Students", "人形机器人全身运控：研究生课题地图"),
    desc=T("Videos and plain-language notes on 13 recent works in humanoid whole-body control, mapped onto an "
           "inspection scenario, with six candidate graduate research topics. Compiled by ONE-G.",
           "13 个人形全身运控前沿工作的真机视频与通俗讲解，对照巡检场景给出 6 个可选研究生课题。ONE-G（万机）整理。"),
    og_desc=T("13 recent works, inspection needs, six candidate topics and a first-month plan.",
              "13 个前沿工作、巡检场景需求、6 个可选课题和第一个月上手路线。"),
    brand=T("Humanoid WBC", "人形全身运控"),
    brand_sub=T("Topic map", "课题地图"),
    nav=[T("Basics", "看懂"), T("Papers", "论文"), T("Route", "场景"), T("Topics", "课题"), T("Start", "上手")],
    nav_label=T("Page sections", "页面导航"),
    lang_label=T("Language", "语言"),
    to_dark=T("Switch to dark mode", "切换到深色模式"),
    to_light=T("Switch to light mode", "切换到浅色模式"),
    h1=T("Humanoid Whole-Body Control", "人形机器人全身运控"),
    h1_sub=T("A topic map for graduate students", "研究生课题地图"),
    lede=T("For graduate students co-supervised with ONE-G. Get the big picture in five minutes, watch 13 recent "
           "works in action, then pick a topic by walking through what an inspection robot has to do.",
           "写给联合培养的研究生同学。先用五分钟看懂这个方向，再看 13 个前沿工作的视频和讲解，最后对照巡检现场，挑一个想做的课题。"),
    spec_k=T("The direction in one sentence:", "方向一句话："),
    spec_v=T("use a large-scale motion-tracking model as the humanoid's general-purpose “cerebellum”, and build "
             "efficient training, cross-embodiment transfer and real-robot deployment around it.",
             "以规模化运动跟踪模型作为人形机器人的通用“小脑”，围绕它做高效训练、跨本体迁移和真机落地。"),
    spec_meta=T("Compiled by ONE-G. Current as of October 2026.", "ONE-G（万机）整理，信息截至 2026 年 10 月。"),
    scene_title=T("Inspection route: robots step off a wet floor onto a grated step, crouch-walk under low pipes, "
                  "kneel to read a low gauge and reach for an electrical cabinet door, each carrying gear on its "
                  "back, while an operator in a remote booth can take over.",
                  "巡检现场示意：机器人沿巡检通道依次跨过湿滑台阶、蹲行通过低矮管架、跪姿读取低位仪表、伸手开配电柜门；"
                  "背部背着检测设备；远处控制室可远程接管。"),
    swipe=T("Swipe sideways to see the whole scene. Tap a number to jump to that need.",
            "左右滑动看完整场景；点数字跳到对应的需求。"),
    legend_label=T("Six needs along an inspection route", "巡检现场的六类需求"),
    s1=T("Understand the field in five minutes", "五分钟看懂这个方向"),
    s1_sub=T("A humanoid learns to move through roughly six stops, like a pipeline. Each stop lists representative "
             "works; click a name to jump to its video card.",
             "人形机器人学动作，大致是一条六站的流水线。每一站都有代表性工作，点名字可以跳到下面的视频卡片。"),
    alias_prefix=T("Like ", "打个比方："),
    trio_h=T("Three lines of work ONE-G is building on", "ONE-G 正在跟进的三条线"),
    trio_p=T("Each one answers a question: is the foundation strong enough, is training affordable, and will it run "
             "on our own robots?",
             "三个工作分别解决三件事：底座够不够强，训练贵不贵，能不能装进自家机器人。"),
    trio_sm_role=T("Cheaper training", "让训练更便宜"),
    trio_sm=T("Replaces most simulator sampling with a differentiable world model. In the paper's comparison, one "
              "GPU beats the released SONIC checkpoint's return in about 3 hours.",
              "用可微世界模型代替大部分仿真采样。按论文的对比，单卡约 3 小时就超过了 SONIC 发布版的回报。"),
    trio_sonic_role=T("The tracking foundation", "通用跟踪底座"),
    trio_sonic=T("A large, general-purpose cerebellum: 42M parameters and 700 hours of motion capture, with every "
                 "kind of high-level input carried out by the same policy.",
                 "一个大号的通用“小脑”：42M 参数、700 小时动捕，各种上层输入都交给同一个策略执行。"),
    trio_a2a_role=T("A new body", "装进新身体"),
    trio_a2a=T("Aligns kinematics first, then uses LoRA to adjust only the dynamics-related parts, moving to a new "
               "robot for about 1% of the cost.",
               "先做运动学对齐，再用 LoRA 只调动力学相关的部分，约 1% 的代价迁移到新本体。"),
    trio_note=T("The foundation sets the ceiling, SuperMimic sets the pace of iteration, and Any2Any decides whether "
                "it lands on our own robots. Those are the three things an inspection robot depends on most.",
                "底座决定能力上限，SuperMimic 决定迭代速度，Any2Any 决定能不能落到自家机器人上。这三件事，正好是做巡检机器人最关心的。"),
    dia_sonic_gpus=T("SONIC: 128 GPUs × 7 days", "SONIC：128 卡 × 7 天"),
    dia_one_gpu=T("1 GPU, about 3 h", "1 卡约 3 小时"),
    dia_inputs=[T("VR teleop", "VR 遥操作"), T("Human video", "人体视频"), T("VLA model", "VLA 指令"), T("Planner", "规划器")],
    dia_policy=[T("One policy,", "同一个策略"), T("steady moves", "稳稳做出来")],
    dia_new=T("New robot", "新本体"),
    s2=T("13 recent works, video first", "13 个前沿工作，先看视频"),
    s2_sub=T("Each card covers what the work does, an analogy, and why it matters for inspection. Videos are "
             "embedded from each paper's official project page and load only when you press play; the tabs "
             "underneath switch clips.",
             "每张卡片：它做了什么、打个比方、和巡检有什么关系。视频都来自论文官方项目页，点“播放”才加载，下方小标签可以切换片段。"),
    filter_label=T("Filter by area", "按方向筛选"),
    all=T("All", "全部"),
    follow=T("ONE-G builds on this", "ONE-G 正在跟进"),
    play=T("Play video", "播放视频"),
    play_aria=T("Play the {name} video", "播放 {name} 视频"),
    fail=T("This clip can't load right now.", "这段视频暂时加载不了"),
    fail_link=T("Watch it on the project page", "去官方项目页观看"),
    clip_note=T("Video from the {name} project page", "视频来自 {name} 官方项目页"),
    caption_tail=T(". Copyright belongs to the authors.", "，版权归原作者。"),
    open_page=T("Open the original page", "打开原页面"),
    clips_label=T("{name} video clips", "{name} 视频片段"),
    analogy=T("Analogy", "打个比方"),
    inspect=T("For inspection", "和巡检的关系"),
    nums_label=T("Key numbers", "关键数字"),
    mj_rows=[(T("Environments and tasks", "环境与任务"), T("Isaac Lab-style API", "Isaac Lab 式 API")),
             (T("GPU-parallel physics", "GPU 并行物理"), T("MuJoCo Warp", "MuJoCo Warp"))],
    mj_caption=T("Diagram: mjlab's two layers and the official one-line demo command.",
                 "示意图：mjlab 的两层结构和官方给出的一行试跑命令。"),
    s3=T("Walk the inspection route", "放到巡检现场看"),
    s3_sub=T("Inspection is one of the deployments we have in mind. Below, each need on site is matched to the "
             "abilities it takes, works to learn from and the related topics. The numbers match the illustration "
             "at the top of the page.",
             "巡检是我们设想的落地场景之一。下面把现场的需求，逐条对到需要的能力、可参考的工作和对应课题。编号和页首插图里的数字一致。"),
    need_ability=T("Abilities needed", "需要的能力"),
    need_works=T("Learn from", "可以参考"),
    need_topics=T("Related topics", "对应课题"),
    need_split=T("Two more needs on the R&D side", "研发侧还有两件事"),
    thumb_many=T("128 GPUs × 7 days", "128 卡 × 7 天"),
    thumb_one=T("1 GPU", "单卡"),
    s4=T("Six candidate topics", "6 个可选课题"),
    s4_sub=T("Each topic lists the question to answer, what to read first and what you could do in month one. "
             "Difficulty is only a rough guide; adjust it to your interests.",
             "每个课题都写了要回答的问题、先读哪几篇、第一个月能做什么。难度只是相对参考，可以按兴趣调整。"),
    chooser_q=T("What kind of work do you enjoy? Pick one and the matching topics stay highlighted.",
                "你更喜欢做哪类事？点一下，适合的课题会留下来。"),
    choice_out=T("Topics that fit: {list}. The rest are dimmed; click again to reset.",
                 "更适合你的课题：{list}（其余已变淡，再点一次恢复）"),
    list_sep=T(", ", "、"),
    level=T("Difficulty: ", "难度："),
    fit=T("Good fit if you enjoy: ", "适合喜欢："),
    t_problem=T("The question", "要回答的问题"),
    t_read=T("Read first", "先读"),
    t_month=T("Month one", "第一个月可以做"),
    t_output=T("Possible outcomes", "可能的产出"),
    topics_note=T("All of these topics can build on ONE-G's inspection scenarios and robot platforms; the details "
                  "are to be agreed between both sides.",
                  "这些课题都可以结合 ONE-G 的巡检场景与机器人平台开展，具体安排以双方沟通为准。"),
    s5=T("Getting started in month one", "第一个月怎么上手"),
    s5_sub=T("Whichever topic you choose, the first four weeks can follow the same path: get things running, make "
             "some data, then choose a direction with real questions in hand.",
             "不管最后选哪个课题，前四周都可以走同一条路：先跑通，再动手做数据，然后带着问题定方向。"),
    week=T("Week {n}", "第 {n} 周"),
    res_h=T("Resources", "资源"),
    tip=T("One-line demo: <code>uvx --from mjlab --refresh demo</code>. Training needs an NVIDIA GPU; macOS "
          "supports evaluation only.",
          "一行命令试跑：<code>uvx --from mjlab --refresh demo</code>。训练需要 NVIDIA GPU，macOS 只能做评估。"),
    gloss_h=T("Glossary", "术语表"),
    gloss_sub=T("The Chinese term is shown next to each entry, for talking with labmates.", ""),
    footer_h=T("Paper sources", "论文来源"),
    footer_note=T("Videos are embedded directly from each paper's official project page and belong to their authors. "
                  "The text was compiled by ONE-G and may contain mistakes; the original papers are the reference.",
                  "页面里的视频都直接嵌入自各论文的官方项目页，版权归原作者所有。文字由 ONE-G（万机）整理，难免有疏漏，请以原论文为准。"),
)
