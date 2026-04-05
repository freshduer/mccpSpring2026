# 3MT 汇报口径（配合 `3mt_slide.html`）

**说明：** 下面是**汇报式**口播，但每一段之间加了**过渡语**，方便一口气讲下来。全文约 **2:50–3:10**（英）；若超时，可略去括号里的补充句。录音时可对照文末「衔接链」。

---

## English — presentation-style talk track (with transitions)

**Roadmap**  
I’ll use this one slide to walk through three things in order: why long user history matters, where current systems get stuck, what we propose—**LONGER**—and what changes in practice.

**From background to the pain point**  
**So first,** recommendation in apps is driven by past behaviour—clicks, views, purchases. **In principle,** the more faithfully we use that history, the better the suggestions tend to be.  
**The problem is** that “faithful” is easy to say and hard to do at scale.

**Left box — why it breaks**  
**That brings us to** the **left** box: **long past behaviours**. In production, history is not short—it is often **thousands** of events over a long horizon. **If** we keep full detail on every request, inference becomes **slow and costly**. **So** teams often truncate or drop most of the history. **That helps efficiency—but** it also **throws away** information that is still relevant to the user. **So we are stuck** between cost and fidelity.

**Middle box — how we respond**  
**To address that trade-off,** our work is **LONGER**, in the **middle** box. **The idea is** to **compress and focus** the long history **without losing what matters**: keep the long trajectory, but produce a **compact representation** the model can use efficiently. **In other words,** the same message as the line at the bottom: from **long, noisy history** to a **clear signal**.

**From method to goals**  
**Given that design,** we have two aims: **one,** use the **entire** long history where it helps accuracy; **two,** stay efficient enough for **real deployment**, not only offline experiments. **Both** need to hold at once.

**Right box — outcomes**  
**With that setup,** the **right** box is the outcome: **better recommendations** when long histories are handled **end-to-end** this way. **Concretely,** we care about **real applications at scale**—for example advertising and e-commerce—where models serve very large user volumes. **So** the significance is not just a benchmark score; it is **usable in production**.

**Back to the title**  
**Putting it together** with the title on the slide: when history is **too long to use naively**, **LONGER** is how we **make it count**—**that is,** better recommendations **in real apps**.

---

## 中文 — 汇报式口播（带衔接）

**路线图**  
我用这一页按顺序讲三件事：长用户历史为什么重要、现有做法卡在哪里、我们提出 **LONGER** 之后实际能带来什么变化。

**从背景到痛点**  
**首先，**推荐系统离不开用户过往行为——点击、浏览、购买等。**原则上**历史用得越充分，推荐往往越准。  
**但问题是，**“用充分”这句话说出来容易，在大规模系统里**做起来很难**。

**左侧框——卡在哪里**  
**这就对应**幻灯片**左边**：**漫长的历史行为**。线上历史往往不是几十条，而是**上千**条、时间跨度很长。**如果**每次都把细节原封不动全用上，在线推理会**又慢又贵**。**所以**常见做法是截断或丢掉大部分历史。**这样**算力省下来了，**但**对用户**仍然有用**的信息也可能一起没了。**于是我们夹在中间：**要么贵，要么丢信号。

**中间框——我们怎么做**  
**针对这个两难，**我们做的是 **LONGER**，也就是**中间**那一块。**核心想法**是：**压缩并聚焦**长历史，同时**尽量保留关键信息**——长轨迹还在，但变成模型能高效使用的**紧凑表示**。**换句话说，**和幻灯片底部那句一样：**从又长又吵的历史，提炼成清晰、可用的信号**。

**从方法到目标**  
**在这个设计下，**目标可以概括成两点：**第一，**在需要时真正用上**整段**长历史，争取推荐**更准确**；**第二，**仍然满足**大规模落地**的效率，而不是只做离线实验。**这两点要同时成立。**

**右侧框——结果与意义**  
**在这样的设定下，**幻灯片**右边**那一框就是结果：把长历史**端到端**这样用起来，能带来**更好的推荐效果**。**具体场景**是**大规模真实业务**，例如广告、电商等海量用户系统。**因此**意义不只是某个数据集上的分数，而是**能进生产、能扩展**。

**扣回标题**  
**最后**和标题对齐一下：当历史**长到不能粗暴全用**时，**LONGER** 的作用就是让它**仍然算数**——**也就是**在真实应用里，做出**更好的推荐**。

---

## 汇报提纲（录音 / 现场用）

| 块 | 英文关键词 | 中文关键词 |
|----|------------|------------|
| 0 | roadmap: three things in order | 路线图：三件事按顺序 |
| 1 | So first / In principle / The problem is | 首先 / 原则上 / 但问题是 |
| 2 | That brings us to / If … So … but / stuck | 这就对应 / 如果…所以…但 / 夹在中间 |
| 3 | To address that trade-off / In other words | 针对两难 / 换句话说 |
| 4 | Given that design / one … two … / Both | 在这个设计下 / 第一…第二… / 同时成立 |
| 5 | With that setup / Concretely / So (significance) | 在这样的设定下 / 具体场景 / 因此 |
| 6 | Putting it together / that is (title) | 最后扣题 / 也就是 |

## 衔接链（只记这一行也可）

**英：** roadmap → So first / The problem is → That brings us to / stuck → To address / In other words → Given that / one, two → With that setup / So → Putting it together.  
**中：** 路线图 → 首先 / 但问题是 → 这就对应 / 夹在中间 → 针对两难 / 换句话说 → 在这个设计下 / 两点同时成立 → 在这样的设定下 / 因此 → 最后扣题。

---

## 录音与 GitHub 链接（提醒）

1. 全屏 `3mt_slide.html`，按提纲走一遍，控制在 **3 分钟内**。  
2. MP3 建议 **128 kbps**，单文件 **< 100 MB**（或 LFS / 网盘）。  
3. 链接写在 `audio_link.md`。
