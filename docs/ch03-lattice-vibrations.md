# 第三章 晶格振动与晶体的热学性质

::: info 教学大纲（建议 9 学时）
- 3.1 绝热近似（玻恩-奥本海默近似）、简谐近似、简正坐标与玻恩-卡门周期性边界条件
- 3.2 一维单原子链的晶格振动与色散关系
- 3.3 一维双原子链（声学支、光学支与频率禁带）及三维晶格振动模式数
- 3.4 晶格振动的量子化与声子
- 3.5 离子晶体中的长光学波（黄昆方程与 LST 关系）
- 3.6 晶格热容理论（杜隆-珀蒂定律、爱因斯坦模型、德拜模型与低温 $T^3$ 定律）
- 3.7 非简谐效应（热膨胀、热传导、N 过程与 U 过程）及晶格振动谱的实验测定
:::

::: tip 核心概念与模型
**1. 核心物理近似链**
- **绝热近似（玻恩-奥本海默近似）**：由于电子质量远小于原子核质量（$m_e \ll M$），电子能瞬时适应原子核的缓慢运动，从而将电子运动与晶格振动退耦。
- **简谐近似**：原子偏离平衡位置的位移远小于晶格常数，势能泰勒展开截断至二次项，体系可经简正坐标变换分解为一组彼此独立的谐振子（格波）。简谐近似下无热膨胀、声子互不散射、热导率趋于无穷大；解释热膨胀与有限热导率必须引入三次及以上**非简谐项**。
- **玻恩-卡门周期性边界条件**：对含 $N$ 个原胞的一维链（周期 $a$），$u_{n+N}=u_n \implies q = \frac{2\pi}{Na}l$，第一布里渊区 $[-\frac{\pi}{a},\frac{\pi}{a}]$ 内恰好包含 $N$ 个独立波矢，波矢空间模式密度为 $\frac{L}{2\pi}$（一维）或 $\frac{V}{(2\pi)^3}$（三维）。

**2. 一维链色散关系与三维模式计数**
- **一维单原子链**（质量 $m$，间距 $a$，最近邻力常数 $\beta$）：
  $$\omega(q) = 2\sqrt{\frac{\beta}{m}}\left|\sin\frac{qa}{2}\right|, \quad q \in \left[-\frac{\pi}{a}, \frac{\pi}{a}\right]$$
  长波极限（$qa \ll 1$）：$\omega \approx v_s|q|$，$v_s = a\sqrt{\beta/m}$；区边界（$q = \pm\frac{\pi}{a}$）：$\omega_m = 2\sqrt{\beta/m}$，群速度 $v_g = \frac{\mathrm{d}\omega}{\mathrm{d}q} = 0$（相邻原子反相驻波）。
- **一维双原子链**（原胞周期 $2a$，质量 $M > m$，相邻间距 $a$，力常数 $\beta$，1st BZ $[-\frac{\pi}{2a}, \frac{\pi}{2a}]$）：
  $$\omega_\pm^2(q) = \beta\left(\frac{1}{m}+\frac{1}{M}\right) \pm \beta\sqrt{\left(\frac{1}{m}+\frac{1}{M}\right)^2 - \frac{4\sin^2(qa)}{mM}}$$
  - $q \to 0$：声学支 $\omega_- \approx a\sqrt{\frac{2\beta}{M+m}}|q|$（原胞内两原子同相同振幅平动）；光学支 $\omega_+(0) = \sqrt{2\beta(\frac{1}{m}+\frac{1}{M})}$（两原子反相振动、质心静止，$A_1/A_2 = -M/m$）。
  - $q = \pm\frac{\pi}{2a}$：光学支下限 $\sqrt{\frac{2\beta}{m}}$（仅轻原子 $m$ 动），声学支上限 $\sqrt{\frac{2\beta}{M}}$（仅重原子 $M$ 动），两者间为频率禁带。
- **三维晶格模式总数**：$N$ 个原胞、每原胞 $n$ 个原子，共有 $3nN$ 个独立模式 = **$3$ 支声学波（1 纵 2 横）+ $(3n-3)$ 支光学波**，每支含 $N$ 个波矢。

**3. 声子与离子晶体长光学波**
- **声子**：晶格简正振动能量量子 $\hbar\omega(\mathbf{q})$，模式能量 $E_q = \left(n_q + \frac{1}{2}\right)\hbar\omega_q$；零化学势玻色分布 $\bar{n}_q = \frac{1}{e^{\hbar\omega_q/(k_B T)} - 1}$；准动量 $\hbar\mathbf{q}$（非机械动量，散射中守恒至差倒格矢 $\hbar\mathbf{G}$）。
- **离子晶体长光学波（黄昆方程与 LST 关系）**：长纵光学波（LO）产生宏观纵向退极化电场增加回复力，使 $\omega_L > \omega_T$，满足
  $$\frac{\omega_L^2}{\omega_T^2} = \frac{\varepsilon(0)}{\varepsilon(\infty)}$$
  红外光（横电磁波）与长横光学波 $\omega_T$ 耦合形成强红外吸收（剩余射线）和极化激元。

**4. 晶格热容模型（$N$ 个单原子原胞，$3N$ 个模式）**

| 模型 | 关键假设 | 低温极限（$T \ll \Theta$） | 高温极限（$T \gg \Theta$） |
| :--- | :--- | :--- | :--- |
| 杜隆-珀蒂定律 | 经典能量均分，每模式 $k_B T$ | 失效（恒为 $3Nk_B$） | $3Nk_B$（$3R$） |
| 爱因斯坦模型 | $3N$ 个模式全取单一频率 $\omega_E$ | $3Nk_B\left(\frac{\Theta_E}{T}\right)^2 e^{-\Theta_E/T}$（衰减过快） | $3Nk_B$ |
| 德拜模型 | 线性色散 $\omega = v_s q$，$g(\omega)=\frac{9N}{\omega_D^3}\omega^2$（$\omega \le \omega_D$） | $\frac{12\pi^4}{5}Nk_B\left(\frac{T}{\Theta_D}\right)^3$（$d$ 维 $\propto T^d$） | $3Nk_B$ |

- 德拜波矢 $q_D = \left(\frac{6\pi^2 N}{V}\right)^{1/3}$，德拜频率 $\omega_D = \bar{v} q_D$（其中 $\frac{3}{\bar{v}^3} = \frac{1}{v_l^3} + \frac{2}{v_t^3}$），德拜温度 $\Theta_D = \frac{\hbar\omega_D}{k_B}$。

**5. 非简谐效应与实验测定**
- **热膨胀**：三次非简谐项 $-gx^3$ 使势阱不对称，热平均位移 $\langle x \rangle \propto T$。
- **热传导**：$\kappa = \frac{1}{3}C_V \bar{v}\bar{l}$；三声子散射中 **N 过程**（$\mathbf{q}_1+\mathbf{q}_2=\mathbf{q}_3$）保持总准动量守恒，不直接产生热阻；**U 过程**（$\mathbf{q}_1+\mathbf{q}_2=\mathbf{q}_3+\mathbf{G},\ \mathbf{G}\ne 0$）反转能流，是晶体本征热阻的根源（高温 $\kappa \propto T^{-1}$，低温边界散射 $\kappa \propto T^3$）。
- **色散谱测定**：**非弹性中子散射**可测全布里渊区色散曲线；**拉曼散射**测 $q\approx 0$ 光学声子；**布里渊散射**测 $q\approx 0$ 声学声子。
:::

![一维单原子链与双原子链色散关系](/figures/ch03-dispersion-chains.svg)

<p class="fig-caption">图 3-1 一维单原子链与一维双原子链（<em>M</em> &gt; <em>m</em>）的晶格振动色散曲线</p>

## 习题及参考解答

### 知识点 1：一维单原子链与周期性边界条件

#### 概念选择与填空

`CH03-KP1-01`（单选）关于研究晶格振动时引入的绝热近似（玻恩-奥本海默近似）与简谐近似，下列说法**错误**的是（ ）。
A. 绝热近似利用电子质量远小于离子实质量的条件，使电子态瞬时跟随原子核位置变化
B. 简谐近似将晶格势能按原子偏离平衡位置的位移展开并保留至二次项
C. 在严格简谐近似下，晶体中各简正振动模式彼此独立，互不交换能量
D. 严格简谐近似即可定量解释晶体的热膨胀现象

::: details 思路提示
检查简谐势 $V(x) = cx^2$ 的对称性，对称势阱中任意温度下的平均位移 $\langle x \rangle$ 是否为零。
:::

::: details 参考答案与解析
**参考答案**：D

**解析**：简谐势关于平衡位置严格偶对称，任意温度下平均位移 $\langle x \rangle = 0$，因此简谐晶体不存在热膨胀（且声子互不散射，热导率为无穷大）。热膨胀和有限热导率均源于三次及以上的非简谐项。A、B、C 均正确。
:::

---

`CH03-KP1-02`（填空）由 $N$ 个相同原子构成的一维单原子链（平衡间距 $a$），采用玻恩-卡门周期性边界条件 $u_{n+N} = u_n$，则其第一布里渊区波矢范围为 ____，独立格波（波矢）总数为 ____，波矢空间单位长度内的模式密度为 ____。

::: details 思路提示
由 $e^{iqNa} = 1$ 解出分立波矢 $q_l = \frac{2\pi}{Na}l$，再用第一布里渊区宽度除以相邻波矢间距 $\Delta q$。
:::

::: details 参考答案与解析
**参考答案**：$\left(-\frac{\pi}{a},\ \frac{\pi}{a}\right]$（或 $\left[-\frac{\pi}{a},\ \frac{\pi}{a}\right]$）；$N$；$\frac{Na}{2\pi} = \frac{L}{2\pi}$。

**解析**：由 $u_{n+N} = u_n$ 得 $e^{iqNa} = 1 \implies q = \frac{2\pi}{Na}l$（$l$ 为整数），相邻允许波矢间距 $\Delta q = \frac{2\pi}{Na} = \frac{2\pi}{L}$。第一布里渊区宽度为 $\frac{2\pi}{a}$，故其内容纳的独立波矢数为 $\frac{2\pi/a}{2\pi/(Na)} = N$，单位波矢区间内的模式数为 $\frac{1}{\Delta q} = \frac{L}{2\pi}$。
:::

---

`CH03-KP1-03`（单选）一维单原子链在第一布里渊区边界 $q = \pm\frac{\pi}{a}$ 处，晶格振动的物理状态是（ ）。
A. 群速度与相速度均为零，所有原子静止
B. 群速度为零，相速度不为零，相邻原子等幅反相振动，形成驻波
C. 群速度最大，能量传播最快
D. 相邻原子同相振动，等效于整个晶体刚性平动

::: details 思路提示
分别计算 $q = \pi/a$ 处的群速度 $v_g = \mathrm{d}\omega/\mathrm{d}q$、相速度 $v_p = \omega/q$ 以及相邻原子位移之比 $u_{n+1}/u_n = e^{iqa}$。
:::

::: details 参考答案与解析
**参考答案**：B

**解析**：在 $q = \frac{\pi}{a}$ 处，$v_g = a\sqrt{\frac{\beta}{m}}\cos\frac{qa}{2}\big|_{q=\pi/a} = 0$，而 $v_p = \frac{\omega_m}{\pi/a} \ne 0$；相邻原子位移满足 $u_{n+1}/u_n = e^{i\pi} = -1$，即相邻原子反相振动，入射波与布拉格反射波叠加形成驻波，无净能量输运。
:::

#### 题型一：一维单原子链色散关系、态密度与次近邻修正

`CH03-KP1-04` 考虑由 $N$ 个质量为 $m$ 的原子构成的一维单原子链，平衡间距为 $a$，仅计最近邻简谐恢复力常数 $\beta$。
1. 建立第 $n$ 个原子的牛顿运动方程并推导色散关系 $\omega(q)$；
2. 分别求长波极限（$qa \ll 1$）下的声速 $v_s$ 与布里渊区边界 $q = \frac{\pi}{a}$ 处的频率 $\omega_m$ 和群速度 $v_g$；
3. 推导该一维单原子链的振动模式态密度 $g(\omega)$，并指出其在 $\omega \to \omega_m$ 处的行为特征。

::: details 思路提示
代入行波试探解 $u_n(t) = A e^{i(qna - \omega t)}$；求一维态密度时注意正负波矢 $\pm q$ 对应同一频率，故 $g(\omega) = 2 \cdot \frac{Na}{2\pi}\left|\frac{\mathrm{d}q}{\mathrm{d}\omega}\right|$。
:::

::: details 参考答案与解析
**参考答案**：
1. $\omega(q) = 2\sqrt{\frac{\beta}{m}}\left|\sin\frac{qa}{2}\right|$；
2. $v_s = a\sqrt{\frac{\beta}{m}}$，$\omega_m = 2\sqrt{\frac{\beta}{m}}$，$v_g(\pi/a) = 0$；
3. $g(\omega) = \frac{2N}{\pi\sqrt{\omega_m^2 - \omega^2}}$（$0 < \omega < \omega_m$），在 $\omega \to \omega_m$ 处发散（一维范霍夫奇点）。

**解析**：
1. **运动方程与色散关系**：第 $n$ 个原子受左右两最近邻恢复力作用：
   $$m\ddot{u}_n = \beta(u_{n+1} - u_n) + \beta(u_{n-1} - u_n) = \beta(u_{n+1} + u_{n-1} - 2u_n)$$
   代入 $u_n = A e^{i(qna - \omega t)}$：
   $$-m\omega^2 = \beta(e^{iqa} + e^{-iqa} - 2) = 2\beta(\cos qa - 1) = -4\beta\sin^2\frac{qa}{2}$$
   开方即得：
   $$\omega(q) = 2\sqrt{\frac{\beta}{m}}\left|\sin\frac{qa}{2}\right|$$

2. **极限与群速度**：
   - 长波极限 $qa \ll 1$ 时 $\sin\frac{qa}{2} \approx \frac{qa}{2}$，故 $\omega \approx a\sqrt{\frac{\beta}{m}}|q|$，声速 $v_s = a\sqrt{\frac{\beta}{m}}$。
   - 在 $q = \frac{\pi}{a}$ 处，$\omega_m = 2\sqrt{\frac{\beta}{m}}$，群速度 $v_g = \frac{\mathrm{d}\omega}{\mathrm{d}q} = a\sqrt{\frac{\beta}{m}}\cos\frac{qa}{2}\Big|_{\pi/a} = 0$。

3. **模式态密度**：取 $q \in (0, \frac{\pi}{a})$，记 $\omega = \omega_m\sin\frac{qa}{2}$，则 $\frac{\mathrm{d}\omega}{\mathrm{d}q} = \frac{a\omega_m}{2}\cos\frac{qa}{2} = \frac{a}{2}\sqrt{\omega_m^2 - \omega^2}$。计入 $\pm q$ 两支对称贡献：
   $$g(\omega) = 2 \cdot \frac{Na}{2\pi}\left|\frac{\mathrm{d}q}{\mathrm{d}\omega}\right| = \frac{Na}{\pi}\cdot\frac{2}{a\sqrt{\omega_m^2 - \omega^2}} = \frac{2N}{\pi\sqrt{\omega_m^2 - \omega^2}} \quad (0 < \omega < \omega_m)$$
   校验总模式数：$\int_0^{\omega_m} g(\omega)\,\mathrm{d}\omega = \frac{2N}{\pi}\arcsin(1) = N$。当 $\omega \to \omega_m$ 时群速度趋于零，$g(\omega)$ 呈现平方根倒数发散（范霍夫奇点）。
:::

---

`CH03-KP1-05` 若在一维单原子链（质量 $m$，间距 $a$）中同时计入最近邻（力常数 $\beta_1$）和次近邻（力常数 $\beta_2$）简谐相互作用：
1. 推导其色散关系 $\omega(q)$ 与长波声速 $v_s$；
2. 求出布里渊区边界 $q = \frac{\pi}{a}$ 处的频率，并讨论当 $\beta_2/\beta_1$ 满足何种条件时，最大振动频率不再出现在布里渊区边界而移入布里渊区内部。

::: details 思路提示
运动方程右侧增加次近邻项 $\beta_2(u_{n+2} + u_{n-2} - 2u_n)$；令 $x = \sin^2\frac{qa}{2} \in [0,1]$，利用倍角公式 $\sin^2(qa) = 4x(1-x)$ 将 $\omega^2$ 化为关于 $x$ 的二次函数求极值。
:::

::: details 参考答案与解析
**参考答案**：
1. $\omega(q) = \sqrt{\frac{4\beta_1}{m}\sin^2\frac{qa}{2} + \frac{4\beta_2}{m}\sin^2(qa)}$，$v_s = a\sqrt{\frac{\beta_1 + 4\beta_2}{m}}$；
2. $\omega(\pi/a) = 2\sqrt{\frac{\beta_1}{m}}$；当 $\frac{\beta_2}{\beta_1} > \frac{1}{4}$ 时，最大频率移入第一布里渊区内部。

**解析**：
1. 运动方程为：
   $$m\ddot{u}_n = \beta_1(u_{n+1} + u_{n-1} - 2u_n) + \beta_2(u_{n+2} + u_{n-2} - 2u_n)$$
   代入 $u_n = A e^{i(qna-\omega t)}$ 得：
   $$m\omega^2 = 2\beta_1(1-\cos qa) + 2\beta_2(1-\cos 2qa) = 4\beta_1\sin^2\frac{qa}{2} + 4\beta_2\sin^2(qa)$$
   长波极限 $qa \ll 1$ 时，$m\omega^2 \approx (\beta_1 + 4\beta_2)(qa)^2$，故声速 $v_s = a\sqrt{\frac{\beta_1 + 4\beta_2}{m}}$。

2. 在 $q = \frac{\pi}{a}$ 处，$\sin(qa) = \sin\pi = 0$，次近邻原子（相距 $2a$）同相振动无相对伸缩，故 $\omega(\pi/a) = 2\sqrt{\frac{\beta_1}{m}}$ 与 $\beta_2$ 无关。
   令 $x = \sin^2\frac{qa}{2} \in [0, 1]$，则 $\sin^2(qa) = 4x(1-x)$：
   $$\frac{m\omega^2}{4} = \beta_1 x + 4\beta_2 x(1-x) = -4\beta_2 x^2 + (\beta_1 + 4\beta_2)x$$
   该开口向下的抛物线对称轴位于 $x_0 = \frac{\beta_1 + 4\beta_2}{8\beta_2} = \frac{1}{2} + \frac{\beta_1}{8\beta_2}$。
   - 若 $x_0 \ge 1$，即 $\frac{\beta_2}{\beta_1} \le \frac{1}{4}$，最大值仍在区边界 $x = 1$（$q = \pi/a$）处；
   - 若 $x_0 < 1$，即 $\frac{\beta_2}{\beta_1} > \frac{1}{4}$，最大值移入布里渊区内部 $x = x_0$ 处，最大频率高于区边界频率。
:::

---

### 知识点 2：一维双原子链与声学支/光学支

#### 概念选择与填空

`CH03-KP2-01`（填空）由 $N$ 个原胞组成的三维晶体，若每个原胞内含 $n$ 个原子，则总计有 ____ 个独立晶格振动模式，其色散关系分为 ____ 支声学波和 ____ 支光学波；对金刚石结构的硅单晶（原胞含 $2$ 个原子），其声学支和光学支分别有 ____ 支和 ____ 支。

::: details 思路提示
三维空间每个原子有 $3$ 个自由度；无论原胞内原子数 $n$ 多大，声学支恒对应原胞质心的三维平动。
:::

::: details 参考答案与解析
**参考答案**：$3nN$；$3$；$3n-3$；$3$；$3$。

**解析**：三维晶体中 $N$ 个原胞共含 $nN$ 个原子，自由度总数为 $3nN$，每支格波在第一布里渊区内含 $N$ 个波矢，因此共有 $3n$ 支色散曲线，其中 $3$ 支为声学波（1 支纵声学 LA + 2 支横声学 TA），其余 $3n-3$ 支为光学波。金刚石结构原胞含 $n = 2$ 个原子，故有 $3$ 支声学波与 $3$ 支光学波（1 支 LO + 2 支 TO）。
:::

---

`CH03-KP2-02`（单选）关于一维双原子链（原胞内两原子质量 $M > m$，间距 $a$，力常数 $\beta$）的振动特征，下列说法**错误**的是（ ）。
A. 长波极限（$q \to 0$）下，声学支表现为原胞内两原子同相、同振幅运动
B. 长波极限（$q \to 0$）下，光学支表现为原胞内两原子反相运动，且原胞质心静止
C. 在第一布里渊区边界 $q = \frac{\pi}{2a}$ 处，声学支对应重原子 $M$ 振动而轻原子 $m$ 静止
D. 在第一布里渊区边界 $q = \frac{\pi}{2a}$ 处，光学支对应重原子 $M$ 振动而轻原子 $m$ 静止

::: details 思路提示
频率较高（光学支）的驻波由质量较轻的原子承载，频率较低（声学支）的驻波由质量较重的原子承载。
:::

::: details 参考答案与解析
**参考答案**：D

**解析**：在 $q = \frac{\pi}{2a}$ 处，光学支频率 $\omega_+ = \sqrt{2\beta/m}$ 只含轻原子质量 $m$，此时轻原子 $m$ 反相振动而重原子 $M$ 静止；声学支频率 $\omega_- = \sqrt{2\beta/M}$ 只含重原子质量 $M$，此时重原子 $M$ 振动而轻原子 $m$ 静止。故 D 错误。
:::

---

`CH03-KP2-03`（单选）在一维双原子链中，若保持相邻间距 $a$ 和力常数 $\beta$ 不变，令两类原子质量相等（$M = m$），则其色散曲线将演变为（ ）。
A. 光学支完全消失，只剩一半振动模式
B. 频率禁带宽度缩小为零，原光学支恰好是一维单原子链在 $\frac{\pi}{2a} \le |q| \le \frac{\pi}{a}$ 区间向第一布里渊区 $[-\frac{\pi}{2a}, \frac{\pi}{2a}]$ 的折合
C. 频率禁带宽度增至最大
D. 声学支与光学支合并为一条水平直线

::: details 思路提示
将 $M = m$ 代入双原子链色散公式 $\omega_\pm^2(q)$ 并用三角恒等式化简。
:::

::: details 参考答案与解析
**参考答案**：B

**解析**：当 $M = m$ 时，$\omega_\pm^2 = \frac{2\beta}{m}(1 \pm \cos qa)$，即 $\omega_- = 2\sqrt{\frac{\beta}{m}}|\sin\frac{qa}{2}|$，$\omega_+ = 2\sqrt{\frac{\beta}{m}}\cos\frac{qa}{2} = 2\sqrt{\frac{\beta}{m}}\sin\left[\frac{(\pi/a - |q|)a}{2}\right]$。在 $q = \pm\frac{\pi}{2a}$ 处两支相接，频率禁带闭合，光学支正是单原子链外半段布里渊区经倒格矢 $\pm\frac{\pi}{a}$ 折合进来的部分（布里渊区折合思想在第五章能带理论中同样核心）。
:::

#### 题型一：一维双原子链与双力常数链色散关系推导

`CH03-KP2-04` 一维双原子链由质量为 $m$ 和 $M$（$M > m$）的原子等距交替排列而成，相邻原子间距为 $a$（原胞周期 $2a$），最近邻力常数为 $\beta$。
1. 建立两类原子的运动方程并推导色散关系 $\omega_\pm(q)$；
2. 求长波极限（$q \to 0$）下声学支的声速 $v_s$、光学支的频率 $\omega_+(0)$ 以及两支各自对应的原子振幅比 $A_1/A_2$；
3. 求第一布里渊区边界 $q = \frac{\pi}{2a}$ 处的频率禁带上下限及两类原子的振幅比。

::: details 思路提示
将第 $n$ 个原胞内质量 $m$ 和 $M$ 的位移记为 $u_{2n}$ 和 $u_{2n+1}$，代入平面波解 $u_{2n} = A_1 e^{i(2nqa-\omega t)}$、$u_{2n+1} = A_2 e^{i[(2n+1)qa-\omega t]}$，令系数行列式为零即得色散方程。
:::

::: details 参考答案与解析
**参考答案**：
1. $\omega_\pm^2(q) = \beta\left(\frac{1}{m}+\frac{1}{M}\right) \pm \beta\sqrt{\left(\frac{1}{m}+\frac{1}{M}\right)^2 - \frac{4\sin^2(qa)}{mM}}$；
2. 声学支：$v_s = a\sqrt{\frac{2\beta}{M+m}}$，$\frac{A_1}{A_2} = 1$；光学支：$\omega_+(0) = \sqrt{2\beta\left(\frac{1}{m}+\frac{1}{M}\right)}$，$\frac{A_1}{A_2} = -\frac{M}{m}$；
3. 区边界：$\omega_+ = \sqrt{\frac{2\beta}{m}}$（$A_2 = 0$，重原子静止），$\omega_- = \sqrt{\frac{2\beta}{M}}$（$A_1 = 0$，轻原子静止），禁带宽度 $\Delta\omega = \sqrt{2\beta}\left(\frac{1}{\sqrt{m}} - \frac{1}{\sqrt{M}}\right)$。

**解析**：
1. **运动方程与色散关系**：
   $$m\ddot{u}_{2n} = \beta(u_{2n+1} + u_{2n-1} - 2u_{2n}), \qquad M\ddot{u}_{2n+1} = \beta(u_{2n+2} + u_{2n} - 2u_{2n+1})$$
   代入 $u_{2n} = A_1 e^{i(2nqa-\omega t)}$，$u_{2n+1} = A_2 e^{i[(2n+1)qa-\omega t]}$，化简得齐次线性方程组：
   $$\begin{pmatrix} 2\beta - m\omega^2 & -2\beta\cos(qa) \\ -2\beta\cos(qa) & 2\beta - M\omega^2 \end{pmatrix} \begin{pmatrix} A_1 \\ A_2 \end{pmatrix} = 0$$
   系数行列式为零：
   $$mM\omega^4 - 2\beta(m+M)\omega^2 + 4\beta^2\sin^2(qa) = 0$$
   解一元二次方程即得：
   $$\omega_\pm^2(q) = \beta\left(\frac{1}{m}+\frac{1}{M}\right) \pm \beta\sqrt{\left(\frac{1}{m}+\frac{1}{M}\right)^2 - \frac{4\sin^2(qa)}{mM}}$$
   且振幅比关系为 $\frac{A_1}{A_2} = \frac{2\beta\cos(qa)}{2\beta - m\omega^2} = \frac{2\beta - M\omega^2}{2\beta\cos(qa)}$。

2. **长波极限（$q \to 0$）**：$\sin(qa) \approx qa$，$\cos(qa) \approx 1$。
   - **声学支（取负号）**：利用 $\sqrt{1-x} \approx 1 - \frac{x}{2}$：
     $$\omega_-^2(q) \approx \frac{2\beta}{M+m}(qa)^2 \implies v_s = a\sqrt{\frac{2\beta}{M+m}}$$
     此时 $\omega_- \to 0$，代入振幅比得 $\frac{A_1}{A_2} = \frac{2\beta}{2\beta} = 1$（两原子同相同幅运动）。
   - **光学支（取正号）**：
     $$\omega_+(0) = \sqrt{2\beta\left(\frac{1}{m}+\frac{1}{M}\right)}$$
     代入振幅比：$\frac{A_1}{A_2} = \frac{2\beta}{2\beta - m\cdot 2\beta(\frac{1}{m}+\frac{1}{M})} = -\frac{M}{m}$，满足 $mA_1 + MA_2 = 0$（两原子反相振动，原胞质心静止）。

3. **布里渊区边界（$q = \frac{\pi}{2a}$）**：此时 $\cos(qa) = 0,\ \sin(qa) = 1$，方程组退耦：
   $$(2\beta - m\omega^2)A_1 = 0, \qquad (2\beta - M\omega^2)A_2 = 0$$
   - 光学支下限 $\omega_+ = \sqrt{\frac{2\beta}{m}}$，此时 $A_2 = 0,\ A_1 \ne 0$（仅轻原子振动）；
   - 声学支上限 $\omega_- = \sqrt{\frac{2\beta}{M}}$，此时 $A_1 = 0,\ A_2 \ne 0$（仅重原子振动）；
   - 两频率之间不存在实波矢解，形成宽度为 $\sqrt{2\beta}\left(\frac{1}{\sqrt{m}} - \frac{1}{\sqrt{M}}\right)$ 的频率禁带。
:::

---

`CH03-KP2-05` 考虑由质量均为 $m$ 的相同原子构成的一维链，相邻原子间的力常数交替取 $\beta_1$ 和 $\beta_2$（$\beta_1 > \beta_2$），原胞周期为 $a$（内含 $2$ 个原子）。
1. 推导该链的晶格振动色散关系 $\omega_\pm(q)$；
2. 求出 $q = 0$ 处的光学支频率以及 $q = \frac{\pi}{a}$ 处的频率禁带上下限。

::: details 思路提示
把第 $n$ 个原胞内左、右两原子位移记作 $u_n, v_n$：$u_n$ 右侧以 $\beta_1$ 连 $v_n$、左侧以 $\beta_2$ 连 $v_{n-1}$；代入 $u_n = A e^{i(qna-\omega t)}$、$v_n = B e^{i(qna-\omega t)}$（因原胞周期为 $a$）。
:::

::: details 参考答案与解析
**参考答案**：
1. $\omega_\pm^2(q) = \frac{\beta_1 + \beta_2}{m} \pm \frac{1}{m}\sqrt{\beta_1^2 + \beta_2^2 + 2\beta_1\beta_2\cos(qa)}$；
2. $\omega_+(0) = \sqrt{\frac{2(\beta_1+\beta_2)}{m}}$；在 $q = \frac{\pi}{a}$ 处，禁带上限 $\omega_+ = \sqrt{\frac{2\beta_1}{m}}$，下限 $\omega_- = \sqrt{\frac{2\beta_2}{m}}$。

**解析**：
1. 两原子的运动方程为：
   $$m\ddot{u}_n = \beta_1(v_n - u_n) + \beta_2(v_{n-1} - u_n)$$
   $$m\ddot{v}_n = \beta_2(u_{n+1} - v_n) + \beta_1(u_n - v_n)$$
   代入 $u_n = A e^{i(qna-\omega t)},\ v_n = B e^{i(qna-\omega t)}$：
   $$\begin{pmatrix} \beta_1+\beta_2 - m\omega^2 & -(\beta_1 + \beta_2 e^{-iqa}) \\ -(\beta_1 + \beta_2 e^{iqa}) & \beta_1+\beta_2 - m\omega^2 \end{pmatrix} \begin{pmatrix} A \\ B \end{pmatrix} = 0$$
   令行列式为零，注意到 $|\beta_1 + \beta_2 e^{iqa}|^2 = \beta_1^2 + \beta_2^2 + 2\beta_1\beta_2\cos(qa)$，解得：
   $$\omega_\pm^2(q) = \frac{\beta_1 + \beta_2}{m} \pm \frac{1}{m}\sqrt{\beta_1^2 + \beta_2^2 + 2\beta_1\beta_2\cos(qa)}$$

2. 代入特殊点：
   - $q = 0$（$\cos qa = 1$）：$\omega_- = 0$，$\omega_+(0) = \sqrt{\frac{2(\beta_1+\beta_2)}{m}}$。
   - $q = \frac{\pi}{a}$（$\cos qa = -1$）：根号项为 $|\beta_1 - \beta_2| = \beta_1 - \beta_2$，故
     $$\omega_+\left(\frac{\pi}{a}\right) = \sqrt{\frac{2\beta_1}{m}}, \qquad \omega_-\left(\frac{\pi}{a}\right) = \sqrt{\frac{2\beta_2}{m}}$$
   即使原子质量完全相同，只要键强周期交替（二聚化），布里渊区边界同样会打开频率禁带。
:::

---

### 知识点 3：声子与离子晶体长光学波（LST 关系）

#### 概念选择与填空

`CH03-KP3-01`（单选）关于晶格振动的量子——声子，下列说法正确的是（ ）。
A. 声子是费米子，每个振动模式最多只能容纳 $1$ 个声子
B. 声子总数在温度变化时保持守恒，具有非零化学势
C. 声子的准动量 $\hbar\mathbf{q}$ 是晶体内部电子或原子核真实的机械动量
D. 声子是零化学势的玻色子，其准动量在晶体中仅守恒至差一个倒格矢 $\hbar\mathbf{G}$

::: details 思路提示
回顾谐振子量子化的能级占据数 $n_q = 0, 1, 2, \dots$ 以及周期晶格平移对称性对应的准动量守恒律。
:::

::: details 参考答案与解析
**参考答案**：D

**解析**：每个简正振动模式可被激发任意整数个量子（$n_q = 0,1,2,\dots$），且声子可随温度升高不断产生或湮灭（总数不守恒 $\implies$ 化学势 $\mu = 0$），故声子是零化学势玻色子。对于任意 $q \ne 0$ 格波，整个晶体的总机械动量 $\sum_n m \dot{u}_n = 0$，故 $\hbar\mathbf{q}$ 不是真实机械动量，而是反映晶格平移对称性的**准动量**。
:::

---

`CH03-KP3-02`（填空）在极性离子晶体的长波光学振动中，纵光学波频率 $\omega_L$ 总是 ____（填“大于”“等于”或“小于”）横光学波频率 $\omega_T$，二者满足利丹-萨克斯-泰勒（LST）关系 ____；红外电磁波可与离子晶体的 ____（填“长纵光学波”或“长横光学波”）发生强共振吸收。

::: details 思路提示
纵光学波产生宏观退极化静电场；电磁波在真空和各向同性介质中是横波。
:::

::: details 参考答案与解析
**参考答案**：大于；$\frac{\omega_L^2}{\omega_T^2} = \frac{\varepsilon(0)}{\varepsilon(\infty)}$；长横光学波（TO）。

**解析**：由于静态相对介电常数同时包含电子位移极化与离子位移极化，而光频介电常数仅含电子位移极化，故恒有 $\varepsilon(0) > \varepsilon(\infty) \implies \omega_L > \omega_T$。红外光是横波，其电场与横光学波极化矢量同向，当 $\omega = \omega_T$ 时发生强共振吸收。
:::

---

`CH03-KP3-03`（单选）在离子晶体（如 NaCl）中，导致长波极限下纵光学波频率 $\omega_L$ 高于横光学波频率 $\omega_T$ 的根本物理原因是（ ）。
A. 纵波方向上的原子质量更小
B. 纵波方向上的短程弹性力常数更大
C. 长纵光学振动中正负离子的相对位移沿波矢方向产生宏观纵向退极化电场，对离子提供了额外的库仑回复力
D. 横光学波存在泡利排斥阻尼

::: details 思路提示
由无自由电荷条件 $\nabla \cdot \mathbf{D} = \nabla \cdot (\varepsilon_0 \mathbf{E} + \mathbf{P}) = 0$ 比较纵波（$\mathbf{P} \parallel \mathbf{q}$）和横波（$\mathbf{P} \perp \mathbf{q}$）所伴随的宏观静电场 $\mathbf{E}$。
:::

::: details 参考答案与解析
**参考答案**：C

**解析**：对平面波 $\mathbf{P} \propto e^{i\mathbf{q}\cdot\mathbf{r}}$，无自由电荷条件给出 $\mathbf{q}\cdot(\varepsilon_0\mathbf{E} + \mathbf{P}) = 0$。对横光学波（$\mathbf{P} \perp \mathbf{q}$），$\mathbf{E} = 0$；对纵光学波（$\mathbf{P} \parallel \mathbf{q}$），产生反向宏观退极化静电场 $\mathbf{E} = -\mathbf{P}/\varepsilon_0$，该电场额外拉回相对位移的正负离子，使等效回复力常数增大，故 $\omega_L > \omega_T$。
:::

#### 题型一：黄昆方程、LST 关系与离子晶体光学声子计算

`CH03-KP3-04` 离子晶体长波光学振动的宏观黄昆方程组写作：
$$\ddot{\mathbf{W}} = b_{11}\mathbf{W} + b_{12}\mathbf{E}, \qquad \mathbf{P} = b_{21}\mathbf{W} + b_{22}\mathbf{E}$$
其中 $\mathbf{W}$ 为折合相对位移矢量，$\mathbf{E}$ 为宏观电场，$\mathbf{P}$ 为宏观极化强度，且由能量守恒满足 $b_{12} = b_{21}$。
1. 导出静态相对介电常数 $\varepsilon(0)$、高频（光频）相对介电常数 $\varepsilon(\infty)$ 及长横光学波频率 $\omega_T$ 与系数 $b_{ij}$ 的关系；
2. 结合静电条件推导长纵光学波频率 $\omega_L$，并证明 LST 关系 $\frac{\omega_L^2}{\omega_T^2} = \frac{\varepsilon(0)}{\varepsilon(\infty)}$。

::: details 思路提示
分别代入简谐解 $\mathbf{W}, \mathbf{E}, \mathbf{P} \propto e^{-i\omega t}$ 导出介电函数 $\varepsilon(\omega)$；高频取 $\omega \gg \omega_T$（离子来不及响应，$\mathbf{W} \to 0$），静态取 $\omega = 0$（$\ddot{\mathbf{W}} = 0$）；纵波满足 $\mathbf{D} = \varepsilon_0 \varepsilon(\omega_L)\mathbf{E} = 0$，横波对应 $\varepsilon(\omega) \to \infty$ 的极点。
:::

::: details 参考答案与解析
**参考答案**：
1. $\omega_T^2 = -b_{11}$，$\varepsilon(\infty) = 1 + \frac{b_{22}}{\varepsilon_0}$，$\varepsilon(0) = 1 + \frac{b_{22}}{\varepsilon_0} - \frac{b_{12}^2}{\varepsilon_0 b_{11}}$；
2. 证明见下。

**解析**：
1. 设时间依赖为 $e^{-i\omega t}$，由第一式得：
   $$(-\omega^2 - b_{11})\mathbf{W} = b_{12}\mathbf{E} \implies \mathbf{W} = \frac{b_{12}}{-b_{11} - \omega^2}\mathbf{E}$$
   当无宏观电场（$\mathbf{E} = 0$，即长横光学波自由振动，忽略推迟效应）时，有非零解要求 $\omega^2 = -b_{11}$，记作 $\omega_T^2 = -b_{11}$（$b_{11} < 0$）。
   将 $\mathbf{W}$ 代入第二式求极化强度与相对介电函数 $\varepsilon(\omega) = 1 + \frac{P}{\varepsilon_0 E}$（利用 $b_{21}=b_{12}$）：
   $$\varepsilon(\omega) = 1 + \frac{b_{22}}{\varepsilon_0} + \frac{b_{12}^2}{\varepsilon_0(\omega_T^2 - \omega^2)}$$
   - 高频极限（$\omega \gg \omega_T$，离子不动，仅电子极化）：$\varepsilon(\infty) = 1 + \frac{b_{22}}{\varepsilon_0}$；
   - 静态极限（$\omega = 0$）：$\varepsilon(0) = \varepsilon(\infty) + \frac{b_{12}^2}{\varepsilon_0 \omega_T^2}$。
   回代得色散介电函数：
   $$\varepsilon(\omega) = \varepsilon(\infty) + \frac{\varepsilon(0) - \varepsilon(\infty)}{1 - \omega^2/\omega_T^2}$$

2. 对无自由电荷的长纵光学波，$\mathbf{D} = \varepsilon_0\varepsilon(\omega_L)\mathbf{E} = 0$ 且 $\mathbf{E} \ne 0$，故必有 $\varepsilon(\omega_L) = 0$：
   $$\varepsilon(\infty) + \frac{\varepsilon(0) - \varepsilon(\infty)}{1 - \omega_L^2/\omega_T^2} = 0 \implies 1 - \frac{\omega_L^2}{\omega_T^2} = -\frac{\varepsilon(0) - \varepsilon(\infty)}{\varepsilon(\infty)} = 1 - \frac{\varepsilon(0)}{\varepsilon(\infty)}$$
   整理即得 LST 关系：
   $$\frac{\omega_L^2}{\omega_T^2} = \frac{\varepsilon(0)}{\varepsilon(\infty)}$$
:::

---

`CH03-KP3-05` 已知 NaCl 晶体的静态相对介电常数 $\varepsilon(0) = 5.62$，光频相对介电常数 $\varepsilon(\infty) = 2.25$，红外吸收峰对应的剩余射线真空波长为 $\lambda_T = 61.0\ \mu\mathrm{m}$。
1. 计算 NaCl 长横光学声子的角频率 $\omega_T$ 和能量 $\hbar\omega_T$（单位：$\mathrm{meV}$）；
2. 计算长纵光学声子的角频率 $\omega_L$ 和能量 $\hbar\omega_L$（单位：$\mathrm{meV}$）；
3. 估算室温（$T = 300\ \mathrm{K}$）下该长横光学声子模式的平均声子占据数 $\bar{n}$。

::: details 思路提示
由 $\omega_T = 2\pi c / \lambda_T$ 先求 $\omega_T$，再用 LST 关系求 $\omega_L$；最后代入玻色-爱因斯坦分布 $\bar{n} = (e^{\hbar\omega_T/(k_B T)} - 1)^{-1}$，室温 $k_B T \approx 25.85\ \mathrm{meV}$。
:::

::: details 参考答案与解析
**参考答案**：
1. $\omega_T \approx 3.09 \times 10^{13}\ \mathrm{rad/s}$，$\hbar\omega_T \approx 20.3\ \mathrm{meV}$；
2. $\omega_L \approx 4.88 \times 10^{13}\ \mathrm{rad/s}$，$\hbar\omega_L \approx 32.1\ \mathrm{meV}$；
3. $\bar{n} \approx 0.837$。

**解析**：
1. 长横光学声子频率与能量：
   $$\omega_T = \frac{2\pi c}{\lambda_T} = \frac{2\pi \times 2.998 \times 10^8}{61.0 \times 10^{-6}} \approx 3.088 \times 10^{13}\ \mathrm{rad/s}$$
   $$\hbar\omega_T = \frac{1.055 \times 10^{-34} \times 3.088 \times 10^{13}}{1.602 \times 10^{-19}}\ \mathrm{eV} \approx 0.02033\ \mathrm{eV} = 20.3\ \mathrm{meV}$$

2. 由 LST 关系 $\frac{\omega_L}{\omega_T} = \sqrt{\frac{\varepsilon(0)}{\varepsilon(\infty)}} = \sqrt{\frac{5.62}{2.25}} \approx 1.580$：
   $$\omega_L = 1.580 \times 3.088 \times 10^{13} \approx 4.88 \times 10^{13}\ \mathrm{rad/s}$$
   $$\hbar\omega_L = 1.580 \times 20.33\ \mathrm{meV} \approx 32.1\ \mathrm{meV}$$

3. 室温 $300\ \mathrm{K}$ 时 $k_B T = 25.85\ \mathrm{meV}$，则 $\frac{\hbar\omega_T}{k_B T} = \frac{20.33}{25.85} \approx 0.786$：
   $$\bar{n} = \frac{1}{e^{0.786} - 1} = \frac{1}{2.195 - 1} \approx 0.837$$
:::

---

### 知识点 4：晶格热容（经典、爱因斯坦与德拜模型）

![晶格热容模型与声子态密度对比](/figures/ch03-heat-capacity.svg)

<p class="fig-caption">图 3-2 晶格热容模型对比曲线及三维声子态密度分布示意</p>

#### 概念选择与填空

`CH03-KP4-01`（单选）关于爱因斯坦模型与德拜模型在极低温（$T \ll \Theta$）下对三维晶体晶格热容的预言，下列评价正确的是（ ）。
A. 爱因斯坦模型预言 $C_V \propto T^3$，与实验完全一致
B. 爱因斯坦模型按指数 $e^{-\Theta_E/T}$ 衰减，比实验值衰减过快，原因是它用单一高频 $\omega_E$ 代替了全部振动模式，忽略了低温易被激发的低频长声学波
C. 德拜模型在低温与实验吻合是因为它精确计入了全部高频光学支声子
D. 德拜模型在高温极限下不满足杜隆-珀蒂定律

::: details 思路提示
低温下热能 $k_B T$ 很小，只有满足 $\hbar\omega \lesssim k_B T$ 的低频声学波模式能被热激发。
:::

::: details 参考答案与解析
**参考答案**：B

**解析**：爱因斯坦模型假设所有原子独立以同一高频率 $\omega_E$ 振动，在 $k_B T \ll \hbar\omega_E$ 时几乎所有模式均被冻结，导致 $C_V$ 指数衰减过快；德拜模型将低频区视作弹性连续介质声学波（$g(\omega) \propto \omega^2$），准确抓住了低温下被激发的长波声学声子数，从而导出与实验高度吻合的 $T^3$ 定律，且因总模式数归一化为 $3N$，高温自然回到 $3Nk_B$。
:::

---

`CH03-KP4-02`（填空）金刚石的德拜温度 $\Theta_D \approx 2230\ \mathrm{K}$，金属铅（Pb）的德拜温度 $\Theta_D \approx 105\ \mathrm{K}$。在室温（$300\ \mathrm{K}$）下，____ 的摩尔定容热容已非常接近经典杜隆-珀蒂值 $3R$，而 ____ 的摩尔热容远小于 $3R$；金刚石德拜温度极高的微观原因是 ____。

::: details 思路提示
比较 $300\ \mathrm{K}$ 分别与两个 $\Theta_D$ 的大小关系；回顾 $\Theta_D \propto \omega_D \propto v_s \propto \sqrt{\beta/m}$。
:::

::: details 参考答案与解析
**参考答案**：铅（Pb）；金刚石；碳原子质量轻且共价键力常数大，导致声速和德拜频率极高。

**解析**：对铅，$300\ \mathrm{K} \gg 105\ \mathrm{K}$，处于高温经典区，$C_{Vm} \approx 3R$；对金刚石，$300\ \mathrm{K} \ll 2230\ \mathrm{K}$，室温下仍处于深量子低温区，大量晶格振动模式被“冻结”，故热容远小于 $3R$（历史上正是金刚石室温热容反常催生了爱因斯坦量子热容理论）。
:::

---

`CH03-KP4-03`（单选）在德拜模型低温极限（$T \ll \Theta_D$）下，一维晶格、二维晶格与三维晶格的声学支晶格热容 $C_V$ 随温度 $T$ 的依赖关系依次为（ ）。
A. $T^3,\ T^3,\ T^3$
B. $T,\ T^2,\ T^3$
C. $T^{1/2},\ T,\ T^{3/2}$
D. $T^2,\ T^3,\ T^4$

::: details 思路提示
在 $d$ 维波矢空间中，球壳体积元 $\propto q^{d-1}\mathrm{d}q$，在线性色散 $\omega = v_s q$ 下态密度 $g(\omega) \propto \omega^{d-1}$，热激发模式数 $\propto \int_0^{k_B T/\hbar} \omega^{d-1}\mathrm{d}\omega \propto T^d$，每激发模式平均能量 $\sim k_B T$，故内能 $U \propto T^{d+1}$。
:::

::: details 参考答案与解析
**参考答案**：B

**解析**：对 $d$ 维线性色散声学波，$g(\omega) \propto \omega^{d-1}$，低温下被激发的声子模式数占总数的比例约为 $(T/\Theta_D)^d$，每模式能量 $\sim k_B T$，故内能 $U \propto T^{d+1}$，求导得热容 $C_V = \frac{\partial U}{\partial T} \propto T^d$。因此 1D、2D、3D 依次为 $T,\ T^2,\ T^3$。
:::

#### 题型一：三维德拜模型推导与德拜温度计算

`CH03-KP4-04` 考虑体积为 $V$、含 $N$ 个原子的三维简单晶体，设 1 支纵波与 2 支横波的平均声速均为 $v_s$。按德拜模型：
1. 推导声子态密度 $g(\omega)$、德拜截止频率 $\omega_D$ 及德拜温度 $\Theta_D$ 的表达式；
2. 写出晶格内能 $U(T)$ 的德拜积分式，并分别导出低温极限（$T \ll \Theta_D$）的德拜 $T^3$ 定律与高温极限（$T \gg \Theta_D$）的杜隆-珀蒂定律（已知 $\int_0^\infty \frac{x^3}{e^x - 1}\,\mathrm{d}x = \frac{\pi^4}{15}$）；
3. 证明 $T = 0\ \mathrm{K}$ 时晶格零点振动总能量为 $E_0 = \frac{9}{8}Nk_B\Theta_D$。

::: details 思路提示
利用三维波矢空间状态密度 $\frac{V}{(2\pi)^3}$ 乘以 3 个极化方向和球壳体积 $4\pi q^2\mathrm{d}q$，结合 $\omega = v_s q$ 与总模式数归一化条件 $\int_0^{\omega_D} g(\omega)\,\mathrm{d}\omega = 3N$。
:::

::: details 参考答案与解析
**参考答案**：
1. $g(\omega) = \frac{3V}{2\pi^2 v_s^3}\omega^2 = \frac{9N}{\omega_D^3}\omega^2$（$0 \le \omega \le \omega_D$），$\omega_D = v_s\left(\frac{6\pi^2 N}{V}\right)^{1/3}$，$\Theta_D = \frac{\hbar\omega_D}{k_B}$；
2. 低温 $C_V = \frac{12\pi^4}{5}Nk_B\left(\frac{T}{\Theta_D}\right)^3$；高温 $C_V = 3Nk_B$；
3. $E_0 = \int_0^{\omega_D} \frac{1}{2}\hbar\omega\,g(\omega)\,\mathrm{d}\omega = \frac{9}{8}Nk_B\Theta_D$。

**解析**：
1. **态密度与 $\omega_D$**：波矢在 $[q, q+\mathrm{d}q]$ 球壳内的三维模式数（含 3 个偏振支）为：
   $$g(q)\,\mathrm{d}q = 3 \cdot \frac{V}{(2\pi)^3} \cdot 4\pi q^2\,\mathrm{d}q = \frac{3V}{2\pi^2}q^2\,\mathrm{d}q$$
   代入线性色散 $q = \omega/v_s$ 得：
   $$g(\omega) = \frac{3V}{2\pi^2 v_s^3}\omega^2$$
   由总模式数归一化 $\int_0^{\omega_D} g(\omega)\,\mathrm{d}\omega = \frac{V\omega_D^3}{2\pi^2 v_s^3} = 3N$，解得：
   $$\omega_D = v_s\left(\frac{6\pi^2 N}{V}\right)^{1/3}, \qquad \Theta_D = \frac{\hbar\omega_D}{k_B}, \qquad g(\omega) = \frac{9N}{\omega_D^3}\omega^2\ (\omega \le \omega_D)$$

2. **热容的高低温极限**：扣除零点能后的热激发内能为：
   $$U_{\text{热}}(T) = \int_0^{\omega_D} \frac{\hbar\omega}{e^{\hbar\omega/(k_B T)} - 1}\cdot\frac{9N}{\omega_D^3}\omega^2\,\mathrm{d}\omega$$
   作代换 $x = \frac{\hbar\omega}{k_B T}$，上限 $x_D = \frac{\Theta_D}{T}$：
   $$U_{\text{热}}(T) = 9Nk_B T\left(\frac{T}{\Theta_D}\right)^3 \int_0^{\Theta_D/T} \frac{x^3}{e^x - 1}\,\mathrm{d}x$$
   - **低温极限（$T \ll \Theta_D$）**：上限 $\Theta_D/T \to \infty$，积分趋于 $\frac{\pi^4}{15}$：
     $$U_{\text{热}}(T) \approx \frac{3\pi^4}{5}Nk_B\frac{T^4}{\Theta_D^3} \implies C_V = \frac{\partial U_{\text{热}}}{\partial T} = \frac{12\pi^4}{5}Nk_B\left(\frac{T}{\Theta_D}\right)^3$$
   - **高温极限（$T \gg \Theta_D$）**：$x \ll 1$，展开 $e^x - 1 \approx x$，积分 $\int_0^{\Theta_D/T} x^2\,\mathrm{d}x = \frac{1}{3}\left(\frac{\Theta_D}{T}\right)^3$：
     $$U_{\text{热}}(T) \approx 3Nk_B T \implies C_V = 3Nk_B$$

3. **零点振动总能量**：
   $$E_0 = \int_0^{\omega_D} \frac{1}{2}\hbar\omega \cdot \frac{9N}{\omega_D^3}\omega^2\,\mathrm{d}\omega = \frac{9N\hbar}{2\omega_D^3}\cdot\frac{\omega_D^4}{4} = \frac{9}{8}N\hbar\omega_D = \frac{9}{8}Nk_B\Theta_D$$
:::

---

`CH03-KP4-05` 已知金属铜（Cu，面心立方结构，晶格常数 $a = 3.615\ \text{Å}$）的纵波声速 $v_l = 4760\ \mathrm{m/s}$，横波声速 $v_t = 2325\ \mathrm{m/s}$。
1. 计算铜的原子数密度 $n = N/V$ 与平均声速 $\bar{v}$（按 $\frac{3}{\bar{v}^3} = \frac{1}{v_l^3} + \frac{2}{v_t^3}$ 定义）；
2. 计算铜的德拜频率 $\omega_D$ 与德拜温度 $\Theta_D$；
3. 利用德拜 $T^3$ 定律估算铜在 $T = 10\ \mathrm{K}$ 时的晶格摩尔定容热容 $C_{Vm}$（单位：$\mathrm{J/(mol\cdot K)}$）。

::: details 思路提示
fcc 惯用胞含 $4$ 个原子，故 $n = 4/a^3$；注意摩尔气体常数 $R = N_A k_B = 8.314\ \mathrm{J/(mol\cdot K)}$，验证 $10\ \mathrm{K} \ll \Theta_D$ 满足低温条件。
:::

::: details 参考答案与解析
**参考答案**：
1. $n \approx 8.47 \times 10^{28}\ \mathrm{m^{-3}}$，$\bar{v} \approx 2612\ \mathrm{m/s}$；
2. $\omega_D \approx 4.47 \times 10^{13}\ \mathrm{rad/s}$，$\Theta_D \approx 341\ \mathrm{K}$；
3. $C_{Vm}(10\ \mathrm{K}) \approx 0.0488\ \mathrm{J/(mol\cdot K)}$（$48.8\ \mathrm{mJ/(mol\cdot K)}$）。

**解析**：
1. 原子数密度与平均声速：
   $$n = \frac{4}{a^3} = \frac{4}{(3.615 \times 10^{-10}\ \mathrm{m})^3} \approx 8.467 \times 10^{28}\ \mathrm{m^{-3}}$$
   $$\frac{1}{\bar{v}^3} = \frac{1}{3}\left(\frac{1}{4760^3} + \frac{2}{2325^3}\right) \approx 5.613 \times 10^{-11}\ \mathrm{s^3/m^3} \implies \bar{v} \approx 2612\ \mathrm{m/s}$$

2. 德拜频率与德拜温度：
   $$\omega_D = \bar{v}(6\pi^2 n)^{1/3} = 2611.7 \times (6\pi^2 \times 8.467 \times 10^{28})^{1/3} \approx 4.470 \times 10^{13}\ \mathrm{rad/s}$$
   $$\Theta_D = \frac{\hbar\omega_D}{k_B} = \frac{1.055 \times 10^{-34} \times 4.470 \times 10^{13}}{1.381 \times 10^{-23}} \approx 341.4\ \mathrm{K}$$
   （与实验值 $343\ \mathrm{K}$ 极为吻合。）

3. $T = 10\ \mathrm{K} \ll 341\ \mathrm{K}$，适用德拜 $T^3$ 定律：
   $$C_{Vm} = \frac{12\pi^4}{5}R\left(\frac{T}{\Theta_D}\right)^3 = 233.78 \times 8.314 \times \left(\frac{10}{341.4}\right)^3 \approx 0.0488\ \mathrm{J/(mol\cdot K)}$$
:::

#### 题型二：二维晶格的德拜热容模型

`CH03-KP4-06` 考虑面积为 $S$、含 $N$ 个原子的二维简单晶体，在二维平面内存在 $2$ 支线性色散声学波（设平均声速均为 $v_s$）。按二维德拜模型：
1. 推导声子态密度 $g(\omega)$ 与德拜截止频率 $\omega_D$；
2. 推导低温极限（$T \ll \Theta_D$）下晶格热容 $C_V$ 的解析表达式（已知 $\int_0^\infty \frac{x^2}{e^x - 1}\,\mathrm{d}x = 2\zeta(3) \approx 2.404$）。

::: details 思路提示
二维波矢空间状态密度为 $\frac{S}{(2\pi)^2}$，波矢环面积元为 $2\pi q\,\mathrm{d}q$，总模式数归一化为 $2N$。
:::

::: details 参考答案与解析
**参考答案**：
1. $g(\omega) = \frac{S}{\pi v_s^2}\omega = \frac{4N}{\omega_D^2}\omega$（$0 \le \omega \le \omega_D$），$\omega_D = v_s\sqrt{\frac{4\pi N}{S}}$；
2. $C_V = 24\zeta(3)\,Nk_B\left(\frac{T}{\Theta_D}\right)^2 \approx 28.85\,Nk_B\left(\frac{T}{\Theta_D}\right)^2$。

**解析**：
1. 含 $2$ 个平面内偏振方向，波矢在 $[q, q+\mathrm{d}q]$ 内的模式数为：
   $$g(q)\,\mathrm{d}q = 2 \cdot \frac{S}{(2\pi)^2} \cdot 2\pi q\,\mathrm{d}q = \frac{S}{\pi}q\,\mathrm{d}q$$
   代入 $q = \omega/v_s$ 得 $g(\omega) = \frac{S}{\pi v_s^2}\omega$。由总模式数归一化 $\int_0^{\omega_D} g(\omega)\,\mathrm{d}\omega = \frac{S\omega_D^2}{2\pi v_s^2} = 2N$：
   $$\omega_D = v_s\sqrt{\frac{4\pi N}{S}}, \qquad g(\omega) = \frac{4N}{\omega_D^2}\omega \quad (0 \le \omega \le \omega_D)$$

2. 令 $x = \frac{\hbar\omega}{k_B T}$，热激发内能为：
   $$U_{\text{热}}(T) = \int_0^{\omega_D} \frac{\hbar\omega}{e^{\hbar\omega/(k_B T)}-1}\cdot\frac{4N}{\omega_D^2}\omega\,\mathrm{d}\omega = 4Nk_B T\left(\frac{T}{\Theta_D}\right)^2 \int_0^{\Theta_D/T} \frac{x^2}{e^x - 1}\,\mathrm{d}x$$
   低温极限 $\Theta_D/T \to \infty$，积分收敛至 $2\zeta(3)$：
   $$U_{\text{热}}(T) \approx 8\zeta(3)Nk_B\frac{T^3}{\Theta_D^2} \implies C_V = \frac{\partial U_{\text{热}}}{\partial T} = 24\zeta(3)Nk_B\left(\frac{T}{\Theta_D}\right)^2 \approx 28.85\,Nk_B\left(\frac{T}{\Theta_D}\right)^2$$
:::

---

### 知识点 5：非简谐效应与实验测定方法

#### 概念选择与填空

`CH03-KP5-01`（单选）若晶体中原子的相互作用势能严格取简谐近似，则下列物理量在非零有限温度下的理论值应为（ ）。
A. 线热膨胀系数 $\alpha = 0$，晶格热导率 $\kappa \to \infty$
B. 线热膨胀系数 $\alpha > 0$，晶格热导率 $\kappa \to \infty$
C. 线热膨胀系数 $\alpha = 0$，晶格热导率 $\kappa = 0$
D. 线热膨胀系数 $\alpha > 0$，晶格热导率 $\kappa$ 为有限值

::: details 思路提示
简谐近似有两大直接推论：势阱对称（无热膨胀）、简正模退耦无散射（声子平均自由程无穷大）。
:::

::: details 参考答案与解析
**参考答案**：A

**解析**：简谐势对称导致 $\langle x \rangle \equiv 0$（热膨胀为零）；简正模式完全独立无碰撞散射，声子平均自由程 $\bar{l} \to \infty$，故晶格热导率 $\kappa = \frac{1}{3}C_V \bar{v}\bar{l} \to \infty$。
:::

---

`CH03-KP5-02`（单选）关于绝缘体中三声子碰撞的 N 过程（正规过程）与 U 过程（倒逆过程），下列说法正确的是（ ）。
A. N 过程满足 $\mathbf{q}_1 + \mathbf{q}_2 = \mathbf{q}_3 + \mathbf{G}$（$\mathbf{G} \ne 0$），直接导致热阻
B. U 过程使声子总准动量守恒，因此不直接产生热阻
C. U 过程满足 $\mathbf{q}_1 + \mathbf{q}_2 = \mathbf{q}_3 + \mathbf{G}$（$\mathbf{G} \ne 0$），能够改变能流总方向，是纯净晶体高温本征热阻的根本原因
D. 在极低温下，U 过程发生概率急剧增加，使热导率迅速下降

::: details 思路提示
区分 $\mathbf{G} = 0$（N 过程）与 $\mathbf{G} \ne 0$（U 过程）；触发 U 过程需要声子波矢够大（能量约 $\sim \frac{1}{2}k_B\Theta_D$），故极低温时 U 过程被指数冻结。
:::

::: details 参考答案与解析
**参考答案**：C

**解析**：N 过程（$\mathbf{G} = 0$）保持总准动量 $\sum \hbar\mathbf{q}$ 不变，不能衰减声子能流，不直接产生热阻；U 过程（$\mathbf{G} \ne 0$）把合成波矢折回第一布里渊区反侧，逆转能流方向，直接产生热阻。在高温下（$T > \Theta_D$），声子数 $\propto T$，平均自由程 $\bar{l} \propto T^{-1}$，而 $C_V$ 趋于常数，故 $\kappa \propto T^{-1}$；极低温下 U 过程指数衰减，热阻转为样品边界散射控制（$\bar{l} \approx \text{常数}$），此时 $\kappa \propto C_V \propto T^3$。
:::

---

`CH03-KP5-03`（填空）实验上测定晶体整个布里渊区完整声子色散曲线 $\omega(\mathbf{q})$ 最主要的方法是 ____；用可见光/激光测定 $q \approx 0$ 处光学声子频率常用 ____ 散射，测定 $q \approx 0$ 处声学声子频率常用 ____ 散射。

::: details 思路提示
对比热中子与光子的动量量级：热中子波长与晶格常数（$\sim \text{Å}$）相当，动量覆盖整个布里渊区；可见光波长数千埃，波矢 $k \ll \pi/a$，只能探测布里渊区中心附近。
:::

::: details 参考答案与解析
**参考答案**：非弹性中子散射；拉曼（Raman）；布里渊（Brillouin）。

**解析**：能量为几十 $\mathrm{meV}$ 的热中子德布罗意波长恰在 $1\text{–}2\ \text{Å}$ 量级，其能量与动量变化同时匹配整个布里渊区内的声子；可见光波矢比布里渊区尺度小 3 个数量级，只能探测 $q \approx 0$ 附近光学声子（拉曼散射）和声学声子（布里渊散射）。
:::

#### 题型一：非简谐势下的晶格热膨胀推导

`CH03-KP5-04` 将晶体中一对相邻原子的相对位移势能按非简谐近似展开至四次项：
$$V(x) = c x^2 - g x^3 - f x^4 \qquad (c, g, f > 0)$$
其中非简谐项满足 $|gx^3|, |fx^4| \ll k_B T$。
1. 在经典玻尔兹曼统计下，利用弱非简谐微扰展开，计算原子在温度 $T$ 时的热平均位移 $\langle x \rangle$；
2. 指出三次项 $-gx^3$ 与四次项 $-fx^4$ 对线热膨胀系数 $\alpha_L = \frac{1}{a}\frac{\mathrm{d}\langle x \rangle}{\mathrm{d}T}$ 各自起什么作用。

::: details 思路提示
将玻尔兹曼因子拆分为 $e^{-V(x)/(k_B T)} \approx e^{-\beta c x^2}\left(1 + \beta g x^3 + \beta f x^4\right)$（$\beta = \frac{1}{k_B T}$），利用对称区间上奇函数积分为零以及高斯积分 $\int_{-\infty}^{\infty} x^4 e^{-\lambda x^2}\,\mathrm{d}x = \frac{3}{4\lambda^2}\sqrt{\frac{\pi}{\lambda}}$。
:::

::: details 参考答案与解析
**参考答案**：
1. $\langle x \rangle = \frac{3g}{4c^2}k_B T$；
2. 线热膨胀系数 $\alpha_L = \frac{3gk_B}{4ac^2}$ 仅来自**三次非简谐项 $-gx^3$**（破坏势阱左右对称性）；偶对称的四次项 $-fx^4$ 对最低阶热平均位移和热膨胀没有贡献。

**解析**：
1. 记 $\beta = \frac{1}{k_B T}$，由经典统计系综平均定义：
   $$\langle x \rangle = \frac{\int_{-\infty}^{\infty} x e^{-\beta(cx^2 - gx^3 - fx^4)}\,\mathrm{d}x}{\int_{-\infty}^{\infty} e^{-\beta(cx^2 - gx^3 - fx^4)}\,\mathrm{d}x}$$
   对弱非简谐项做一阶展开 $e^{\beta(gx^3 + fx^4)} \approx 1 + \beta g x^3 + \beta f x^4$：
   - 分子积分：$\int_{-\infty}^{\infty} \left(x + \beta g x^4 + \beta f x^5\right)e^{-\beta c x^2}\,\mathrm{d}x$。其中 $x$ 与 $x^5$ 为奇函数，积分为零，仅保留 $x^4$ 项：
     $$\text{分子} = \beta g \int_{-\infty}^{\infty} x^4 e^{-\beta c x^2}\,\mathrm{d}x = \beta g \cdot \frac{3}{4(\beta c)^2}\sqrt{\frac{\pi}{\beta c}}$$
   - 分母取主阶（简谐归一化因子）：
     $$\text{分母} \approx \int_{-\infty}^{\infty} e^{-\beta c x^2}\,\mathrm{d}x = \sqrt{\frac{\pi}{\beta c}}$$
   两式相除即得：
   $$\langle x \rangle = \frac{3\beta g}{4(\beta c)^2} = \frac{3g}{4\beta c^2} = \frac{3g}{4c^2}k_B T$$

2. 由此得高温经典区线热膨胀系数 $\alpha_L = \frac{1}{a}\frac{\mathrm{d}\langle x \rangle}{\mathrm{d}T} = \frac{3gk_B}{4ac^2}$（常温以上近似为常数）。由于 $x^4$ 是偶函数，不破坏势能关于平衡位置的左右对称性，因此在积分中给出奇函数 $x^5$ 积分为零，不产生热膨胀；真正引起热膨胀的是使势能曲线左侧更陡、右侧更缓的三次非对称项 $-gx^3$。
:::
