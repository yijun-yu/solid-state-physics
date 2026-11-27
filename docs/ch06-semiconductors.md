# 第六章 半导体电子理论

::: info 教学大纲（建议 6 学时）
- 6.1 半导体的基本能带结构（导带、价带、直接/间接带隙、带边有效质量）
- 6.2 半导体的掺杂（施主、受主与类氢杂质模型）
- 6.3 费米统计分布、费米能级与载流子浓度
- 6.4 半导体的电导率、迁移率与霍尔效应
- 6.5 PN 结、MIS 结构、异质结与非晶态半导体基础
:::

::: tip 核心概念与模型
**1. 半导体能带结构与浅杂质类氢模型**
- **直接带隙与间接带隙**：导带底与价带顶位于同一波矢（如 $\Gamma$ 点，GaAs、InP）为**直接带隙**，带边光跃迁直接守恒动量、发光效率高；位于不同波矢（如 Si、Ge）为**间接带隙**，带边跃迁需借助**声子**协助提供波矢差 $\Delta\mathbf{k}$，发光效率低。
- **掺杂与类氢模型**：四价半导体（Si、Ge）中掺入五价元素（P、As）形成**施主能级**（靠近导带底，$n$ 型），掺入三价元素（B、Ga）形成**受主能级**（靠近价带顶，$p$ 型）。在连续介质与有效质量近似下，浅杂质束缚能与有效玻尔半径为：
  $$\Delta E_D = \frac{m_n^*/m_0}{\varepsilon_r^2}E_0, \qquad a_B^* = \frac{\varepsilon_r}{m_n^*/m_0}a_B$$
  因 $\varepsilon_r \sim 10\text{--}16$，$\Delta E_D$ 仅数毫电子伏至数十毫电子伏（室温几乎全电离），$a_B^*$ 跨越数十个晶格常数。

**2. 非简并半导体载流子统计与质量作用定律**
- 在非简并条件（$E_c - E_F \gg k_B T$ 且 $E_F - E_v \gg k_B T$）下，费米分布退化为玻尔兹曼分布，热平衡电子与空穴浓度为：
  $$\begin{aligned} n_0 &= N_c \exp\!\left(-\frac{E_c - E_F}{k_B T}\right), \qquad N_c = 2\left(\frac{2\pi m_{dn}^* k_B T}{h^2}\right)^{3/2} \\ p_0 &= N_v \exp\!\left(-\frac{E_F - E_v}{k_B T}\right), \qquad N_v = 2\left(\frac{2\pi m_{dp}^* k_B T}{h^2}\right)^{3/2} \end{aligned}$$
- **质量作用定律与本征半导体**：
  $$n_0 p_0 = n_i^2 = N_c N_v \exp\!\left(-\frac{E_g}{k_B T}\right), \qquad E_{Fi} = \frac{E_c + E_v}{2} + \frac{3}{4}k_B T \ln\!\left(\frac{m_{dp}^*}{m_{dn}^*}\right)$$
- **电中性条件**（杂质全电离）：$n_0 + N_A = p_0 + N_D$。$n$ 型半导体升温依次经历**低温弱电离区**（斜率 $-\frac{\Delta E_D}{2k_B}$）、**杂质饱和电离区**（$n_0 \approx N_D$）和**高温本征区**（斜率 $-\frac{E_g}{2k_B}$）。

**3. 输运、散射机制与霍尔效应**
- **电导率与迁移率**：$\sigma = e(n\mu_n + p\mu_p)$。两大主要散射机制为**晶格声学声子散射**（$\mu_L \propto T^{-3/2}$，高温主导）与**电离杂质散射**（$\mu_I \propto T^{3/2}/N_I$，低温主导），合成迁移率满足 $\frac{1}{\mu} = \frac{1}{\mu_L} + \frac{1}{\mu_I}$。
- **霍尔效应**（弱场、$r_H \approx 1$）：$U_H = R_H \frac{IB}{d}$，单载流子 $R_H = -\frac{1}{ne}$（$n$ 型）或 $+\frac{1}{pe}$（$p$ 型），霍尔迁移率 $\mu_H = \lvert R_H\rvert\sigma$；双载流子霍尔系数为：
  $$R_H = \frac{p\mu_p^2 - n\mu_n^2}{e(p\mu_p + n\mu_n)^2}$$

**4. PN 结、MIS 结构、异质结与非晶态半导体**
- **突变 PN 结**（耗尽近似）：热平衡全结费米能级平齐，内建电势差 $V_{bi} = \frac{k_B T}{e}\ln\frac{N_A N_D}{n_i^2}$；由电中性 $N_A x_p = N_D x_n$，耗尽层主要向**低掺杂一侧**延伸，总宽度与结面最大电场为：
  $$W = \sqrt{\frac{2\varepsilon_0\varepsilon_r}{e}\left(\frac{1}{N_A} + \frac{1}{N_D}\right)(V_{bi} - V)}, \qquad \lvert\mathcal{E}_{\max}\rvert = \frac{2(V_{bi} - V)}{W}$$
- **MIS 结构**（$p$ 型衬底）：随栅压 $V_G$ 升高依次进入**积累**（$V_G < 0$）、**耗尽**、**反型**；强反型开启判据为表面势 $\psi_s = 2\phi_F = \frac{2k_B T}{e}\ln\frac{N_A}{n_i}$。
- **异质结与非晶态半导体**：安德森定则给出异质结带阶 $\Delta E_c = \chi_2 - \chi_1$、$\Delta E_v = (E_{g1} - E_{g2}) - \Delta E_c$（调制掺杂可在界面形成高迁移率二维电子气）；非晶态半导体虽无长程序但保留**近程有序**，仍具有类能带结构，但长程无序导致**带尾局域态**与**迁移率边**。
:::

![直接带隙与间接带隙跃迁及n型半导体三温区曲线](/figures/ch06-semiconductor-stats.svg)

<p class="fig-caption">图 6-1 直接与间接带隙光学跃迁对比（左）及 <em>n</em> 型半导体载流子浓度随温度倒数的变化（右）</p>

## 习题及参考解答

### 知识点 1：半导体能带结构与杂质能级

#### 概念选择与填空

`CH06-KP1-01`（单选）关于直接带隙半导体（如 GaAs）与间接带隙半导体（如 Si、Ge）的能带特征与光学跃迁，下列说法**错误**的是（ ）。
A. 直接带隙半导体的导带底与价带顶位于布里渊区中的同一波矢 $\mathbf{k}$ 处
B. 间接带隙半导体的导带底与价带顶位于不同的波矢 $\mathbf{k}$ 处
C. 由于可见光/近红外光子的动量远小于布里渊区尺度，间接带隙半导体发生带边光吸收或辐射复合时必须借助声子提供波矢差 $\Delta\mathbf{k}$
D. 硅（Si）作为间接带隙半导体，其带边辐射复合发光效率远高于直接带隙半导体砷化镓（GaAs）

::: details 思路提示
比较直接跃迁（二体过程：电子+光子）与间接跃迁（三体过程：电子+光子+声子）的跃迁几率大小。
:::

::: details 参考答案与解析
**参考答案**：D

**解析**：光子的波矢 $k_{\text{ph}} = \frac{2\pi}{\lambda} \sim 10^7\ \mathrm{m}^{-1}$，远小于布里渊区尺寸 $\frac{\pi}{a} \sim 10^{10}\ \mathrm{m}^{-1}$，故光学跃迁在 $E(\mathbf{k})$ 图中近乎严格竖直。直接带隙半导体（GaAs）电子可直接垂直复合发光，辐射复合几率高，广泛用于 LED 和半导体激光器；间接带隙半导体（Si）需要晶格声子同时参与以守恒准动量，属于二级过程，发光效率极低。A、B、C 均正确。
:::

---

`CH06-KP1-02`（填空）在纯硅（Si）晶体中掺入少量五价元素磷（P）形成 ____ 型半导体，磷原子起 ____（填“施主”或“受主”）作用，其电离能级位于禁带中靠近 ____ 的位置；掺入少量三价元素硼（B）形成 ____ 型半导体，其杂质能级位于禁带中靠近 ____ 的位置。

::: details 思路提示
五价原子与周围四个硅原子形成共价键后多出 $1$ 个价电子；三价原子缺少 $1$ 个价电子，易于从价带夺取电子而留下空穴。
:::

::: details 参考答案与解析
**参考答案**：$n$；施主；导带底；$p$；价带顶。

**解析**：五价磷原子在硅中以弱库仑力束缚第 $5$ 个价电子，只需很小的能量 $\Delta E_D$ 即可激发至导带成为导电电子，故称为**施主**，能级 $E_D$ 紧邻导带底下方；三价硼原子容易从价带接受电子补全四面体共价键并在价带产生导电空穴，称为**受主**，能级 $E_A$ 紧邻价带顶上方。
:::

---

`CH06-KP1-03`（单选）在采用类氢模型估算半导体中浅施主杂质电离能 $\Delta E_D$ 与有效玻尔半径 $a_B^*$ 时，下列说法正确的是（ ）。
A. 半导体高相对介电常数 $\varepsilon_r$ 屏蔽了施主离子实与束缚电子间的库仑吸引，使 $\Delta E_D$ 缩小约 $\varepsilon_r^2$ 倍
B. 浅杂质电子的轨道半径 $a_B^*$ 通常小于晶格常数 $a$，因此电子高度局域在单个杂质原子核附近
C. 导带电子有效质量 $m_n^*$ 越小，浅施主电离能 $\Delta E_D$ 越大、有效玻尔半径 $a_B^*$ 越小
D. 室温下硅中浅施主杂质因电离能高达数电子伏特，几乎完全无法电离

::: details 思路提示
核对类氢模型公式 $\Delta E_D = \frac{m_n^*/m_0}{\varepsilon_r^2}E_0$ 与 $a_B^* = \frac{\varepsilon_r}{m_n^*/m_0}a_B$ 中 $\varepsilon_r$ 和 $m_n^*$ 的幂次位置。
:::

::: details 参考答案与解析
**参考答案**：A

**解析**：类氢模型用有效质量 $m_n^*$ 代替自由电子质量 $m_0$、用 $\varepsilon_0\varepsilon_r$ 代替真空介电常数 $\varepsilon_0$，得 $\Delta E_D = \frac{m_n^*/m_0}{\varepsilon_r^2}E_0$ 与 $a_B^* = \frac{\varepsilon_r}{m_n^*/m_0}a_B$。由于 $\varepsilon_r \sim 10\text{--}16$ 且 $m_n^* < m_0$，$\Delta E_D$ 降至数至数十毫电子伏（与室温 $k_B T \approx 26\ \mathrm{meV}$ 相当或更小，易于热电离），$a_B^*$ 展宽至数纳米至十余纳米（远大于晶格常数，反过来证实了连续介质屏蔽与有效质量近似的自洽性）。故 A 正确，B、C、D 均错误。
:::

#### 题型一：浅杂质类氢模型计算与重掺杂莫特转变

`CH06-KP1-04` 已知砷化镓（GaAs）的相对介电常数 $\varepsilon_r = 12.9$、导带底电子有效质量 $m_n^* = 0.067 m_0$；硅（Si）的相对介电常数 $\varepsilon_r = 11.7$、取导带电导有效质量 $m_n^* = 0.26 m_0$。
1. 从氢原子基态电离能 $E_0 = \frac{m_0 e^4}{32\pi^2 \varepsilon_0^2 \hbar^2} = 13.6\ \mathrm{eV}$ 与玻尔半径 $a_B = \frac{4\pi\varepsilon_0 \hbar^2}{m_0 e^2} = 0.529\ \text{Å}$ 出发，写出浅施主类氢模型的 $\Delta E_D$ 与 $a_B^*$ 表达式；
2. 分别计算 GaAs 与 Si 中浅施主杂质的 $\Delta E_D$（单位：$\mathrm{meV}$）和 $a_B^*$（单位：$\text{Å}$），比较 $a_B^*$ 与晶格常数（$a \approx 5.4\text{--}5.7\ \text{Å}$）说明连续介质近似的合理性；
3. 当施主浓度 $N_D$ 升高至满足莫特金属-绝缘体转变判据 $N_D^{1/3} a_B^* \approx 0.25$ 时，杂质态交叠形成杂质带并与导带合并（简并半导体）。估算 GaAs 与 Si 的临界掺杂浓度 $N_{D,c}$（单位：$\mathrm{cm}^{-3}$）。

::: details 思路提示
直接将 $m_0 \to m_n^*$、$\varepsilon_0 \to \varepsilon_0\varepsilon_r$ 代入氢原子公式；第 3 问由 $N_{D,c} = (0.25 / a_B^*)^3$ 注意将 $a_B^*$ 换算为厘米（$1\ \text{Å} = 10^{-8}\ \mathrm{cm}$）。
:::

::: details 参考答案与解析
**参考答案**：
1. $\Delta E_D = \frac{m_n^*/m_0}{\varepsilon_r^2}E_0$，$a_B^* = \frac{\varepsilon_r}{m_n^*/m_0}a_B$；
2. GaAs：$\Delta E_D \approx 5.48\ \mathrm{meV}$，$a_B^* \approx 102\ \text{Å}$；Si：$\Delta E_D \approx 25.8\ \mathrm{meV}$，$a_B^* \approx 23.8\ \text{Å}$；
3. GaAs：$N_{D,c} \approx 1.48 \times 10^{16}\ \mathrm{cm}^{-3}$；Si：$N_{D,c} \approx 1.16 \times 10^{18}\ \mathrm{cm}^{-3}$。

**解析**：
1. **类氢替换**：在均匀介电屏蔽与各向同性有效质量近似下，将 $m_0 \to m_n^*$、$\varepsilon_0 \to \varepsilon_0 \varepsilon_r$ 代入氢原子基态公式即得：
   $$\Delta E_D = \frac{m_n^* e^4}{32\pi^2 \varepsilon_0^2 \varepsilon_r^2 \hbar^2} = \frac{m_n^*/m_0}{\varepsilon_r^2}E_0, \qquad a_B^* = \frac{4\pi\varepsilon_0\varepsilon_r \hbar^2}{m_n^* e^2} = \frac{\varepsilon_r}{m_n^*/m_0}a_B$$

2. **GaAs 与 Si 数值**：
   - **GaAs**：
     $$\Delta E_D = \frac{0.067}{12.9^2} \times 13.61\ \mathrm{eV} \approx 5.48\ \mathrm{meV}, \qquad a_B^* = \frac{12.9}{0.067} \times 0.529\ \text{Å} \approx 102\ \text{Å}$$
   - **Si**：
     $$\Delta E_D = \frac{0.26}{11.7^2} \times 13.61\ \mathrm{eV} \approx 25.8\ \mathrm{meV}, \qquad a_B^* = \frac{11.7}{0.26} \times 0.529\ \text{Å} \approx 23.8\ \text{Å}$$
   两者的有效玻尔半径分别为晶格常数（$\sim 5.5\ \text{Å}$）的约 $18$ 倍（GaAs）与 $4.4$ 倍（Si），电子波函数覆盖大量晶胞，因此将晶格视为宏观介电连续介质并采用带边有效质量具有良好合理性。（硅中磷/砷实测电离能约 $45\text{--}54\ \mathrm{meV}$，高于简单估算的原因在于杂质核心短程势的中心胞修正。）

3. **莫特临界掺杂浓度**：由 $N_{D,c} = \left(\frac{0.25}{a_B^*}\right)^3$：
   - **GaAs**（$a_B^* = 1.019 \times 10^{-6}\ \mathrm{cm}$）：
     $$N_{D,c} = \left(\frac{0.25}{1.019 \times 10^{-6}\ \mathrm{cm}}\right)^3 \approx 1.48 \times 10^{16}\ \mathrm{cm}^{-3}$$
   - **Si**（$a_B^* = 2.38 \times 10^{-7}\ \mathrm{cm}$）：
     $$N_{D,c} = \left(\frac{0.25}{2.38 \times 10^{-7}\ \mathrm{cm}}\right)^3 \approx 1.16 \times 10^{18}\ \mathrm{cm}^{-3}$$
   可见电子有效质量极轻的 GaAs 在较低掺杂浓度下即进入简并态，而硅需要高约两个数量级的重掺杂才发生金属化。
:::

---

### 知识点 2：费米能级与平衡载流子浓度

#### 概念选择与填空

`CH06-KP2-01`（单选）关于处于热平衡状态的非简并半导体，下列说法**错误**的是（ ）。
A. 导带平衡电子浓度满足 $n_0 = N_c e^{-(E_c - E_F)/(k_B T)}$，价带平衡空穴浓度满足 $p_0 = N_v e^{-(E_F - E_v)/(k_B T)}$
B. 质量作用定律 $n_0 p_0 = n_i^2$ 仅取决于半导体材料与温度，与是否掺杂及掺杂浓度无关（非简并范围内）
C. 一定温度下，向本征硅中掺入施主杂质使电子浓度增大 $10^6$ 倍时，空穴浓度将随之减小为原来的 $10^{-6}$ 倍
D. 掺入施主杂质提高电子浓度的同时，由于热激发增强，平衡空穴浓度也会同步增大

::: details 思路提示
由质量作用定律 $n_0 p_0 = n_i^2(T)$ 直接判断恒温下 $n_0$ 增大时 $p_0$ 的变化方向。
:::

::: details 参考答案与解析
**参考答案**：D

**解析**：恒定温度下，非简并半导体满足质量作用定律 $n_0 p_0 = n_i^2(T) = \text{const}$。掺入施主杂质使多子电子浓度 $n_0$ 大幅上升，大量电子增加了与空穴的复合几率，使平衡态少子空穴浓度 $p_0 = n_i^2/n_0$ 剧烈下降（抑制少子）。A、B、C 均正确。
:::

---

`CH06-KP2-02`（填空）本征半导体的费米能级为 $E_{Fi} = \frac{E_c + E_v}{2} + \frac{3}{4}k_B T \ln\!\left(\frac{m_{dp}^*}{m_{dn}^*}\right)$，当空穴态密度有效质量大于电子态密度有效质量（$m_{dp}^* > m_{dn}^*$）时，随温度升高 $E_{Fi}$ 向 ____ 方向偏移；对 $n$ 型半导体，随温度从极低温升至高温，载流子浓度依次经历 ____ 区、____ 区和 ____ 区，其费米能级最终趋近于 ____。

::: details 思路提示
当 $m_{dp}^* > m_{dn}^*$ 时，$\ln(m_{dp}^*/m_{dn}^*) > 0$，即价带态密度大于导带态密度，为了保持 $n_0 = p_0$ 必须提高 $E_{Fi}$ 以拉大空穴激发势垒、减小电子激发势垒。
:::

::: details 参考答案与解析
**参考答案**：导带（上方）；低温弱电离（冻结）；杂质饱和电离；高温本征；本征费米能级 $E_{Fi}$（禁带中线附近）。

**解析**：$m_{dp}^* > m_{dn}^* \implies N_v > N_c$，为维持 $n_0 = p_0$，费米能级须更靠近态密度较小的一侧（导带侧）。对 $n$ 型半导体，温度极低时处于弱电离（冻结）区（$E_F$ 位于 $E_c$ 与 $E_D$ 之间）；中等温度进入饱和电离区（$n_0 \approx N_D$，$E_F$ 随温度升高向禁带中线下移）；高温时本征激发压倒杂质电离，进入高温本征区，$E_F \to E_{Fi}$。
:::

---

`CH06-KP2-03`（单选）某非简并 $n$ 型半导体处于杂质饱和电离区（$n_0 \approx N_D \gg n_i$）。若保持温度 $T$ 不变，将施主掺杂浓度 $N_D$ 增大为原来的 $e$ 倍（自然对数底），则该半导体的费米能级 $E_F$ 将（ ）。
A. 向上（向导带底）移动 $k_B T$
B. 向下（向禁带中线）移动 $k_B T$
C. 向上移动 $\frac{1}{2}k_B T$
D. 保持不变

::: details 思路提示
由 $n_0 = N_c e^{-(E_c - E_F)/(k_B T)} = N_D$ 反解出 $E_F = E_c - k_B T \ln(N_c / N_D)$，计算 $N_D \to e N_D$ 时的改变量。
:::

::: details 参考答案与解析
**参考答案**：A

**解析**：在饱和电离区，$E_F = E_c - k_B T \ln\frac{N_c}{N_D} = E_c + k_B T \ln\frac{N_D}{N_c}$。当 $N_D' = e N_D$ 时：
$$E_F' - E_F = k_B T \ln\frac{N_D'}{N_D} = k_B T \ln e = +k_B T$$
即费米能级向导带底方向上移 $k_B T$。
:::

#### 题型一：本征半导体载流子浓度与费米能级推导计算

`CH06-KP2-04` 
1. 在非简并玻尔兹曼近似下，从导带单位体积态密度 $D_c(E) = \frac{1}{2\pi^2}\left(\frac{2m_{dn}^*}{\hbar^2}\right)^{3/2}(E - E_c)^{1/2}$ 出发，推导热平衡电子浓度 $n_0 = N_c e^{-(E_c - E_F)/(k_B T)}$ 及导带有效状态密度 $N_c$ 的表达式（已知高斯型伽马积分 $\int_0^\infty x^{1/2} e^{-x}\,\mathrm{d}x = \frac{\sqrt{\pi}}{2}$）；并结合对称的空穴浓度公式导出质量作用定律与本征费米能级 $E_{Fi}$；
2. 已知室温（$T = 300\ \mathrm{K}$）下硅的禁带宽度 $E_g = 1.12\ \mathrm{eV}$，导带与价带总态密度有效质量分别为 $m_{dn}^* = 1.08 m_0$、$m_{dp}^* = 0.81 m_0$。计算室温下硅的 $N_c$、$N_v$、本征载流子浓度 $n_i$（单位：$\mathrm{cm}^{-3}$）及本征费米能级相对于禁带中线 $E_m = \frac{E_c + E_v}{2}$ 的偏移量 $E_{Fi} - E_m$（单位：$\mathrm{meV}$）。

::: details 思路提示
做无量纲变量代换 $x = \frac{E - E_c}{k_B T}$ 即可将积分化为 $\int_0^\infty x^{1/2} e^{-x}\,\mathrm{d}x = \frac{\sqrt{\pi}}{2}$；注意单位换算 $1\ \mathrm{m}^{-3} = 10^{-6}\ \mathrm{cm}^{-3}$。
:::

::: details 参考答案与解析
**参考答案**：
1. $N_c = 2\left(\frac{2\pi m_{dn}^* k_B T}{h^2}\right)^{3/2}$，证明见下；
2. $N_c \approx 2.82 \times 10^{19}\ \mathrm{cm}^{-3}$，$N_v \approx 1.83 \times 10^{19}\ \mathrm{cm}^{-3}$，$n_i \approx 8.88 \times 10^9\ \mathrm{cm}^{-3}$，$E_{Fi} - E_m \approx -5.58\ \mathrm{meV}$。

**解析**：
1. **导带平衡电子浓度推导**：非简并条件下 $E - E_F \ge E_c - E_F \gg k_B T$，故 $f(E) \approx \exp\!\left(-\frac{E - E_F}{k_B T}\right)$。积分上限延至无穷大：
   $$n_0 = \int_{E_c}^\infty D_c(E) f(E)\,\mathrm{d}E \approx \frac{1}{2\pi^2}\left(\frac{2m_{dn}^*}{\hbar^2}\right)^{3/2} \int_{E_c}^\infty (E - E_c)^{1/2} \exp\!\left(-\frac{E - E_F}{k_B T}\right)\mathrm{d}E$$
   令 $x = \frac{E - E_c}{k_B T}$，则 $E - E_F = (E_c - E_F) + k_B T x$，$\mathrm{d}E = k_B T\,\mathrm{d}x$：
   $$n_0 = \frac{1}{2\pi^2}\left(\frac{2m_{dn}^* k_B T}{\hbar^2}\right)^{3/2} e^{-(E_c - E_F)/(k_B T)} \int_0^\infty x^{1/2} e^{-x}\,\mathrm{d}x$$
   代入 $\int_0^\infty x^{1/2} e^{-x}\,\mathrm{d}x = \frac{\sqrt{\pi}}{2}$ 及 $h = 2\pi\hbar$，化简系数得：
   $$N_c = \frac{1}{4\pi^{3/2}}\left(\frac{2m_{dn}^* k_B T}{\hbar^2}\right)^{3/2} = 2\left(\frac{2\pi m_{dn}^* k_B T}{h^2}\right)^{3/2}$$
   同理空穴占据几率 $1 - f(E) \approx e^{-(E_F - E)/(k_B T)}$ 给出 $p_0 = N_v e^{-(E_F - E_v)/(k_B T)}$，其中 $N_v = 2\left(\frac{2\pi m_{dp}^* k_B T}{h^2}\right)^{3/2}$。两式相乘消去 $E_F$ 即得质量作用定律：
   $$n_0 p_0 = N_c N_v \exp\!\left(-\frac{E_c - E_v}{k_B T}\right) = N_c N_v e^{-E_g/(k_B T)} \equiv n_i^2$$
   对本征半导体令 $n_0 = p_0$，即 $N_c e^{-(E_c - E_{Fi})/(k_B T)} = N_v e^{-(E_{Fi} - E_v)/(k_B T)}$，两边取对数解得：
   $$E_{Fi} = \frac{E_c + E_v}{2} + \frac{k_B T}{2}\ln\frac{N_v}{N_c} = \frac{E_c + E_v}{2} + \frac{3}{4}k_B T \ln\frac{m_{dp}^*}{m_{dn}^*}$$

2. **室温硅的数值计算**（$T = 300\ \mathrm{K}$，$k_B T = 0.02585\ \mathrm{eV}$，$h = 6.626 \times 10^{-34}\ \mathrm{J\cdot s}$）：
   $$N_c = 2\left(\frac{2\pi \times 1.08 \times 9.109 \times 10^{-31} \times 1.381 \times 10^{-23} \times 300}{(6.626 \times 10^{-34})^2}\right)^{3/2} \approx 2.82 \times 10^{25}\ \mathrm{m}^{-3} = 2.82 \times 10^{19}\ \mathrm{cm}^{-3}$$
   $$N_v = N_c \left(\frac{0.81}{1.08}\right)^{3/2} = 2.816 \times 10^{19} \times (0.75)^{3/2} \approx 1.83 \times 10^{19}\ \mathrm{cm}^{-3}$$
   $$n_i = \sqrt{N_c N_v}\,\exp\!\left(-\frac{E_g}{2k_B T}\right) = \sqrt{2.816 \times 1.829} \times 10^{19} \times \exp\!\left(-\frac{1.12}{2 \times 0.02585}\right) \approx 8.88 \times 10^9\ \mathrm{cm}^{-3}$$
   $$E_{Fi} - E_m = \frac{3}{4} \times 25.85\ \mathrm{meV} \times \ln\frac{0.81}{1.08} \approx -5.58\ \mathrm{meV}$$
   （偏移量远小于 $E_g = 1120\ \mathrm{meV}$，故室温下本征费米能级极接近禁带正中。）
:::

#### 题型二：补偿半导体电中性方程与高温混合区求解

`CH06-KP2-05` 向硅单晶中同时掺入浓度为 $N_D = 4.0 \times 10^{16}\ \mathrm{cm}^{-3}$ 的磷（施主）与 $N_A = 1.0 \times 10^{16}\ \mathrm{cm}^{-3}$ 的硼（受主），设杂质均已完全电离：
1. 在室温（$T = 300\ \mathrm{K}$，$k_B T = 0.02585\ \mathrm{eV}$）下，取硅参数 $n_i = 1.0 \times 10^{10}\ \mathrm{cm}^{-3}$、$N_c = 2.8 \times 10^{19}\ \mathrm{cm}^{-3}$。判断该补偿半导体的导电类型，计算平衡电子浓度 $n_0$ 与平衡空穴浓度 $p_0$；
2. 计算室温下费米能级距导带底的距离 $E_c - E_F$ 以及高于本征费米能级的能量 $E_F - E_{Fi}$，检验非简并近似是否成立；
3. 若将样品升温至高温 $T = 680\ \mathrm{K}$（$k_B T = 0.0586\ \mathrm{eV}$），已知此时硅的本征载流子浓度升至 $n_i(680\ \mathrm{K}) = 2.0 \times 10^{16}\ \mathrm{cm}^{-3}$。精确联立电中性方程与质量作用定律，求此高温下的 $n_0$、$p_0$ 及 $E_F - E_{Fi}$。

::: details 思路提示
杂质全部电离时电中性条件为 $n_0 + N_A = p_0 + N_D$，结合 $p_0 = n_i^2 / n_0$ 消去 $p_0$ 得关于 $n_0$ 的一元二次方程 $n_0^2 - (N_D - N_A)n_0 - n_i^2 = 0$。室温下 $N_D - N_A \gg n_i$ 可直接简化，而高温下 $n_i$ 与 $N_D - N_A$ 同量级，必须取精确求根公式。
:::

::: details 参考答案与解析
**参考答案**：
1. $n$ 型；$n_0 = 3.0 \times 10^{16}\ \mathrm{cm}^{-3}$，$p_0 \approx 3.33 \times 10^3\ \mathrm{cm}^{-3}$；
2. $E_c - E_F \approx 0.177\ \mathrm{eV}$（$\approx 6.8 k_B T$，非简并近似成立），$E_F - E_{Fi} \approx 0.386\ \mathrm{eV}$；
3. $n_0 = 4.00 \times 10^{16}\ \mathrm{cm}^{-3}$，$p_0 = 1.00 \times 10^{16}\ \mathrm{cm}^{-3}$，$E_F - E_{Fi} \approx 0.041\ \mathrm{eV}$。

**解析**：
1. **室温平衡载流子浓度**：电中性方程 $n_0 + N_A = p_0 + N_D \implies n_0 - p_0 = N_D - N_A = 3.0 \times 10^{16}\ \mathrm{cm}^{-3} > 0$，表现为 **$n$ 型**补偿半导体。室温下 $N_D - N_A \gg n_i = 1.0 \times 10^{10}\ \mathrm{cm}^{-3}$，故：
   $$n_0 \approx N_D - N_A = 3.0 \times 10^{16}\ \mathrm{cm}^{-3}$$
   $$p_0 = \frac{n_i^2}{n_0} = \frac{(1.0 \times 10^{10})^2}{3.0 \times 10^{16}} \approx 3.33 \times 10^3\ \mathrm{cm}^{-3}$$

2. **室温费米能级位置**：
   $$E_c - E_F = k_B T \ln\frac{N_c}{n_0} = 0.02585 \times \ln\frac{2.8 \times 10^{19}}{3.0 \times 10^{16}} \approx 0.02585 \times 6.839 \approx 0.177\ \mathrm{eV}$$
   因为 $E_c - E_F \approx 6.8 k_B T \gg k_B T$（通常 $> 3 k_B T$ 即良好满足），非简并玻尔兹曼近似完全有效。又由 $n_0 = n_i e^{(E_F - E_{Fi})/(k_B T)}$：
   $$E_F - E_{Fi} = k_B T \ln\frac{n_0}{n_i} = 0.02585 \times \ln\left(3.0 \times 10^6\right) \approx 0.386\ \mathrm{eV}$$

3. **高温 $680\ \mathrm{K}$ 精确求解**：联立 $n_0 - p_0 = N_D - N_A$ 与 $n_0 p_0 = n_i^2$，得二次方程：
   $$n_0^2 - (N_D - N_A) n_0 - n_i^2 = 0$$
   取正根：
   $$n_0 = \frac{(N_D - N_A) + \sqrt{(N_D - N_A)^2 + 4 n_i^2}}{2} = \frac{3.0 + \sqrt{3.0^2 + 4 \times 2.0^2}}{2} \times 10^{16} = \frac{3.0 + 5.0}{2} \times 10^{16} = 4.00 \times 10^{16}\ \mathrm{cm}^{-3}$$
   $$p_0 = \frac{n_i^2}{n_0} = \frac{(2.0 \times 10^{16})^2}{4.00 \times 10^{16}} = 1.00 \times 10^{16}\ \mathrm{cm}^{-3}$$
   （校验：$n_0 - p_0 = 3.00 \times 10^{16}\ \mathrm{cm}^{-3} = N_D - N_A$。）此时费米能级已大幅落回本征费米能级附近：
   $$E_F - E_{Fi} = k_B T \ln\frac{n_0}{n_i} = 0.0586 \times \ln 2 \approx 0.041\ \mathrm{eV}$$
:::

#### 题型三：低温弱电离区电子浓度与费米能级推导

`CH06-KP2-06` 考虑仅掺施主（浓度 $N_D$，电离能 $\Delta E_D = E_c - E_D$）的非简并 $n$ 型半导体，已知施主能级自旋简并度 $g_D = 2$，处于低温弱电离区（忽略价带空穴 $p_0 \approx 0$）：
1. 写出施主能级被电子占据的几率 $f_D$ 及电离施主浓度 $N_D^+$ 的表达式；
2. 利用电中性条件 $n_0 = N_D^+$，在低温弱电离极限（$E_F - E_D \gg k_B T$）下，推导导带电子浓度 $n_0(T)$ 与费米能级 $E_F(T)$ 的解析表达式，并求出 $T \to 0\ \mathrm{K}$ 时费米能级的极限位置。

::: details 思路提示
一个中性施主能级可容纳 $1$ 个自旋向上或 $1$ 个自旋向下的电子（但因强库仑排斥不能同时容纳 $2$ 个），故占据几率分母指数项前带权重 $\frac{1}{g_D} = \frac{1}{2}$；电离施主浓度 $N_D^+ = N_D(1 - f_D)$。
:::

::: details 参考答案与解析
**参考答案**：
1. $f_D = \frac{1}{1 + \frac{1}{2}e^{(E_D - E_F)/(k_B T)}}$，$N_D^+ = \frac{N_D}{1 + 2 e^{(E_F - E_D)/(k_B T)}}$；
2. $n_0(T) \approx \sqrt{\frac{N_c N_D}{2}}\,\exp\!\left(-\frac{\Delta E_D}{2k_B T}\right)$，$E_F(T) \approx \frac{E_c + E_D}{2} + \frac{k_B T}{2}\ln\frac{N_D}{2N_c}$；$T \to 0\ \mathrm{K}$ 时 $E_F \to \frac{E_c + E_D}{2}$。

**解析**：
1. **施主统计分布**：施主中心有 $2$ 个等价自旋束缚态、$1$ 个空（电离）态，由巨正则配分函数给出束缚电子占据几率：
   $$f_D = \frac{2 e^{-(E_D - E_F)/(k_B T)}}{1 + 2 e^{-(E_D - E_F)/(k_B T)}} = \frac{1}{1 + \frac{1}{2} e^{(E_D - E_F)/(k_B T)}}$$
   因此已电离的施主浓度为：
   $$N_D^+ = N_D(1 - f_D) = \frac{N_D}{1 + 2 e^{(E_F - E_D)/(k_B T)}}$$

2. **低温弱电离区解**：忽略价带空穴，电中性条件为 $n_0 = N_D^+$：
   $$N_c \exp\!\left(-\frac{E_c - E_F}{k_B T}\right) = \frac{N_D}{1 + 2\exp\!\left(\frac{E_F - E_D}{k_B T}\right)}$$
   在低温弱电离区，$E_F$ 位于 $E_D$ 之上且满足 $E_F - E_D \gg k_B T$，分母中 $1$ 可忽略不计，于是：
   $$N_c e^{-(E_c - E_F)/(k_B T)} \approx \frac{N_D}{2} e^{-(E_F - E_D)/(k_B T)}$$
   整理含 $E_F$ 的指数项：
   $$\exp\!\left(\frac{2E_F - (E_c + E_D)}{k_B T}\right) = \frac{N_D}{2 N_c}$$
   两边取自然对数解得费米能级：
   $$E_F(T) = \frac{E_c + E_D}{2} + \frac{k_B T}{2}\ln\frac{N_D}{2N_c}$$
   当 $T \to 0\ \mathrm{K}$ 时，$k_B T \ln(N_D / 2N_c) \to 0$，故 $E_F(0) = \frac{E_c + E_D}{2}$（恰好位于导带底与施主能级的正中央）。将 $E_F(T)$ 代回 $n_0 = N_c e^{-(E_c - E_F)/(k_B T)}$ 即得：
   $$n_0(T) = \sqrt{\frac{N_c N_D}{2}}\,\exp\!\left(-\frac{E_c - E_D}{2k_B T}\right) = \sqrt{\frac{N_c N_D}{2}}\,\exp\!\left(-\frac{\Delta E_D}{2k_B T}\right)$$
   可见在 $\ln n_0\text{--}(1/T)$ 图中，低温弱电离区的斜率为 $-\frac{\Delta E_D}{2k_B}$（注意分母中的因子 $2$，若忽略补偿杂质则是激活能的一半）。
:::

---

### 知识点 3：电导率与霍尔效应

#### 概念选择与填空

`CH06-KP3-01`（单选）关于半导体中载流子迁移率 $\mu$ 随温度 $T$ 的变化规律及主要散射机制，下列说法正确的是（ ）。
A. 高温区以晶格声学声子散射为主，迁移率随温度升高按 $\mu_L \propto T^{3/2}$ 增大
B. 低温区以电离杂质散射为主，温度越低电子热运动速率越慢、受库仑偏转越强，因此迁移率按 $\mu_I \propto T^{3/2}$ 随温度升高而增大
C. 杂质浓度 $N_I$ 越高，电离杂质散射越弱，低温迁移率越高
D. 两种散射机制同时存在时，总迁移率等于两者直接相加 $\mu = \mu_L + \mu_I$

::: details 思路提示
区分声子散射（温度越高声子越多，散射越强）与库仑杂质散射（卢瑟福散射截面反比于动能平方，温度越高电子跑得越快越不易偏转），以及马西森定则是对散射率 $1/\tau$（即 $1/\mu$）相加。
:::

::: details 参考答案与解析
**参考答案**：B

**解析**：
- 晶格声学声子散射在高温主导：温度升高使声子数增多且电子热速率增大，导致 $\mu_L \propto T^{-3/2}$（A 错）；
- 电离杂质散射在低温主导：温度升高时电子热速率增大，穿过电离杂质库仑场的时间缩短、偏转角变小，故 $\mu_I \propto T^{3/2}/N_I$（B 对，C 错）；
- 总散射几率相加给出倒数求和 $\frac{1}{\mu} = \frac{1}{\mu_L} + \frac{1}{\mu_I}$（D 错），因此半导体迁移率随温度升高通常呈现先升后降的峰形曲线。
:::

---

`CH06-KP3-02`（填空）同时含电子（浓度 $n$，迁移率 $\mu_n$）和空穴（浓度 $p$，迁移率 $\mu_p$）的非简并半导体，其电导率 $\sigma =$ ____；在弱磁场且散射因子 $r_H \approx 1$ 时，双载流子霍尔系数为 $R_H =$ ____；当两类载流子浓度之比 $p/n =$ ____ 时，霍尔系数恰好等于零。

::: details 思路提示
电子与空穴沿相反方向漂移但电荷相反，两者对电导率同向相加；而在磁场洛伦兹力作用下两者向同侧偏转但电荷相反，因此对横向霍尔电场贡献相互抵消！
:::

::: details 参考答案与解析
**参考答案**：$e(n\mu_n + p\mu_p)$；$\frac{p\mu_p^2 - n\mu_n^2}{e(p\mu_p + n\mu_n)^2}$；$\left(\frac{\mu_n}{\mu_p}\right)^2$。

**解析**：电导率由电子和空穴漂移电流同向叠加给出 $\sigma = e(n\mu_n + p\mu_p)$。弱磁场下由横向总电流 $J_y = 0$ 解得双载流子霍尔系数：
$$R_H = \frac{p\mu_p^2 - n\mu_n^2}{e(p\mu_p + n\mu_n)^2}$$
令分子为零即得霍尔反号零点条件 $p\mu_p^2 = n\mu_n^2 \implies \frac{p}{n} = \left(\frac{\mu_n}{\mu_p}\right)^2$。
:::

---

`CH06-KP3-03`（单选）关于半导体电阻率 $\rho$ 随温度 $T$ 的变化特征，下列说法**错误**的是（ ）。
A. 在低温弱电离区，载流子浓度随温度升高呈指数增长，电阻率 $\rho$ 随温度升高而迅速减小
B. 在杂质饱和电离区，多数载流子浓度基本恒定（$n_0 \approx N_D$），而声子散射增强使迁移率下降，电阻率 $\rho$ 反而随温度升高而增大
C. 在高温本征区，本征激发使 $n_i \propto e^{-E_g/(2k_B T)}$ 剧增，电阻率 $\rho$ 随温度升高迅速减小
D. 掺杂半导体在所有温度区间内都严格表现出“温度越高、电阻率越低”的单调行为

::: details 思路提示
分别考察 $\sigma = e n_0(T) \mu(T)$ 在三个温区中 $n_0(T)$ 与 $\mu(T)$ 哪一个的变化占主导。
:::

::: details 参考答案与解析
**参考答案**：D

**解析**：在杂质饱和电离区（如室温附近常规掺杂硅），载流子浓度基本锁死在 $N_D$，此时声学声子散射使迁移率按 $T^{-3/2}$ 下降，因此电阻率 $\rho = (e N_D \mu)^{-1} \propto T^{3/2}$ 随温度升高而**增大**（局部呈现类金属正温度系数）。故 D 错误，A、B、C 均正确。
:::

#### 题型一：霍尔效应测算与双载流子霍尔反号

`CH06-KP3-04` 一长方体掺杂硅样品，厚度 $d = 0.50\ \mathrm{mm}$、宽度 $w = 4.0\ \mathrm{mm}$、沿电流方向两电压探针间距 $L = 10.0\ \mathrm{mm}$。室温下通入稳恒电流 $I = 2.0\ \mathrm{mA}$，垂直宽面施加磁感应强度 $B = 0.50\ \mathrm{T}$，测得纵向压降 $U_\parallel = 50.0\ \mathrm{mV}$，横向霍尔电压 $U_H = -1.25\ \mathrm{mV}$（符号按标准右手定则约定与 $R_H$ 同号）：
1. 判断样品的导电类型，计算样品的电阻率 $\rho$（单位：$\Omega\cdot\mathrm{cm}$）与电导率 $\sigma$（单位：$\mathrm{S/cm}$）；
2. 计算霍尔系数 $R_H$（单位：$\mathrm{cm^3/C}$）、多数载流子浓度（取霍尔因子 $r_H = 1$）与霍尔迁移率 $\mu_H$（单位：$\mathrm{cm^2/(V\cdot s)}$）；
3. 另取一块受主浓度为 $N_A$ 的 $p$ 型硅样品（杂质全电离），已知电子与空穴迁移率之比 $b = \mu_n / \mu_p = 3.0$。当样品加热进入混合导电区时，求霍尔系数 $R_H$ 由正转负（恰好为零）时，本征热激发产生的电子浓度 $n$ 与 $N_A$ 之比 $n / N_A$。

::: details 思路提示
注意区分纵向截面积 $S = w d$ 与霍尔公式中只含沿磁场方向的厚度 $d$（$U_H = R_H \frac{IB}{d}$）；第 3 问联立 $R_H = 0$ 条件 $p = b^2 n$ 与电中性条件 $p = n + N_A$。
:::

::: details 参考答案与解析
**参考答案**：
1. $n$ 型；$\rho = 0.50\ \Omega\cdot\mathrm{cm}$，$\sigma = 2.00\ \mathrm{S/cm}$；
2. $R_H = -625\ \mathrm{cm^3/C}$，$n \approx 1.00 \times 10^{16}\ \mathrm{cm}^{-3}$，$\mu_H = 1250\ \mathrm{cm^2/(V\cdot s)}$；
3. $n / N_A = \frac{1}{8} = 0.125$（此时 $p = \frac{9}{8}N_A$，仍以空穴为多数载流子）。

**解析**：
1. **导电类型、电阻率与电导率**：霍尔电压 $U_H < 0 \implies R_H < 0$，多数载流子为电子，故为 **$n$ 型**半导体。样品电阻 $R = \frac{U_\parallel}{I} = \frac{50.0\ \mathrm{mV}}{2.0\ \mathrm{mA}} = 25.0\ \Omega$，由 $R = \rho \frac{L}{w d}$：
   $$\rho = R \frac{w d}{L} = 25.0 \times \frac{0.40\ \mathrm{cm} \times 0.050\ \mathrm{cm}}{1.00\ \mathrm{cm}} = 0.50\ \Omega\cdot\mathrm{cm}$$
   $$\sigma = \frac{1}{\rho} = 2.00\ \mathrm{S/cm}$$

2. **霍尔系数、载流子浓度与迁移率**：由 $U_H = R_H \frac{IB}{d}$：
   $$R_H = \frac{U_H d}{IB} = \frac{-1.25 \times 10^{-3}\ \mathrm{V} \times 0.50 \times 10^{-3}\ \mathrm{m}}{2.0 \times 10^{-3}\ \mathrm{A} \times 0.50\ \mathrm{T}} = -6.25 \times 10^{-4}\ \mathrm{m^3/C} = -625\ \mathrm{cm^3/C}$$
   单载流子（$r_H = 1$）下电子浓度与霍尔迁移率：
   $$n = \frac{1}{e \lvert R_H\rvert} = \frac{1}{1.602 \times 10^{-19}\ \mathrm{C} \times 625\ \mathrm{cm^3/C}} \approx 1.00 \times 10^{16}\ \mathrm{cm}^{-3}$$
   $$\mu_H = \lvert R_H\rvert \sigma = 625\ \mathrm{cm^3/C} \times 2.00\ \mathrm{S/cm} = 1250\ \mathrm{cm^2/(V\cdot s)}$$

3. **$p$ 型半导体高温霍尔反号**：双载流子霍尔系数为零的条件为：
   $$p \mu_p^2 - n \mu_n^2 = 0 \implies p = \left(\frac{\mu_n}{\mu_p}\right)^2 n = b^2 n = 9 n$$
   结合电中性条件 $p = n + N_A$：
   $$n + N_A = 9 n \implies \frac{n}{N_A} = \frac{1}{b^2 - 1} = \frac{1}{8} = 0.125$$
   可见由于电子迁移率显著大于空穴迁移率，当电子浓度仅为受主浓度的 $\frac{1}{8}$（空穴浓度仍为电子浓度的 $9$ 倍）时，霍尔系数便已由正翻转为负。
:::

#### 题型二：半导体最小电导率极值分析

`CH06-KP3-05` 某恒温非简并半导体的本征载流子浓度为 $n_i$，电子与空穴迁移率分别为 $\mu_n$、$\mu_p$（通常 $\mu_n > \mu_p$）：
1. 利用质量作用定律 $n_0 p_0 = n_i^2$，证明通过调节掺杂可获得的最小电导率为 $\sigma_{\min} = 2 e n_i \sqrt{\mu_n \mu_p}$，求出取得最小电导率（最大电阻率）时的 $n_0$、$p_0$ 并判断其导电类型；
2. 已知室温硅的 $n_i = 1.0 \times 10^{10}\ \mathrm{cm}^{-3}$、$\mu_n = 1400\ \mathrm{cm^2/(V\cdot s)}$、$\mu_p = 450\ \mathrm{cm^2/(V\cdot s)}$，分别计算室温本征硅电阻率 $\rho_i$、理论最大电阻率 $\rho_{\max}$ 及实现最大电阻率所需掺入的净受主浓度 $N_A$。

::: details 思路提示
对 $\sigma = e(n_0 \mu_n + \frac{n_i^2}{n_0}\mu_p)$ 直接应用均值不等式 $a + b \ge 2\sqrt{ab}$（或对 $n_0$ 求一阶导数为零）即可一步求出极值！
:::

::: details 参考答案与解析
**参考答案**：
1. $\sigma_{\min} = 2 e n_i \sqrt{\mu_n \mu_p}$，此时 $n_0 = n_i\sqrt{\frac{\mu_p}{\mu_n}}$、$p_0 = n_i\sqrt{\frac{\mu_n}{\mu_p}}$，因 $\mu_n > \mu_p$ 故 $p_0 > n_0$，呈轻微 **$p$ 型**；
2. $\rho_i \approx 3.37 \times 10^5\ \Omega\cdot\mathrm{cm}$，$\rho_{\max} \approx 3.93 \times 10^5\ \Omega\cdot\mathrm{cm}$，$N_A \approx 1.20 \times 10^{10}\ \mathrm{cm}^{-3}$。

**解析**：
1. **最小电导率证明**：将 $p_0 = n_i^2 / n_0$ 代入电导率公式，并由均值不等式：
   $$\sigma = e\left(n_0 \mu_n + \frac{n_i^2}{n_0}\mu_p\right) \ge 2 e \sqrt{n_0 \mu_n \cdot \frac{n_i^2}{n_0}\mu_p} = 2 e n_i \sqrt{\mu_n \mu_p}$$
   等号成立当且仅当两项相等 $n_0 \mu_n = p_0 \mu_p$，结合 $n_0 p_0 = n_i^2$ 解得：
   $$n_0 = n_i\sqrt{\frac{\mu_p}{\mu_n}}, \qquad p_0 = n_i\sqrt{\frac{\mu_n}{\mu_p}}$$
   因 $\mu_n > \mu_p$，故 $p_0 > n_i > n_0$，即取得最高电阻率的并非严格本征半导体，而是轻微掺受主的 **$p$ 型**半导体（以迁移率较低的空穴替代部分高迁移率电子）。

2. **室温硅数值计算**：
   - 本征硅电导率与电阻率：
     $$\sigma_i = e n_i (\mu_n + \mu_p) = 1.602 \times 10^{-19} \times 1.0 \times 10^{10} \times (1400 + 450) \approx 2.96 \times 10^{-6}\ \mathrm{S/cm}$$
     $$\rho_i = \frac{1}{\sigma_i} \approx 3.37 \times 10^5\ \Omega\cdot\mathrm{cm}$$
   - 最小电导率与最大电阻率：
     $$\sigma_{\min} = 2 \times 1.602 \times 10^{-19} \times 1.0 \times 10^{10} \times \sqrt{1400 \times 450} \approx 2.54 \times 10^{-6}\ \mathrm{S/cm}$$
     $$\rho_{\max} = \frac{1}{\sigma_{\min}} \approx 3.93 \times 10^5\ \Omega\cdot\mathrm{cm}$$
   - 所需净受主浓度：
     $$n_0 = 1.0 \times 10^{10}\sqrt{\frac{450}{1400}} \approx 5.67 \times 10^9\ \mathrm{cm}^{-3}, \qquad p_0 = 1.0 \times 10^{10}\sqrt{\frac{1400}{450}} \approx 1.76 \times 10^{10}\ \mathrm{cm}^{-3}$$
     $$N_A = p_0 - n_0 \approx 1.20 \times 10^{10}\ \mathrm{cm}^{-3}$$
:::

---

### 知识点 4：PN 结、MIS 结构、异质结与非晶态半导体

![热平衡 PN 结能带图与 p 型 MIS 结构强反型能带图](/figures/ch06-pn-mis-bands.svg)

<p class="fig-caption">图 6-2 热平衡突变 PN 结能带图（左）及 <em>p</em> 型 MIS 结构在强反型状态下的能带图（右）</p>

#### 概念选择与填空

`CH06-KP4-01`（单选）关于 PN 结的能带结构与偏压响应，下列说法**错误**的是（ ）。
A. 热平衡时 P 区与 N 区的费米能级平齐，空间电荷区中内建电场由带正电施主离子的 N 区指向带负电受主离子的 P 区
B. 热平衡下穿过冶金结面的扩散电流与漂移电流大小相等、方向相反，净电流为零
C. 在单边突变结（如 $N_A \gg N_D$）中，耗尽层宽度几乎全部向轻掺杂的 N 区一侧延伸
D. 给 PN 结施加正向偏压（P 区接正极、N 区接负极）时，势垒高度增大、耗尽层变宽，电流迅速减小

::: details 思路提示
检查正向偏压产生的外电场方向与内建电场方向是同向增强还是反向削弱。
:::

::: details 参考答案与解析
**参考答案**：D

**解析**：PN 结内建电场由 N 区指向 P 区。施加正向偏压 $V > 0$（P 正 N 负）时，外电场由 P 指向 N，部分抵消内建电场，使势垒高度由 $eV_{bi}$ 降至 $e(V_{bi} - V)$、耗尽层变窄，多子扩散势垒大幅降低从而产生指数增长的正向扩散电流；反向偏压才使势垒增高、耗尽层变宽。A、B、C 均正确。
:::

---

`CH06-KP4-02`（填空）以 $p$ 型半导体为衬底的理想 MIS 结构，随着金属栅极电压 $V_G$ 从负值连续增大至正值，半导体表面空间电荷区依次呈现 ____、____ 和 ____ 三种状态；当表面电子浓度等于体内空穴浓度时达到**强反型**阈值，此时表面势满足 $\psi_s =$ ____（用体内费米势 $\phi_F = \frac{E_{Fi} - E_F}{e}$ 表示）。

::: details 思路提示
回忆图 6-2 右图：$p$ 型体内 $E_F$ 低于 $E_{Fi}$ 距离 $e\phi_F$，要使表面电子浓度等于体内空穴浓度，必须让表面 $E_F$ 高于表面 $E_{Fi}$ 同样距离 $e\phi_F$。
:::

::: details 参考答案与解析
**参考答案**：积累；耗尽；反型；$2\phi_F$。

**解析**：对 $p$ 型衬底，$V_G < 0$ 吸引空穴聚集于界面（积累）；小正压排斥空穴暴露负受主离子（耗尽）；栅压足够大时能带剧烈向下弯曲使表面 $E_{Fi}$ 落至 $E_F$ 以下（反型）。当表面弯曲量 $e\psi_s = 2e\phi_F$（即 $\psi_s = 2\phi_F$）时，表面 $E_F - E_{Fi}(0) = E_{Fi}(\text{bulk}) - E_F = e\phi_F$，表面电子浓度 $n_s = n_i e^{e\phi_F/(k_B T)} = p_{\text{bulk}} = N_A$，标志着强反型开启。
:::

---

`CH06-KP4-03`（单选）关于半导体异质结与非晶态半导体的基本概念，下列说法**错误**的是（ ）。
A. 由两种不同带隙半导体形成的异质结在界面处一般存在导带带阶 $\Delta E_c$ 与价带带阶 $\Delta E_v$
B. 调制掺杂 $\mathrm{AlGaAs/GaAs}$ 异质结把电离施主留在宽带隙侧，电子落入窄带隙无掺杂界面势阱中，显著削弱电离杂质散射从而获得极高低温迁移率
C. 非晶态半导体虽缺乏晶体的长程周期有序，但保留了与晶体相似的近程化学键有序（如非晶硅的四面体配位），因此仍存在类价带、类导带及光学带隙
D. 非晶态半导体因长程无序引入的带尾态属于完全非局域的扩展态，因此其室温载流子迁移率远高于单晶半导体

::: details 思路提示
辨析非晶态半导体中“长程无序”引发的安德森局域化（带尾局域态与迁移率边）对载流子迁移率的影响。
:::

::: details 参考答案与解析
**参考答案**：D

**解析**：非晶态半导体中键长、键角的随机涨落（长程无序）在带边引入大量**带尾局域态**，迁移率边将能带深处的扩展态与带尾局域态隔开。处于局域态中的载流子波函数局域在有限空间内，只能依靠声子辅助热激活跳跃导电，迁移率比单晶半导体低几个数量级。A、B、C 均正确。
:::

#### 题型一：突变 PN 结内建电势差、耗尽层宽度与结电容计算

`CH06-KP4-04` 室温（$300\ \mathrm{K}$）下一硅突变 PN 结，P 区受主浓度 $N_A = 1.0 \times 10^{17}\ \mathrm{cm}^{-3}$，N 区施主浓度 $N_D = 1.0 \times 10^{16}\ \mathrm{cm}^{-3}$，取 $\varepsilon_r = 11.7$、$n_i = 1.0 \times 10^{10}\ \mathrm{cm}^{-3}$、$k_B T / e = 0.02585\ \mathrm{V}$。在耗尽近似下求解：
1. 推导并计算热平衡内建电势差 $V_{bi}$；
2. 利用一维泊松方程与电中性条件 $N_A x_p = N_D x_n$，推导热平衡总耗尽层宽度 $W$ 和结面最大电场强度 $\lvert\mathcal{E}_{\max}\rvert$，计算 $W$、$x_p$、$x_n$（单位：$\mu\mathrm{m}$）与 $\lvert\mathcal{E}_{\max}\rvert$（单位：$\mathrm{V/cm}$）；
3. 若施加 $V_R = 4.0\ \mathrm{V}$ 反向偏压，计算此时的总耗尽层宽度 $W(V_R)$ 及单位面积势垒结电容 $C_j$（单位：$\mathrm{nF/cm^2}$）。

::: details 思路提示
由 P 区 $p_{p0} = N_A = n_i e^{(E_{Fi,p} - E_F)/(k_B T)}$ 和 N 区 $n_{n0} = N_D = n_i e^{(E_F - E_{Fi,n})/(k_B T)}$ 相乘直接得 $eV_{bi} = E_{Fi,p} - E_{Fi,n}$；一维泊松方程 $\frac{\mathrm{d}\mathcal{E}}{\mathrm{d}x} = \frac{\rho(x)}{\varepsilon_0\varepsilon_r}$ 给出三角形电场分布，积分面积即总电势降 $V_{bi} = \frac{1}{2}\lvert\mathcal{E}_{\max}\rvert W$！
:::

::: details 参考答案与解析
**参考答案**：
1. $V_{bi} = \frac{k_B T}{e}\ln\frac{N_A N_D}{n_i^2} \approx 0.774\ \mathrm{V}$；
2. $W(0) \approx 0.332\ \mu\mathrm{m}$，$x_p \approx 0.0302\ \mu\mathrm{m}$，$x_n \approx 0.302\ \mu\mathrm{m}$，$\lvert\mathcal{E}_{\max}\rvert \approx 4.67 \times 10^4\ \mathrm{V/cm}$；
3. $W(V_R) \approx 0.824\ \mu\mathrm{m}$，$C_j \approx 12.6\ \mathrm{nF/cm^2}$。

**解析**：
1. **内建电势差推导与计算**：热平衡下全结费米能级平齐，结两侧本征能级差即内建势垒高度 $eV_{bi} = E_{Fi,p} - E_{Fi,n}$：
   $$N_A N_D = p_{p0} n_{n0} = n_i^2 \exp\!\left(\frac{E_{Fi,p} - E_{Fi,n}}{k_B T}\right) = n_i^2 e^{eV_{bi}/(k_B T)} \implies V_{bi} = \frac{k_B T}{e}\ln\frac{N_A N_D}{n_i^2}$$
   代入数值：
   $$V_{bi} = 0.02585 \times \ln\frac{1.0 \times 10^{17} \times 1.0 \times 10^{16}}{(1.0 \times 10^{10})^2} = 0.02585 \times \ln\left(10^{13}\right) \approx 0.774\ \mathrm{V}$$

2. **耗尽层宽度与最大电场**：耗尽近似下，P 侧（$-x_p \le x < 0$）电荷密度 $\rho = -e N_A$，N 侧（$0 < x \le x_n$）电荷密度 $\rho = +e N_D$。对泊松方程 $\frac{\mathrm{d}\mathcal{E}}{\mathrm{d}x} = \frac{\rho}{\varepsilon_0\varepsilon_r}$ 积分（边界 $\mathcal{E}(-x_p) = \mathcal{E}(x_n) = 0$）：
   $$\mathcal{E}(x) = -\frac{e N_A}{\varepsilon_0\varepsilon_r}(x + x_p) \quad (-x_p \le x \le 0), \qquad \mathcal{E}(x) = -\frac{e N_D}{\varepsilon_0\varepsilon_r}(x_n - x) \quad (0 \le x \le x_n)$$
   $x = 0$ 处电场连续即得电中性条件 $N_A x_p = N_D x_n$，且最大电场大小 $\lvert\mathcal{E}_{\max}\rvert = \frac{e N_A x_p}{\varepsilon_0\varepsilon_r} = \frac{e N_D x_n}{\varepsilon_0\varepsilon_r}$。电场为三角形分布，总电势降等于三角形面积：
   $$V_{bi} = \frac{1}{2}\lvert\mathcal{E}_{\max}\rvert (x_p + x_n) = \frac{e}{2\varepsilon_0\varepsilon_r} N_D x_n W$$
   结合 $x_n = \frac{N_A}{N_A + N_D}W$ 与 $x_p = \frac{N_D}{N_A + N_D}W$，解得：
   $$W = \sqrt{\frac{2\varepsilon_0\varepsilon_r}{e}\left(\frac{1}{N_A} + \frac{1}{N_D}\right)V_{bi}}$$
   代入国际单位（$\varepsilon_0\varepsilon_r = 11.7 \times 8.854 \times 10^{-12} = 1.036 \times 10^{-10}\ \mathrm{F/m}$，$N_A = 10^{23}\ \mathrm{m}^{-3}$，$N_D = 10^{22}\ \mathrm{m}^{-3}$）：
   $$W(0) = \sqrt{\frac{2 \times 1.036 \times 10^{-10}}{1.602 \times 10^{-19}}\left(10^{-23} + 10^{-22}\right) \times 0.774} \approx 3.32 \times 10^{-7}\ \mathrm{m} = 0.332\ \mu\mathrm{m}$$
   $$x_p = \frac{1}{11}W(0) \approx 0.0302\ \mu\mathrm{m}, \qquad x_n = \frac{10}{11}W(0) \approx 0.302\ \mu\mathrm{m}$$
   （可见耗尽区向低掺杂 N 区延伸的深度是重掺杂 P 区的 $10$ 倍。）
   $$\lvert\mathcal{E}_{\max}\rvert = \frac{2 V_{bi}}{W(0)} = \frac{2 \times 0.774\ \mathrm{V}}{3.32 \times 10^{-5}\ \mathrm{cm}} \approx 4.67 \times 10^4\ \mathrm{V/cm}$$

3. **反偏 $V_R = 4.0\ \mathrm{V}$ 下的耗尽层宽度与结电容**：反偏下势垒总压降变为 $V_{bi} + V_R = 4.774\ \mathrm{V}$：
   $$W(V_R) = W(0)\sqrt{\frac{V_{bi} + V_R}{V_{bi}}} = 0.332 \times \sqrt{\frac{4.774}{0.774}} \approx 0.824\ \mu\mathrm{m}$$
   单位面积势垒电容（等效平行板电容器）：
   $$C_j = \frac{\varepsilon_0\varepsilon_r}{W(V_R)} = \frac{1.036 \times 10^{-10}\ \mathrm{F/m}}{8.24 \times 10^{-7}\ \mathrm{m}} \approx 1.26 \times 10^{-4}\ \mathrm{F/m^2} = 12.6\ \mathrm{nF/cm^2}$$
:::

#### 题型二：异质结安德森能带排列与 MIS 强反型计算

`CH06-KP4-05` 
1. 某锐利异质结由宽带隙材料 $\mathrm{Al_{0.3}Ga_{0.7}As}$（电子亲和能 $\chi_1 = 3.74\ \mathrm{eV}$，带隙 $E_{g1} = 1.80\ \mathrm{eV}$）与窄带隙材料 $\mathrm{GaAs}$（电子亲和能 $\chi_2 = 4.07\ \mathrm{eV}$，带隙 $E_{g2} = 1.42\ \mathrm{eV}$）组成。根据安德森电子亲和能定则，计算界面处的导带带阶 $\Delta E_c$ 与价带带阶 $\Delta E_v$，判断该异质结的能带排列类型，并说明调制掺杂如何产生高迁移率二维电子气；
2. 对室温下受主浓度 $N_A = 1.0 \times 10^{16}\ \mathrm{cm}^{-3}$ 的 $p$ 型硅衬底理想 MIS 结构（$\varepsilon_r = 11.7$，$n_i = 1.0 \times 10^{10}\ \mathrm{cm}^{-3}$，$k_B T/e = 0.02585\ \mathrm{V}$），计算体内费米势 $\phi_F$、强反型开启表面势 $\psi_{s,\text{inv}} = 2\phi_F$ 以及表面最大耗尽层宽度 $W_{\max}$。

::: details 思路提示
安德森定则要求界面处真空能级连续，故导带底相对真空能级的深度直接等于各自电子亲和能 $\chi_1, \chi_2$，价带顶相对真空能级深度为 $\chi_i + E_{gi}$；MIS 强反型时由一维耗尽区泊松方程直接给出 $W_{\max} = \sqrt{\frac{2\varepsilon_0\varepsilon_r (2\phi_F)}{e N_A}}$。
:::

::: details 参考答案与解析
**参考答案**：
1. $\Delta E_c = 0.33\ \mathrm{eV}$，$\Delta E_v = 0.05\ \mathrm{eV}$，属于 **I 型（跨立式）异质结**；
2. $\phi_F \approx 0.357\ \mathrm{V}$，$\psi_{s,\text{inv}} \approx 0.714\ \mathrm{V}$，$W_{\max} \approx 0.304\ \mu\mathrm{m}$。

**解析**：
1. **异质结带阶与排列类型**：界面处真空能级连续，两侧导带底距真空能级分别为 $\chi_1 = 3.74\ \mathrm{eV}$ 与 $\chi_2 = 4.07\ \mathrm{eV}$，故导带带阶：
   $$\Delta E_c = \chi_2 - \chi_1 = 4.07 - 3.74 = 0.33\ \mathrm{eV}$$
   两侧价带顶距真空能级分别为 $\chi_1 + E_{g1} = 5.54\ \mathrm{eV}$ 与 $\chi_2 + E_{g2} = 5.49\ \mathrm{eV}$，故价带带阶：
   $$\Delta E_v = (\chi_1 + E_{g1}) - (\chi_2 + E_{g2}) = (E_{g1} - E_{g2}) - \Delta E_c = (1.80 - 1.42) - 0.33 = 0.05\ \mathrm{eV}$$
   由于窄带隙 $\mathrm{GaAs}$ 的导带底低于 $\mathrm{AlGaAs}$ 且价带顶高于 $\mathrm{AlGaAs}$（整个窄带隙完全嵌于宽带隙之内），该结构属于 **I 型（跨立式）异质结**。当仅在宽带隙 $\mathrm{AlGaAs}$ 侧掺杂施主而 $\mathrm{GaAs}$ 侧保持本征（调制掺杂）时，电子自发跨过界面落入低能量的 $\mathrm{GaAs}$ 侧，并在界面静电吸引下局域于纳米厚度的三角形量子势阱中形成**二维电子气（2DEG）**；由于电子与留在 $\mathrm{AlGaAs}$ 侧的带正电电离施主实现了空间分离，低温下的电离杂质散射被大幅削弱，从而获得极高的电子迁移率。

2. **$p$ 型硅 MIS 强反型参量**：
   $$\phi_F = \frac{k_B T}{e}\ln\frac{N_A}{n_i} = 0.02585 \times \ln\frac{1.0 \times 10^{16}}{1.0 \times 10^{10}} = 0.02585 \times \ln(10^6) \approx 0.357\ \mathrm{V}$$
   强反型开启时的表面势：
   $$\psi_{s,\text{inv}} = 2\phi_F \approx 0.714\ \mathrm{V}$$
   强反型后栅压继续升高所增加的电荷主要由薄反型电子层承担，耗尽层宽度基本钉扎在最大值 $W_{\max}$：
   $$W_{\max} = \sqrt{\frac{2\varepsilon_0\varepsilon_r (2\phi_F)}{e N_A}} = \sqrt{\frac{2 \times 11.7 \times 8.854 \times 10^{-12} \times 0.714}{1.602 \times 10^{-19} \times 1.0 \times 10^{22}}} \approx 3.04 \times 10^{-7}\ \mathrm{m} = 0.304\ \mu\mathrm{m}$$
:::
