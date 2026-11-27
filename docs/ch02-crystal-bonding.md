# 第二章 晶体的结合

::: info 教学大纲（建议 3 学时）
- 2.1 晶体的结合类型（离子、共价、金属、分子、氢键）与原子电负性
- 2.2 结合力与结合能的一般性质（吸引势、排斥势、平衡间距与体弹性模量）
- 2.3 离子晶体的结合能（马德隆常数、玻恩-兰德/玻恩-梅耶势、玻恩-哈伯循环）
- 2.4 非极性分子晶体的结合能（范德瓦尔斯力、伦纳德-琼斯势）
- 2.5 元素与化合物晶体结合的规律
:::

::: tip 核心概念与模型
**1. 五种基本结合类型与电负性规律**

| 结合类型 | 典型晶体 | 结合机制 | 方向性与饱和性 | 典型结构与物理特性 |
| :--- | :--- | :--- | :---: | :--- |
| 离子键 | NaCl、CsCl、MgO | 电负性差大，正负离子静电库仑吸引 | 无 | 高配位数（6/8），熔点高、固态绝缘、熔融导电 |
| 共价键 | 金刚石、Si、Ge | 相邻原子共享价电子对（如 $sp^3$ 杂化） | 强 | 低配位数（4，致密度 $34\%$），硬度高，半导体/绝缘体 |
| 金属键 | Cu、Na、Fe | 价电子公有化，正离子实浸没于自由电子气 | 无 | 密堆积（fcc/hcp/bcc），导电导热与延展性好 |
| 分子键（范德瓦尔斯） | Ne、Ar、Kr、Xe | 闭壳层原子瞬时偶极—诱导偶极吸引（$-r^{-6}$） | 无 | fcc 密堆积，结合能最弱（$\sim 0.01\text{–}0.1\ \mathrm{eV}$），低熔沸点 |
| 氢键 | 冰（$\mathrm{H_2O}$）、HF | 氢原子与强电负性小原子（F、O、N）静电吸引 | 有 | 键能介于分子键与共价键之间，结构较疏松 |

- **电负性规律**：同周期从左到右增大，同族从上到下减小。等电子 $A^{N}B^{8-N}$ 序列（如 $\mathrm{Ge} \to \mathrm{GaAs} \to \mathrm{ZnSe} \to \mathrm{CuBr}$）中，电负性差增大 $\implies$ 离子性增强、共价性减弱、禁带宽度增大。

**2. 结合能、结合力与体弹性模量的通用模型**
- **核心近似**：晶体结合势能 = 长程吸引势 + 短程泡利排斥势（源于闭壳层电子云交叠时泡利不相容原理迫使电子跃迁至高能态），例如 $u(r) = -\frac{A}{r^m} + \frac{B}{r^n}$（稳定平衡要求 $n > m > 0$）。
- **结合能定义**：$W = -U(R_0) > 0$（拆散晶体为无穷远孤立原子或离子所需能量）。
- **平衡条件与断裂点**：平衡间距 $R_0$ 满足 $\left.\frac{\mathrm{d}U}{\mathrm{d}r}\right|_{R_0} = 0$；最大结合力（理论抗拉极限）位于势能拐点 $\left.\frac{\mathrm{d}^2 U}{\mathrm{d}r^2}\right|_{r_m} = 0$。
- **体弹性模量通用公式**（$T=0\ \mathrm{K}$，忽略零点能，设体积 $V = c N r^3$）：
  $$K = \frac{1}{\beta} = V_0\left.\frac{\mathrm{d}^2 U}{\mathrm{d}V^2}\right|_{V_0} = \frac{R_0^2}{9 V_0}\left.\frac{\mathrm{d}^2 U}{\mathrm{d}r^2}\right|_{R_0}$$
  （其中 $\beta$ 为等温压缩率；NaCl 型 $V_0/N = 2R_0^3$，sc 型 $V_0/N = R_0^3$，fcc 型 $V_0/N = R_0^3/\sqrt{2}$。）

**3. 离子晶体结合能**
- **幂次排斥（玻恩-兰德模型）**：$N$ 对正负离子总势能 $U(r) = N\left(-\frac{\alpha q^2}{4\pi\varepsilon_0 r} + \frac{B}{r^n}\right)$。
  $$U(R_0) = -\frac{N\alpha q^2}{4\pi\varepsilon_0 R_0}\left(1 - \frac{1}{n}\right), \qquad K_{\mathrm{NaCl}} = \frac{(n-1)\alpha q^2}{72\pi\varepsilon_0 R_0^4}$$
- **指数排斥（玻恩-梅耶模型）**：$U(r) = N\left(-\frac{\alpha q^2}{4\pi\varepsilon_0 r} + z\lambda e^{-r/\rho}\right)$，平衡时 $U(R_0) = -\frac{N\alpha q^2}{4\pi\varepsilon_0 R_0}\left(1 - \frac{\rho}{R_0}\right)$。
- **马德隆常数 $\alpha$**：仅取决于晶体几何结构（一维等距链 $2\ln 2 \approx 1.386$；NaCl 型 $1.7476$；CsCl 型 $1.7627$；闪锌矿型 $1.6381$）。
- **玻恩-哈伯循环**：$W_{\text{离子}} = W_{\text{原子}} + I - E_A$（$I$ 为金属电离能，$E_A$ 为卤素电子亲和能）。

**4. 非极性分子晶体结合能（伦纳德-琼斯 6-12 势）**
- 两原子对势：$u(r) = 4\varepsilon\left[\left(\frac{\sigma}{r}\right)^{12} - \left(\frac{\sigma}{r}\right)^6\right]$；晶体总势能（注意避免重复计数乘 $\frac{1}{2}$）：
  $$U(R) = 2N\varepsilon\left[A_{12}\left(\frac{\sigma}{R}\right)^{12} - A_6\left(\frac{\sigma}{R}\right)^6\right]$$
- 平衡间距与单原子结合能（fcc 晶格求和常数 $A_6 = 14.45,\ A_{12} = 12.13$）：
  $$\frac{R_0}{\sigma} = \left(\frac{2A_{12}}{A_6}\right)^{1/6} \approx 1.090, \qquad w = -\frac{U(R_0)}{N} = \frac{1}{2}\varepsilon\frac{A_6^2}{A_{12}} \approx 8.61\varepsilon$$
:::

![结合势能曲线与一维马德隆求和](/figures/ch02-bonding-potential.svg)

<p class="fig-caption">图 2-1 原子间结合势能、结合力曲线及一维等距正负离子链马德隆求和示意</p>

## 习题及参考解答

### 知识点 1：晶体结合类型与电负性规律

#### 概念选择与填空

`CH02-KP1-01`（单选）在五种基本晶体结合键中，具有明显**方向性**与**饱和性**的是（ ）。
A. 离子键与金属键
B. 共价键与氢键
C. 金属键与范德瓦尔斯键
D. 离子键与范德瓦尔斯键

::: details 思路提示
方向性源于电子云轨道杂化（如 $sp^3$）或质子局域桥接；球对称静电作用（离子、金属、范德瓦尔斯）没有方向性。
:::

::: details 参考答案与解析
**参考答案**：B

**解析**：共价键依赖共享电子对的轨道最大重叠（如金刚石 $sp^3$ 四面体键），具有强方向性和饱和性；氢键中质子体积小且沿电负性原子连线形成局域作用，同样具有方向性和饱和性。离子键、金属键与范德瓦尔斯键均为无方向性的中心力作用，倾向形成高配位数密堆积。
:::

---

`CH02-KP1-02`（单选）金属铜（fcc）的致密度达 $74\%$，而单晶硅（金刚石结构）的致密度仅为 $34\%$，其根本物理原因是（ ）。
A. 硅原子的原子量小于铜原子
B. 硅晶体的金属键强度弱于铜晶体
C. 硅原子间以 $sp^3$ 杂化共价键结合，键的强方向性与饱和性将配位数限制为 $4$
D. 硅晶体中范德瓦尔斯排斥力异常强烈

::: details 思路提示
从结合键的方向性与饱和性对配位数的约束切入。
:::

::: details 参考答案与解析
**参考答案**：C

**解析**：金属键无方向性、无饱和性，原子按刚球密堆积排列以尽可能降低势能，配位数达 $12$（致密度 $74\%$）。硅为四价元素，形成 $sp^3$ 杂化正四面体共价键，每个原子只能与 $4$ 个最近邻成键，配位数仅为 $4$，因而结构疏松、致密度仅 $34\%$。
:::

---

`CH02-KP1-03`（填空）按同周期等电子化合物序列 $\mathrm{Ge} \to \mathrm{GaAs} \to \mathrm{ZnSe} \to \mathrm{CuBr}$ 变化时，两组成元素的电负性差逐渐 ____，化学键的离子性成分逐渐 ____，晶体的禁带宽度 $E_g$ 逐渐 ____。

::: details 思路提示
这四种晶体均含平均每原子 4 个价电子（Ⅳ 族、Ⅲ-Ⅴ 族、Ⅱ-Ⅵ 族、Ⅰ-Ⅶ 族）并采用金刚石/闪锌矿结构，观察元素在周期表中的左右跨度变化。
:::

::: details 参考答案与解析
**参考答案**：增大；增强（增大）；增大。

**解析**：从 $\mathrm{Ge}$（纯共价）到 $\mathrm{GaAs}$（Ⅲ-Ⅴ）、$\mathrm{ZnSe}$（Ⅱ-Ⅵ）再到 $\mathrm{CuBr}$（Ⅰ-Ⅶ），阴阳离子在周期表中的横向间距加大，电负性差单调增大，成键电子云逐渐向阴离子偏移，离子键成分增强，价电子束缚更紧，导致禁带宽度单调增大（常温 $E_g$ 约从 $0.67\ \mathrm{eV} \to 1.42\ \mathrm{eV} \to 2.7\ \mathrm{eV} \to 3.0\ \mathrm{eV}$）。
:::

---

`CH02-KP1-04`（单选）关于固态惰性气体（如固态氩 Ar）中的范德瓦尔斯结合，下列说法正确的是（ ）。
A. 其吸引力源于原子间永久电偶极矩的静电作用，势能按 $-r^{-3}$ 衰减
B. 其吸引力源于量子涨落产生的瞬时偶极矩与诱导偶极矩之间的作用，势能按 $-r^{-6}$ 衰减
C. 范德瓦尔斯键具有很强的方向性，因此惰性气体晶体多呈金刚石结构
D. 固态惰性气体的结合能通常在 $5\text{–}10\ \mathrm{eV}$ 量级，与离子晶体相当

::: details 思路提示
闭壳层惰性气体原子没有永久电偶极矩；结合范德瓦尔斯力（伦敦色散力）的量子机制与量级判断。
:::

::: details 参考答案与解析
**参考答案**：B

**解析**：惰性气体原子核外电子呈球对称闭壳层，平均电偶极矩为零，但电子瞬时涨落产生瞬时偶极矩 $\mathbf{p}_1$，在距离 $r$ 处产生电场 $E \propto p_1/r^3$，诱导邻近原子产生偶极矩 $\mathbf{p}_2 = \alpha E \propto r^{-3}$，二者相互作用能 $u \propto -\mathbf{p}_2\cdot\mathbf{E} \propto -r^{-6}$。该作用无方向性（形成 fcc 密堆积）且极弱（$\sim 0.01\text{–}0.1\ \mathrm{eV}$）。
:::

---

### 知识点 2：结合力一般性质与离子晶体结合能

#### 概念选择与填空

`CH02-KP2-01`（单选）离子晶体中正负离子靠库仑力相互吸引，却不会无限塌缩到一起。阻止离子间无限接近的短程排斥作用，其主要物理来源是（ ）。
A. 两个原子核之间的直接库仑排斥力
B. 闭壳层电子云开始交叠时，泡利不相容原理迫使部分电子跃迁到能量更高的未占据态
C. 离子热运动产生的惯性离心力
D. 万有引力与电磁力的抵消

::: details 思路提示
两离子靠近到平衡间距附近时，最先交叠的是外层闭壳电子云而非裸露的原子核。
:::

::: details 参考答案与解析
**参考答案**：B

**解析**：当正负离子的满壳层电子云发生空间交叠时，根据泡利不相容原理，相同量子态不能容纳多余电子，部分电子被迫提升至高能级，引起体系总能量急剧上升，宏观上表现为随距离迅速衰减的强短程排斥力（常以 $B/r^n$ 或 $\lambda e^{-r/\rho}$ 经验描述）。
:::

---

`CH02-KP2-02`（填空）离子晶体的马德隆常数 $\alpha$ 仅取决于晶体的 ____，与晶格常数和离子电荷大小 ____（填“有关”或“无关”）；一维无限长等距正负离子链的马德隆常数精确值为 ____。

::: details 思路提示
回顾马德隆常数定义 $\alpha = \sum_{j \ne 0} \frac{\pm 1}{p_{0j}}$，其中 $p_{0j} = r_{0j}/R$ 为无量纲距离比。
:::

::: details 参考答案与解析
**参考答案**：几何结构（晶体结构类型）；无关；$2\ln 2$（约 $1.386$）。

**解析**：马德隆常数是对无量纲相对距离 $p_{0j} = r_{0j}/R$ 的纯几何级数求和，因此只依赖晶格的几何构型。
:::

---

`CH02-KP2-03`（单选）若两原子间的相互作用势能为 $u(r) = -\frac{A}{r^m} + \frac{B}{r^n}$（$A, B > 0$），则该系统能形成稳定平衡态的条件以及最大吸引力（断裂点）所在位置分别为（ ）。
A. $n < m$；平衡位置 $r_0$ 处
B. $n > m$；平衡位置 $r_0$ 处
C. $n > m$；势能曲线的拐点 $r_m$ 处（满足 $\mathrm{d}^2 u/\mathrm{d}r^2 = 0$）
D. $n > m$；势能为零的位置 $r = \sigma$ 处

::: details 思路提示
稳定平衡要求在 $r_0$ 处 $\mathrm{d}^2 u/\mathrm{d}r^2 > 0$（即排斥势比吸引势随距离衰减更快）；作用力 $f(r) = -\mathrm{d}u/\mathrm{d}r$ 取极值时需满足 $\mathrm{d}f/\mathrm{d}r = -\mathrm{d}^2 u/\mathrm{d}r^2 = 0$。
:::

::: details 参考答案与解析
**参考答案**：C

**解析**：平衡点满足 $\frac{\mathrm{d}u}{\mathrm{d}r} = \frac{mA}{r_0^{m+1}} - \frac{nB}{r_0^{n+1}} = 0$，代入二阶导数得 $\left.\frac{\mathrm{d}^2 u}{\mathrm{d}r^2}\right|_{r_0} = \frac{m(n-m)A}{r_0^{m+2}}$，稳定极小值要求 $n > m$。作用力 $f(r) = -\frac{\mathrm{d}u}{\mathrm{d}r}$ 在 $r_0$ 处为零；拉伸时 $r > r_0$ 表现为吸引力，其极值出现在 $\frac{\mathrm{d}f}{\mathrm{d}r} = -\frac{\mathrm{d}^2 u}{\mathrm{d}r^2} = 0$ 即势能曲线拐点 $r_m$ 处（见图 2-1 左）。
:::

#### 题型一：马德隆常数、离子晶体结合能与玻恩-哈伯循环

`CH02-KP2-04` 考虑一维无限长等距交替排列的一价正负离子链，相邻正负离子间距为 $a$（见图 2-1 右）。
1. 求该一维离子链的马德隆常数 $\alpha$；
2. 若取幂次排斥势 $B/r^n$ 且排斥指数 $n = 9$，求平衡状态下每对离子的结合能占纯马德隆静电吸引能的百分比。

::: details 思路提示
任取一个正离子作为参考点 $0$，左右两侧距离 $ja$ 处各有 $1$ 个电荷为 $(-1)^j e$ 的离子；利用泰勒级数 $\ln(1+x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \cdots$ 在 $x=1$ 处求和。
:::

::: details 参考答案与解析
**参考答案**：
1. $\alpha = 2\ln 2 \approx 1.386$；
2. $\frac{8}{9} \approx 88.9\%$。

**解析**：
1. 取原点 $0$ 处正离子为参考，其余所有离子对它的静电势能为：
   $$u_{\mathrm{Mad}} = \frac{e^2}{4\pi\varepsilon_0 a} \cdot 2\left(-1 + \frac{1}{2} - \frac{1}{3} + \frac{1}{4} - \cdots\right) = -\frac{\alpha e^2}{4\pi\varepsilon_0 a}$$
   对比泰勒展开 $\ln(1+x) = \sum_{j=1}^{\infty}\frac{(-1)^{j-1}x^j}{j}$ 在 $x=1$ 处的收敛值 $\ln 2$，得：
   $$\alpha = 2\left(1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \cdots\right) = 2\ln 2 \approx 1.386$$
   （注意：求和时对称地成对计入左右第 $j$ 近邻，保持电荷中性。）

2. 由平衡条件 $\left.\frac{\mathrm{d}}{\mathrm{d}r}\left(-\frac{\alpha e^2}{4\pi\varepsilon_0 r} + \frac{B}{r^n}\right)\right|_{R_0} = 0$ 得 $\frac{B}{R_0^n} = \frac{1}{n}\frac{\alpha e^2}{4\pi\varepsilon_0 R_0}$，故每对离子结合能：
   $$w = -u(R_0) = \frac{\alpha e^2}{4\pi\varepsilon_0 R_0}\left(1 - \frac{1}{n}\right)$$
   当 $n = 9$ 时，结合能占马德隆静电吸引能的比例为 $1 - \frac{1}{9} = \frac{8}{9} \approx 88.9\%$（排斥能仅抵消约 $11.1\%$ 的静电吸引能）。
:::

---

`CH02-KP2-05` 已知 NaCl 晶体的平衡最近邻离子间距 $R_0 = 2.82\ \text{Å}$，马德隆常数 $\alpha = 1.7476$，实验测得体弹性模量 $K = 2.40 \times 10^{10}\ \mathrm{N/m^2}$。采用玻恩-兰德模型，总势能为 $U(r) = N\left(-\frac{\alpha e^2}{4\pi\varepsilon_0 r} + \frac{B}{r^n}\right)$。
1. 推导 NaCl 晶体平衡态下体弹性模量 $K$ 与排斥指数 $n$、平衡间距 $R_0$ 的关系式；
2. 计算排斥指数 $n$ 及每对离子的离子结合能 $w_{\text{离子}}$（单位：$\mathrm{eV}$）；
3. 已知 Na 的第一电离能 $I = 5.14\ \mathrm{eV}$，Cl 的电子亲和能 $E_A = 3.61\ \mathrm{eV}$，用玻恩-哈伯循环计算每对原子的原子结合能 $w_{\text{原子}}$。

::: details 思路提示
NaCl 惯用胞边长 $a = 2R_0$，含 $4$ 对离子，故每对离子所占体积 $V/N = a^3/4 = 2R_0^3$；利用通用公式 $K = \frac{R_0^2}{9V_0}\left.\frac{\mathrm{d}^2 U}{\mathrm{d}r^2}\right|_{R_0}$ 即可一步推出 $K$。
:::

::: details 参考答案与解析
**参考答案**：
1. $K = \frac{(n-1)\alpha e^2}{72\pi\varepsilon_0 R_0^4}$；
2. $n \approx 7.78$，$w_{\text{离子}} \approx 7.78\ \mathrm{eV}$；
3. $w_{\text{原子}} \approx 6.25\ \mathrm{eV}$。

**解析**：
1. **推导 $K$**：由平衡条件 $\left.\frac{\mathrm{d}U}{\mathrm{d}r}\right|_{R_0} = 0$ 得 $\frac{nB}{R_0^{n+1}} = \frac{\alpha e^2}{4\pi\varepsilon_0 R_0^2}$。对 $U(r)$ 求二阶导数并代入该关系：
   $$\left.\frac{\mathrm{d}^2 U}{\mathrm{d}r^2}\right|_{R_0} = N\left(-\frac{2\alpha e^2}{4\pi\varepsilon_0 R_0^3} + \frac{n(n+1)B}{R_0^{n+2}}\right) = \frac{N(n-1)\alpha e^2}{4\pi\varepsilon_0 R_0^3}$$
   NaCl 晶体立方惯用胞边长 $a = 2R_0$，含 $4$ 对正负离子，故 $V_0 = \frac{N}{4}(2R_0)^3 = 2NR_0^3$。代入 $K = \frac{R_0^2}{9V_0}\left.\frac{\mathrm{d}^2 U}{\mathrm{d}r^2}\right|_{R_0}$：
   $$K = \frac{R_0^2}{9(2NR_0^3)}\cdot\frac{N(n-1)\alpha e^2}{4\pi\varepsilon_0 R_0^3} = \frac{(n-1)\alpha e^2}{72\pi\varepsilon_0 R_0^4}$$

2. **计算 $n$ 与 $w_{\text{离子}}$**：反解 $n$：
   $$n = 1 + \frac{72\pi\varepsilon_0 R_0^4 K}{\alpha e^2} = 1 + \frac{18 R_0^4 K}{\alpha k_e e^2}$$
   其中 $k_e = \frac{1}{4\pi\varepsilon_0} = 8.988 \times 10^9\ \mathrm{N\cdot m^2/C^2}$，代入 $R_0 = 2.82 \times 10^{-10}\ \mathrm{m}$：
   $$n = 1 + \frac{18 \times (2.82 \times 10^{-10})^4 \times 2.40 \times 10^{10}}{1.7476 \times 8.988 \times 10^9 \times (1.602 \times 10^{-19})^2} \approx 1 + 6.776 = 7.78$$
   纯马德隆静电吸引能为：
   $$u_{\mathrm{Mad}} = \frac{\alpha k_e e^2}{R_0} = \frac{1.7476 \times 8.988 \times 10^9 \times 1.602 \times 10^{-19}}{2.82 \times 10^{-10}}\ \mathrm{eV} \approx 8.924\ \mathrm{eV}$$
   每对离子结合能：
   $$w_{\text{离子}} = u_{\mathrm{Mad}}\left(1 - \frac{1}{n}\right) = 8.924 \times \left(1 - \frac{1}{7.776}\right)\ \mathrm{eV} \approx 7.78\ \mathrm{eV}$$

3. **玻恩-哈伯循环求原子结合能**：把晶体先拆成孤立正负离子（耗能 $w_{\text{离子}}$），再将 $\mathrm{Cl^-}$ 夺走的电子还给 $\mathrm{Na^+}$ 变为中性原子（放出能量 $I - E_A$）：
   $$w_{\text{原子}} = w_{\text{离子}} - I + E_A = 7.78 - 5.14 + 3.61 = 6.25\ \mathrm{eV}$$
:::

#### 题型二：玻恩-梅耶指数排斥势模型

`CH02-KP2-06` 设某离子晶体仅计最近邻排斥作用，总势能写成玻恩-梅耶形式：
$$U(r) = N\left(-\frac{\alpha q^2}{4\pi\varepsilon_0 r} + z\lambda e^{-r/\rho}\right)$$
其中每对离子所占体积为 $V/N = c r^3$（$c$ 为结构几何常数）。证明：
1. 平衡态下晶体的总结合能为 $W = \frac{N\alpha q^2}{4\pi\varepsilon_0 R_0}\left(1 - \frac{\rho}{R_0}\right)$；
2. 晶体在 $T = 0\ \mathrm{K}$ 时的体弹性模量为 $K = \frac{\alpha q^2}{36\pi\varepsilon_0 c R_0^4}\left(\frac{R_0}{\rho} - 2\right)$。

::: details 思路提示
先由 $\left.\frac{\mathrm{d}U}{\mathrm{d}r}\right|_{R_0} = 0$ 消去未知组合 $z\lambda e^{-R_0/\rho}$，再代入 $U(R_0)$ 和 $\left.\frac{\mathrm{d}^2 U}{\mathrm{d}r^2}\right|_{R_0}$。
:::

::: details 参考答案与解析
**参考答案**：证明见下。

**解析**：
1. 对 $U(r)$ 求一阶导数并令其在 $r = R_0$ 处为零：
   $$\left.\frac{\mathrm{d}U}{\mathrm{d}r}\right|_{R_0} = N\left(\frac{\alpha q^2}{4\pi\varepsilon_0 R_0^2} - \frac{z\lambda}{\rho}e^{-R_0/\rho}\right) = 0 \implies z\lambda e^{-R_0/\rho} = \frac{\rho}{R_0}\cdot\frac{\alpha q^2}{4\pi\varepsilon_0 R_0}$$
   回代势能表达式得平衡结合能：
   $$W = -U(R_0) = N\left(\frac{\alpha q^2}{4\pi\varepsilon_0 R_0} - \frac{\rho}{R_0}\frac{\alpha q^2}{4\pi\varepsilon_0 R_0}\right) = \frac{N\alpha q^2}{4\pi\varepsilon_0 R_0}\left(1 - \frac{\rho}{R_0}\right)$$

2. 求二阶导数并代入上述平衡关系：
   $$\left.\frac{\mathrm{d}^2 U}{\mathrm{d}r^2}\right|_{R_0} = N\left(-\frac{2\alpha q^2}{4\pi\varepsilon_0 R_0^3} + \frac{z\lambda}{\rho^2}e^{-R_0/\rho}\right) = N\frac{\alpha q^2}{4\pi\varepsilon_0 R_0^3}\left(\frac{R_0}{\rho} - 2\right)$$
   将 $V_0 = c N R_0^3$ 代入 $K = \frac{R_0^2}{9 V_0}\left.\frac{\mathrm{d}^2 U}{\mathrm{d}r^2}\right|_{R_0}$：
   $$K = \frac{R_0^2}{9 c N R_0^3}\cdot N\frac{\alpha q^2}{4\pi\varepsilon_0 R_0^3}\left(\frac{R_0}{\rho} - 2\right) = \frac{\alpha q^2}{36\pi\varepsilon_0 c R_0^4}\left(\frac{R_0}{\rho} - 2\right)$$
   （稳定晶体要求 $K > 0 \implies R_0/\rho > 2$；实际碱金属卤化物中 $\rho/R_0 \approx 0.1$。）
:::

---

### 知识点 3：非极性分子晶体结合能与体弹性模量

#### 概念选择与填空

`CH02-KP3-01`（单选）用伦纳德-琼斯 6-12 势 $u(r) = 4\varepsilon\left[\left(\frac{\sigma}{r}\right)^{12} - \left(\frac{\sigma}{r}\right)^6\right]$ 描述惰性气体原子间相互作用，下列说法正确的是（ ）。
A. 孤立双原子分子的平衡间距为 $\sigma$，势阱深度为 $4\varepsilon$
B. 孤立双原子分子的平衡间距为 $2^{1/6}\sigma \approx 1.122\sigma$，势阱深度为 $\varepsilon$；形成 fcc 晶体后最近邻间距收缩至 $1.090\sigma$
C. 形成 fcc 晶体后，由于存在更多排斥邻近，最近邻间距比孤立双原子分子更大
D. 参数 $\varepsilon$ 的物理意义是 $r = \sigma$ 处的势能值

::: details 思路提示
区分孤立双原子对势的极小值位置 $r_0 = 2^{1/6}\sigma$ 与三维 fcc 晶格求和后的平衡间距 $R_0 = (2A_{12}/A_6)^{1/6}\sigma$。
:::

::: details 参考答案与解析
**参考答案**：B

**解析**：对孤立双原子，$u(\sigma) = 0$；令 $\mathrm{d}u/\mathrm{d}r = 0$ 得 $r_0 = 2^{1/6}\sigma \approx 1.122\sigma$，此时 $u(r_0) = -\varepsilon$（势阱深度为 $\varepsilon$）。形成 fcc 晶体后，因次近邻及更远原子对吸引项 $A_6 = 14.45$ 的贡献显著大于对短程排斥项 $A_{12} = 12.13$ 的贡献（$A_{12}/A_6 < 1$），平衡最近邻间距收缩为 $R_0 = (2A_{12}/A_6)^{1/6}\sigma \approx 1.090\sigma < r_0$。
:::

---

`CH02-KP3-02`（填空）对于一般双幂次双原子势 $u(r) = -\frac{A}{r^m} + \frac{B}{r^n}$（$n > m > 0$），最大吸引力对应的间距 $r_m$ 与平衡间距 $r_0$ 的比值 $\frac{r_m}{r_0} =$ ____；对伦纳德-琼斯 6-12 势（$m=6,\ n=12$），该比值约为 ____。

::: details 思路提示
分别联立 $\frac{\mathrm{d}u}{\mathrm{d}r}\big|_{r_0} = 0$ 与 $\frac{\mathrm{d}^2 u}{\mathrm{d}r^2}\big|_{r_m} = 0$ 消去 $A, B$。
:::

::: details 参考答案与解析
**参考答案**：$\left(\frac{n+1}{m+1}\right)^{\frac{1}{n-m}}$；$1.109$。

**解析**：
由 $\left.\frac{\mathrm{d}u}{\mathrm{d}r}\right|_{r_0} = 0$ 得 $r_0^{n-m} = \frac{nB}{mA}$；由 $\left.\frac{\mathrm{d}^2 u}{\mathrm{d}r^2}\right|_{r_m} = 0$ 得 $r_m^{n-m} = \frac{n(n+1)B}{m(m+1)A}$。两式相除：
$$\frac{r_m}{r_0} = \left(\frac{n+1}{m+1}\right)^{\frac{1}{n-m}}$$
代入 $m = 6,\ n = 12$ 得 $\frac{r_m}{r_0} = \left(\frac{13}{7}\right)^{1/6} \approx 1.109$（即只需拉伸约 $11\%$ 即达理论最大拉力）。
:::

---

`CH02-KP3-03`（单选）在由 $N$ 个同类原子组成的分子晶体中，若任一参考原子与其余所有原子的相互作用势能之和为 $u_{\text{总}}(R)$，则晶体总结合势能写作 $U(R) = \frac{1}{2}N u_{\text{总}}(R)$。系数 $\frac{1}{2}$ 的物理含义是（ ）。
A. 仅有一半原子参与成键
B. 抵消量子零点振动能的一半贡献
C. 避免每一对原子之间的相互作用势能被重复计入两次
D. 考虑排斥势抵消了一半吸引势

::: details 思路提示
每对原子 $(i, j)$ 的相互作用在分别以 $i$ 和 $j$ 为中心求和时各被计算了一次。
:::

::: details 参考答案与解析
**参考答案**：C

**解析**：晶体总势能是所有无序原子对 $(i < j)$ 势能之和，写成对全部原子求和 $\sum_i \sum_{j \ne i} u(r_{ij})$ 时每对原子被计入两次，因此必须乘以 $\frac{1}{2}$。
:::

#### 题型一：伦纳德-琼斯势求解分子晶体平衡参数与体弹性模量

`CH02-KP3-04` 固态氩（Ar）为面心立方（fcc）分子晶体，原子间相互作用采用伦纳德-琼斯势 $u(r) = 4\varepsilon\left[\left(\frac{\sigma}{r}\right)^{12} - \left(\frac{\sigma}{r}\right)^6\right]$，已知 fcc 晶格求和常数 $A_6 = 14.45$，$A_{12} = 12.13$。
1. 推导平衡最近邻间距 $R_0/\sigma$ 及单原子结合能 $w = -U(R_0)/N$ 的解析表达式；
2. 证明 fcc 分子晶体在 $T = 0\ \mathrm{K}$ 时的体弹性模量为 $K = \frac{4\sqrt{2}\varepsilon}{R_0^3}\frac{A_6^2}{A_{12}} = \frac{8\sqrt{2}w}{R_0^3}$；
3. 已知固态氩的参数 $\varepsilon = 1.67 \times 10^{-21}\ \mathrm{J}$，$\sigma = 3.40\ \text{Å}$，计算其 $R_0$（$\text{Å}$）、单原子结合能 $w$（$\mathrm{eV}$）和体弹性模量 $K$（$\mathrm{GPa}$）。

::: details 思路提示
fcc 惯用胞边长 $a = \sqrt{2}R$，含 $4$ 个原子，故单原子所占体积 $V/N = a^3/4 = R^3/\sqrt{2}$；求 $\left.\frac{\mathrm{d}^2 U}{\mathrm{d}R^2}\right|_{R_0}$ 后把 $(\sigma/R_0)^6 = A_6/(2A_{12})$ 代入化简。
:::

::: details 参考答案与解析
**参考答案**：
1. $\frac{R_0}{\sigma} = \left(\frac{2A_{12}}{A_6}\right)^{1/6} \approx 1.090$，$w = \frac{1}{2}\varepsilon\frac{A_6^2}{A_{12}} \approx 8.61\varepsilon$；
2. 证明见下；
3. $R_0 \approx 3.71\ \text{Å}$，$w \approx 0.0897\ \mathrm{eV}$（$89.7\ \mathrm{meV}$），$K \approx 3.19\ \mathrm{GPa}$。

**解析**：
1. **平衡间距与结合能**：$N$ 个原子的总势能为
   $$U(R) = \frac{1}{2}N\cdot 4\varepsilon\left[A_{12}\left(\frac{\sigma}{R}\right)^{12} - A_6\left(\frac{\sigma}{R}\right)^6\right] = 2N\varepsilon\left[A_{12}\left(\frac{\sigma}{R}\right)^{12} - A_6\left(\frac{\sigma}{R}\right)^6\right]$$
   由平衡条件 $\left.\frac{\mathrm{d}U}{\mathrm{d}R}\right|_{R_0} = 2N\varepsilon\left[-12A_{12}\frac{\sigma^{12}}{R_0^{13}} + 6A_6\frac{\sigma^6}{R_0^7}\right] = 0$ 得：
   $$\left(\frac{\sigma}{R_0}\right)^6 = \frac{A_6}{2A_{12}} \implies \frac{R_0}{\sigma} = \left(\frac{2A_{12}}{A_6}\right)^{1/6} = \left(\frac{2\times 12.13}{14.45}\right)^{1/6} \approx 1.090$$
   代回 $U(R_0)$ 得单原子结合能：
   $$w = -\frac{U(R_0)}{N} = -2\varepsilon\left[A_{12}\left(\frac{A_6}{2A_{12}}\right)^2 - A_6\left(\frac{A_6}{2A_{12}}\right)\right] = \frac{1}{2}\varepsilon\frac{A_6^2}{A_{12}} \approx 8.61\varepsilon$$

2. **体弹性模量**：对 $U(R)$ 求二阶导数并代入 $(\sigma/R_0)^6 = A_6/(2A_{12})$：
   $$\left.\frac{\mathrm{d}^2 U}{\mathrm{d}R^2}\right|_{R_0} = \frac{2N\varepsilon}{R_0^2}\left[156A_{12}\left(\frac{A_6}{2A_{12}}\right)^2 - 42A_6\left(\frac{A_6}{2A_{12}}\right)\right] = \frac{2N\varepsilon}{R_0^2}\left(39 - 21\right)\frac{A_6^2}{A_{12}} = \frac{36N\varepsilon}{R_0^2}\frac{A_6^2}{A_{12}}$$
   fcc 结构单原子体积 $V_0/N = \frac{(\sqrt{2}R_0)^3}{4} = \frac{R_0^3}{\sqrt{2}}$，代入 $K = \frac{R_0^2}{9V_0}\left.\frac{\mathrm{d}^2 U}{\mathrm{d}R^2}\right|_{R_0}$：
   $$K = \frac{R_0^2}{9 N R_0^3/\sqrt{2}}\cdot\frac{36N\varepsilon}{R_0^2}\frac{A_6^2}{A_{12}} = \frac{4\sqrt{2}\varepsilon}{R_0^3}\frac{A_6^2}{A_{12}} = \frac{8\sqrt{2}w}{R_0^3}$$

3. **数值代入**：
   $$R_0 = 1.0902 \times 3.40\ \text{Å} \approx 3.71\ \text{Å}$$
   $$w = 8.607 \times 1.67 \times 10^{-21}\ \mathrm{J} = 1.437 \times 10^{-20}\ \mathrm{J} \approx 0.0897\ \mathrm{eV}$$
   $$K = \frac{8\sqrt{2} \times 1.437 \times 10^{-20}}{(3.707 \times 10^{-10})^3}\ \mathrm{Pa} \approx 3.19 \times 10^9\ \mathrm{Pa} = 3.19\ \mathrm{GPa}$$
:::

#### 题型二：短程最近邻近似评估与晶体结构稳定性比较

`CH02-KP3-05` 考虑由 $N$ 个原子组成的一维单原子链（相邻原子间距为 $a$），原子间满足伦纳德-琼斯势 $u(r) = 4\varepsilon\left[\left(\frac{\sigma}{r}\right)^{12} - \left(\frac{\sigma}{r}\right)^6\right]$。分别计算：
1. 仅考虑最近邻相互作用时的平衡间距 $a_0/\sigma$ 与单原子结合能 $w/\varepsilon$；
2. 计入全部原子相互作用时的 $a_0/\sigma$ 与 $w/\varepsilon$（已知 $\zeta(6) = \sum_{m=1}^{\infty} m^{-6} = \frac{\pi^6}{945} \approx 1.0173$，$\zeta(12) = \sum_{m=1}^{\infty} m^{-12} \approx 1.00025$），并评述短程近似的精度。

::: details 思路提示
一维链中每个原子左右各有 $1$ 个第 $m$ 近邻（距离 $ma$），因此晶格求和常数 $A_6 = 2\sum_{m=1}^{\infty} m^{-6} = 2\zeta(6)$，$A_{12} = 2\zeta(12)$；仅计最近邻则取 $m=1$ 得 $A_6 = A_{12} = 2$。
:::

::: details 参考答案与解析
**参考答案**：
1. 仅计最近邻：$a_0/\sigma = 2^{1/6} \approx 1.122$，$w/\varepsilon = 1.000$；
2. 计入全部原子：$a_0/\sigma \approx 1.119$，$w/\varepsilon \approx 1.035$。

**解析**：
1. **仅计最近邻**：每个原子有 $2$ 个最近邻，故 $A_6 = 2,\ A_{12} = 2$。代入通式：
   $$\frac{a_0}{\sigma} = \left(\frac{2A_{12}}{A_6}\right)^{1/6} = 2^{1/6} \approx 1.1225, \qquad \frac{w}{\varepsilon} = \frac{1}{2}\frac{A_6^2}{A_{12}} = 1.000$$

2. **计入全部原子**：左右对称求和得 $A_6 = 2\zeta(6) \approx 2.0347$，$A_{12} = 2\zeta(12) \approx 2.0005$：
   $$\frac{a_0}{\sigma} = \left(\frac{2\times 2.0005}{2.0347}\right)^{1/6} \approx 1.1193$$
   $$\frac{w}{\varepsilon} = \frac{1}{2}\frac{(2.0347)^2}{2.0005} \approx 1.0347$$
   对比可知，仅计最近邻使平衡间距偏大仅 $0.28\%$、结合能偏小约 $3.5\%$，说明 $r^{-6}$ 与 $r^{-12}$ 型分子间相互作用高度局域，最近邻近似已有较高精度（而对 $r^{-1}$ 长程库仑力则必须计入全部远邻马德隆求和）。
:::

---

`CH02-KP3-06` 某假想一价离子晶体在 NaCl 型结构中配位数 $z_1 = 6$、马德隆常数 $\alpha_1 = 1.7476$，在 CsCl 型结构中配位数 $z_2 = 8$、马德隆常数 $\alpha_2 = 1.7627$。假设排斥势仅计最近邻且每对最近邻离子的排斥势均为 $\frac{B}{r^n}$（同一套离子参数 $B, n$ 不随结构改变），总势能为 $U(r) = N\left(-\frac{\alpha e^2}{4\pi\varepsilon_0 r} + \frac{zB}{r^n}\right)$。
1. 推导平衡态下两种结构的平衡间距之比 $\frac{R_{02}}{R_{01}}$ 和结合能之比 $\frac{W_2}{W_1}$；
2. 求出使 CsCl 型比 NaCl 型更稳定的临界排斥指数 $n_c$；
3. 当 $n = 9$ 时计算 $\frac{W_2}{W_1}$，说明为何大多数碱金属卤化物在常温下采用 NaCl 型结构而非马德隆常数更大的 CsCl 型结构。

::: details 思路提示
切勿假设两种结构的平衡间距 $R_0$ 相同！因为 CsCl 配位数更大（$z_2=8 > z_1=6$），先各自用平衡条件求出 $R_0 \propto (z/\alpha)^{\frac{1}{n-1}}$，再代回结合能比较。
:::

::: details 参考答案与解析
**参考答案**：
1. $\frac{R_{02}}{R_{01}} = \left(\frac{z_2 \alpha_1}{z_1 \alpha_2}\right)^{\frac{1}{n-1}}$，$\frac{W_2}{W_1} = \left(\frac{\alpha_2}{\alpha_1}\right)^{\frac{n}{n-1}}\left(\frac{z_1}{z_2}\right)^{\frac{1}{n-1}}$；
2. $n_c = \frac{\ln(z_2/z_1)}{\ln(\alpha_2/\alpha_1)} \approx 33.4$；
3. $n = 9$ 时 $\frac{W_2}{W_1} \approx 0.974 < 1$，故 NaCl 型能量更低、更稳定。

**解析**：
1. 由平衡条件 $\frac{\mathrm{d}U}{\mathrm{d}r} = 0$ 得：
   $$\frac{\alpha e^2}{4\pi\varepsilon_0 R_0^2} = \frac{n z B}{R_0^{n+1}} \implies R_0 = \left(\frac{4\pi\varepsilon_0 n B}{e^2}\cdot\frac{z}{\alpha}\right)^{\frac{1}{n-1}} \propto \left(\frac{z}{\alpha}\right)^{\frac{1}{n-1}}$$
   故两结构平衡间距之比为：
   $$\frac{R_{02}}{R_{01}} = \left(\frac{z_2 \alpha_1}{z_1 \alpha_2}\right)^{\frac{1}{n-1}}$$
   平衡结合能 $W = \frac{N\alpha e^2}{4\pi\varepsilon_0 R_0}\left(1 - \frac{1}{n}\right) \propto \frac{\alpha}{R_0} \propto \alpha\left(\frac{\alpha}{z}\right)^{\frac{1}{n-1}} = \alpha^{\frac{n}{n-1}} z^{-\frac{1}{n-1}}$，因此：
   $$\frac{W_2}{W_1} = \left(\frac{\alpha_2}{\alpha_1}\right)^{\frac{n}{n-1}}\left(\frac{z_1}{z_2}\right)^{\frac{1}{n-1}}$$

2. 令 $\frac{W_2}{W_1} = 1$，即 $\left(\frac{\alpha_2}{\alpha_1}\right)^{n_c} = \frac{z_2}{z_1}$，取对数得：
   $$n_c = \frac{\ln(z_2/z_1)}{\ln(\alpha_2/\alpha_1)} = \frac{\ln(8/6)}{\ln(1.7627/1.7476)} \approx \frac{0.2877}{0.00860} \approx 33.4$$

3. 当 $n = 9$ 时：
   $$\frac{R_{02}}{R_{01}} = \left(\frac{8 \times 1.7476}{6 \times 1.7627}\right)^{1/8} \approx 1.0355$$
   $$\frac{W_2}{W_1} = \left(\frac{1.7627}{1.7476}\right)^{9/8}\left(\frac{6}{8}\right)^{1/8} \approx 1.0097 \times 0.9647 \approx 0.974 < 1$$
   物理原因：虽然 CsCl 型的马德隆常数比 NaCl 型略大 $0.86\%$，但其最近邻配位数由 $6$ 增至 $8$（增幅 $33\%$），导致短程排斥作用显著增强、平衡间距被迫拉大 $3.6\%$，反而削弱了总静电结合能。实际碱金属卤化物排斥指数 $n \approx 7\text{–}12 \ll 33.4$，因此多数采用 NaCl 型结构（仅 $\mathrm{CsCl, CsBr, CsI}$ 因离子极化与范德瓦尔斯附加吸引而采取 CsCl 结构）。
:::
