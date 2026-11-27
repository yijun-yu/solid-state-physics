# 第五章 固体的能带理论

::: info 教学大纲（建议 9 学时）
- 5.1 布洛赫定理与能带的基本概念
- 5.2 近自由电子近似（平面波微扰法与布里渊区边界能隙）
- 5.3 晶体的布里渊区与能带图示（简约、扩展、周期图示）
- 5.4 紧束缚近似与等能面
- 5.5 准经典近似、电子群速度与有效质量
- 5.6 导体、绝缘体、半导体与空穴概念
- 5.7 费米面的构造与测量及光电子能谱（ARPES）
:::

::: tip 核心概念与模型
**1. 布洛赫定理与能带基本性质**
- **单电子周期势近似**：晶体中电子在等效周期势 $V(\mathbf{r} + \mathbf{R}_l) = V(\mathbf{r})$ 中运动，能量本征函数满足**布洛赫定理**：
  $$\psi_{n\mathbf{k}}(\mathbf{r}) = e^{i\mathbf{k}\cdot\mathbf{r}} u_{n\mathbf{k}}(\mathbf{r}), \qquad u_{n\mathbf{k}}(\mathbf{r} + \mathbf{R}_l) = u_{n\mathbf{k}}(\mathbf{r})$$
  等价平移关系：$\psi_{n\mathbf{k}}(\mathbf{r} + \mathbf{R}_l) = e^{i\mathbf{k}\cdot\mathbf{R}_l}\psi_{n\mathbf{k}}(\mathbf{r})$。电子在各原胞中的几率密度 $|\psi_{n\mathbf{k}}(\mathbf{r})|^2$ 具有晶格周期性。
- **能带对称性与容量**：$E_n(\mathbf{k} + \mathbf{G}) = E_n(\mathbf{k})$（倒空间周期性），$E_n(-\mathbf{k}) = E_n(\mathbf{k})$（时间反演对称性）。对含 $N$ 个原胞的晶体，第一布里渊区含 $N$ 个独立波矢 $\mathbf{k}$，计入自旋后**每个能带最多容纳 $2N$ 个电子**。
- **三种等价能带图示**：简约布里渊区图示（所有能带折回第一布里渊区）、扩展布里渊区图示（第 $n$ 带画在第 $n$ 布里渊区，便于与自由电子对比）、周期图示（每个能带按倒格矢周期延拓）。

**2. 两种互补的能带近似方法**

| 方法 | 物理出发点 | 适用体系 | 核心结果 |
| :--- | :--- | :--- | :--- |
| 近自由电子近似（平面波法） | 弱周期势 $V(\mathbf{r}) = \sum_{\mathbf{G}} V_{\mathbf{G}} e^{i\mathbf{G}\cdot\mathbf{r}}$ 作为微扰 | 简单金属（碱金属、Al 等）$s/p$ 价带 | 在布拉格面 $2\mathbf{k}\cdot\mathbf{G} + G^2 = 0$ 处简并态混合成驻波，打开能隙 $E_g = 2|V_{\mathbf{G}}|$ |
| 紧束缚近似（LCAO 法） | 孤立原子轨道线性组合 $\sum_l e^{i\mathbf{k}\cdot\mathbf{R}_l}\phi(\mathbf{r}-\mathbf{R}_l)$ | 窄能带（过渡金属 $d$ 带、绝缘体价带、分子晶体） | $E(\mathbf{k}) = E_0 - \alpha - J\sum_{\boldsymbol{\delta}} e^{i\mathbf{k}\cdot\boldsymbol{\delta}}$，交叠越强带宽越宽 |

- **三维立方晶格 $s$ 态紧束缚能带**（仅计最近邻 $J > 0$）：
  - 简单立方（sc）：$E(\mathbf{k}) = E_0 - \alpha - 2J(\cos k_x a + \cos k_y a + \cos k_z a)$，带宽 $12J$；
  - 体心立方（bcc）：$E(\mathbf{k}) = E_0 - \alpha - 8J\cos\frac{k_x a}{2}\cos\frac{k_y a}{2}\cos\frac{k_z a}{2}$，带宽 $16J$；
  - 面心立方（fcc）：$E(\mathbf{k}) = E_0 - \alpha - 4J\!\left(\cos\frac{k_x a}{2}\cos\frac{k_y a}{2} + \cos\frac{k_y a}{2}\cos\frac{k_z a}{2} + \cos\frac{k_z a}{2}\cos\frac{k_x a}{2}\right)$，带宽 $16J$。

**3. 准经典运动、有效质量与空穴**
- **电子群速度与准动量定理**：
  $$\mathbf{v}(\mathbf{k}) = \frac{1}{\hbar}\nabla_{\mathbf{k}} E(\mathbf{k}), \qquad \hbar\frac{\mathrm{d}\mathbf{k}}{\mathrm{d}t} = \mathbf{F}_{\text{外}} = -e(\mathbf{E} + \mathbf{v}\times\mathbf{B})$$
  $\hbar\mathbf{k}$ 为**准动量**而非电子真实机械动量；外力仅改变 $\hbar\mathbf{k}$，晶格周期内力已全部封装于能带色散 $E(\mathbf{k})$ 及**有效质量张量**中：
  $$\left(\frac{1}{m^*}\right)_{ij} = \frac{1}{\hbar^2}\frac{\partial^2 E(\mathbf{k})}{\partial k_i \partial k_j}$$
- **满带不导电与空穴**：满带总电流恒为零。满带顶附近缺失一个状态为 $(\mathbf{k}_e, E_e, \mathbf{v}_e, m_e^* < 0)$ 的电子，等效于一个电荷 $q_h = +e$、波矢 $\mathbf{k}_h = -\mathbf{k}_e$、速度 $\mathbf{v}_h = \mathbf{v}_e$、正有效质量 $m_h^* = -m_e^* > 0$ 的**空穴**。

**4. 导体/绝缘体/半导体判别与费米面实验测量**
- **能带填充判据**：存在未满带（奇数价电子单原子原胞，或偶数价电子但三维能带交叠如 Mg/Be）为**金属**；所有被占能带全满且与空导带间有禁带 $E_g$，按禁带宽度区分**半导体**（$E_g \lesssim 3\ \mathrm{eV}$）与**绝缘体**（$E_g \gtrsim 4\ \mathrm{eV}$）。
- **实验探测技术**：
  - **回旋共振**：$\omega_c = \frac{eB}{m_c^*}$，直接测定回旋有效质量 $m_c^*$；
  - **德哈斯-范阿尔芬（dHvA）效应**：磁化率随 $1/B$ 周期振荡，$\Delta\left(\frac{1}{B}\right) = \frac{2\pi e}{\hbar S_{\text{ext}}}$，测定费米面垂直于 $\mathbf{B}$ 的极值截面积 $S_{\text{ext}}$；
  - **角分辨光电子能谱（ARPES）**：直接测量能带色散 $E(\mathbf{k}_\parallel)$，满足：
    $$\begin{aligned} E_B &= E_F - E = h\nu - W - E_{\text{kin}} \\ k_\parallel &= \frac{\sqrt{2m_0 E_{\text{kin}}}}{\hbar}\sin\theta \end{aligned}$$
:::

![一维近自由电子能带与二维正方晶格紧束缚等能线](/figures/ch05-band-diagrams.svg)

<p class="fig-caption">图 5-1 一维近自由电子能带（扩展与简约图示）及二维正方晶格第一布里渊区紧束缚等能线</p>

## 习题及参考解答

### 知识点 1：布洛赫定理与能带图示

#### 概念选择与填空

`CH05-KP1-01`（单选）关于晶体中电子的布洛赫波函数 $\psi_{n\mathbf{k}}(\mathbf{r}) = e^{i\mathbf{k}\cdot\mathbf{r}} u_{n\mathbf{k}}(\mathbf{r})$，下列说法**错误**的是（ ）。
A. 调幅函数 $u_{n\mathbf{k}}(\mathbf{r})$ 具有与晶格正格子相同的平移周期性，即 $u_{n\mathbf{k}}(\mathbf{r} + \mathbf{R}_l) = u_{n\mathbf{k}}(\mathbf{r})$
B. 电子出现在晶体中任意等价格点周围的几率密度 $|\psi_{n\mathbf{k}}(\mathbf{r})|^2$ 具有晶格周期性
C. 当电子坐标平移一个晶格矢量 $\mathbf{R}_l$ 时，波函数仅乘以相位因子 $e^{i\mathbf{k}\cdot\mathbf{R}_l}$
D. 布洛赫波函数是电子动量算符 $\hat{\mathbf{p}} = -i\hbar\nabla$ 的本征函数，其本征值为 $\hbar\mathbf{k}$

::: details 思路提示
将动量算符 $-i\hbar\nabla$ 直接作用在乘积 $e^{i\mathbf{k}\cdot\mathbf{r}} u_{n\mathbf{k}}(\mathbf{r})$ 上，检查是否仅得到常数乘以原波函数。
:::

::: details 参考答案与解析
**参考答案**：D

**解析**：由于周期势破坏了空间的连续平移对称性（仅保留分立晶格平移对称性），$[\hat{\mathbf{p}}, \hat{H}] \ne 0$。直接求导得：
$$-i\hbar\nabla\left[e^{i\mathbf{k}\cdot\mathbf{r}} u_{n\mathbf{k}}(\mathbf{r})\right] = \hbar\mathbf{k}\psi_{n\mathbf{k}}(\mathbf{r}) + e^{i\mathbf{k}\cdot\mathbf{r}}\left(-i\hbar\nabla u_{n\mathbf{k}}(\mathbf{r})\right)$$
因一般 $\nabla u_{n\mathbf{k}} \ne 0$，布洛赫态**不是**动量算符的本征态，$\hbar\mathbf{k}$ 是反映晶格平移对称性的**准动量（晶格动量）**而非电子的机械动量本征值。A、B、C 均正确。
:::

---

`CH05-KP1-02`（填空）由 $N$ 个原胞构成的晶体在玻恩-卡门周期性边界条件下，第一布里渊区内共有 ____ 个独立的波矢 $\mathbf{k}$；计入电子自旋简并度后，每个能带最多可容纳 ____ 个电子；能带本征能量在倒空间中满足平移周期性 $E_n(\mathbf{k} + \mathbf{G}) =$ ____ 及空间/时间反演对称性 $E_n(-\mathbf{k}) =$ ____。

::: details 思路提示
回想倒空间每个波矢态占体积 $\frac{(2\pi)^3}{V}$、第一布里渊区体积等于倒格子原胞体积 $\frac{(2\pi)^3}{\Omega}$；结合布洛赫波矢仅定义至相差倒格矢 $\mathbf{G}$ 与薛定谔方程复共轭对称性。
:::

::: details 参考答案与解析
**参考答案**：$N$；$2N$；$E_n(\mathbf{k})$；$E_n(\mathbf{k})$。

**解析**：第一布里渊区体积为 $\frac{(2\pi)^3}{\Omega}$，每个允许波矢占体积 $\frac{(2\pi)^3}{N\Omega}$，故波矢总数为 $N$，计及自旋 $\pm\frac{1}{2}$ 后每能带可容纳 $2N$ 个电子。因 $e^{i\mathbf{G}\cdot\mathbf{R}_l} = 1$，$\mathbf{k}$ 与 $\mathbf{k} + \mathbf{G}$ 标记同一平移本征值，故 $E_n(\mathbf{k} + \mathbf{G}) = E_n(\mathbf{k})$；无外磁场时哈密顿量实对称，取复共轭立得 $E_n(-\mathbf{k}) = E_n(\mathbf{k})$。
:::

---

`CH05-KP1-03`（单选）关于能带的简约布里渊区图示、扩展布里渊区图示与周期图示，下列说法**错误**的是（ ）。
A. 三种图示描述的物理本征态与能谱完全等价，只是选取波矢 $\mathbf{k}$ 的区间方式不同
B. 简约布里渊区图示将所有能带通过减去适当倒格矢 $\mathbf{G}$ 全部折回第一布里渊区内，最便于表示多能带结构与直接/间接跃迁
C. 扩展布里渊区图示将第 $n$ 条能带画在第 $n$ 布里渊区内，便于与自由电子抛物线色散直接对照
D. 在一维非简并能带中，所有能带在布里渊区边界 $k = \pm\frac{\pi}{a}$ 处的斜率 $\frac{\mathrm{d}E}{\mathrm{d}k}$ 均不等于零

::: details 思路提示
结合能带的倒空间周期性 $E(k + \frac{2\pi}{a}) = E(k)$ 与偶对称性 $E(-k) = E(k)$，检查 $E(k)$ 在 $k = \frac{\pi}{a}$ 两侧的对称性。
:::

::: details 参考答案与解析
**参考答案**：D

**解析**：对一维能带，由周期性与偶对称性联合得 $E\left(\frac{\pi}{a} + q\right) = E\left(-\frac{\pi}{a} + q\right) = E\left(\frac{\pi}{a} - q\right)$，即 $E(k)$ 关于区边界 $k = \frac{\pi}{a}$ 严格偶对称。若该处能带非简并且可微，则导数必满足 $\left.\frac{\mathrm{d}E}{\mathrm{d}k}\right|_{k=\pi/a} = 0$（群速度为零，对应驻波，等能面垂直于布里渊区边界）。故 D 错误。
:::

#### 题型一：布洛赫定理的证明与准动量辨析

`CH05-KP1-04` 考虑一维（或三维）严格周期势场中的单电子哈密顿量 $\hat{H} = -\frac{\hbar^2}{2m}\nabla^2 + V(\mathbf{r})$，其中 $V(\mathbf{r} + \mathbf{R}) = V(\mathbf{r})$（$\mathbf{R}$ 为任意布拉维格矢）。
1. 定义晶格平移算符 $\hat{T}_{\mathbf{R}} \psi(\mathbf{r}) = \psi(\mathbf{r} + \mathbf{R})$，证明 $[\hat{T}_{\mathbf{R}}, \hat{H}] = 0$ 及平移算符构成阿贝尔群 $\hat{T}_{\mathbf{R}_1}\hat{T}_{\mathbf{R}_2} = \hat{T}_{\mathbf{R}_1 + \mathbf{R}_2}$；
2. 结合玻恩-卡门周期性边界条件 $\psi(\mathbf{r} + N_i \mathbf{a}_i) = \psi(\mathbf{r})$，导出 $\hat{H}$ 与 $\hat{T}_{\mathbf{R}}$ 共同本征函数的形式 $\psi_{\mathbf{k}}(\mathbf{r}) = e^{i\mathbf{k}\cdot\mathbf{r}} u_{\mathbf{k}}(\mathbf{r})$（布洛赫定理）；
3. 证明布洛赫波函数可按倒格矢展开为平面波叠加 $\psi_{\mathbf{k}}(\mathbf{r}) = \sum_{\mathbf{G}} C_{\mathbf{k}-\mathbf{G}} e^{i(\mathbf{k}-\mathbf{G})\cdot\mathbf{r}}$，并据此说明为何电子在晶格中的动量平均值一般不等于 $\hbar\mathbf{k}$。

::: details 思路提示
第 1 问对任意波函数 $\psi(\mathbf{r})$ 检验 $\hat{T}_{\mathbf{R}}(\hat{H}\psi(\mathbf{r}))$ 与 $\hat{H}(\hat{T}_{\mathbf{R}}\psi(\mathbf{r}))$；第 2 问设共同本征值 $\hat{T}_{\mathbf{R}}\psi = c(\mathbf{R})\psi$，利用乘法性质 $c(\mathbf{R}_1)c(\mathbf{R}_2) = c(\mathbf{R}_1+\mathbf{R}_2)$ 及周期性边界条件确定模长为 $1$ 的指数形式 $c(\mathbf{R}) = e^{i\mathbf{k}\cdot\mathbf{R}}$；第 3 问对周期函数 $u_{\mathbf{k}}(\mathbf{r})$ 做傅里叶展开。
:::

::: details 参考答案与解析
**参考答案**：
1. 证明见下；
2. $\psi_{\mathbf{k}}(\mathbf{r}) = e^{i\mathbf{k}\cdot\mathbf{r}} u_{\mathbf{k}}(\mathbf{r})$，其中 $u_{\mathbf{k}}(\mathbf{r}+\mathbf{R}) = u_{\mathbf{k}}(\mathbf{r})$；
3. $\langle \hat{\mathbf{p}} \rangle = \sum_{\mathbf{G}} |C_{\mathbf{k}-\mathbf{G}}|^2 \hbar(\mathbf{k} - \mathbf{G}) = \hbar\mathbf{k} - \sum_{\mathbf{G}} |C_{\mathbf{k}-\mathbf{G}}|^2 \hbar\mathbf{G}$，一般不等于 $\hbar\mathbf{k}$。

**解析**：
1. **对易性与群性质**：对任意函数 $\psi(\mathbf{r})$，动能算符在坐标平移 $\mathbf{r} \to \mathbf{r} + \mathbf{R}$ 下不变，势能满足 $V(\mathbf{r}+\mathbf{R}) = V(\mathbf{r})$，故：
   $$\hat{T}_{\mathbf{R}}\left[\hat{H}(\mathbf{r})\psi(\mathbf{r})\right] = \hat{H}(\mathbf{r}+\mathbf{R})\psi(\mathbf{r}+\mathbf{R}) = \hat{H}(\mathbf{r})\psi(\mathbf{r}+\mathbf{R}) = \hat{H}\left[\hat{T}_{\mathbf{R}}\psi(\mathbf{r})\right]$$
   即 $[\hat{T}_{\mathbf{R}}, \hat{H}] = 0$。连续平移满足：
   $$\hat{T}_{\mathbf{R}_1}\hat{T}_{\mathbf{R}_2}\psi(\mathbf{r}) = \psi(\mathbf{r}+\mathbf{R}_1+\mathbf{R}_2) = \hat{T}_{\mathbf{R}_1+\mathbf{R}_2}\psi(\mathbf{r}) = \hat{T}_{\mathbf{R}_2}\hat{T}_{\mathbf{R}_1}\psi(\mathbf{r})$$
   故所有平移算符彼此对易且与 $\hat{H}$ 对易，存在共同本征函数组。

2. **布洛赫定理导出**：设共同本征态满足 $\hat{T}_{\mathbf{R}}\psi(\mathbf{r}) = c(\mathbf{R})\psi(\mathbf{r})$。由 $\hat{T}_{\mathbf{R}_1}\hat{T}_{\mathbf{R}_2} = \hat{T}_{\mathbf{R}_1+\mathbf{R}_2}$ 得 $c(\mathbf{R}_1)c(\mathbf{R}_2) = c(\mathbf{R}_1+\mathbf{R}_2)$。对三个原胞基矢 $\mathbf{a}_i$，由玻恩-卡门条件 $\hat{T}_{N_i \mathbf{a}_i}\psi = \psi \implies [c(\mathbf{a}_i)]^{N_i} = 1$，解得：
   $$c(\mathbf{a}_i) = \exp\!\left(i\frac{2\pi n_i}{N_i}\right) \quad (n_i \in \mathbb{Z})$$
   引入实波矢 $\mathbf{k} = \sum_{i=1}^3 \frac{n_i}{N_i}\mathbf{b}_i$（满足 $\mathbf{a}_i\cdot\mathbf{b}_j = 2\pi\delta_{ij}$），则对任意格矢 $\mathbf{R} = \sum_i l_i \mathbf{a}_i$ 有：
   $$c(\mathbf{R}) = \prod_{i=1}^3 [c(\mathbf{a}_i)]^{l_i} = e^{i\mathbf{k}\cdot\mathbf{R}} \implies \psi_{\mathbf{k}}(\mathbf{r}+\mathbf{R}) = e^{i\mathbf{k}\cdot\mathbf{R}}\psi_{\mathbf{k}}(\mathbf{r})$$
   定义 $u_{\mathbf{k}}(\mathbf{r}) \equiv e^{-i\mathbf{k}\cdot\mathbf{r}}\psi_{\mathbf{k}}(\mathbf{r})$，立即验证：
   $$u_{\mathbf{k}}(\mathbf{r}+\mathbf{R}) = e^{-i\mathbf{k}\cdot(\mathbf{r}+\mathbf{R})}\psi_{\mathbf{k}}(\mathbf{r}+\mathbf{R}) = e^{-i\mathbf{k}\cdot\mathbf{r}}\psi_{\mathbf{k}}(\mathbf{r}) = u_{\mathbf{k}}(\mathbf{r})$$
   从而证明 $\psi_{\mathbf{k}}(\mathbf{r}) = e^{i\mathbf{k}\cdot\mathbf{r}} u_{\mathbf{k}}(\mathbf{r})$。

3. **平面波展开与动量期望值**：因 $u_{\mathbf{k}}(\mathbf{r})$ 具有晶格周期性，可按倒格矢做傅里叶级数展开 $u_{\mathbf{k}}(\mathbf{r}) = \sum_{\mathbf{G}} C_{\mathbf{k}-\mathbf{G}} e^{-i\mathbf{G}\cdot\mathbf{r}}$，于是：
   $$\psi_{\mathbf{k}}(\mathbf{r}) = \sum_{\mathbf{G}} C_{\mathbf{k}-\mathbf{G}} e^{i(\mathbf{k}-\mathbf{G})\cdot\mathbf{r}}$$
   归一化条件为 $\sum_{\mathbf{G}} |C_{\mathbf{k}-\mathbf{G}}|^2 = 1$，电子真实动量期望值为：
   $$\langle \hat{\mathbf{p}} \rangle = \langle \psi_{\mathbf{k}} | -i\hbar\nabla | \psi_{\mathbf{k}} \rangle = \sum_{\mathbf{G}} |C_{\mathbf{k}-\mathbf{G}}|^2 \hbar(\mathbf{k} - \mathbf{G}) = \hbar\mathbf{k} - \sum_{\mathbf{G}} |C_{\mathbf{k}-\mathbf{G}}|^2 \hbar\mathbf{G}$$
   由于晶格势场与电子交换倒格矢动量 $\hbar\mathbf{G}$，$\langle \hat{\mathbf{p}} \rangle = m_0 \mathbf{v}(\mathbf{k}) = \frac{m_0}{\hbar}\nabla_{\mathbf{k}} E(\mathbf{k})$ 一般不等于 $\hbar\mathbf{k}$（例如在布里渊区边界驻波态处 $\langle \hat{\mathbf{p}} \rangle = 0$，但 $\hbar\mathbf{k} = \pm\frac{\hbar\pi}{a} \ne 0$）。
:::

---

### 知识点 2：近自由电子近似与布里渊区能隙

#### 概念选择与填空

`CH05-KP2-01`（单选）在近自由电子近似中，一维布里渊区边界 $k = \pm\frac{\pi}{a}$ 处打开能隙 $E_g = 2|V_1|$ 的根本物理原因是（ ）。
A. 电子间库仑排斥导致高能电子跃迁受阻
B. 在布拉格反射条件下，波矢为 $\frac{\pi}{a}$ 与 $-\frac{\pi}{a}$ 的两列简并平面波受周期势耦合形成两类驻波，其电荷密度分别聚集于离子实处与离子实间隙处，产生静电势能差
C. 泡利不相容原理禁止电子占据 $k = \pm\frac{\pi}{a}$ 处的状态
D. 晶格热振动吸收电子能量产生频率禁带

::: details 思路提示
回顾 $\psi_+ \propto \cos\frac{\pi x}{a}$ 与 $\psi_- \propto \sin\frac{\pi x}{a}$ 对应的电子几率密度 $|\psi_+|^2 \propto \cos^2\frac{\pi x}{a}$ 和 $|\psi_-|^2 \propto \sin^2\frac{\pi x}{a}$ 在格点 $x = na$ 处的分布差异。
:::

::: details 参考答案与解析
**参考答案**：B

**解析**：在 $k = \frac{\pi}{a}$ 处，平面波 $e^{i\pi x/a}$ 与布拉格反射波 $e^{-i\pi x/a}$ 能量简并，弱周期势 $V(x)$ 将两者线性组合成驻波 $\psi_+ \propto \cos\frac{\pi x}{a}$ 与 $\psi_- \propto \sin\frac{\pi x}{a}$。$|\psi_+|^2$ 峰值位于带正电的离子实位置（$x = na$），吸引势能更低；$|\psi_-|^2$ 峰值位于离子实中点间隙（$x = (n+\frac{1}{2})a$），势能较高。两驻波平均势能之差即为能隙 $2|V_1|$。
:::

---

`CH05-KP2-02`（填空）一维晶格（晶格常数 $a$）的弱周期势展开为 $V(x) = \sum_n V_n e^{i\frac{2\pi n}{a}x}$，则在第 $n$ 布里渊区边界 $k = \pm\frac{n\pi}{a}$ 处由一级简并微扰打开的能隙大小为 ____；若具体势能为 $V(x) = -2V_0 \cos\left(\frac{2\pi x}{a}\right)$（$V_0 > 0$），则第一布里渊区边界处的能隙宽度为 ____，能量较低的驻波形式正比于 ____（填 $\cos\frac{\pi x}{a}$ 或 $\sin\frac{\pi x}{a}$），第二布里渊区边界在一级简并微扰下的能隙为 ____。

::: details 思路提示
利用欧拉公式将 $-2V_0\cos\left(\frac{2\pi x}{a}\right)$ 拆为 $-V_0 e^{i\frac{2\pi}{a}x} - V_0 e^{-i\frac{2\pi}{a}x}$ 读出各阶傅里叶分量 $V_n$；在 $x = 0$（格点）处势能 $-2V_0$ 最低。
:::

::: details 参考答案与解析
**参考答案**：$2|V_n|$；$2V_0$；$\cos\frac{\pi x}{a}$；$0$。

**解析**：将 $V(x) = -2V_0\cos\left(\frac{2\pi x}{a}\right) = -V_0 e^{i\frac{2\pi}{a}x} - V_0 e^{-i\frac{2\pi}{a}x}$ 与傅里叶级数比对得 $V_{\pm 1} = -V_0$，而 $V_{\pm 2} = 0$。故 $k = \pm\frac{\pi}{a}$ 处能隙为 $2|V_1| = 2V_0$；因 $V(x)$ 在格点 $x = na$ 处取极小值 $-2V_0$，电荷聚集于格点的驻波 $\cos\frac{\pi x}{a}$ 能量较低（$E_0 - V_0$）。因 $V_2 = 0$，第二布里渊区边界在一级简并微扰下能隙为 $0$（仅在二级微扰下出现量级 $\sim V_0^2 / E_0$ 的微弱能隙）。
:::

---

`CH05-KP2-03`（单选）在一维克朗尼格-彭尼（Kronig-Penney）周期 $\delta$ 势垒模型中，电子允许能量由特征方程 $\frac{P\sin(\alpha a)}{\alpha a} + \cos(\alpha a) = \cos(ka)$（其中 $\alpha = \sqrt{2mE}/\hbar$，$P > 0$ 为势垒强度无量纲参量）决定。下列分析**错误**的是（ ）。
A. 当势垒强度 $P \to 0$ 时，方程退化为 $\alpha = \pm k$，还原自由电子抛物线能谱 $E = \frac{\hbar^2 k^2}{2m}$
B. 当势垒强度 $P \to \infty$ 时，仅允许 $\sin(\alpha a) = 0$，能带收缩为一维无限深势阱的分立能级 $E_n = \frac{\hbar^2 \pi^2 n^2}{2m a^2}$
C. 随能量升高（$\alpha a$ 增大），$\frac{P\sin(\alpha a)}{\alpha a}$ 振幅衰减，因此高能区的允许能带越来越宽、禁带越来越窄
D. 对任意 $P > 0$，由于方程右端 $\cos(ka) \in [-1, 1]$，在 $ka = n\pi$ 处相邻能带必定连续相交，不存在禁带

::: details 思路提示
令方程左端记为 $F(\alpha a)$，观察在 $\alpha a = n\pi$ 附近 $F(\alpha a)$ 是否会超出 $[-1, 1]$ 范围。
:::

::: details 参考答案与解析
**参考答案**：D

**解析**：对 $P > 0$，在 $\alpha a = n\pi$ 处 $F(n\pi) = (-1)^n$，但在 $\alpha a = n\pi - \epsilon$（略小于 $n\pi$）一侧，若 $n$ 为奇数则 $F(\alpha a) > 1$（或 $n$ 为偶数则 $F(\alpha a) < -1$），使得 $|F(\alpha a)| > 1$，没有实波矢 $k$ 的解，恰好在 $ka = n\pi$（布里渊区边界）处形成禁带！故 D 错误，A、B、C 均正确。
:::

#### 题型一：平面波微扰法求一维近自由电子能带与带边有效质量

`CH05-KP2-04` 一维晶格（晶格常数 $a$）中的电子受到弱周期势 $V(x) = -2V_0 \cos\left(\frac{2\pi x}{a}\right) - 2V_1 \cos\left(\frac{4\pi x}{a}\right)$（$V_0, V_1 > 0$）的作用：
1. 采用双平面波简并微扰法，推导第一布里渊区边界 $k = \frac{\pi}{a}$ 附近（记 $k = \frac{\pi}{a} + q$，$|q| \ll \frac{\pi}{a}$）上下两条能带的色散关系 $E_\pm(q)$；
2. 求出 $k = \frac{\pi}{a}$ 处的能隙宽度 $\Delta E_1$、上下能带边缘对应的驻波波函数，并推导第二能带底与第一能带顶的电子有效质量 $m_\pm^*$；
3. 若取 $a = 4.00\ \text{Å}$、$V_0 = 0.50\ \mathrm{eV}$，计算自由电子在 $k = \frac{\pi}{a}$ 处的未微扰动能 $E_0(\pi/a)$、能隙宽度 $\Delta E_1$ 以及上下能带边缘的有效质量比 $m_+^*/m_0$ 与 $m_-^*/m_0$。

::: details 思路提示
写出耦合平面波 $|k\rangle$ 与 $|k - G_1\rangle$（$G_1 = \frac{2\pi}{a}$）的 $2\times 2$ 久期方程，解出 $E_\pm(q)$ 后对小量 $q$ 做泰勒展开至 $q^2$ 项，与 $E_{\text{edge}} + \frac{\hbar^2 q^2}{2m^*}$ 对比即可直接读出有效质量。
:::

::: details 参考答案与解析
**参考答案**：
1. $E_\pm(q) = E_0 + \frac{\hbar^2 q^2}{2m_0} \pm \sqrt{V_0^2 + 4 E_0 \frac{\hbar^2 q^2}{2m_0}}$，其中 $E_0 = \frac{\hbar^2 \pi^2}{2m_0 a^2}$；
2. $\Delta E_1 = 2V_0$；下边缘驻波 $\psi_- \propto \cos\frac{\pi x}{a}$，上边缘驻波 $\psi_+ \propto \sin\frac{\pi x}{a}$；$m_\pm^* = \frac{m_0}{1 \pm 2E_0/V_0}$；
3. $E_0(\pi/a) \approx 2.35\ \mathrm{eV}$，$\Delta E_1 = 1.00\ \mathrm{eV}$，$m_+^*/m_0 \approx 0.0961$，$m_-^*/m_0 \approx -0.119$。

**解析**：
1. **双平面波简并微扰**：势能展开得 $V_{\pm 1} = -V_0$、$V_{\pm 2} = -V_1$。在 $k = \frac{\pi}{a} + q$ 附近，平面波 $|k\rangle$ 与 $|k - G_1\rangle$（$G_1 = \frac{2\pi}{a}$，故 $k - G_1 = -\frac{\pi}{a} + q$）近简并，未微扰动能为：
   $$E_1^0 = \frac{\hbar^2}{2m_0}\left(\frac{\pi}{a} + q\right)^2 = E_0 + \frac{\hbar^2\pi}{m_0 a}q + \frac{\hbar^2 q^2}{2m_0}, \qquad E_2^0 = \frac{\hbar^2}{2m_0}\left(-\frac{\pi}{a} + q\right)^2 = E_0 - \frac{\hbar^2\pi}{m_0 a}q + \frac{\hbar^2 q^2}{2m_0}$$
   矩阵元 $\langle k | V | k - G_1 \rangle = V_1 = -V_0$，久期方程：
   $$\begin{vmatrix} E_1^0 - E & -V_0 \\ -V_0 & E_2^0 - E \end{vmatrix} = 0$$
   解得：
   $$E_\pm(q) = \frac{E_1^0 + E_2^0}{2} \pm \sqrt{\left(\frac{E_1^0 - E_2^0}{2}\right)^2 + V_0^2} = E_0 + \frac{\hbar^2 q^2}{2m_0} \pm \sqrt{V_0^2 + \left(\frac{\hbar^2 \pi}{m_0 a}q\right)^2}$$
   注意到 $\left(\frac{\hbar^2 \pi}{m_0 a}q\right)^2 = 4 E_0 \cdot \frac{\hbar^2 q^2}{2m_0}$，即得所求色散关系。

2. **能隙、驻波与有效质量**：令 $q = 0$ 得 $E_\pm(0) = E_0 \pm V_0$，能隙 $\Delta E_1 = 2V_0$。代回特征方程 $(-V_0)C_2 = (E - E_0)C_1$：
   - 下边缘 $E_- = E_0 - V_0$：$C_1 = C_2 \implies \psi_- \propto e^{i\pi x/a} + e^{-i\pi x/a} \propto \cos\frac{\pi x}{a}$；
   - 上边缘 $E_+ = E_0 + V_0$：$C_1 = -C_2 \implies \psi_+ \propto e^{i\pi x/a} - e^{-i\pi x/a} \propto \sin\frac{\pi x}{a}$。

   对 $|q| \ll \frac{\pi}{a}$ 做二阶展开 $\sqrt{V_0^2 + 4E_0 \frac{\hbar^2 q^2}{2m_0}} \approx V_0 + \frac{2E_0}{V_0}\frac{\hbar^2 q^2}{2m_0}$：
   $$E_\pm(q) \approx (E_0 \pm V_0) + \frac{\hbar^2 q^2}{2m_0}\left(1 \pm \frac{2E_0}{V_0}\right)$$
   与 $\frac{\hbar^2 q^2}{2m_\pm^*}$ 比较即得带边有效质量：
   $$\frac{m_0}{m_\pm^*} = 1 \pm \frac{2E_0}{V_0} \implies m_\pm^* = \frac{m_0}{1 \pm 2E_0/V_0}$$
   可见窄禁带（$V_0 \ll E_0$）会使带边电子有效质量远小于自由电子质量 $m_0$，且第一带顶处 $m_-^* < 0$。

3. **数值计算**（$a = 4.00\ \text{Å}$，$V_0 = 0.50\ \mathrm{eV}$）：
   $$E_0\left(\frac{\pi}{a}\right) = \frac{(1.055 \times 10^{-34})^2 \pi^2}{2 \times 9.109 \times 10^{-31} \times (4.00 \times 10^{-10})^2} \approx 3.765 \times 10^{-19}\ \mathrm{J} \approx 2.35\ \mathrm{eV}$$
   $$\Delta E_1 = 2V_0 = 1.00\ \mathrm{eV}, \qquad \frac{2E_0}{V_0} = \frac{2 \times 2.350}{0.50} = 9.40$$
   $$\frac{m_+^*}{m_0} = \frac{1}{1 + 9.40} \approx 0.0961, \qquad \frac{m_-^*}{m_0} = \frac{1}{1 - 9.40} \approx -0.119$$
:::

#### 题型二：二维正方晶格近自由电子布里渊区与能带交叠判据

`CH05-KP2-05` 考虑晶格常数为 $a$ 的二维正方晶格，每个原胞含 $2$ 个价电子：
1. 求第一布里渊区中边界中点 $X\left(\frac{\pi}{a}, 0\right)$ 与角点 $M\left(\frac{\pi}{a}, \frac{\pi}{a}\right)$ 处的自由电子未微扰动能 $E_X^0$、$E_M^0$ 及两者之比；
2. 求空晶格（自由电子）模型下费米圆半径 $k_F$，与 $\Gamma X$ 距离 $\frac{\pi}{a}$ 及 $\Gamma M$ 距离 $\frac{\sqrt{2}\pi}{a}$ 比较，说明为何弱周期势下该二价晶体呈金属性；
3. 设晶体存在弱周期势，其最邻近倒格矢 $\mathbf{G}_{10} = \left(\frac{2\pi}{a}, 0\right)$ 对应的傅里叶分量幅值为 $|V_{10}|$。在忽略角点 $M$ 处能量修正、仅考虑 $X$ 点处打开能隙 $\Delta E_X = 2|V_{10}|$ 的简化模型下，求该二价晶体转变为绝缘体所需的临界势幅 $|V_{10}|_{\min}$（用 $E_X^0$ 表示）。

::: details 思路提示
二维正方晶格第一布里渊区面积为 $\left(\frac{2\pi}{a}\right)^2$，恰好容纳每原胞 $2$ 个电子，故费米圆面积 $\pi k_F^2 = \left(\frac{2\pi}{a}\right)^2$；晶体变为绝缘体的条件是第一能带最高点（$M$ 点）低于第二能带最低点（$X$ 点上边缘），即两能带不再交叠。
:::

::: details 参考答案与解析
**参考答案**：
1. $E_X^0 = \frac{\hbar^2\pi^2}{2m_0 a^2}$，$E_M^0 = \frac{\hbar^2\pi^2}{m_0 a^2}$，$E_M^0 / E_X^0 = 2$；
2. $k_F = \frac{2}{\sqrt{\pi}}\frac{\pi}{a} \approx 1.13\frac{\pi}{a}$，满足 $\frac{\pi}{a} < k_F < \frac{\sqrt{2}\pi}{a}$，费米圆越过 $X$ 点进入第二布里渊区而 $M$ 点附近仍有空态，第一、二能带交叠呈金属性；
3. $|V_{10}|_{\min} = E_X^0 = \frac{\hbar^2\pi^2}{2m_0 a^2}$。

**解析**：
1. 自由电子动能 $E^0(\mathbf{k}) = \frac{\hbar^2(k_x^2 + k_y^2)}{2m_0}$：
   $$E_X^0 = \frac{\hbar^2}{2m_0}\left(\frac{\pi}{a}\right)^2, \qquad E_M^0 = \frac{\hbar^2}{2m_0}\left[\left(\frac{\pi}{a}\right)^2 + \left(\frac{\pi}{a}\right)^2\right] = 2 E_X^0 \implies \frac{E_M^0}{E_X^0} = 2$$

2. 每原胞 $2$ 个价电子（$n_{2\mathrm{D}} = 2/a^2$），计入自旋简并度 $2$，费米圆面积等于第一布里渊区面积：
   $$\pi k_F^2 = \left(\frac{2\pi}{a}\right)^2 \implies k_F = \frac{2\sqrt{\pi}}{a} = \frac{2}{\sqrt{\pi}}\cdot\frac{\pi}{a} \approx 1.128\frac{\pi}{a}$$
   因 $1 < 1.128 < \sqrt{2} \approx 1.414$，费米圆已穿过 $X$ 点溢出至第二布里渊区，但在 $M$ 点附近尚未填满第一布里渊区。因此在弱周期势下，第一能带未全满（$M$ 处为空穴口袋）且第二能带已部分填充（$X$ 外侧为电子口袋），体系表现为导体。

3. 在 $X$ 点处，双平面波微扰使第一能带降至 $E_X^0 - |V_{10}|$，第二能带底升至 $E_X^+ = E_X^0 + |V_{10}|$。按题目简化模型，第一能带顶位于 $M$ 点且能量为 $E_M^0 = 2E_X^0$。要使第一能带全满、第二能带全空（金属-绝缘体转变），须要求第二能带底高于第一能带顶：
   $$E_X^+ > E_M^0 \implies E_X^0 + |V_{10}| > 2 E_X^0 \implies |V_{10}| > E_X^0 = \frac{\hbar^2\pi^2}{2m_0 a^2}$$
   （注：若进一步在 $M$ 点计入四个简并平面波 $\left(\pm\frac{\pi}{a}, \pm\frac{\pi}{a}\right)$ 由 $V_{10} = V_{01}$ 引起的 $4\times 4$ 简并耦合，第一带顶降至 $E_M^0 - 2|V_{10}|$，则临界条件变为 $E_X^0 + |V_{10}| > 2E_X^0 - 2|V_{10}| \implies |V_{10}| > \frac{1}{3}E_X^0$。）
:::

---

### 知识点 3：紧束缚近似与等能面

#### 概念选择与填空

`CH05-KP3-01`（单选）关于能带理论中的紧束缚近似（LCAO 方法），下列说法**错误**的是（ ）。
A. 紧束缚近似以孤立原子轨道波函数的布洛赫和作为零级波函数，适用于相邻原子波函数交叠较小的窄能带体系
B. 原子间距越小，近邻交叠积分 $J$ 的绝对值越大，由原子能级展宽形成的能带宽度就越宽
C. 在紧束缚近似下，对于非简并原子 $s$ 态，晶格中相邻原子的轨道交叠可使能带宽度达到数电子伏特
D. 紧束缚能带的能量中心严格等于孤立原子的对应能级 $E_0$，不会发生整体平移

::: details 思路提示
检查紧束缚能带表达式 $E(\mathbf{k}) = E_0 - \alpha - J\sum_{\boldsymbol{\delta}} e^{i\mathbf{k}\cdot\boldsymbol{\delta}}$ 中晶体场积分 $\alpha$ 的物理意义。
:::

::: details 参考答案与解析
**参考答案**：D

**解析**：晶体中某格点上的电子除了受本原子势场作用外，还受到周围其他离子实吸引势 $\Delta U(\mathbf{r})$ 的平均作用，给出晶体场库仑积分 $-\alpha = \int |\phi(\mathbf{r})|^2 \Delta U(\mathbf{r})\,\mathrm{d}^3 r$（一般 $\alpha > 0$），导致能带中心由孤立原子能级 $E_0$ 整体平移至 $E_0 - \alpha$。A、B、C 均正确。
:::

---

`CH05-KP3-02`（填空）晶格常数为 $a$ 的简单立方（sc）晶体，其 $s$ 态紧束缚能带色散为 $E(\mathbf{k}) = E_0 - \alpha - 2J(\cos k_x a + \cos k_y a + \cos k_z a)$（$J > 0$）。该能带的带底能量为 ____（位于 $\mathbf{k} =$ ____），带顶能量为 ____（位于 $\mathbf{k} =$ ____），能带总宽度为 ____，带底附近的电子有效质量 $m^* =$ ____。

::: details 思路提示
余弦函数取值范围为 $[-1, 1]$；在 $\mathbf{k} \to 0$ 处用 $\cos(k_i a) \approx 1 - \frac{1}{2}k_i^2 a^2$ 展开并与 $\frac{\hbar^2 k^2}{2m^*}$ 对比。
:::

::: details 参考答案与解析
**参考答案**：$E_0 - \alpha - 6J$；$(0, 0, 0)$；$E_0 - \alpha + 6J$；$\left(\pm\frac{\pi}{a}, \pm\frac{\pi}{a}, \pm\frac{\pi}{a}\right)$；$12J$；$\frac{\hbar^2}{2Ja^2}$。

**解析**：当 $\cos k_x a = \cos k_y a = \cos k_z a = 1$（即 $\Gamma$ 点 $(0,0,0)$）时取极小值 $E_{\min} = E_0 - \alpha - 6J$；当三者均为 $-1$（即角点 $R(\pm\frac{\pi}{a}, \pm\frac{\pi}{a}, \pm\frac{\pi}{a})$）时取极大值 $E_{\max} = E_0 - \alpha + 6J$，带宽 $W = 12J$。在 $\mathbf{k} \to 0$ 附近展开：
$$E(\mathbf{k}) \approx E_0 - \alpha - 6J + J a^2 (k_x^2 + k_y^2 + k_z^2)$$
与 $\frac{\hbar^2 k^2}{2m^*}$ 对比得 $m^* = \frac{\hbar^2}{2Ja^2}$。
:::

---

`CH05-KP3-03`（单选）对于二维正方晶格 $s$ 态紧束缚能带 $E(k_x, k_y) = E_c - 2J(\cos k_x a + \cos k_y a)$（$J > 0$），关于第一布里渊区内等能线的几何特征，下列说法**错误**的是（ ）。
A. 在能带底 $\Gamma(0,0)$ 附近，等能线近似为以原点为中心的同心圆（电子型等能线）
B. 在能带顶 $M\left(\pm\frac{\pi}{a}, \pm\frac{\pi}{a}\right)$ 附近，等能线近似为以 $M$ 点为中心的圆弧（空穴型等能线）
C. 当能带半满（$E_F = E_c$）时，费米线满足 $|k_x| + |k_y| = \frac{\pi}{a}$，是一个顶点落在布里渊区边界中点 $X$ 处的旋转正方形
D. 凡是与布里渊区边界相交的等能线，在交点处均以锐角斜交于布里渊区边界

::: details 思路提示
等能线的法线方向就是梯度方向 $\nabla_{\mathbf{k}} E = \hbar\mathbf{v}$，检查在 $k_x = \pm\frac{\pi}{a}$ 边界上速度分量 $v_x$ 等于多少。
:::

::: details 参考答案与解析
**参考答案**：D

**解析**：在第一布里渊区边界 $k_x = \pm\frac{\pi}{a}$ 处，垂直于边界的群速度分量 $v_x = \frac{1}{\hbar}\frac{\partial E}{\partial k_x} = \frac{2Ja}{\hbar}\sin(k_x a) = 0$，即等能线法线平行于边界、等能线切线**垂直于布里渊区边界**（正交，在半满奇异鞍点 $X$ 处除外）。A、B、C 均正确。
:::

#### 题型一：三维立方晶格（bcc/fcc）紧束缚色散、带宽与有效质量推导

`CH05-KP3-04` 在仅计最近邻交叠积分 $J > 0$ 的 $s$ 轨道紧束缚近似下，能带色散由 $E(\mathbf{k}) = E_0 - \alpha - J\sum_{\boldsymbol{\delta}} e^{i\mathbf{k}\cdot\boldsymbol{\delta}}$ 给出（$\boldsymbol{\delta}$ 遍及所有最近邻格矢）：
1. 分别写出体心立方（bcc，晶格常数 $a$）与面心立方（fcc，晶格常数 $a$）的最近邻格矢集合 $\boldsymbol{\delta}$，并推导两者的紧束缚色散关系 $E(\mathbf{k})$；
2. 分别求出 bcc 与 fcc 能带的极小值 $E_{\min}$、极大值 $E_{\max}$ 和能带宽度 $W$（特别说明为何 fcc 的能带宽度不是 $24J$）；
3. 将 bcc 与 fcc 的色散关系在 $\Gamma(0,0,0)$ 附近展开至 $k^2$ 项，分别求出两者的带底电子有效质量 $m^*$。

::: details 思路提示
bcc 有 $8$ 个最近邻 $\left(\pm\frac{a}{2}, \pm\frac{a}{2}, \pm\frac{a}{2}\right)$，利用 $\sum_{\pm} e^{i(\pm u \pm v \pm w)} = 8\cos u\cos v\cos w$；fcc 有 $12$ 个最近邻（三个坐标平面各 $4$ 个），如 $\left(\pm\frac{a}{2}, \pm\frac{a}{2}, 0\right)$；求 fcc 极值时将 $c_i = \cos\frac{k_i a}{2} \in [-1, 1]$ 代入 $c_1 c_2 + c_2 c_3 + c_3 c_1$ 考察多线性极值。
:::

::: details 参考答案与解析
**参考答案**：
1. bcc：$E(\mathbf{k}) = E_0 - \alpha - 8J\cos\frac{k_x a}{2}\cos\frac{k_y a}{2}\cos\frac{k_z a}{2}$；fcc：$E(\mathbf{k}) = E_0 - \alpha - 4J\left(\cos\frac{k_x a}{2}\cos\frac{k_y a}{2} + \cos\frac{k_y a}{2}\cos\frac{k_z a}{2} + \cos\frac{k_z a}{2}\cos\frac{k_x a}{2}\right)$；
2. bcc：$E_{\min} = E_0 - \alpha - 8J$，$E_{\max} = E_0 - \alpha + 8J$，$W_{\text{bcc}} = 16J$；fcc：$E_{\min} = E_0 - \alpha - 12J$，$E_{\max} = E_0 - \alpha + 4J$，$W_{\text{fcc}} = 16J$；
3. 两者在 $\Gamma$ 点处的带底有效质量均为 $m^* = \frac{\hbar^2}{2Ja^2}$。

**解析**：
1. **色散关系推导**：
   - **bcc**：$8$ 个最近邻位矢为 $\boldsymbol{\delta} = \frac{a}{2}(\pm 1, \pm 1, \pm 1)$。求和可因式分解为：
     $$\sum_{\boldsymbol{\delta}} e^{i\mathbf{k}\cdot\boldsymbol{\delta}} = \left(e^{ik_x a/2} + e^{-ik_x a/2}\right)\left(e^{ik_y a/2} + e^{-ik_y a/2}\right)\left(e^{ik_z a/2} + e^{-ik_z a/2}\right) = 8\cos\frac{k_x a}{2}\cos\frac{k_y a}{2}\cos\frac{k_z a}{2}$$
     故 $E_{\text{bcc}}(\mathbf{k}) = E_0 - \alpha - 8J\cos\frac{k_x a}{2}\cos\frac{k_y a}{2}\cos\frac{k_z a}{2}$。
   - **fcc**：$12$ 个最近邻位矢为 $\frac{a}{2}(\pm 1, \pm 1, 0)$、$\frac{a}{2}(0, \pm 1, \pm 1)$、$\frac{a}{2}(\pm 1, 0, \pm 1)$。对 $xy$ 平面 $4$ 个位矢求和得 $\left(e^{ik_x a/2}+e^{-ik_x a/2}\right)\left(e^{ik_y a/2}+e^{-ik_y a/2}\right) = 4\cos\frac{k_x a}{2}\cos\frac{k_y a}{2}$，同理加另两平面得：
     $$E_{\text{fcc}}(\mathbf{k}) = E_0 - \alpha - 4J\!\left(\cos\frac{k_x a}{2}\cos\frac{k_y a}{2} + \cos\frac{k_y a}{2}\cos\frac{k_z a}{2} + \cos\frac{k_z a}{2}\cos\frac{k_x a}{2}\right)$$

2. **能带极值与宽度**：记 $c_i = \cos\frac{k_i a}{2} \in [-1, 1]$（$i = 1, 2, 3$）。
   - **bcc**：乘积 $c_1 c_2 c_3 \in [-1, 1]$（如 $\Gamma(0,0,0)$ 取 $+1$，$H(\frac{2\pi}{a},0,0)$ 取 $-1$），故 $E_{\min} = E_0 - \alpha - 8J$，$E_{\max} = E_0 - \alpha + 8J$，带宽 $W_{\text{bcc}} = 16J$。
   - **fcc**：记 $F(c_1, c_2, c_3) = c_1 c_2 + c_2 c_3 + c_3 c_1$。因 $F$ 对每个 $c_i$ 均为线性函数，其全局极值必取在立方体 $[-1, 1]^3$ 的顶点 $c_i = \pm 1$ 上：
     - 三者同号（如 $(1,1,1)$，对应 $\Gamma$ 点）：$F_{\max} = +3 \implies E_{\min} = E_0 - \alpha - 12J$；
     - 两个同号、一个异号（如 $(-1, 1, 1)$，对应 $X(\frac{2\pi}{a}, 0, 0)$ 点，或 $W(\frac{2\pi}{a}, \frac{\pi}{a}, 0)$ 处 $c=(-1,0,1)$）：$F_{\min} = -1 \implies E_{\max} = E_0 - \alpha + 4J$。
     由于三个两两乘积**不可能同时为 $-1$**（几何阻挫），$F$ 的下界为 $-1$ 而非 $-3$，因此 fcc 的精确带宽是 $W_{\text{fcc}} = (E_0 - \alpha + 4J) - (E_0 - \alpha - 12J) = 16J$，而非 $24J$。

3. **$\Gamma$ 点带底有效质量**：令 $u_i = \frac{k_i a}{2} \ll 1$，使用 $\cos u_i \approx 1 - \frac{1}{2}u_i^2$：
   - **bcc**：$c_1 c_2 c_3 \approx 1 - \frac{1}{2}(u_1^2 + u_2^2 + u_3^2) = 1 - \frac{a^2 k^2}{8}$，故：
     $$E_{\text{bcc}}(\mathbf{k}) \approx E_0 - \alpha - 8J + J a^2 k^2 \implies m_{\text{bcc}}^* = \frac{\hbar^2}{2Ja^2}$$
   - **fcc**：$c_1 c_2 \approx 1 - \frac{1}{2}(u_1^2 + u_2^2)$，三项相加得 $F \approx 3 - (u_1^2 + u_2^2 + u_3^2) = 3 - \frac{a^2 k^2}{4}$，故：
     $$E_{\text{fcc}}(\mathbf{k}) \approx E_0 - \alpha - 12J + J a^2 k^2 \implies m_{\text{fcc}}^* = \frac{\hbar^2}{2Ja^2}$$
   （值得注意：sc、bcc、fcc 在相同晶格常数 $a$ 与交叠积分 $J$ 下，带底有效质量表达式完全相同，均为 $\frac{\hbar^2}{2Ja^2}$！）
:::

#### 题型二：二维紧束缚等能面鞍点分析与轨道杂化

`CH05-KP3-05` 考虑晶格常数为 $a$ 的二维正方晶格 $s$ 态紧束缚能带 $E(k_x, k_y) = E_c - 2J(\cos k_x a + \cos k_y a)$（$J > 0$）：
1. 求电子群速度分量 $(v_x, v_y)$，证明在布里渊区边界 $k_x = \pm\frac{\pi}{a}$ 处等能线与边界正交；
2. 写出能带半满（每原胞 $1$ 个电子）时的费米能 $E_F$ 与费米线方程，并求布里渊区边界中点 $X\left(\frac{\pi}{a}, 0\right)$ 处的有效质量张量主值 $(m_{xx}^*, m_{yy}^*)$，说明该点的能带鞍点特征；
3. 结合碳/硅的 $sp^3$ 轨道杂化图像，简述四面体共价晶体中如何由杂化轨道分裂形成满价带与空导带。

::: details 思路提示
利用 $v_i = \frac{1}{\hbar}\frac{\partial E}{\partial k_i}$ 及 $\left(\frac{1}{m^*}\right)_{ij} = \frac{1}{\hbar^2}\frac{\partial^2 E}{\partial k_i \partial k_j}$；半满时由能带粒子-空穴对称性 $E\left(\frac{\pi}{a}-k_x, \frac{\pi}{a}-k_y\right) - E_c = -[E(k_x, k_y) - E_c]$ 立知 $E_F = E_c$。
:::

::: details 参考答案与解析
**参考答案**：
1. $v_x = \frac{2Ja}{\hbar}\sin(k_x a)$，$v_y = \frac{2Ja}{\hbar}\sin(k_y a)$；在 $k_x = \pm\frac{\pi}{a}$ 处 $v_x = 0$，梯度平行于边界，故等能线正交于边界；
2. $E_F = E_c$，费米线方程 $|k_x| + |k_y| = \frac{\pi}{a}$；$X$ 点处 $m_{xx}^* = -\frac{\hbar^2}{2Ja^2} < 0$，$m_{yy}^* = +\frac{\hbar^2}{2Ja^2} > 0$（双曲鞍点，对应二维对数发散范霍夫奇点）；
3. 见解析。

**解析**：
1. 群速度分量为：
   $$v_x = \frac{1}{\hbar}\frac{\partial E}{\partial k_x} = \frac{2Ja}{\hbar}\sin(k_x a), \qquad v_y = \frac{1}{\hbar}\frac{\partial E}{\partial k_y} = \frac{2Ja}{\hbar}\sin(k_y a)$$
   在布里渊区边界 $k_x = \pm\frac{\pi}{a}$ 上，$\sin(\pm\pi) = 0 \implies v_x = 0$。由于 $\nabla_{\mathbf{k}} E = \hbar\mathbf{v}$ 垂直于等能线且此处平行于 $k_y$ 轴（边界切向），故等能线必然垂直交于布里渊区边界。

2. 能带关于 $E = E_c$ 严格上下对称（平移 $\mathbf{Q} = (\frac{\pi}{a}, \frac{\pi}{a})$ 使 $\cos$ 反号），因此半满（每原胞 $1$ 个电子，占第一布里渊区一半面积）时费米能必为 $E_F = E_c$。费米线方程为：
   $$\cos(k_x a) + \cos(k_y a) = 0 \implies 2\cos\frac{(k_x + k_y)a}{2}\cos\frac{(k_x - k_y)a}{2} = 0$$
   在第一布里渊区内对应四条直线 $|k_x| + |k_y| = \frac{\pi}{a}$（顶点位于 $(\pm\frac{\pi}{a}, 0)$ 与 $(0, \pm\frac{\pi}{a})$ 的正方形）。

   计算二阶偏导得对角有效质量张量（混合偏导为零）：
   $$\frac{1}{m_{xx}^*} = \frac{2Ja^2}{\hbar^2}\cos(k_x a), \qquad \frac{1}{m_{yy}^*} = \frac{2Ja^2}{\hbar^2}\cos(k_y a)$$
   在 $X\left(\frac{\pi}{a}, 0\right)$ 处，$\cos\pi = -1$、$\cos 0 = +1$，故：
   $$m_{xx}^* = -\frac{\hbar^2}{2Ja^2} < 0, \qquad m_{yy}^* = +\frac{\hbar^2}{2Ja^2} > 0$$
   两主曲率异号且此处群速度 $\mathbf{v} = 0$，表明 $X$ 点是能带的**双曲鞍点**（导致二维态密度在 $E = E_c$ 处出现对数发散的范霍夫奇点）。

3. **共价晶体轨道杂化与带隙成因**：对金刚石或硅，每个原胞含 $2$ 个四价原子（共 $8$ 个价电子）。孤立原子的 $1$ 个 $s$ 轨道与 $3$ 个 $p$ 轨道先在原位线性组合为 $4$ 个指向正四面体顶点的 $sp^3$ 杂化轨道；相邻原子相向的杂化轨道强烈交叠，分裂为能量较低的**成键态**（每原胞 $4$ 个，计自旋可容纳 $8$ 个电子）与能量较高的**反键态**（每原胞 $4$ 个）。当原子组成晶体，成键态展宽为完全填满的**价带**，反键态展宽为完全空置的**导带**，只要成键-反键分裂大于能带展宽，两者之间即形成禁带 $E_g$（金刚石为绝缘体，硅、锗为半导体）。
:::

---

### 知识点 4：准经典运动、有效质量与空穴

![一维紧束缚色散、群速度、倒有效质量及固体导电类型判别](/figures/ch05-tight-binding-effective-mass.svg)

<p class="fig-caption">图 5-2 一维紧束缚能带色散、群速度与倒有效质量关系（左）及固体能带填充分类（右）</p>

#### 概念选择与填空

`CH05-KP4-01`（单选）关于晶体中电子准经典运动及有效质量概念，下列说法**错误**的是（ ）。
A. 在弱缓变外场下，电子波矢随时间的变化率满足 $\hbar\frac{\mathrm{d}\mathbf{k}}{\mathrm{d}t} = \mathbf{F}_{\text{外}}$，右端仅包含外场力
B. 有效质量张量 $\left(\frac{1}{m^*}\right)_{ij} = \frac{1}{\hbar^2}\frac{\partial^2 E}{\partial k_i \partial k_j}$ 把晶格周期势对电子加速度的调制作用概括在能带曲率之中
C. 当电子处于非球形各向异性等能面时，电子加速度方向一般与外电场方向不再共线
D. 在能带顶部附近电子有效质量为负值（$m^* < 0$），这说明晶体中电子的静质量变成了负数

::: details 思路提示
辨析 $m^* < 0$ 反映的是外场力与晶格周期势内场力的合力方向问题，而不是电子固有惯性质量变号。
:::

::: details 参考答案与解析
**参考答案**：D

**解析**：电子的固有质量始终为正值 $m_0$。有效质量 $m^*$ 是把外力与加速度直接关联的等效动力学参数：在能带上半部（接近布里渊区边界），随着外力加速波矢逼近区边界，晶格布拉格反射对电子施加的反向晶格力超过外场力，导致电子实际速度减小（加速度与外力反向），表现为 $m^* < 0$。A、B、C 均正确。
:::

---

`CH05-KP4-02`（填空）一个完全被电子填满的能带在任意弱外电场下的总电流密度为 ____；若满带顶附近缺失一个状态为波矢 $\mathbf{k}_e$、能量 $E_e$、群速度 $\mathbf{v}_e$、有效质量 $m_e^* < 0$ 的电子，则剩余电子体系的动力学与电学行为可等效为一个带电量 $q_h =$ ____、波矢 $\mathbf{k}_h =$ ____、群速度 $\mathbf{v}_h =$ ____、有效质量 $m_h^* =$ ____ 的**空穴**。

::: details 思路提示
牢记空穴的“四变一不变”口诀：电量、波矢、能量（相对于带顶）、有效质量均反号，唯独**群速度保持相同**（$\mathbf{v}_h = \mathbf{v}_e$）。
:::

::: details 参考答案与解析
**参考答案**：$0$；$+e$；$-\mathbf{k}_e$；$\mathbf{v}_e$；$-m_e^*$（正值）。

**解析**：满带总波矢 $\sum \mathbf{k} = 0$、总速度 $\sum \mathbf{v}(\mathbf{k}) = 0$。缺失状态 $\mathbf{k}_e$ 的电子后，剩余电子总波矢为 $0 - \mathbf{k}_e = -\mathbf{k}_e \equiv \mathbf{k}_h$；总电流 $\mathbf{J} = (-e)\sum_{\mathbf{k}\ne\mathbf{k}_e}\mathbf{v}(\mathbf{k}) = (-e)[0 - \mathbf{v}_e] = (+e)\mathbf{v}_e$，故电荷 $q_h = +e$、速度 $\mathbf{v}_h = \mathbf{v}_e$；加速度 $\dot{\mathbf{v}}_h = \dot{\mathbf{v}}_e = \frac{-e\mathbf{E}}{m_e^*} = \frac{+e\mathbf{E}}{-m_e^*}$，故有效质量 $m_h^* = -m_e^* > 0$。
:::

---

`CH05-KP4-03`（单选）在完全无散射的一维理想晶体中，给某窄能带内的单个电子施加恒定均匀直流电场 $\mathcal{E}$，该电子在实空间中的运动规律是（ ）。
A. 沿与电场相反的方向一直做匀加速直线运动，速度无限增大
B. 先加速后趋于某一恒定漂移速度
C. 波矢匀速穿过布里渊区并周期折返，电子在实空间做周期性往复振荡（布洛赫振荡），平均直流速度为零
D. 立即停止在布里渊区边界处保持静止

::: details 思路提示
根据 $\hbar\dot{k} = -e\mathcal{E}$ 得 $k(t)$ 随时间线性变化，而能带 $E(k)$ 与群速度 $v(k)$ 均是 $k$ 的周期函数（周期 $\frac{2\pi}{a}$）。
:::

::: details 参考答案与解析
**参考答案**：C

**解析**：恒定电场使 $k(t) = k_0 - \frac{e\mathcal{E}}{\hbar}t$ 线性演化。由于 $v(k)$ 以倒格矢 $\frac{2\pi}{a}$ 为周期正负交替，电子每经历周期 $T_B = \frac{2\pi\hbar}{e\mathcal{E}a}$ 就完成一次往复振荡（布洛赫振荡），不产生净直流漂移。普通金属中因散射弛豫时间 $\tau \ll T_B$，电子在到达布里渊区边界前早已被散射，故呈现欧姆导电。
:::

#### 题型一：一维能带的群速度、有效质量极值与布洛赫振荡

`CH05-KP4-04` 设一维晶格（晶格常数 $a$）的某紧束缚能带色散为 $E(k) = E_0 - 2J\cos(ka)$（$J > 0$，$k \in [-\frac{\pi}{a}, \frac{\pi}{a}]$）：
1. 推导电子群速度 $v(k)$ 与有效质量 $m^*(k)$，指出 $v(k)$ 取极值及 $m^*(k)$ 变号（发散）的波矢位置；
2. 无散射条件下施加沿 $+x$ 方向的恒定外电场 $\mathcal{E}$（外力 $F = -e\mathcal{E}$），初态 $k(0) = 0$、$x(0) = 0$，求解 $k(t)$、$v(t)$ 和 $x(t)$，写出布洛赫振荡角频率 $\omega_B$、周期 $T_B$ 与最大空间位移范围 $\Delta x$；
3. 若 $a = 4.00\ \text{Å}$、$J = 0.50\ \mathrm{eV}$、$\mathcal{E} = 1.0 \times 10^4\ \mathrm{V/m}$，计算 $T_B$ 与 $\Delta x$，并与室温典型金属弛豫时间 $\tau \sim 10^{-14}\ \mathrm{s}$ 对比。

::: details 思路提示
直接对 $E(k)$ 求一、二阶导数；由 $\hbar\dot{k} = -e\mathcal{E}$ 积分得 $k(t) = -\frac{e\mathcal{E}}{\hbar}t$，再对 $v(t) = v(k(t))$ 积分得实空间轨迹 $x(t)$。
:::

::: details 参考答案与解析
**参考答案**：
1. $v(k) = \frac{2Ja}{\hbar}\sin(ka)$，$m^*(k) = \frac{\hbar^2}{2Ja^2 \cos(ka)}$；$k = \pm\frac{\pi}{2a}$ 处 $|v|$ 取极大值 $\frac{2Ja}{\hbar}$ 且 $m^*$ 变号发散；
2. $k(t) = -\frac{e\mathcal{E}}{\hbar}t$，$v(t) = -\frac{2Ja}{\hbar}\sin(\omega_B t)$，$x(t) = -\frac{2J}{e\mathcal{E}}[1 - \cos(\omega_B t)]$；$\omega_B = \frac{e\mathcal{E}a}{\hbar}$，$T_B = \frac{2\pi\hbar}{e\mathcal{E}a}$，$\Delta x = \frac{4J}{e\mathcal{E}} = \frac{W}{e\mathcal{E}}$；
3. $T_B \approx 1.03 \times 10^{-9}\ \mathrm{s}$（比 $\tau \sim 10^{-14}\ \mathrm{s}$ 大 $5$ 个数量级），$\Delta x = 200\ \mu\mathrm{m}$。

**解析**：
1. **群速度与有效质量**：
   $$v(k) = \frac{1}{\hbar}\frac{\mathrm{d}E}{\mathrm{d}k} = \frac{2Ja}{\hbar}\sin(ka)$$
   $$\frac{1}{m^*(k)} = \frac{1}{\hbar^2}\frac{\mathrm{d}^2 E}{\mathrm{d}k^2} = \frac{2Ja^2}{\hbar^2}\cos(ka) \implies m^*(k) = \frac{\hbar^2}{2Ja^2\cos(ka)}$$
   - 在 $k = 0$ 与 $k = \pm\frac{\pi}{a}$ 处，$v = 0$；
   - 在拐点 $k = \pm\frac{\pi}{2a}$ 处，速度达极值 $v_{\max} = \pm\frac{2Ja}{\hbar}$，同时 $\cos(ka) = 0$，$1/m^* = 0$（$m^* \to \pm\infty$），有效质量由正（$|k| < \frac{\pi}{2a}$）转为负（$|k| > \frac{\pi}{2a}$）。

2. **布洛赫振荡求解**：由 $\hbar\frac{\mathrm{d}k}{\mathrm{d}t} = -e\mathcal{E}$ 及 $k(0) = 0$ 得：
   $$k(t) = -\frac{e\mathcal{E}}{\hbar}t$$
   定义布洛赫频率 $\omega_B = \frac{e\mathcal{E}a}{\hbar}$，则 $ka = -\omega_B t$，代入群速度：
   $$v(t) = -\frac{2Ja}{\hbar}\sin(\omega_B t)$$
   对时间积分并利用 $x(0) = 0$：
   $$x(t) = \int_0^t v(t')\,\mathrm{d}t' = -\frac{2Ja}{\hbar\omega_B}[1 - \cos(\omega_B t)] = -\frac{2J}{e\mathcal{E}}[1 - \cos(\omega_B t)]$$
   振荡周期 $T_B = \frac{2\pi}{\omega_B} = \frac{2\pi\hbar}{e\mathcal{E}a}$，实空间往复总跨度（峰-峰位移）为 $\Delta x = \frac{4J}{e\mathcal{E}} = \frac{W}{e\mathcal{E}}$（恰好等于带宽 $W = 4J$ 除以静电力 $e\mathcal{E}$，能量守恒清晰可见！振幅为 $\frac{2J}{e\mathcal{E}}$）。

3. **数值计算**：
   $$\omega_B = \frac{1.602 \times 10^{-19} \times 1.0 \times 10^4 \times 4.00 \times 10^{-10}}{1.055 \times 10^{-34}} \approx 6.08 \times 10^9\ \mathrm{rad/s}$$
   $$T_B = \frac{2\pi}{\omega_B} \approx 1.03 \times 10^{-9}\ \mathrm{s} = 1.03\ \mathrm{ns}, \qquad \Delta x = \frac{4 \times 0.50\ \mathrm{eV}}{e \times 1.0 \times 10^4\ \mathrm{V/m}} = 2.00 \times 10^{-4}\ \mathrm{m} = 200\ \mu\mathrm{m}$$
   因 $T_B \approx 10^5 \tau$，常规晶格中电子远未完成一个布洛赫周期便已遭遇声子/杂质散射；只有在周期 $d \gg a$（数十纳米）的半导体超晶格低温高纯样品中才能使 $T_B \lesssim \tau$ 而直接观测到布洛赫振荡。
:::

#### 题型二：满带不导电证明与空穴动力学方程推导

`CH05-KP4-05` 
1. 利用能带对称性 $E(-\mathbf{k}) = E(\mathbf{k})$，证明满带中所有电子产生的净电流密度为零；
2. 当满带中仅缺少一个处于状态 $\mathbf{k}_e$ 的电子时，从全带剩余电子的总电流密度、总准动量及在电磁场 $(\mathbf{E}, \mathbf{B})$ 下的加速度出发，严格证明该空态等效为一个电荷 $q_h = +e$、波矢 $\mathbf{k}_h = -\mathbf{k}_e$、速度 $\mathbf{v}_h = \mathbf{v}(\mathbf{k}_e)$、有效质量 $m_h^* = -m_e^*$ 的空穴，且其准经典运动方程满足 $\hbar\frac{\mathrm{d}\mathbf{k}_h}{\mathrm{d}t} = +e(\mathbf{E} + \mathbf{v}_h \times \mathbf{B})$。

::: details 思路提示
对 $E(-\mathbf{k}) = E(\mathbf{k})$ 两边求 $\mathbf{k}$ 梯度得 $\mathbf{v}(-\mathbf{k}) = -\mathbf{v}(\mathbf{k})$；剩余电子体系的所有宏观量均等于“满带总量（恒为零）减去被移走电子的量”。
:::

::: details 参考答案与解析
**参考答案**：证明见下（空穴参数 $q_h = +e$、$\mathbf{k}_h = -\mathbf{k}_e$、$\mathbf{v}_h = \mathbf{v}(\mathbf{k}_e)$、$m_h^* = -m_e^*$）。

**解析**：
1. **满带不导电证明**：由时间反演对称性 $E(-\mathbf{k}) = E(\mathbf{k})$，两边对 $\mathbf{k}$ 求梯度：
   $$-\nabla_{-\mathbf{k}} E(-\mathbf{k}) = \nabla_{\mathbf{k}} E(\mathbf{k}) \implies \mathbf{v}(-\mathbf{k}) = -\mathbf{v}(\mathbf{k})$$
   因第一布里渊区关于原点中心对称，满带中每个 $\mathbf{k}$ 态与 $-\mathbf{k}$ 态均被成对占据，故总电流密度：
   $$\mathbf{J}_{\text{满}} = \frac{-e}{V} \sum_{\mathbf{k}\in \text{1st BZ}} 2\mathbf{v}(\mathbf{k}) = \frac{-e}{V}\sum_{\mathbf{k}} \left[\mathbf{v}(\mathbf{k}) + \mathbf{v}(-\mathbf{k})\right] = \mathbf{0}$$
   外场作用仅使满带内各电子波矢按布里渊区周期性循环置换，所有态仍被完全占据，故满带总电流恒为零。

2. **空穴参数与动力学方程推导**：设满带中仅移走一个波矢为 $\mathbf{k}_e$（带顶附近，$m_e^* < 0$）的电子。
   - **波矢**：满带总波矢 $\sum_{\mathbf{k}} \mathbf{k} = \mathbf{0}$，故剩余电子总波矢定义为空穴波矢：
     $$\mathbf{k}_h = \sum_{\mathbf{k}\ne \mathbf{k}_e} \mathbf{k} = -\mathbf{k}_e$$
   - **电流与速度**：剩余电子总电流密度为：
     $$\mathbf{J} = \frac{-e}{V}\sum_{\mathbf{k}\ne \mathbf{k}_e} \mathbf{v}(\mathbf{k}) = \frac{-e}{V}\left[\mathbf{0} - \mathbf{v}(\mathbf{k}_e)\right] = \frac{+e}{V}\mathbf{v}(\mathbf{k}_e)$$
     与单个粒子电流 $\frac{q_h}{V}\mathbf{v}_h$ 比对，得空穴电荷 $q_h = +e$、速度 $\mathbf{v}_h = \mathbf{v}(\mathbf{k}_e)$。
   - **运动方程**：外电磁场中空态 $\mathbf{k}_e$ 随其余电子一起遵循 $\hbar\frac{\mathrm{d}\mathbf{k}_e}{\mathrm{d}t} = -e[\mathbf{E} + \mathbf{v}(\mathbf{k}_e)\times\mathbf{B}]$。将 $\mathbf{k}_e = -\mathbf{k}_h$ 与 $\mathbf{v}(\mathbf{k}_e) = \mathbf{v}_h$ 代入：
     $$\hbar\frac{\mathrm{d}(-\mathbf{k}_h)}{\mathrm{d}t} = -e(\mathbf{E} + \mathbf{v}_h \times \mathbf{B}) \implies \hbar\frac{\mathrm{d}\mathbf{k}_h}{\mathrm{d}t} = +e(\mathbf{E} + \mathbf{v}_h \times \mathbf{B})$$
   - **有效质量**：对空穴速度求导（设各向同性带顶，电子有效质量 $m_e^* < 0$）：
     $$\frac{\mathrm{d}\mathbf{v}_h}{\mathrm{d}t} = \frac{\mathrm{d}\mathbf{v}(\mathbf{k}_e)}{\mathrm{d}t} = \frac{-e(\mathbf{E} + \mathbf{v}_e\times\mathbf{B})}{m_e^*} = \frac{+e(\mathbf{E} + \mathbf{v}_h\times\mathbf{B})}{-m_e^*}$$
     可见空穴有效质量 $m_h^* = -m_e^* > 0$，表现为一个质量为正、带正电 $+e$ 的经典粒子。
:::

#### 题型三：各向异性椭球能谷的态密度与电导有效质量

`CH05-KP4-06` 硅（Si）导带底在第一布里渊区 $[100]$ 等价方向上共有 $6$ 个等价的旋转椭球能谷。对沿 $k_z$ 轴的单个能谷（谷底位于 $\mathbf{k}_0$），其附近色散关系为：
$$E(\mathbf{k}) = E_c + \frac{\hbar^2}{2}\left[\frac{(k_x - k_{0x})^2 + (k_y - k_{0y})^2}{m_t^*} + \frac{(k_z - k_{0z})^2}{m_l^*}\right]$$
已知硅的横向有效质量 $m_t^* = 0.19 m_0$、纵向有效质量 $m_l^* = 0.98 m_0$。
1. 写出该能谷的有效质量张量，并判断当外电场沿 $[111]$ 方向时，电子初始加速度方向是否与电场方向共线；
2. 通过坐标伸缩变换推导单个椭球能谷的能量态密度 $g_1(E)$，由此导出单谷态密度有效质量 $m_d^* = (m_l^* m_t^{*2})^{1/3}$ 及 $6$ 个能谷合并后的总态密度有效质量 $m_{dn}^* = 6^{2/3} m_d^*$ 并计算数值；
3. 假设 $6$ 个等价能谷电子数相等且弛豫时间 $\tau$ 各向同性，推导宏观电导有效质量 $m_c^*$ 满足 $\frac{1}{m_c^*} = \frac{1}{3}\left(\frac{1}{m_l^*} + \frac{2}{m_t^*}\right)$ 并计算 $m_c^*/m_0$。

::: details 思路提示
第 2 问做无量纲（或等质量）变量代换 $k_x' = \sqrt{\frac{m_d^*}{m_t^*}}(k_x - k_{0x})$ 等将椭球化为球体，注意雅可比行列式 $\mathrm{d}k_x \mathrm{d}k_y \mathrm{d}k_z = \frac{\sqrt{m_t^{*2} m_l^*}}{(m_d^*)^{3/2}}\mathrm{d}^3 k'$；第 3 问沿 $x$ 方向施加外电场，分别写出 $2$ 个沿 $\pm x$ 轴能谷（呈现 $m_l^*$）与 $4$ 个沿 $\pm y, \pm z$ 轴能谷（呈现 $m_t^*$）的电导率再求和。
:::

::: details 参考答案与解析
**参考答案**：
1. 有效质量张量为对角阵 $\mathrm{diag}(m_t^*, m_t^*, m_l^*)$；因 $m_t^* \ne m_l^*$，沿 $[111]$ 方向施场时加速度与电场**不共线**；
2. 单谷 $m_d^* \approx 0.328 m_0$；$6$ 谷总态密度有效质量 $m_{dn}^* \approx 1.08 m_0$；
3. $m_c^* \approx 0.260 m_0$。

**解析**：
1. **有效质量张量与加速度方向**：求二阶偏导得倒有效质量张量 $\mathbf{M}^{*-1} = \mathrm{diag}\!\left(\frac{1}{m_t^*}, \frac{1}{m_t^*}, \frac{1}{m_l^*}\right)$，即有效质量张量为 $\mathrm{diag}(m_t^*, m_t^*, m_l^*)$。设外电场 $\mathbf{E} = E_0(1, 1, 1)/\sqrt{3}$，外力 $\mathbf{F} = -e\mathbf{E}$，加速度为：
   $$\mathbf{a} = \mathbf{M}^{*-1}\mathbf{F} = -\frac{eE_0}{\sqrt{3}}\left(\frac{1}{m_t^*}, \frac{1}{m_t^*}, \frac{1}{m_l^*}\right)$$
   由于 $m_t^* \ne m_l^*$，向量 $\mathbf{a}$ 与 $(1,1,1)$ 不平行，即加速度方向偏离电场方向（偏向质量更轻的横向平面）。

2. **态密度有效质量推导**：令 $\varepsilon = E - E_c$，作坐标代换 $u_x = \frac{\hbar(k_x - k_{0x})}{\sqrt{2m_t^*}}$、$u_y = \frac{\hbar(k_y - k_{0y})}{\sqrt{2m_t^*}}$、$u_z = \frac{\hbar(k_z - k_{0z})}{\sqrt{2m_l^*}}$，则等能面变为球面 $u_x^2 + u_y^2 + u_z^2 = \varepsilon$，体积元 $\mathrm{d}^3 k = \left(\frac{2}{\hbar^2}\right)^{3/2}\sqrt{m_t^{*2} m_l^*}\,\mathrm{d}^3 u$。单谷能量不超过 $E$ 的态数为：
   $$Z_1(E) = \frac{2V}{(2\pi)^3}\left(\frac{2}{\hbar^2}\right)^{3/2}(m_l^* m_t^{*2})^{1/2}\cdot \frac{4}{3}\pi \varepsilon^{3/2} = \frac{V}{3\pi^2}\left(\frac{2 m_d^*}{\hbar^2}\right)^{3/2}(E - E_c)^{3/2}$$
   其中单谷态密度有效质量 $m_d^* = (m_l^* m_t^{*2})^{1/3}$。求导得单谷态密度 $g_1(E) = \frac{V}{2\pi^2}\left(\frac{2m_d^*}{\hbar^2}\right)^{3/2}(E - E_c)^{1/2}$。计入 $6$ 个等价能谷，总态密度 $g(E) = 6 g_1(E)$，写入统一有效质量 $m_{dn}^*$ 形式要求 $(m_{dn}^*)^{3/2} = 6(m_d^*)^{3/2} \implies m_{dn}^* = 6^{2/3} m_d^*$。代入硅数值：
   $$m_d^* = (0.98 \times 0.19^2)^{1/3} m_0 = (0.03538)^{1/3} m_0 \approx 0.328 m_0$$
   $$m_{dn}^* = 6^{2/3} \times 0.3283 m_0 \approx 3.302 \times 0.3283 m_0 \approx 1.08 m_0$$

3. **电导有效质量推导**：设总电子浓度为 $n$，每个等价能谷分得 $n/6$。沿 $x$ 轴施加外电场：
   - 沿 $\pm k_x$ 轴的 $2$ 个能谷，电子沿 $x$ 方向的惯性质量为 $m_l^*$，贡献电导率 $\sigma_l = 2 \cdot \frac{(n/6)e^2\tau}{m_l^*}$；
   - 沿 $\pm k_y, \pm k_z$ 轴的 $4$ 个能谷，电子沿 $x$ 方向的惯性质量为 $m_t^*$，贡献电导率 $\sigma_t = 4 \cdot \frac{(n/6)e^2\tau}{m_t^*}$。
   总电导率为：
   $$\sigma = \sigma_l + \sigma_t = n e^2 \tau \cdot \frac{1}{3}\left(\frac{1}{m_l^*} + \frac{2}{m_t^*}\right) \equiv \frac{n e^2 \tau}{m_c^*}$$
   故：
   $$\frac{1}{m_c^*} = \frac{1}{3}\left(\frac{1}{m_l^*} + \frac{2}{m_t^*}\right) = \frac{1}{3}\left(\frac{1}{0.98} + \frac{2}{0.19}\right)\frac{1}{m_0} \approx \frac{3.849}{m_0} \implies m_c^* \approx 0.260 m_0$$
:::

---

### 知识点 5：导体/绝缘体/半导体判别与费米面测量

#### 概念选择与填空

`CH05-KP5-01`（单选）根据单电子能带理论判别固体的导电类型，下列说法**错误**的是（ ）。
A. 每个原胞含单个一价原子（如 Na、K、Cu）的晶体，最高被占能带必为半满带，表现为金属导体
B. 每个原胞含偶数个价电子的晶体（如二价碱土金属 Mg、Be、Ca）必然因能带恰好填满而成为绝缘体
C. 金刚石与晶体硅每个原胞均含 $2$ 个四价原子（共 $8$ 个价电子），恰好填满 $4$ 条价带，两者导电性差异源于禁带宽度 $E_g$ 大小不同
D. 某些具有未满 $d$ 带的过渡金属氧化物（如 NiO）实测为绝缘体，这源于强电子-电子关联效应（莫特绝缘体），超出了单电子近似的适用范围

::: details 思路提示
思考三维布里渊区中不同方向边界距离不同如何导致第一、二能带发生能量交叠。
:::

::: details 参考答案与解析
**参考答案**：B

**解析**：尽管二价碱土金属（Mg、Be、Ca 等）每原胞含 $2$ 个价电子（在电子总数上恰好等于单个能带的满带容量），但在三维晶格中不同方向布里渊区边界能量不等，第一能带顶高于第二能带底，导致两能带发生**能量交叠**；电子溢出至第二能带而在第一能带留下空态，两个能带均为部分填充带，因此碱土金属都是良好的金属导体。A、C、D 均正确。
:::

---

`CH05-KP5-02`（填空）在强磁场低温条件下，通过测量金属磁化率随 $1/B$ 的周期性振荡来测定费米面垂直于磁场方向的极值截面积 $S_{\text{ext}}$，该量子振荡现象称为 ____ 效应；通过微波吸收直接测定载流子回旋有效质量 $m_c^*$ 的方法称为 ____ 实验；而能够同时分辨能量与动量、直接绘出固体能带色散关系 $E(\mathbf{k})$ 的现代谱学技术是 ____（英文缩写 ____）。

::: details 思路提示
回忆费米面实验测量的两种经典磁学手段与基于光电效应的现代能带谱学技术。
:::

::: details 参考答案与解析
**参考答案**：德哈斯-范阿尔芬（dHvA）；回旋共振；角分辨光电子能谱；ARPES。

**解析**：德哈斯-范阿尔芬效应（磁化率振荡）与舒勃尼科夫-德哈斯效应（磁阻振荡）均源于朗道能级随磁场升高依次穿过费米面，其 $1/B$ 振荡周期直接反比于费米面极值截面积 $S_{\text{ext}}$；回旋共振利用 $\omega = \omega_c = \frac{eB}{m_c^*}$ 测定有效质量；角分辨光电子能谱（Angle-Resolved Photoemission Spectroscopy, ARPES）利用光电发射能量守恒与平行表面动量守恒直接成像电子能带结构。
:::

---

`CH05-KP5-03`（单选）关于角分辨光电子能谱（ARPES）探测二维层状晶体能带结构 $E(\mathbf{k}_\parallel)$ 的基本原理，下列说法正确的是（ ）。
A. 光电子飞出晶体表面进入真空时，其动量的三个分量 $(k_x, k_y, k_z)$ 均严格守恒
B. 由于晶体表面在平行于表面方向保持平移周期性，光电子平行于表面的波矢分量守恒，满足 $k_\parallel = \frac{\sqrt{2m_0 E_{\text{kin}}}}{\hbar}\sin\theta$（$\theta$ 为光电子出射极角）
C. 测得的光电子动能 $E_{\text{kin}}$ 越大，说明该电子在晶体内部的束缚能 $E_B = E_F - E$ 越大
D. ARPES 可以同时直接测得费米能级以下的已占据态以及费米能级以上远离 $k_B T$ 的全部空导带

::: details 思路提示
回忆光电效应能量守恒 $E_{\text{kin}} = h\nu - W - E_B$；检查晶体表面在哪一方向破坏了平移对称性，以及光电子发射前提条件是什么。
:::

::: details 参考答案与解析
**参考答案**：B

**解析**：
- A 错误：晶体表面破坏了垂直于表面方向（$z$ 方向）的平移对称性，存在表面势垒跃变，故垂直波矢 $k_\perp$ 不守恒，仅平行分量 $\mathbf{k}_\parallel$ 守恒（至相差表面倒格矢）。
- B 正确：真空中光电子动量大小为 $p = \sqrt{2m_0 E_{\text{kin}}}$，平行表面分量 $k_\parallel = \frac{p}{\hbar}\sin\theta = \frac{\sqrt{2m_0 E_{\text{kin}}}}{\hbar}\sin\theta$。
- C 错误：由 $E_B = h\nu - W - E_{\text{kin}}$，$E_{\text{kin}}$ 越大对应束缚能 $E_B$ 越小（越接近费米能级）。
- D 错误：普通光电子能谱只能激发晶体中原本被电子**占据**的态（$E \lesssim E_F + \text{数个 } k_B T$），探测空态需借助反光电子能谱或时间分辨泵浦-探测 ARPES。
:::

#### 题型一：德哈斯-范阿尔芬（dHvA）效应与回旋共振计算

`CH05-KP5-04` 在低温强磁场中对单价金属钾（K，费米面高度近似球形）进行费米面实验测量：
1. 写出德哈斯-范阿尔芬振荡周期 $\Delta\left(\frac{1}{B}\right)$ 与费米面极值截面积 $S_{\text{ext}}$ 之间的昂萨格关系，以及回旋共振角频率 $\omega_c$ 与回旋有效质量 $m_c^*$ 的关系；
2. 测得钾的 dHvA 振荡周期为 $\Delta\left(\frac{1}{B}\right) = 5.46 \times 10^{-5}\ \mathrm{T}^{-1}$。计算钾的费米面极值截面积 $S_{\text{ext}}$、费米波矢 $k_F$ 以及由此推算的价电子数密度 $n$；
3. 若在频率 $\nu = 24.0\ \mathrm{GHz}$ 的微波场中观测到钾的回旋共振吸收峰位于磁场 $B_c = 1.04\ \mathrm{T}$，计算其回旋有效质量比 $m_c^*/m_0$。

::: details 思路提示
由昂萨格关系 $\Delta(1/B) = \frac{2\pi e}{\hbar S_{\text{ext}}}$ 先求 $S_{\text{ext}}$；球形费米面最大截面积为 $S_{\text{ext}} = \pi k_F^2$，再利用三维自由电子气关系 $n = \frac{k_F^3}{3\pi^2}$；回旋共振满足 $2\pi\nu = \frac{eB_c}{m_c^*}$。
:::

::: details 参考答案与解析
**参考答案**：
1. $\Delta\left(\frac{1}{B}\right) = \frac{2\pi e}{\hbar S_{\text{ext}}}$，$\omega_c = \frac{eB}{m_c^*}$；
2. $S_{\text{ext}} \approx 1.75 \times 10^{20}\ \mathrm{m}^{-2}$，$k_F \approx 7.46 \times 10^9\ \mathrm{m}^{-1}$（$0.746\ \text{Å}^{-1}$），$n \approx 1.40 \times 10^{28}\ \mathrm{m}^{-3}$；
3. $m_c^*/m_0 \approx 1.21$。

**解析**：
1. 磁场下电子在 $k$ 空间轨道截面积满足昂萨格量子化条件 $S_n = \left(n + \gamma\right)\frac{2\pi e B}{\hbar}$，当连续朗道管穿过费米面极值截面 $S_{\text{ext}}$ 时，有 $\Delta\left(\frac{1}{B}\right) = \frac{2\pi e}{\hbar S_{\text{ext}}}$；回旋共振满足 $\omega_c = 2\pi\nu = \frac{eB}{m_c^*}$。

2. 由 dHvA 周期求极值截面积、费米波矢与电子数密度：
   $$S_{\text{ext}} = \frac{2\pi e}{\hbar\,\Delta(1/B)} = \frac{2\pi \times 1.602 \times 10^{-19}}{1.055 \times 10^{-34} \times 5.46 \times 10^{-5}} \approx 1.748 \times 10^{20}\ \mathrm{m}^{-2}$$
   对球形费米面，$S_{\text{ext}} = \pi k_F^2$：
   $$k_F = \sqrt{\frac{S_{\text{ext}}}{\pi}} = \sqrt{\frac{1.748 \times 10^{20}}{\pi}} \approx 7.46 \times 10^9\ \mathrm{m}^{-1} = 0.746\ \text{Å}^{-1}$$
   $$n = \frac{k_F^3}{3\pi^2} = \frac{(7.460 \times 10^9)^3}{3\pi^2} \approx 1.40 \times 10^{28}\ \mathrm{m}^{-3}$$
   （与由钾低温 bcc 晶格常数 $a \approx 5.23\ \text{Å}$ 算得的 $2/a^3 \approx 1.40 \times 10^{28}\ \mathrm{m}^{-3}$ 高度吻合。）

3. 回旋有效质量：$\omega_c = 2\pi\nu = 2\pi \times 24.0 \times 10^9 \approx 1.508 \times 10^{11}\ \mathrm{rad/s}$，故：
   $$m_c^* = \frac{eB_c}{\omega_c} = \frac{1.602 \times 10^{-19} \times 1.04}{1.508 \times 10^{11}} \approx 1.105 \times 10^{-30}\ \mathrm{kg}$$
   $$\frac{m_c^*}{m_0} = \frac{1.105 \times 10^{-30}}{9.109 \times 10^{-31}} \approx 1.21$$
   （偏离 $1.0$ 主要反映电子-声子相互作用及周期势对能带的微弱重整化。）
:::

#### 题型二：角分辨光电子能谱（ARPES）能带色散还原计算

`CH05-KP5-05` 采用氦放电灯（He I 谱线，光子能量 $h\nu = 21.22\ \mathrm{eV}$）对某二维层状晶体进行角分辨光电子能谱（ARPES）实验测量，已知谱仪分析器功函数为 $W = 4.50\ \mathrm{eV}$：
1. 写出光电子动能 $E_{\text{kin}}$ 与晶体中电子束缚能 $E_B = E_F - E$ 的关系，以及平行表面波矢 $k_\parallel$ 与出射角 $\theta$ 的关系；
2. 实验在 $\Gamma$ 点正出射（$\theta = 0^\circ$）处观测到一条抛物线形电子能带的带底，对应光电子动能 $E_{\text{kin}}(0) = 16.32\ \mathrm{eV}$；当出射极角增至 $\theta_F = 10.0^\circ$ 时，该能带恰好穿过费米能级（$E = E_F$）。求该能带底相对于费米能级的束缚能 $E_B(0)$、费米波矢 $k_F$（同时给出 $\text{Å}^{-1}$ 值）以及该能带的电子有效质量比 $m^*/m_0$。

::: details 思路提示
先求费米能级处对应的光电子动能 $E_{\text{kin}}(E_F) = h\nu - W$，进而得带底束缚能 $E_B(0) = E_{\text{kin}}(E_F) - E_{\text{kin}}(0)$；在 $\theta_F = 10.0^\circ$ 处以 $E_{\text{kin}}(E_F)$ 代入 $k_\parallel$ 公式求 $k_F$，最后利用抛物线色散 $E_B(0) = \frac{\hbar^2 k_F^2}{2m^*}$ 解出 $m^*$。
:::

::: details 参考答案与解析
**参考答案**：
1. $E_B = E_F - E = h\nu - W - E_{\text{kin}}$，$k_\parallel = \frac{\sqrt{2m_0 E_{\text{kin}}}}{\hbar}\sin\theta$；
2. $E_B(0) = 0.40\ \mathrm{eV}$，$k_F \approx 3.64 \times 10^9\ \mathrm{m}^{-1}$（$0.364\ \text{Å}^{-1}$），$m^*/m_0 \approx 1.26$。

**解析**：
1. 由光电发射能量守恒与平行表面动量守恒（忽略微小的光子动量）：
   $$E_{\text{kin}} = h\nu - W - E_B \implies E_B = h\nu - W - E_{\text{kin}}$$
   $$k_\parallel = \frac{\sqrt{2m_0 E_{\text{kin}}}}{\hbar}\sin\theta$$

2. **费米边动能与带底束缚能**：费米能级（$E_B = 0$）对应的光电子动能为：
   $$E_{\text{kin}}(E_F) = h\nu - W = 21.22 - 4.50 = 16.72\ \mathrm{eV}$$
   带底相对于费米能级的束缚能为：
   $$E_B(0) = E_{\text{kin}}(E_F) - E_{\text{kin}}(0) = 16.72 - 16.32 = 0.40\ \mathrm{eV}$$

   **费米波矢 $k_F$**：在 $\theta_F = 10.0^\circ$（$\sin 10.0^\circ \approx 0.1736$）处能带穿过费米能级，此时出射电子动能为 $E_{\text{kin}}(E_F) = 16.72\ \mathrm{eV} = 2.679 \times 10^{-18}\ \mathrm{J}$：
   $$k_F = \frac{\sqrt{2m_0 E_{\text{kin}}(E_F)}}{\hbar}\sin\theta_F = \frac{\sqrt{2 \times 9.109 \times 10^{-31} \times 2.679 \times 10^{-18}}}{1.055 \times 10^{-34}} \times 0.1736 \approx 3.64 \times 10^9\ \mathrm{m}^{-1} = 0.364\ \text{Å}^{-1}$$

   **电子有效质量 $m^*$**：对抛物线能带 $E(k_\parallel) = E(0) + \frac{\hbar^2 k_\parallel^2}{2m^*}$，在费米面处满足 $E_F - E(0) = E_B(0) = \frac{\hbar^2 k_F^2}{2m^*}$，故：
   $$m^* = \frac{\hbar^2 k_F^2}{2 E_B(0)} = \frac{(1.055 \times 10^{-34})^2 \times (3.638 \times 10^9)^2}{2 \times 0.40 \times 1.602 \times 10^{-19}} \approx 1.148 \times 10^{-30}\ \mathrm{kg}$$
   $$\frac{m^*}{m_0} = \frac{1.148 \times 10^{-30}}{9.109 \times 10^{-31}} \approx 1.26$$
:::
