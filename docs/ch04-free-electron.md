# 第四章 金属电子理论

::: info 教学大纲（建议 6 学时）
- 4.1 金属自由电子气模型与费米-狄拉克统计分布
- 4.2 电子气状态密度、费米能、费米波矢与基态平均能量
- 4.3 电子气的比热容（低温线性项与晶格热容的比较）
- 4.4 功函数、接触电势与电子热发射
- 4.5 电子气的电导、热导与维德曼-弗朗茨定律
:::

::: tip 核心概念与模型
**1. 索末菲自由电子气模型与 $k$ 空间状态密度**
- **基本假设**：忽略电子与离子实间的周期势起伏（等效为恒定背景势阱）及电子间库仑相互作用（独立电子近似），电子视为箱中自由费米子，能量色散 $E(\mathbf{k}) = \frac{\hbar^2 k^2}{2m}$。
- **周期性边界条件（玻恩-卡门条件）**：对体积 $V = L^3$ 的晶体，$k_i = \frac{2\pi}{L} n_i$（$n_i \in \mathbb{Z}$），每个 $\mathbf{k}$ 状态占据 $k$ 空间体积 $\frac{(2\pi)^3}{V}$。计入电子自旋简并度 $2$，单位 $k$ 空间体积内的状态数为 $\frac{2V}{(2\pi)^3} = \frac{V}{4\pi^3}$。

**2. 不同维度自由电子气的态密度与基态参量（$T = 0\ \mathrm{K}$）**

| 维度 | 能量态密度 $g(E) = \mathrm{d}Z/\mathrm{d}E$ | 费米波矢 $k_F$ | 费米能 $E_F$ | 基态平均能量 $\bar{E}_0$ |
| :---: | :--- | :--- | :--- | :---: |
| 3D（体积 $V$） | $\frac{V}{2\pi^2}\left(\frac{2m}{\hbar^2}\right)^{3/2} E^{1/2} = \frac{3N}{2E_F}\left(\frac{E}{E_F}\right)^{1/2}$ | $(3\pi^2 n)^{1/3}$ | $\frac{\hbar^2}{2m}(3\pi^2 n)^{2/3}$ | $\frac{3}{5}E_F$ |
| 2D（面积 $S$） | $\frac{Sm}{\pi\hbar^2}$（与能量无关的常数） | $(2\pi n_{2\mathrm{D}})^{1/2}$ | $\frac{\pi\hbar^2}{m} n_{2\mathrm{D}}$ | $\frac{1}{2}E_F$ |
| 1D（长度 $L$） | $\frac{L}{\pi}\left(\frac{2m}{\hbar^2}\right)^{1/2} E^{-1/2}$ | $\frac{\pi}{2} n_{1\mathrm{D}}$ | $\frac{\pi^2\hbar^2}{8m} n_{1\mathrm{D}}^2$ | $\frac{1}{3}E_F$ |

- 费米速率 $v_F = \frac{\hbar k_F}{m}$，费米温度 $T_F = \frac{E_F}{k_B}$。典型金属 $E_F \sim 2\text{--}12\ \mathrm{eV}$，$T_F \sim 10^4\text{--}10^5\ \mathrm{K}$，室温下 $T \ll T_F$，金属电子气处于**强简并态**。
- 三维自由电子气基态总能量 $U_0 = \frac{3}{5}NE_F$，简并压强 $P = -\left(\frac{\partial U_0}{\partial V}\right)_N = \frac{2}{5}nE_F$，电子贡献的体弹性模量 $B = -V\frac{\partial P}{\partial V} = \frac{5}{3}P = \frac{2}{3}nE_F$。

**3. 费米-狄拉克统计与电子热容**
- **分布函数**：$f(E) = \frac{1}{e^{(E - \mu)/(k_B T)} + 1}$，满足 $f(\mu) = \frac{1}{2}$ 及中心对称性 $f(\mu + \Delta E) + f(\mu - \Delta E) = 1$。
- **低温索末菲展开（$T \ll T_F$）**：
  $$\mu(T) \approx E_F\left[1 - \frac{\pi^2}{12}\left(\frac{k_B T}{E_F}\right)^2\right] \quad (\text{3D}), \qquad U(T) \approx U_0 + \frac{\pi^2}{6}g(E_F)(k_B T)^2$$
- **电子定容热容**：因泡利不相容原理，仅费米面附近 $\sim k_B T$ 薄层内约 $\frac{T}{T_F}$ 比例的电子被热激发：
  $$C_{Ve} = \frac{\pi^2}{3}g(E_F)k_B^2 T = \frac{\pi^2}{2}Nk_B\frac{T}{T_F} = \gamma T$$
- **金属低温总热容**（$T \ll \Theta_D \ll T_F$）：$C_V = \gamma T + A T^3 \implies \frac{C_V}{T} = \gamma + A T^2$，作直线图截距给出电子热容系数 $\gamma$，斜率给出晶格德拜系数 $A = \frac{12\pi^4}{5}\frac{Nk_B}{\Theta_D^3}$。

**4. 功函数、接触电势与热电子发射**
- **功函数 $W$**：绝对零度下将电子从费米能级移至金属外紧邻真空处所需的最小能量；金属势阱总深度 $V_0 = E_F + W$。因表面电子云外溢形成表面电偶极层，同一金属不同晶面的功函数不同。
- **接触电势差**：金属 A、B 接触达到热平衡时**费米能级对齐**（$E_{F,A} = E_{F,B}$），电子从功函数小的金属流向功函数大的金属，在紧邻外表面间形成接触电势差 $\varphi_A - \varphi_B = \frac{W_B - W_A}{e}$。
- **热电子发射（理查森-杜什曼公式）**：电子逸出需垂直表面动能 $\frac{\hbar^2 k_z^2}{2m} \ge E_F + W$，在 $W \gg k_B T$ 下：
  $$j = A_0 T^2 e^{-W/(k_B T)}, \qquad A_0 = \frac{4\pi e m_0 k_B^2}{h^3} \approx 1.20 \times 10^6\ \mathrm{A/(m^2\cdot K^2)}$$

**5. 电子气的电导、马西森定则与热导**
- **索末菲电导图像**：外电场 $\mathbf{E}$ 使费米球在 $k$ 空间整体平移 $\Delta\mathbf{k} = -\frac{e\tau}{\hbar}\mathbf{E}$，净电流由费米面附近高速电子（速率 $v_F$）贡献；宏观电导率形式与德鲁德模型一致：
  $$\sigma = \frac{n e^2 \tau(E_F)}{m} = n e \mu_e, \qquad l = v_F \tau$$
- **马西森定则**：声子散射与静态杂质/缺陷散射几率相加，$\rho(T) = \rho_0 + \rho_{\text{ph}}(T)$（高温 $T \gg \Theta_D$ 时 $\rho_{\text{ph}} \propto T$，极低温 $\rho_{\text{ph}} \propto T^5$；剩余电阻率 $\rho_0$ 与温度无关）。
- **电子热导率与维德曼-弗朗茨定律**：
  $$\begin{aligned} \kappa_e &= \frac{1}{3}c_{Ve} v_F^2 \tau = \frac{\pi^2 n k_B^2 T \tau}{3m} \\ \frac{\kappa_e}{\sigma T} &= L = \frac{\pi^2}{3}\left(\frac{k_B}{e}\right)^2 \approx 2.44 \times 10^{-8}\ \mathrm{W\cdot\Omega/K^2} \end{aligned}$$
  该定律在弹性散射占主导（高温 $T \gtrsim \Theta_D$ 或极低温杂质散射区）时成立良好。
:::

![1D/2D/3D 自由电子态密度与费米-狄拉克分布](/figures/ch04-fermi-dos.svg)

<p class="fig-caption">图 4-1 一维、二维、三维自由电子能量态密度及费米-狄拉克分布函数</p>

## 习题及参考解答

### 知识点 1：自由电子气、态密度与费米能（1D/2D/3D）

#### 概念选择与填空

`CH04-KP1-01`（单选）关于索末菲量子自由电子气模型与经典德鲁德模型，下列说法**错误**的是（ ）。
A. 索末菲模型同样忽略电子与离子实周期势的起伏以及电子间的相互作用，但以费米-狄拉克统计取代麦克斯韦-玻尔兹曼统计
B. 在绝对零度 $T = 0\ \mathrm{K}$ 时，索末菲模型中电子动能并不为零，电子占据直至费米能 $E_F$ 的所有量子态
C. 典型金属的费米温度 $T_F$ 远高于室温（$T \ll T_F$），因此在室温下仍可视为强简并费米气体
D. 根据泡利不相容原理，三维 $k$ 空间中每个允许的波矢 $\mathbf{k}$ 只能容纳 $1$ 个电子

::: details 思路提示
回忆电子除了轨道波矢 $\mathbf{k}$ 外还有哪一内禀自由度；核对三维 $k$ 空间的状态密度系数。
:::

::: details 参考答案与解析
**参考答案**：D

**解析**：电子自旋为 $\frac{1}{2}$，同一波矢 $\mathbf{k}$ 对应自旋向上、自旋向下两个独立量子态，故每个允许波矢 $\mathbf{k}$ 最多容纳 **$2$ 个**电子，单位 $k$ 空间体积内的量子态数为 $\frac{2V}{(2\pi)^3} = \frac{V}{4\pi^3}$。A、B、C 均为索末菲模型的核心结论。
:::

---

`CH04-KP1-02`（填空）对于自由电子气，一维、二维和三维体系的能量态密度 $g(E)$ 对能量 $E$ 的依赖关系分别为 $g_{1\mathrm{D}}(E) \propto$ ____、$g_{2\mathrm{D}}(E) \propto$ ____、$g_{3\mathrm{D}}(E) \propto$ ____；绝对零度下，三维自由电子气中单个电子的平均动能与费米能之比 $\bar{E}_0 / E_F =$ ____。

::: details 思路提示
由 $d$ 维 $k$ 空间体积 $V_k \propto k^d \propto E^{d/2}$ 对 $E$ 求导即得 $g_d(E) \propto E^{d/2 - 1}$；平均能量 $\bar{E}_0 = \frac{\int_0^{E_F} E g(E)\,\mathrm{d}E}{\int_0^{E_F} g(E)\,\mathrm{d}E}$。
:::

::: details 参考答案与解析
**参考答案**：$E^{-1/2}$；$E^0$（常数）；$E^{1/2}$；$\frac{3}{5}$。

**解析**：对 $d$ 维自由电子，$E \propto k^2$，波矢不超过 $k$ 的总态数 $Z(E) \propto k^d \propto E^{d/2}$，求导得态密度 $g_d(E) = \frac{\mathrm{d}Z}{\mathrm{d}E} \propto E^{d/2 - 1}$。分别取 $d = 1, 2, 3$ 得 $E^{-1/2}$、常数（$E^0$）和 $E^{1/2}$。绝对零度平均能量：
$$\frac{\bar{E}_0}{E_F} = \frac{\int_0^{E_F} E \cdot E^{d/2 - 1}\,\mathrm{d}E}{E_F \int_0^{E_F} E^{d/2 - 1}\,\mathrm{d}E} = \frac{d}{d + 2}$$
对三维（$d = 3$）有 $\bar{E}_0 = \frac{3}{5} E_F$（二维为 $\frac{1}{2}E_F$，一维为 $\frac{1}{3}E_F$）。
:::

---

`CH04-KP1-03`（单选）若三维自由电子气的电子数密度 $n$ 增大为原来的 $8$ 倍，则绝对零度下其费米波矢 $k_F$、费米能 $E_F$、费米速率 $v_F$ 及费米面处的单位体积态密度 $D(E_F) = g(E_F)/V$ 分别变为原来的（ ）。
A. $2$ 倍、$4$ 倍、$2$ 倍、$2$ 倍
B. $2$ 倍、$4$ 倍、$2$ 倍、$4$ 倍
C. $2$ 倍、$2$ 倍、$2$ 倍、$4$ 倍
D. $4$ 倍、$8$ 倍、$2$ 倍、$2$ 倍

::: details 思路提示
依次写出 $k_F \propto n^{1/3}$、$E_F \propto k_F^2$、$v_F \propto k_F$ 以及 $D(E_F) = \frac{3n}{2E_F}$ 对 $n$ 的幂次关系。
:::

::: details 参考答案与解析
**参考答案**：A

**解析**：三维自由电子气满足：
- $k_F = (3\pi^2 n)^{1/3} \propto n^{1/3} \implies 8^{1/3} = 2$ 倍；
- $E_F = \frac{\hbar^2 k_F^2}{2m} \propto n^{2/3} \implies 8^{2/3} = 4$ 倍；
- $v_F = \frac{\hbar k_F}{m} \propto n^{1/3} \implies 2$ 倍；
- $D(E_F) = \frac{g(E_F)}{V} = \frac{3n}{2E_F} \propto n^{1/3}$（或由 $D(E) \propto E^{1/2} \propto k_F$）$\implies 2$ 倍。

故正确选项为 A。
:::

#### 题型一：1D/2D/3D 自由电子态密度与费米能推导

`CH04-KP1-04` 考虑自由电子气（电子质量 $m$，总数 $N$）：
1. 采用玻恩-卡门周期性边界条件，分别推导二维（面积 $S$，面密度 $n_{2\mathrm{D}} = N/S$）与三维（体积 $V$，体密度 $n = N/V$）自由电子气的能量态密度 $g(E)$ 及绝对零度费米能 $E_F$；
2. 推导三维自由电子气在绝对零度下的总能量 $U_0$、简并压强 $P$ 及电子气对金属体弹性模量的贡献 $B$，证明 $P = \frac{2}{5}nE_F$ 且 $B = \frac{2}{3}nE_F$。

::: details 思路提示
状态计数时务必乘以自旋简并度 $2$；简并压强由热力学恒等式 $P = -\left(\frac{\partial U_0}{\partial V}\right)_N$ 导出，体弹性模量定义为 $B = -V\left(\frac{\partial P}{\partial V}\right)_N$。
:::

::: details 参考答案与解析
**参考答案**：
1. 二维：$g_{2\mathrm{D}}(E) = \frac{Sm}{\pi\hbar^2}$，$E_{F,2\mathrm{D}} = \frac{\pi\hbar^2}{m} n_{2\mathrm{D}}$；三维：$g_{3\mathrm{D}}(E) = \frac{V}{2\pi^2}\left(\frac{2m}{\hbar^2}\right)^{3/2}E^{1/2}$，$E_{F,3\mathrm{D}} = \frac{\hbar^2}{2m}(3\pi^2 n)^{2/3}$；
2. $U_0 = \frac{3}{5}N E_F$，$P = \frac{2}{5}nE_F$，$B = \frac{2}{3}nE_F$（证明见下）。

**解析**：
1. **二维自由电子气**：周期性边界条件给出 $k_x, k_y = \frac{2\pi}{L_x}n_x, \frac{2\pi}{L_y}n_y$，每个 $\mathbf{k}$ 态占 $k$ 空间面积 $\frac{(2\pi)^2}{S}$。计入自旋简并度 $2$，能量不超过 $E = \frac{\hbar^2 k^2}{2m}$ 的总量子态数为：
   $$Z_{2\mathrm{D}}(E) = 2 \cdot \frac{\pi k^2}{(2\pi)^2 / S} = \frac{S k^2}{2\pi} = \frac{Sm}{\pi\hbar^2} E$$
   求导得态密度（与能量无关）：
   $$g_{2\mathrm{D}}(E) = \frac{\mathrm{d}Z_{2\mathrm{D}}}{\mathrm{d}E} = \frac{Sm}{\pi\hbar^2}$$
   由绝对零度粒子数条件 $Z_{2\mathrm{D}}(E_F) = N$ 得：
   $$\frac{Sm}{\pi\hbar^2} E_{F,2\mathrm{D}} = N \implies E_{F,2\mathrm{D}} = \frac{\pi\hbar^2}{m} n_{2\mathrm{D}}$$

   **三维自由电子气**：每个 $\mathbf{k}$ 态占 $k$ 空间体积 $\frac{(2\pi)^3}{V}$，计入自旋简并度 $2$：
   $$Z_{3\mathrm{D}}(E) = 2 \cdot \frac{\frac{4}{3}\pi k^3}{(2\pi)^3 / V} = \frac{V k^3}{3\pi^2} = \frac{V}{3\pi^2}\left(\frac{2mE}{\hbar^2}\right)^{3/2}$$
   求导得能量态密度：
   $$g_{3\mathrm{D}}(E) = \frac{\mathrm{d}Z_{3\mathrm{D}}}{\mathrm{d}E} = \frac{V}{2\pi^2}\left(\frac{2m}{\hbar^2}\right)^{3/2} E^{1/2}$$
   令 $Z_{3\mathrm{D}}(E_F) = N$，得 $k_F = (3\pi^2 n)^{1/3}$，进而：
   $$E_{F,3\mathrm{D}} = \frac{\hbar^2}{2m}(3\pi^2 n)^{2/3}$$

2. **基态能量、简并压与体弹性模量**：将 $g_{3\mathrm{D}}(E) = \frac{3N}{2E_F^{3/2}}E^{1/2}$ 代入总能量积分：
   $$U_0 = \int_0^{E_F} E g_{3\mathrm{D}}(E)\,\mathrm{d}E = \frac{3N}{2E_F^{3/2}}\cdot \frac{2}{5}E_F^{5/2} = \frac{3}{5} N E_F$$
   将 $n = N/V$ 代入可见 $U_0 = \frac{3}{5} N \frac{\hbar^2}{2m}(3\pi^2 N)^{2/3} V^{-2/3} \propto V^{-2/3}$。在 $T = 0\ \mathrm{K}$ 且 $N$ 恒定时，简并压强为：
   $$P = -\left(\frac{\partial U_0}{\partial V}\right)_N = \frac{2}{3}\frac{U_0}{V} = \frac{2}{5} n E_F$$
   由于 $P \propto V^{-5/3}$，体弹性模量为：
   $$B = -V\left(\frac{\partial P}{\partial V}\right)_N = \frac{5}{3} P = \frac{2}{3} n E_F$$
:::

#### 题型二：典型金属费米参量与二维电子气计算

`CH04-KP1-05` 金属铜（Cu）为面心立方（fcc）结构，晶格常数 $a = 3.61\ \text{Å}$，每个铜原子贡献 $1$ 个传导电子。在自由电子气近似下计算：
1. 传导电子数密度 $n$；
2. 绝对零度下的费米波矢 $k_F$、费米能 $E_F$（以 $\mathrm{eV}$ 计）、费米温度 $T_F$ 和费米速率 $v_F$；
3. 自由电子气的简并压强 $P$ 及电子气对体弹性模量的贡献 $B$（以 $\mathrm{GPa}$ 计）。

::: details 思路提示
面心立方（fcc）惯用胞体积为 $a^3$，含 $4$ 个原子，故 $n = 4 / a^3$；依次代入 $k_F = (3\pi^2 n)^{1/3}$、$E_F = \frac{\hbar^2 k_F^2}{2m_0}$、$T_F = E_F/k_B$、$v_F = \hbar k_F/m_0$ 及 $P = \frac{2}{5}nE_F$、$B = \frac{2}{3}nE_F$（注意 $E_F$ 换算为焦耳再求压强）。
:::

::: details 参考答案与解析
**参考答案**：
1. $n \approx 8.50 \times 10^{28}\ \mathrm{m}^{-3}$；
2. $k_F \approx 1.36 \times 10^{10}\ \mathrm{m}^{-1}$（$1.36\ \text{Å}^{-1}$），$E_F \approx 7.05\ \mathrm{eV}$，$T_F \approx 8.18 \times 10^4\ \mathrm{K}$，$v_F \approx 1.57 \times 10^6\ \mathrm{m/s}$；
3. $P \approx 38.4\ \mathrm{GPa}$，$B \approx 64.0\ \mathrm{GPa}$。

**解析**：
1. fcc 晶胞含 $4$ 个铜原子，每原子 $1$ 个价电子：
   $$n = \frac{4}{a^3} = \frac{4}{(3.61 \times 10^{-10}\ \mathrm{m})^3} \approx 8.50 \times 10^{28}\ \mathrm{m}^{-3}$$

2. 费米参量计算：
   $$k_F = (3\pi^2 n)^{1/3} = \left(3\pi^2 \times 8.502 \times 10^{28}\right)^{1/3} \approx 1.360 \times 10^{10}\ \mathrm{m}^{-1}$$
   $$E_F = \frac{\hbar^2 k_F^2}{2m_0} = \frac{(1.055 \times 10^{-34})^2 \times (1.360 \times 10^{10})^2}{2 \times 9.109 \times 10^{-31}} \approx 1.130 \times 10^{-18}\ \mathrm{J} \approx 7.05\ \mathrm{eV}$$
   $$T_F = \frac{E_F}{k_B} = \frac{1.130 \times 10^{-18}}{1.381 \times 10^{-23}} \approx 8.18 \times 10^4\ \mathrm{K}$$
   $$v_F = \frac{\hbar k_F}{m_0} = \frac{1.055 \times 10^{-34} \times 1.360 \times 10^{10}}{9.109 \times 10^{-31}} \approx 1.57 \times 10^6\ \mathrm{m/s}$$

3. 简并压强与体弹性模量：
   $$P = \frac{2}{5} n E_F = 0.4 \times 8.502 \times 10^{28} \times 1.130 \times 10^{-18} \approx 3.84 \times 10^{10}\ \mathrm{Pa} = 38.4\ \mathrm{GPa}$$
   $$B = \frac{2}{3} n E_F = \frac{5}{3} P \approx 6.40 \times 10^{10}\ \mathrm{Pa} = 64.0\ \mathrm{GPa}$$
   （铜的实验体弹性模量约为 $137\ \mathrm{GPa}$，自由电子简并压贡献了约一半的不可压缩性，其余来自离子实 $d$ 壳层间的排斥作用。）
:::

---

`CH04-KP1-06` 
1. 金属铝（Al）为 fcc 结构（$a_{\mathrm{Al}} = 4.05\ \text{Å}$，每原子 $3$ 个价电子），金属钠（Na）为 bcc 结构（$a_{\mathrm{Na}} = 4.29\ \text{Å}$，每原子 $1$ 个价电子）。求两者的价电子密度之比 $n_{\mathrm{Al}}/n_{\mathrm{Na}}$ 及费米能之比 $E_{F,\mathrm{Al}}/E_{F,\mathrm{Na}}$；
2. 半导体异质结（如 GaAs/AlGaAs）界面可形成高质量二维电子气。已知界面电子面密度 $n_{2\mathrm{D}} = 5.0 \times 10^{15}\ \mathrm{m}^{-2}$，电子有效质量 $m^* = 0.067 m_0$，求该二维电子气的费米波矢 $k_F$ 与费米能 $E_F$（单位：$\mathrm{meV}$）。

::: details 思路提示
第 1 问注意 fcc 每惯用胞 $4$ 个原子、bcc 每惯用胞 $2$ 个原子，再乘以各自价电子数；第 2 问直接应用二维关系 $k_F = \sqrt{2\pi n_{2\mathrm{D}}}$ 与 $E_F = \frac{\pi\hbar^2}{m^*}n_{2\mathrm{D}}$。
:::

::: details 参考答案与解析
**参考答案**：
1. $n_{\mathrm{Al}}/n_{\mathrm{Na}} \approx 7.13$，$E_{F,\mathrm{Al}}/E_{F,\mathrm{Na}} \approx 3.71$；
2. $k_F \approx 1.77 \times 10^8\ \mathrm{m}^{-1}$，$E_F \approx 17.9\ \mathrm{meV}$。

**解析**：
1. 价电子密度分别为：
   $$n_{\mathrm{Al}} = \frac{4 \times 3}{(4.05 \times 10^{-10})^3} \approx 1.81 \times 10^{29}\ \mathrm{m}^{-3}, \qquad n_{\mathrm{Na}} = \frac{2 \times 1}{(4.29 \times 10^{-10})^3} \approx 2.53 \times 10^{28}\ \mathrm{m}^{-3}$$
   两者之比为：
   $$\frac{n_{\mathrm{Al}}}{n_{\mathrm{Na}}} = \frac{12}{2}\left(\frac{4.29}{4.05}\right)^3 \approx 7.13$$
   因 $E_F \propto n^{2/3}$，故：
   $$\frac{E_{F,\mathrm{Al}}}{E_{F,\mathrm{Na}}} = \left(\frac{n_{\mathrm{Al}}}{n_{\mathrm{Na}}}\right)^{2/3} = 7.131^{2/3} \approx 3.71$$
   （对应 $E_{F,\mathrm{Al}} \approx 11.7\ \mathrm{eV}$，$E_{F,\mathrm{Na}} \approx 3.15\ \mathrm{eV}$。）

2. 对二维电子气，计入自旋简并度 $2$，由 $\frac{k_F^2}{2\pi} = n_{2\mathrm{D}}$ 得：
   $$k_F = \sqrt{2\pi n_{2\mathrm{D}}} = \sqrt{2\pi \times 5.0 \times 10^{15}} \approx 1.77 \times 10^8\ \mathrm{m}^{-1}$$
   $$E_F = \frac{\hbar^2 k_F^2}{2m^*} = \frac{\pi\hbar^2 n_{2\mathrm{D}}}{m^*} = \frac{\pi (1.055 \times 10^{-34})^2 \times 5.0 \times 10^{15}}{0.067 \times 9.109 \times 10^{-31}} \approx 2.86 \times 10^{-21}\ \mathrm{J} \approx 17.9\ \mathrm{meV}$$
:::

---

### 知识点 2：费米分布与电子气热容

#### 概念选择与填空

`CH04-KP2-01`（单选）关于费米-狄拉克分布函数 $f(E) = \frac{1}{e^{(E - \mu)/(k_B T)} + 1}$，下列说法**错误**的是（ ）。
A. 无论温度多高（$T > 0$），能量 $E = \mu$ 处的电子占据几率恒为 $\frac{1}{2}$
B. 若能量 $E_1 = \mu + \Delta E$ 的电子占据几率为 $0.15$，则能量 $E_2 = \mu - \Delta E$ 处的电子占据几率为 $0.85$
C. 金属在室温下（$k_B T \ll E_F$）所有自由电子都吸收约 $\frac{3}{2}k_B T$ 的热能，因而电子热容远大于晶格热容
D. 当能量满足 $E - \mu \gg k_B T$ 时，费米-狄拉克分布退化为经典的玻尔兹曼分布 $f(E) \approx e^{-(E - \mu)/(k_B T)}$

::: details 思路提示
注意泡利不相容原理如何限制费米球深处电子的热激发。
:::

::: details 参考答案与解析
**参考答案**：C

**解析**：由于泡利不相容原理，能量远低于费米面（$E_F - E \gg k_B T$）的电子无法吸收量级为 $k_B T$ 的热能跃迁到已被占满的邻近高能态，仅有费米面附近 $\sim k_B T$ 宽度薄层内约 $\frac{T}{T_F} \sim 10^{-2}$ 比例的电子参与热激发，每个被激发电子增能约 $k_B T$，故室温下电子热容比经典值 $\frac{3}{2}Nk_B$ 小两个数量级，远小于晶格热容 $3Nk_B$。A、B、D 均正确。
:::

---

`CH04-KP2-02`（填空）常温下金属的定容热容主要由 ____ 贡献，电子热容仅约为经典理论值 $\frac{3}{2}Nk_B$ 的 ____（用 $T$ 与 $T_F$ 的量级比表示）量级；在液氦温区等极低温下（$T \ll \Theta_D \ll T_F$），金属总热容表示为 $C_V = \gamma T + A T^3$，随着温度进一步降低，____ 贡献最终超过 ____ 贡献而占主导。

::: details 思路提示
比较低温下 $T$ 的一次幂与三次幂谁衰减得更慢。
:::

::: details 参考答案与解析
**参考答案**：晶格振动（声子）；$\frac{T}{T_F}$；电子热容（$\gamma T$）；晶格热容（$A T^3$）。

**解析**：室温下（$T \gtrsim \Theta_D$）晶格热容接近杜隆-珀蒂值 $3Nk_B$，而电子热容 $C_{Ve} = \frac{\pi^2}{2}Nk_B\frac{T}{T_F} \sim 10^{-2}Nk_B$，故常温下晶格占主导。极低温下晶格热容按 $T^3$ 迅速衰减，电子热容仅按 $T$ 线性衰减，因此当 $T < T_0 = \sqrt{\gamma/A}$（通常在数开尔文以下）时电子热容占主导。
:::

---

`CH04-KP2-03`（单选）根据低温索末菲展开，粒子数 $N$ 守恒的自由电子气在低温（$T \ll T_F$）下化学势满足 $\mu(T) \approx E_F - \frac{\pi^2}{6}(k_B T)^2 \frac{g'(E_F)}{g(E_F)}$。由此可知，当温度从 $0\ \mathrm{K}$ 略有升高时，三维（3D）与一维（1D）自由电子气的化学势 $\mu(T)$ 相对于 $E_F$ 的变化趋势分别是（ ）。
A. 3D 下降，1D 下降
B. 3D 上升，1D 下降
C. 3D 下降，1D 上升
D. 3D 与 1D 均严格保持不变

::: details 思路提示
利用 $g_{3\mathrm{D}}(E) \propto E^{1/2}$ 与 $g_{1\mathrm{D}}(E) \propto E^{-1/2}$ 分别判断导数 $g'(E_F)$ 的正负号；也可从粒子数守恒的几何面积平衡直观判断。
:::

::: details 参考答案与解析
**参考答案**：C

**解析**：
- 3D 中 $g(E) \propto E^{1/2}$，故 $\frac{g'(E_F)}{g(E_F)} = \frac{1}{2E_F} > 0$，即费米面之上态密度大于之下；若 $\mu$ 不动，高能侧增加的占据数会多于低能侧空出的占据数，为维持总粒子数 $N$ 守恒，化学势 $\mu(T)$ 必须**略微下降**（$\mu(T) \approx E_F\left[1 - \frac{\pi^2}{12}\left(\frac{k_B T}{E_F}\right)^2\right]$）。
- 1D 中 $g(E) \propto E^{-1/2}$，故 $\frac{g'(E_F)}{g(E_F)} = -\frac{1}{2E_F} < 0$，高能侧态密度更小，因此 $\mu(T)$ 随温度升高反而**略微上升**。
- （注：2D 中 $g(E)$ 为常数，$g'(E_F) = 0$，展开至任意幂次 $T^n$ 系数均为零，严格解给出 $\mu(T) = k_B T \ln\left(e^{E_F/(k_B T)} - 1\right) \approx E_F - k_B T e^{-E_F/(k_B T)}$，低温下几乎不变。）
:::

#### 题型一：索末菲展开与低温电子热容推导

`CH04-KP2-04` 已知低温（$k_B T \ll \mu$）下的索末菲展开公式为：
$$\int_0^\infty H(E) f(E)\,\mathrm{d}E \approx \int_0^\mu H(E)\,\mathrm{d}E + \frac{\pi^2}{6}(k_B T)^2 H'(\mu)$$
1. 对三维自由电子气，分别令 $H(E) = g(E)$ 和 $H(E) = E g(E)$，推导低温下化学势 $\mu(T)$（保留至 $T^2$ 项）、电子内能 $U(T)$ 及定容热容 $C_{Ve}$；
2. 取金属铜的费米能 $E_F = 7.05\ \mathrm{eV}$（$T_F = 8.18 \times 10^4\ \mathrm{K}$），计算室温 $T = 300\ \mathrm{K}$ 时化学势的相对偏移 $\frac{|\mu(T) - E_F|}{E_F}$ 与摩尔电子热容 $C_{Ve,m}$，并与经典值 $\frac{3}{2}R$ 及晶格高温热容 $3R$ 比较。

::: details 思路提示
由粒子数守恒 $N = \int_0^\infty g(E) f(E)\,\mathrm{d}E = \int_0^{E_F} g(E)\,\mathrm{d}E$ 消去 $\int_0^\mu g(E)\,\mathrm{d}E$ 并用 $\int_{E_F}^\mu g(E)\,\mathrm{d}E \approx (\mu - E_F)g(E_F)$ 即可求出 $\mu(T) - E_F$；求 $U(T)$ 时同样将 $\int_0^\mu E g(E)\,\mathrm{d}E$ 拆成 $\int_0^{E_F} + \int_{E_F}^\mu$，利用刚求出的 $(\mu - E_F)g(E_F)$ 替换以消去 $g'(E_F)$ 项！
:::

::: details 参考答案与解析
**参考答案**：
1. $\mu(T) \approx E_F\left[1 - \frac{\pi^2}{12}\left(\frac{k_B T}{E_F}\right)^2\right]$，$U(T) \approx \frac{3}{5}NE_F + \frac{\pi^2}{6}g(E_F)(k_B T)^2$，$C_{Ve} = \frac{\pi^2}{3}g(E_F)k_B^2 T = \frac{\pi^2}{2}Nk_B\frac{T}{T_F}$；
2. $|\mu(300\ \mathrm{K}) - E_F|/E_F \approx 1.11 \times 10^{-5}$，$C_{Ve,m}(300\ \mathrm{K}) \approx 0.150\ \mathrm{J/(mol\cdot K)}$，仅为经典电子热容 $\frac{3}{2}R$ 的 $1.21\%$、室温晶格热容 $3R$ 的 $0.60\%$。

**解析**：
1. **化学势 $\mu(T)$**：令 $H(E) = g(E)$，由粒子数守恒：
   $$N = \int_0^{E_F} g(E)\,\mathrm{d}E \approx \int_0^\mu g(E)\,\mathrm{d}E + \frac{\pi^2}{6}(k_B T)^2 g'(\mu)$$
   将 $\int_0^\mu - \int_0^{E_F} = \int_{E_F}^\mu g(E)\,\mathrm{d}E \approx (\mu - E_F)g(E_F)$，且在 $T^2$ 阶近似下用 $g'(E_F)$ 代换 $g'(\mu)$：
   $$(\mu - E_F)g(E_F) + \frac{\pi^2}{6}(k_B T)^2 g'(E_F) = 0 \implies \mu(T) \approx E_F - \frac{\pi^2}{6}(k_B T)^2 \frac{g'(E_F)}{g(E_F)}$$
   对三维自由电子气，$g(E) \propto E^{1/2}$，故 $\frac{g'(E_F)}{g(E_F)} = \frac{1}{2E_F}$，代入得：
   $$\mu(T) \approx E_F\left[1 - \frac{\pi^2}{12}\left(\frac{k_B T}{E_F}\right)^2\right]$$

   **电子内能与定容热容**：令 $H(E) = E g(E)$，其导数 $H'(E) = g(E) + E g'(E)$：
   $$U(T) \approx \int_0^\mu E g(E)\,\mathrm{d}E + \frac{\pi^2}{6}(k_B T)^2\left[g(E_F) + E_F g'(E_F)\right]$$
   注意到 $\int_0^\mu E g(E)\,\mathrm{d}E \approx U_0 + E_F (\mu - E_F) g(E_F)$，将上式得到的 $(\mu - E_F) g(E_F) = -\frac{\pi^2}{6}(k_B T)^2 g'(E_F)$ 代入，$E_F g'(E_F)$ 项**精确抵消**！得到对任意态密度形式均成立的通用表达式：
   $$U(T) \approx U_0 + \frac{\pi^2}{6}g(E_F)(k_B T)^2$$
   对 $T$ 求导即得电子定容热容（利用三维关系 $g(E_F) = \frac{3N}{2E_F}$ 及 $E_F = k_B T_F$）：
   $$C_{Ve} = \left(\frac{\partial U}{\partial T}\right)_{V,N} = \frac{\pi^2}{3}g(E_F)k_B^2 T = \frac{\pi^2}{2}Nk_B\frac{T}{T_F}$$

2. **铜在 $300\ \mathrm{K}$ 时的数值**：$\frac{T}{T_F} = \frac{300}{8.18 \times 10^4} \approx 3.67 \times 10^{-3}$。
   $$\frac{|\mu(300\ \mathrm{K}) - E_F|}{E_F} = \frac{\pi^2}{12}\left(3.667 \times 10^{-3}\right)^2 \approx 1.11 \times 10^{-5}$$
   可见室温下化学势与 $E_F$ 几乎无差别。摩尔电子热容（$R = 8.314\ \mathrm{J/(mol\cdot K)}$）：
   $$C_{Ve,m}(300\ \mathrm{K}) = \frac{\pi^2}{2} R \frac{T}{T_F} = 4.935 \times 8.314 \times 3.667 \times 10^{-3} \approx 0.150\ \mathrm{J/(mol\cdot K)}$$
   对比经典值 $\frac{3}{2}R \approx 12.5\ \mathrm{J/(mol\cdot K)}$（占比 $1.21\%$）与晶格高温热容 $3R \approx 24.9\ \mathrm{J/(mol\cdot K)}$（占比 $0.60\%$），充分解释了经典自由电子论的热容疑难。
:::

#### 题型二：低温金属热容 $C_V/T - T^2$ 实验数据分析

`CH04-KP2-05` 实验测得 $1\ \mathrm{mol}$ 某单价金属在液氦温区附近的定容热容满足 $C_V = \gamma T + A T^3$。作 $C_V/T$ 对 $T^2$ 的线性拟合图，测得纵轴截距 $\gamma = 1.35 \times 10^{-3}\ \mathrm{J/(mol\cdot K^2)}$，直线斜率 $A = 4.64 \times 10^{-4}\ \mathrm{J/(mol\cdot K^4)}$。求：
1. 电子热容与晶格热容相等时的特征温度 $T_0$；
2. 在自由电子气近似下（有效质量取 $m_0$），该金属的费米温度 $T_F$ 与费米能 $E_F$（单位：$\mathrm{eV}$）；
3. 该金属的德拜温度 $\Theta_D$；
4. 分别计算 $T = 1.0\ \mathrm{K}$ 与 $T = 10.0\ \mathrm{K}$ 时，电子热容占总热容的百分比。

::: details 思路提示
由 $\gamma T_0 = A T_0^3$ 得 $T_0 = \sqrt{\gamma/A}$；再由 $\gamma = \frac{\pi^2 R}{2 T_F}$ 求 $T_F$ 和 $E_F = k_B T_F$，由 $A = \frac{12\pi^4 R}{5 \Theta_D^3}$ 求 $\Theta_D$。
:::

::: details 参考答案与解析
**参考答案**：
1. $T_0 \approx 1.71\ \mathrm{K}$；
2. $T_F \approx 3.04 \times 10^4\ \mathrm{K}$，$E_F \approx 2.62\ \mathrm{eV}$；
3. $\Theta_D \approx 161\ \mathrm{K}$；
4. $T = 1.0\ \mathrm{K}$ 时电子占比约 $74.4\%$；$T = 10.0\ \mathrm{K}$ 时电子占比约 $2.83\%$。

**解析**：
1. 令电子热容等于晶格热容 $\gamma T_0 = A T_0^3$：
   $$T_0 = \sqrt{\frac{\gamma}{A}} = \sqrt{\frac{1.35 \times 10^{-3}}{4.64 \times 10^{-4}}} \approx 1.71\ \mathrm{K}$$

2. 对 $1\ \mathrm{mol}$ 单价金属（电子数 $N = N_A$），$\gamma = \frac{\pi^2}{2}\frac{R}{T_F}$，其中 $R = 8.314\ \mathrm{J/(mol\cdot K)}$：
   $$T_F = \frac{\pi^2 R}{2\gamma} = \frac{\pi^2 \times 8.314}{2 \times 1.35 \times 10^{-3}} \approx 3.04 \times 10^4\ \mathrm{K}$$
   $$E_F = k_B T_F = 8.617 \times 10^{-5}\ \mathrm{eV/K} \times 3.039 \times 10^4\ \mathrm{K} \approx 2.62\ \mathrm{eV}$$

3. 低温德拜热容系数 $A = \frac{12\pi^4 R}{5 \Theta_D^3} \approx \frac{1944\ \mathrm{J/(mol\cdot K)}}{\Theta_D^3}$：
   $$\Theta_D = \left(\frac{12\pi^4 R}{5 A}\right)^{1/3} = \left(\frac{1943.7}{4.64 \times 10^{-4}}\right)^{1/3} \approx 161\ \mathrm{K}$$

4. 电子热容占比为 $\eta_e(T) = \frac{\gamma T}{\gamma T + A T^3} = \frac{1}{1 + (T/T_0)^2}$：
   - $T = 1.0\ \mathrm{K}$：$\eta_e = \frac{1.35 \times 10^{-3}}{1.35 \times 10^{-3} + 4.64 \times 10^{-4}} \approx 74.4\%$（电子主导）；
   - $T = 10.0\ \mathrm{K}$：$\eta_e = \frac{1.35 \times 10^{-2}}{1.35 \times 10^{-2} + 4.64 \times 10^{-1}} \approx 2.83\%$（晶格主导）。
:::

---

### 知识点 3：功函数、接触电势与热电子发射

![金属接触电势差与外电场下费米球平移](/figures/ch04-contact-transport.svg)

<p class="fig-caption">图 4-2 热平衡时的金属接触电势差（<em>W</em><sub>A</sub> &lt; <em>W</em><sub>B</sub>）与外电场下的费米球平移</p>

#### 概念选择与填空

`CH04-KP3-01`（单选）关于金属功函数与接触电势差，下列说法**错误**的是（ ）。
A. 同一金属单晶的不同晶面具有不同的表面电偶极层，因此功函数与晶面指数有关
B. 两种不同金属接触达到热平衡时，它们的费米能级（电化学势）必相等
C. 将两种金属首尾相连构成闭合等温回路，由于存在接触电势差，回路中将产生持续稳恒电流
D. 功函数较小的金属在接触平衡后因失去部分电子而带正电，其表面外紧邻真空处的电势高于功函数较大的金属

::: details 思路提示
检查由两块或三块不同金属组成的闭合等温回路中，沿闭合路径的接触电势差代数和，并结合热力学第二定律判断。
:::

::: details 参考答案与解析
**参考答案**：C

**解析**：在由金属 A、B（或更多种金属）构成的等温闭合回路中，两个接触点处的接触电势差大小相等、方向相反，总电动势 $\Delta\varphi_{AB} + \Delta\varphi_{BA} = \frac{W_B - W_A}{e} + \frac{W_A - W_B}{e} = 0$，不会产生持续电流（否则将违背热力学第二定律构成第二类永动机）。A、B、D 均正确。
:::

---

`CH04-KP3-02`（填空）金属 A 与金属 B 的功函数分别为 $W_A = 4.25\ \mathrm{eV}$、$W_B = 4.65\ \mathrm{eV}$。当两者接触并达到热平衡时，电子从金属 ____ 流向金属 ____，平衡后金属 ____ 的电势较高，两金属外表面紧邻真空处的接触电势差大小为 ____ $\mathrm{V}$。

::: details 思路提示
接触前真空能级相同时，功函数越小则费米能级越高，电子自发从高费米能级流向低费米能级；接触电势差 $|\Delta\varphi_{AB}| = |W_B - W_A|/e$。
:::

::: details 参考答案与解析
**参考答案**：A；B；A；$0.40$。

**解析**：由于 $W_A < W_B$，接触前 A 的费米能级高于 B，接触后电子由 A 流向 B 直至 $E_{F,A} = E_{F,B}$。金属 A 失电子带正电、电势较高，金属 B 得电子带负电、电势较低，接触电势差为：
$$\varphi_A - \varphi_B = \frac{W_B - W_A}{e} = \frac{4.65\ \mathrm{eV} - 4.25\ \mathrm{eV}}{e} = 0.40\ \mathrm{V}$$
:::

---

`CH04-KP3-03`（单选）关于金属的热电子发射现象及理查森-杜什曼公式 $j = A_0 T^2 e^{-W/(k_B T)}$，下列叙述正确的是（ ）。
A. 只要金属内部电子的总动能大于势阱深度 $E_F + W$，该电子就一定能沿垂直表面方向逸出金属
B. 若以 $\ln(j / T^2)$ 为纵坐标、$1/T$ 为横坐标作理查森图，所得直线的斜率为 $-W/k_B$
C. 热电子发射电流密度随温度升高主要按幂函数 $T^2$ 缓慢增长，指数项变化可忽略
D. 在金属表面外施加加速电子逸出的外电场 $\mathcal{E}$ 会增大有效功函数，使发射电流减小

::: details 思路提示
检查逸出条件是对垂直分量 $k_z$ 还是总波矢 $k$ 的要求，并对理查森公式两边取自然对数。
:::

::: details 参考答案与解析
**参考答案**：B

**解析**：
- A 错误：电子沿 $z$ 方向逸出表面要求**垂直表面方向的动能**满足 $\frac{\hbar^2 k_z^2}{2m} \ge E_F + W$，平行于表面的动能 $\frac{\hbar^2(k_x^2+k_y^2)}{2m}$ 无助于克服表面势垒。
- B 正确：对 $j = A_0 T^2 e^{-W/(k_B T)}$ 改写得 $\ln(j/T^2) = \ln A_0 - \frac{W}{k_B}\cdot\frac{1}{T}$，故斜率为 $-W/k_B$，这是实验测定金属功函数的标准方法。
- C 错误：因 $W \gg k_B T$，温度变化时指数因子 $e^{-W/(k_B T)}$ 的剧烈变化远比 $T^2$ 占主导。
- D 错误：外加加速电场因镜像力与外场叠加产生肖特基效应，使表面有效势垒降低 $\Delta W = \sqrt{\frac{e^3\mathcal{E}}{4\pi\varepsilon_0}}$，从而增大发射电流。
:::

#### 题型一：理查森-杜什曼公式推导与功函数测算

`CH04-KP3-04` 设金属占据 $z < 0$ 半空间，表面位于 $z = 0$，表面势阱深度 $V_0 = E_F + W$（$W$ 为功函数），忽略表面电子反射：
1. 写出电子沿 $+z$ 方向逸出金属表面的波矢条件，并在高温尾部近似 $W \gg k_B T$ 下推导热电子发射电流密度公式 $j = A_0 T^2 e^{-W/(k_B T)}$，给出理查森常数 $A_0$ 的表达式并计算其理论数值；
2. 实验测得某钨（W）丝阴极在 $T_1 = 2000\ \mathrm{K}$ 时热发射电流密度 $j_1 = 8.70\ \mathrm{A/m^2}$，在 $T_2 = 2500\ \mathrm{K}$ 时 $j_2 = 2.65 \times 10^3\ \mathrm{A/m^2}$。求该钨阴极的功函数 $W$（单位：$\mathrm{eV}$）与有效发射常数 $A_{\text{eff}}$，并简述 $A_{\text{eff}}$ 通常小于理论值 $A_0$ 的物理原因。

::: details 思路提示
电流密度积分 $j = e \int v_z f(\mathbf{k}) \frac{2\,\mathrm{d}^3 k}{(2\pi)^3}$，对 $k_x, k_y \in (-\infty, +\infty)$ 用高斯积分 $\int_{-\infty}^\infty e^{-\alpha x^2}\mathrm{d}x = \sqrt{\pi/\alpha}$，对 $k_z \ge k_{z0}$ 用变量替换 $u = \frac{\hbar^2 k_z^2}{2m_0}$。
:::

::: details 参考答案与解析
**参考答案**：
1. $A_0 = \frac{e m_0 k_B^2}{2\pi^2 \hbar^3} = \frac{4\pi e m_0 k_B^2}{h^3} \approx 1.20 \times 10^6\ \mathrm{A/(m^2\cdot K^2)}$（$120\ \mathrm{A/(cm^2\cdot K^2)}$）；
2. $W \approx 4.54\ \mathrm{eV}$，$A_{\text{eff}} \approx 6.12 \times 10^5\ \mathrm{A/(m^2\cdot K^2)}$（$61.2\ \mathrm{A/(cm^2\cdot K^2)}$）。

**解析**：
1. **理查森-杜什曼公式推导**：电子逸出条件为：
   $$\frac{\hbar^2 k_z^2}{2m_0} \ge E_F + W \quad (k_z > 0)$$
   由于能逸出的电子满足 $E - E_F \ge W \gg k_B T$，费米-狄拉克分布可近似为玻尔兹曼尾部（取 $\mu \approx E_F$）：
   $$f(\mathbf{k}) \approx \exp\!\left(-\frac{E - E_F}{k_B T}\right) = \exp\!\left(\frac{E_F}{k_B T}\right) \exp\!\left(-\frac{\hbar^2 (k_x^2 + k_y^2 + k_z^2)}{2m_0 k_B T}\right)$$
   单位时间穿过单位表面积的发射电流密度（计入自旋简并度 $2$，速率 $v_z = \frac{\hbar k_z}{m_0}$）：
   $$j = e \cdot \frac{2}{(2\pi)^3} \int_{-\infty}^{\infty} \mathrm{d}k_x \int_{-\infty}^{\infty} \mathrm{d}k_y \int_{k_{z0}}^{\infty} \frac{\hbar k_z}{m_0} f(\mathbf{k})\,\mathrm{d}k_z$$
   其中 $\frac{\hbar^2 k_{z0}^2}{2m_0} = E_F + W$。横向高斯积分给出：
   $$\int_{-\infty}^{\infty} \exp\!\left(-\frac{\hbar^2 k_x^2}{2m_0 k_B T}\right)\mathrm{d}k_x = \sqrt{\frac{2\pi m_0 k_B T}{\hbar^2}}$$
   $k_x, k_y$ 两维积分之积为 $\frac{2\pi m_0 k_B T}{\hbar^2}$。对 $k_z$ 积分令 $E_z = \frac{\hbar^2 k_z^2}{2m_0}$，则 $\frac{\hbar k_z}{m_0}\,\mathrm{d}k_z = \frac{\mathrm{d}E_z}{\hbar}$：
   $$\int_{E_F + W}^{\infty} \exp\!\left(-\frac{E_z}{k_B T}\right)\frac{\mathrm{d}E_z}{\hbar} = \frac{k_B T}{\hbar} \exp\!\left(-\frac{E_F + W}{k_B T}\right)$$
   合并所有因子（$\exp(E_F/(k_B T))$ 恰好消去）：
   $$j = \frac{e}{4\pi^3} \cdot \frac{2\pi m_0 k_B T}{\hbar^2} \cdot \frac{k_B T}{\hbar} e^{-W/(k_B T)} = \frac{e m_0 k_B^2}{2\pi^2 \hbar^3} T^2 e^{-W/(k_B T)} = \frac{4\pi e m_0 k_B^2}{h^3} T^2 e^{-W/(k_B T)}$$
   代入物理常数计算理论值 $A_0$：
   $$A_0 = \frac{1.602 \times 10^{-19} \times 9.109 \times 10^{-31} \times (1.381 \times 10^{-23})^2}{2\pi^2 \times (1.055 \times 10^{-34})^3} \approx 1.20 \times 10^6\ \mathrm{A/(m^2\cdot K^2)}$$

2. **钨阴极的功函数与有效常数**：由 $\ln(j/T^2) = \ln A_{\text{eff}} - \frac{W}{k_B T}$ 对两温度作差：
   $$\ln\frac{j_2 / T_2^2}{j_1 / T_1^2} = \frac{W}{k_B}\left(\frac{1}{T_1} - \frac{1}{T_2}\right)$$
   代入数值：$\frac{j_2/T_2^2}{j_1/T_1^2} = \frac{2650 / 2500^2}{8.70 / 2000^2} = \frac{4.240 \times 10^{-4}}{2.175 \times 10^{-6}} \approx 194.94$，$\ln(194.94) \approx 5.273$；$\frac{1}{T_1} - \frac{1}{T_2} = \frac{1}{2000} - \frac{1}{2500} = 1.00 \times 10^{-4}\ \mathrm{K}^{-1}$。故：
   $$W = \frac{5.273 \times 8.617 \times 10^{-5}\ \mathrm{eV/K}}{1.00 \times 10^{-4}\ \mathrm{K}^{-1}} \approx 4.54\ \mathrm{eV}$$
   回代 $T_1 = 2000\ \mathrm{K}$ 求有效发射常数：
   $$A_{\text{eff}} = \frac{j_1}{T_1^2} \exp\!\left(\frac{W}{k_B T_1}\right) = \frac{8.70}{4.00 \times 10^6} \exp\!\left(\frac{4.544}{0.1723}\right) \approx 6.12 \times 10^5\ \mathrm{A/(m^2\cdot K^2)}$$
   **偏小原因**：(i) 逸出电子在表面势垒处存在量子力学反射（反射系数 $r$，因子变为 $1-r$）；(ii) 功函数随温度线性微变 $W(T) = W_0 + \alpha T$，使表观指前因子乘以 $e^{-\alpha/k_B}$；(iii) 多晶钨表面各晶面功函数不均匀及有效质量偏离 $m_0$。
:::

---

### 知识点 4：金属电导、平均自由程与热导

#### 概念选择与填空

`CH04-KP4-01`（单选）在索末菲金属导电理论中，关于稳恒弱外电场 $\mathbf{E}$ 作用下金属中电子的输运图像，下列说法正确的是（ ）。
A. 只有费米球内深处的电子被外电场加速产生净电流，费米面上的电子保持静止
B. 外电场使整个费米球在 $k$ 空间刚性平移 $\Delta\mathbf{k} = -\frac{e\tau}{\hbar}\mathbf{E}$，由于球内深处对称状态仍两两抵消，净电流等效由费米面附近速率为 $v_F$ 的少数电子贡献
C. 自由电子的平均自由程由经典热速率决定，$l = \sqrt{\frac{3k_B T}{m}}\,\tau$，通常与晶格常数同量级
D. 严格周期性排列且静止的理想晶格离子实会对传导电子造成强烈散射，这是金属室温电阻的主要来源

::: details 思路提示
区分德鲁德经典图像与索末菲量子图像在“参与散射的电子速率”以及“金属电阻真正起源”上的差异。
:::

::: details 参考答案与解析
**参考答案**：B

**解析**：外电场使电子波矢按 $\hbar\dot{\mathbf{k}} = -e\mathbf{E}$ 演化，与散射弛豫平衡后费米球整体平移 $\Delta\mathbf{k} = -\frac{e\tau}{\hbar}\mathbf{E}$。球内重叠区 $\mathbf{k}$ 与 $-\mathbf{k}$ 态全满、速度两两抵消，净电流完全来源于费米面附近薄月牙壳层中高速（速率 $v_F \sim 10^6\ \mathrm{m/s}$）电子的不对称分布，其平均自由程 $l = v_F\tau$ 在室温可达数十纳米（上百个晶格常数）。理想静止周期晶格中电子波无阻传播，金属电阻真正来源于**声子（晶格热振动）**及**杂质/缺陷**对周期性的破坏。故 B 正确。
:::

---

`CH04-KP4-02`（填空）按照马西森定则，金属总电阻率可写为 $\rho(T) = \rho_0 + \rho_{\text{ph}}(T)$，其中与温度无关的剩余电阻率 $\rho_0$ 源于 ____ 散射，随温度变化的 $\rho_{\text{ph}}(T)$ 源于 ____ 散射；当温度高于德拜温度（$T \gg \Theta_D$）时，$\rho_{\text{ph}}(T)$ 与温度 $T$ 近似呈 ____ 关系；在极低温（$T \ll \Theta_D$）下，由布洛赫-格林艾森定律有 $\rho_{\text{ph}}(T) \propto$ ____。

::: details 思路提示
高温下声子数 $\bar{n}_q \propto T$；极低温下声子总密度 $\propto T^3$，且每次小角度散射的动量传递权重因子 $(1 - \cos\theta) \propto (q/k_F)^2 \propto T^2$。
:::

::: details 参考答案与解析
**参考答案**：静态杂质与晶格缺陷；晶格热振动（声子）；线性（正比于 $T$）；$T^5$。

**解析**：当声子散射与杂质/缺陷散射相互独立时，总散射几率相加 $\frac{1}{\tau} = \frac{1}{\tau_0} + \frac{1}{\tau_{\text{ph}}(T)}$，故 $\rho(T) = \rho_0 + \rho_{\text{ph}}(T)$。高温（$T \gg \Theta_D$）时声子数正比于 $T$，故 $\rho_{\text{ph}} \propto T$；极低温（$T \ll \Theta_D$）时可激发的声子数 $\propto T^3$，且长波声子仅能造成小角度散射，背向动量损减因子 $(1 - \cos\theta) \propto \theta^2 \propto (T/\Theta_D)^2$，两者相乘给出 $\rho_{\text{ph}} \propto T^5$。
:::

---

`CH04-KP4-03`（单选）关于金属中的维德曼-弗朗茨定律 $\frac{\kappa_e}{\sigma T} = L$，下列说法**错误**的是（ ）。
A. 索末菲量子理论给出的普适洛伦兹数 $L = \frac{\pi^2}{3}\left(\frac{k_B}{e}\right)^2 \approx 2.44 \times 10^{-8}\ \mathrm{W\cdot\Omega/K^2}$，与具体金属的 $n, m, \tau$ 无关
B. 经典德鲁德模型之所以算出了同量级的洛伦兹数，是因为它同时高估了电子热容约两个数量级、低估了电子均方速率约两个数量级，两个错误恰好在比值中近似抵消
C. 该定律要求决定电导与热导的电子弛豫时间相等（$\tau_\sigma = \tau_\kappa$），因此在弹性散射占主导的高温区或极低温杂质散射区成立良好
D. 在中低温区（$T \ll \Theta_D$ 但声子散射仍显著时），小角度非弹性声子散射对电流衰减比对热流更有效，因此实验测得的洛伦兹数总是远大于理论值 $L$

::: details 思路提示
分析能量约为 $k_B T$ 的小角度声子散射对“改变电子动量方向（衰减电流）”与“改变电子能量（衰减热流）”哪一种作用更强。
:::

::: details 参考答案与解析
**参考答案**：D

**解析**：在中低温区，热激发声子波矢很小（$q \ll k_F$），但声子能量 $\hbar\omega_q \sim k_B T$ 与费米面热激发层厚度相当。因此一次小角度非弹性声子散射几乎不改变电子速度方向（对衰减电流效率极低，$\tau_\sigma$ 较大），却能直接将高能热电子散射到费米面之下从而显著衰减热流（$\tau_\kappa$ 较小）。结果导致 $\tau_\kappa < \tau_\sigma$，实验洛伦兹数 $L_{\text{exp}} = \frac{\kappa_e}{\sigma T} \propto \frac{\tau_\kappa}{\tau_\sigma} L < L$（**低于**理论值而非大于）。A、B、C 均正确。
:::

#### 题型一：玻尔兹曼输运方程、电导率与平均自由程计算

`CH04-KP4-04` 
1. 在弛豫时间近似下写出稳态均匀弱电场 $\mathbf{E}$ 作用时三维自由电子气的玻尔兹曼输运方程，求出分布函数的一阶线性偏离 $\delta f(\mathbf{k})$，并由此证明电导率公式 $\sigma = \frac{n e^2 \tau(E_F)}{m}$；
2. 已知室温（$300\ \mathrm{K}$）下铜的电阻率 $\rho = 1.72 \times 10^{-8}\ \Omega\cdot\mathrm{m}$，取铜的传导电子数密度 $n = 8.50 \times 10^{28}\ \mathrm{m}^{-3}$，费米波矢 $k_F = 1.36 \times 10^{10}\ \mathrm{m}^{-1}$，费米速率 $v_F = 1.57 \times 10^6\ \mathrm{m/s}$，晶格常数 $a = 3.61\ \text{Å}$。计算室温下铜的弛豫时间 $\tau$、电子平均自由程 $l$（并求 $l/a$），以及在 $E = 1.0\ \mathrm{V/m}$ 弱电场下的电子漂移速率 $v_d$ 和费米球相对偏移量 $|\Delta k|/k_F$。

::: details 思路提示
稳态均匀场中 $\frac{\partial f}{\partial t} = 0$、$\nabla_{\mathbf{r}} f = 0$，玻尔兹曼方程简化为 $\dot{\mathbf{k}}\cdot\nabla_{\mathbf{k}} f = -\frac{f - f_0}{\tau}$；在线性近似下用 $f_0$ 代替左侧的 $f$，利用低温极限 $-\frac{\partial f_0}{\partial E} \approx \delta(E - E_F)$ 完成球坐标积分（各向同性因子 $\langle v_x^2 \rangle = \frac{1}{3}v_F^2$）。
:::

::: details 参考答案与解析
**参考答案**：
1. $\delta f(\mathbf{k}) = e\tau \mathbf{v}\cdot\mathbf{E}\left(-\frac{\partial f_0}{\partial E}\right)$，$\sigma = \frac{n e^2 \tau(E_F)}{m}$（证明见下）；
2. $\tau \approx 2.43 \times 10^{-14}\ \mathrm{s}$，$l \approx 38.2\ \mathrm{nm}$（约 $106 a$），$v_d \approx 4.27 \times 10^{-3}\ \mathrm{m/s}$，$|\Delta k|/k_F \approx 2.71 \times 10^{-9}$。

**解析**：
1. **玻尔兹曼方程与电导率推导**：对空间均匀、定态自由电子气，外电场 $\mathbf{E} = E \hat{\mathbf{x}}$ 驱动波矢变化 $\dot{\mathbf{k}} = -\frac{e\mathbf{E}}{\hbar}$。弛豫时间近似下的玻尔兹曼方程为：
   $$-\frac{e}{\hbar}\mathbf{E}\cdot\nabla_{\mathbf{k}} f(\mathbf{k}) = -\frac{f(\mathbf{k}) - f_0(\mathbf{k})}{\tau(\mathbf{k})}$$
   弱场线性响应下，以平衡分布 $f_0(E)$ 替代左侧的 $f$，并利用 $\nabla_{\mathbf{k}} f_0 = \frac{\partial f_0}{\partial E}\nabla_{\mathbf{k}} E = \hbar \mathbf{v}\frac{\partial f_0}{\partial E}$：
   $$\delta f(\mathbf{k}) = f(\mathbf{k}) - f_0(\mathbf{k}) = e\tau(\mathbf{k})\mathbf{v}\cdot\mathbf{E}\left(-\frac{\partial f_0}{\partial E}\right)$$
   电流密度沿 $x$ 方向（注意平衡态 $f_0$ 无净电流，计入自旋简并度 $2$）：
   $$J_x = \frac{2}{(2\pi)^3} \int (-e) v_x \delta f(\mathbf{k})\,\mathrm{d}^3 k = e^2 E \cdot \frac{1}{4\pi^3}\int \tau(E) v_x^2 \left(-\frac{\partial f_0}{\partial E}\right)\mathrm{d}^3 k$$
   由球对称性，$v_x^2$ 在等能面上可替换为 $\frac{1}{3}v^2 = \frac{2E}{3m}$；又因 $\frac{2}{(2\pi)^3}\mathrm{d}^3 k = D(E)\,\mathrm{d}E$（单位体积态密度 $D(E) = g(E)/V$），故：
   $$\sigma = \frac{J_x}{E} = e^2 \int_0^\infty \frac{1}{3} v^2 \tau(E) D(E)\left(-\frac{\partial f_0}{\partial E}\right)\mathrm{d}E$$
   在强简并低温条件（$T \ll T_F$）下，$-\frac{\partial f_0}{\partial E} \approx \delta(E - E_F)$，立得：
   $$\sigma = \frac{1}{3} e^2 v_F^2 \tau(E_F) D(E_F)$$
   代入 $D(E_F) = \frac{3n}{2E_F}$ 与 $\frac{1}{2}m v_F^2 = E_F$，即证：
   $$\sigma = \frac{1}{3} e^2 \left(\frac{2E_F}{m}\right)\tau(E_F)\left(\frac{3n}{2E_F}\right) = \frac{n e^2 \tau(E_F)}{m}$$

2. **铜的室温输运参量**：电导率 $\sigma = \frac{1}{\rho} = \frac{1}{1.72 \times 10^{-8}} \approx 5.81 \times 10^7\ \mathrm{S/m}$。
   - **弛豫时间**：
     $$\tau = \frac{m_0}{n e^2 \rho} = \frac{9.109 \times 10^{-31}}{8.502 \times 10^{28} \times (1.602 \times 10^{-19})^2 \times 1.72 \times 10^{-8}} \approx 2.43 \times 10^{-14}\ \mathrm{s}$$
   - **平均自由程**：
     $$l = v_F \tau = 1.575 \times 10^6 \times 2.427 \times 10^{-14} \approx 3.82 \times 10^{-8}\ \mathrm{m} = 38.2\ \mathrm{nm}$$
     与晶格常数之比 $\frac{l}{a} = \frac{38.2\ \mathrm{nm}}{0.361\ \mathrm{nm}} \approx 106$，远大于晶格间距。
   - **漂移速率与费米球偏移**（$E = 1.0\ \mathrm{V/m}$）：
     $$v_d = \frac{e\tau E}{m_0} = \frac{1.602 \times 10^{-19} \times 2.427 \times 10^{-14} \times 1.0}{9.109 \times 10^{-31}} \approx 4.27 \times 10^{-3}\ \mathrm{m/s}$$
     $$|\Delta k| = \frac{e\tau E}{\hbar} = \frac{m_0 v_d}{\hbar} \approx 36.9\ \mathrm{m}^{-1}, \qquad \frac{|\Delta k|}{k_F} = \frac{v_d}{v_F} \approx 2.71 \times 10^{-9}$$
     可见常规弱电场引起的费米球偏移微乎其微，充分验证了线性响应近似的准确性。
:::

#### 题型二：维德曼-弗朗茨定律与马西森定则综合计算

`CH04-KP4-05` 
1. 结合三维自由电子气单位体积热容 $c_{Ve} = \frac{\pi^2}{2} n k_B \frac{T}{T_F}$ 与气体动理论热导公式 $\kappa_e = \frac{1}{3} c_{Ve} v_F l$（其中 $l = v_F \tau$），推导电子热导率 $\kappa_e$，证明维德曼-弗朗茨定律并计算洛伦兹数 $L$；
2. 利用室温（$300\ \mathrm{K}$）纯铜的电阻率 $\rho = 1.72 \times 10^{-8}\ \Omega\cdot\mathrm{m}$，由维德曼-弗朗茨定律估算铜的室温电子热导率 $\kappa_e$（已知铜室温实验总热导率约 $401\ \mathrm{W/(m\cdot K)}$，据此说明金属导热的主导机制）；
3. 若在该纯铜中掺入少量杂质，测得极低温 $4.2\ \mathrm{K}$ 时的剩余电阻率 $\rho_0 = 8.60 \times 10^{-10}\ \Omega\cdot\mathrm{m}$。假定马西森定则与弹性散射区维德曼-弗朗茨定律均成立，求掺杂铜在 $300\ \mathrm{K}$ 时的总电阻率 $\rho'$、剩余电阻比 $RRR = \rho'(300\ \mathrm{K})/\rho_0$ 及 $4.2\ \mathrm{K}$ 时的电子热导率 $\kappa_e(4.2\ \mathrm{K})$。

::: details 思路提示
第 1 问中注意利用 $k_B T_F = E_F = \frac{1}{2}m v_F^2$ 消去 $v_F$ 和 $T_F$；第 3 问中 $300\ \mathrm{K}$ 纯铜电阻率近似视为声子项 $\rho_{\text{ph}}(300\ \mathrm{K})$，掺杂后总电阻率 $\rho' = \rho_{\text{ph}} + \rho_0$，在 $4.2\ \mathrm{K}$ 杂质弹性散射主导时直接用 $\kappa_e = L T / \rho_0$ 估算。
:::

::: details 参考答案与解析
**参考答案**：
1. $\kappa_e = \frac{\pi^2 n k_B^2 T \tau}{3m}$，$L = \frac{\pi^2}{3}\left(\frac{k_B}{e}\right)^2 \approx 2.44 \times 10^{-8}\ \mathrm{W\cdot\Omega/K^2}$；
2. $\kappa_e(300\ \mathrm{K}) \approx 426\ \mathrm{W/(m\cdot K)}$，与实验总热导率高度接近，表明金属中热量主要由自由电子输运；
3. $\rho'(300\ \mathrm{K}) \approx 1.81 \times 10^{-8}\ \Omega\cdot\mathrm{m}$，$RRR = 21.0$，$\kappa_e(4.2\ \mathrm{K}) \approx 119\ \mathrm{W/(m\cdot K)}$。

**解析**：
1. **电子热导率与洛伦兹数推导**：将 $c_{Ve} = \frac{\pi^2}{2} n k_B \frac{T}{T_F}$ 与 $l = v_F \tau$ 代入 $\kappa_e = \frac{1}{3}c_{Ve} v_F l$：
   $$\kappa_e = \frac{1}{3}\left(\frac{\pi^2}{2} n k_B \frac{T}{T_F}\right) v_F^2 \tau$$
   利用 $k_B T_F = E_F = \frac{1}{2} m v_F^2 \implies \frac{v_F^2}{T_F} = \frac{2k_B}{m}$，消去 $v_F$ 与 $T_F$ 得：
   $$\kappa_e = \frac{\pi^2 n k_B^2 T \tau}{3m}$$
   与电导率 $\sigma = \frac{n e^2 \tau}{m}$ 相除（假设同一弛豫时间 $\tau$）：
   $$\frac{\kappa_e}{\sigma T} = \frac{\pi^2}{3}\left(\frac{k_B}{e}\right)^2 \equiv L$$
   代入常数得普适洛伦兹数：
   $$L = \frac{\pi^2}{3}\left(\frac{1.381 \times 10^{-23}}{1.602 \times 10^{-19}}\right)^2 \approx 2.44 \times 10^{-8}\ \mathrm{W\cdot\Omega/K^2}$$
   （若采用严格玻尔兹曼输运方程按索末菲展开求解热流与电流，所得系数亦精确为 $\frac{\pi^2}{3}$。）

2. **室温纯铜热导率估算**：
   $$\kappa_e(300\ \mathrm{K}) = \frac{L T}{\rho} = \frac{2.443 \times 10^{-8} \times 300}{1.72 \times 10^{-8}} \approx 426\ \mathrm{W/(m\cdot K)}$$
   该估算值与实验总热导率（$\approx 401\ \mathrm{W/(m\cdot K)}$）非常接近，说明在优良金属中**自由电子导热占绝对主导**，声子晶格热导仅占很小比例。

3. **掺杂铜的马西森定则与低温热导率**：室温下纯铜电阻率主要由声子贡献，掺杂后由马西森定则：
   $$\rho'(300\ \mathrm{K}) = \rho_{\text{ph}}(300\ \mathrm{K}) + \rho_0 = 1.72 \times 10^{-8} + 8.60 \times 10^{-10} = 1.806 \times 10^{-8}\ \Omega\cdot\mathrm{m} \approx 1.81 \times 10^{-8}\ \Omega\cdot\mathrm{m}$$
   剩余电阻比：
   $$RRR = \frac{\rho'(300\ \mathrm{K})}{\rho_0} = \frac{1.806 \times 10^{-8}}{8.60 \times 10^{-10}} = 21.0$$
   在 $T = 4.2\ \mathrm{K}$ 时，静态杂质弹性散射占主导（$\rho(4.2\ \mathrm{K}) \approx \rho_0$），维德曼-弗朗茨定律重新精确适用：
   $$\kappa_e(4.2\ \mathrm{K}) = \frac{L \cdot 4.2}{\rho_0} = \frac{2.443 \times 10^{-8} \times 4.2}{8.60 \times 10^{-10}} \approx 119\ \mathrm{W/(m\cdot K)}$$
:::
