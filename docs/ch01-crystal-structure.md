# 第一章 晶体结构

::: info 教学大纲（建议 9 学时）
- 1.1 晶格实例与周期性：布拉伐格子、基元、原胞（元胞）与惯用胞、配位数与致密度
- 1.2 晶向指数 `[uvw]`、晶面指数 `(hkl)` 与晶面间距
- 1.3 晶体中的对称元素与对称操作（旋转对称限制、七大晶系、准晶体）
- 1.4 倒格子与布里渊区
- 1.5 X 射线衍射理论（布拉格方程、劳厄方程、厄瓦尔德球、几何结构因子与系统消光）
:::

::: tip 核心概念与模型
**1. 晶体周期性模型：晶体结构 = 布拉伐格子（周期点阵） + 基元（原子团）**
- 格矢 $\mathbf{R}_n = n_1\mathbf{a}_1 + n_2\mathbf{a}_2 + n_3\mathbf{a}_3$（$n_1,n_2,n_3 \in \mathbb{Z}$）。
- **原胞**：只含 $1$ 个格点、体积最小 $\Omega = |\mathbf{a}_1\cdot(\mathbf{a}_2\times\mathbf{a}_3)|$，选取不唯一；**维格纳-赛茨（W-S）原胞**由相邻格点连线的中垂面包围而成，保留格子全部点群对称性。**惯用胞**按对称性选取，可含多个格点。
- 所有原子等效且环境相同的是**简单格子（布拉伐格子）**；每个格点附带多个原子的是**复式格子**。

| 结构类型 | 布拉伐格子 / 基元 | 惯用胞原子数 | 配位数 | 最近邻间距 | 致密度 |
| :--- | :--- | :---: | :---: | :---: | :---: |
| 简立方（sc） | sc / 1 原子 | $1$ | $6$ | $a$ | $\frac{\pi}{6} \approx 52.4\%$ |
| 体心立方（bcc） | bcc / 1 原子 | $2$ | $8$ | $\frac{\sqrt{3}}{2}a$ | $\frac{\sqrt{3}\pi}{8} \approx 68.0\%$ |
| 面心立方（fcc） | fcc / 1 原子 | $4$ | $12$ | $\frac{\sqrt{2}}{2}a$ | $\frac{\sqrt{2}\pi}{6} \approx 74.0\%$ |
| 六角密排（hcp） | 简六角 / 2 原子 | $2$（原胞） | $12$ | $a$（理想 $c/a=\sqrt{8/3}$） | $\frac{\sqrt{2}\pi}{6} \approx 74.0\%$ |
| 金刚石（Si, Ge, C） | fcc / 2 原子 $(0,0,0), (\frac{1}{4},\frac{1}{4},\frac{1}{4})$ | $8$ | $4$ | $\frac{\sqrt{3}}{4}a$ | $\frac{\sqrt{3}\pi}{16} \approx 34.0\%$ |
| NaCl | fcc / 2 离子 $(0,0,0), (\frac{1}{2},0,0)$ | $4\ \mathrm{Na^+} + 4\ \mathrm{Cl^-}$ | $6$ | $\frac{1}{2}a$ | — |
| CsCl | sc / 2 离子 $(0,0,0), (\frac{1}{2},\frac{1}{2},\frac{1}{2})$ | $1\ \mathrm{Cs^+} + 1\ \mathrm{Cl^-}$ | $8$ | $\frac{\sqrt{3}}{2}a$ | — |
| 闪锌矿（GaAs） | fcc / 2 异类原子 $(0,0,0), (\frac{1}{4},\frac{1}{4},\frac{1}{4})$ | $4\ \mathrm{Ga} + 4\ \mathrm{As}$ | $4$ | $\frac{\sqrt{3}}{4}a$ | — |

**2. 晶向与晶面**
- 晶向 `[uvw]`：方向分量约化为互质整数；等效晶向族 `<uvw>`。
- 晶面 `(hkl)`：三轴截距倒数约化为互质整数，负号置于数字上方如 $(\bar{1}10)$；等效晶面族 `{hkl}`。
- 晶带定律：晶向 `[uvw]` 位于晶面 `(hkl)` 内 $\iff hu + kv + lw = 0$。
- **立方晶系特有结论**：`[hkl]` $\perp$ `(hkl)`；晶面间距 $d_{hkl} = \frac{a}{\sqrt{h^2+k^2+l^2}}$。

**3. 晶体对称性**
- 点群操作：旋转 $C_n$、反演 $i$、镜面 $\sigma$、旋转反演；平移周期性要求 $2\cos\theta \in \mathbb{Z}$，故晶体中只允许 $1, 2, 3, 4, 6$ 重旋转轴。
- 三维晶体分类：**7 大晶系、14 种布拉伐格子、32 种点群、230 种空间群**。
- **准晶体**：具有长程取向序（可出现 5 重、10 重衍射对称）而无周期平移对称。

**4. 倒格子与布里渊区**
- 倒格子基矢：$\mathbf{b}_1 = 2\pi\frac{\mathbf{a}_2\times\mathbf{a}_3}{\Omega}$（轮换），满足 $\mathbf{a}_i\cdot\mathbf{b}_j = 2\pi\delta_{ij}$，体积 $\Omega^* = \frac{(2\pi)^3}{\Omega}$。
- 倒格矢 $\mathbf{G}_{hkl} = h\mathbf{b}_1 + k\mathbf{b}_2 + l\mathbf{b}_3$（按原胞基矢且 $h,k,l$ 互质）垂直于 `(hkl)` 晶面族，且 $d_{hkl} = \frac{2\pi}{|\mathbf{G}_{hkl}|}$。
- 正倒对偶：`sc ↔ sc`，`bcc ↔ fcc`；**第一布里渊区**是倒格子的 W-S 原胞，边界方程 $\mathbf{k}\cdot\mathbf{G} = \frac{1}{2}G^2$，各阶布里渊区体积均等于 $\Omega^*$。

**5. X 射线衍射与几何结构因子**
- 布拉格方程：$2d\sin\theta = n\lambda$；劳厄方程：$\Delta\mathbf{k} = \mathbf{k}' - \mathbf{k} = \mathbf{G}$（与 $2\mathbf{k}\cdot\mathbf{G} + G^2 = 0$ 等价）。
- 几何结构因子（立方惯用胞指标）：$S(hkl) = \sum_j f_j e^{-i2\pi(h u_j + k v_j + l w_j)}$。
- 系统消光条件（惯用胞指标）：
  - `bcc`：$h+k+l$ 为奇数消光（允许 $h^2+k^2+l^2 = 2,4,6,8,\dots$）；
  - `fcc`：$h,k,l$ 奇偶混杂消光（允许 $h^2+k^2+l^2 = 3,4,8,11,12,\dots$）；
  - `金刚石`：在 fcc 允许基础上，$h,k,l$ 全偶且 $h+k+l = 4m+2$ 消光（允许 $h^2+k^2+l^2 = 3,8,11,16,19,\dots$）。
:::

![bcc 与 fcc 惯用胞与原胞基矢](/figures/ch01-primitive-cells.svg)

<p class="fig-caption">图 1-1 bcc 与 fcc 的立方惯用胞及标准原胞基矢</p>

## 习题及参考解答

### 知识点 1：晶格周期性、原胞与惯用胞、典型晶体结构

#### 概念选择与填空

`CH01-KP1-01`（单选）下列晶体结构中，属于**复式格子**的是（ ）。
A. 金属铜（fcc）
B. 金属铁（$\alpha$-Fe，bcc）
C. 氯化铯（CsCl）
D. 金属钋（$\alpha$-Po，sc）

::: details 思路提示
检查每个格点上是否只挂 1 个原子，以及所有原子所处的几何与化学环境是否完全等同。
:::

::: details 参考答案与解析
**参考答案**：C

**解析**：
- 铜（fcc）、$\alpha$-Fe（bcc）、$\alpha$-Po（sc）的原子全部相同且每个原子的周围环境完全等价，均为简单布拉伐格子。
- CsCl 结构虽然外观像体心立方，但顶角为 $\mathrm{Cs^+}$、体心为 $\mathrm{Cl^-}$，两类离子化学性质不同，平移矢量 $\frac{a}{2}(\hat{\mathbf{x}}+\hat{\mathbf{y}}+\hat{\mathbf{z}})$ 不是周期平移矢量。因此 CsCl 是**简立方（sc）布拉伐格子**加上含 2 个离子的基元，属于复式格子。
:::

---

`CH01-KP1-02`（填空）晶格常数为 $a$ 的体心立方（bcc）、面心立方（fcc）和金刚石结构，其立方惯用胞内的原子数分别为 ____、____、____；配位数分别为 ____、____、____；最近邻原子间距分别为 ____、____、____。

::: details 思路提示
按顶角占 $\frac{1}{8}$、面心占 $\frac{1}{2}$、体心与体内原子占 $1$ 统计惯用胞原子数；最近邻沿体对角线或面对角线寻找。
:::

::: details 参考答案与解析
**参考答案**：
- 惯用胞原子数：$2$、$4$、$8$
- 配位数：$8$、$12$、$4$
- 最近邻间距：$\frac{\sqrt{3}}{2}a$、$\frac{\sqrt{2}}{2}a$、$\frac{\sqrt{3}}{4}a$

**解析**：
- **bcc**：$8\times\frac{1}{8}+1=2$；体心原子与 8 个顶角最近，间距为体对角线一半 $\frac{\sqrt{3}}{2}a$。
- **fcc**：$8\times\frac{1}{8}+6\times\frac{1}{2}=4$；每个顶角在 $xy, yz, zx$ 三个平面各有 4 个最近邻面心原子，配位数 12，间距为面对角线一半 $\frac{\sqrt{2}}{2}a$。
- **金刚石**：由两套 fcc 沿体对角线平移 $\frac{1}{4}$ 套构而成，原子数 $4+4=8$；体内 4 个原子分别位于 4 个小正四面体中心，配位数 4，间距为体对角线的 $\frac{1}{4}$，即 $\frac{\sqrt{3}}{4}a$。
:::

---

`CH01-KP1-03`（单选）关于晶体的原胞与维格纳-赛茨（Wigner-Seitz）原胞，下列说法**错误**的是（ ）。
A. 同一布拉伐格子的原胞选取方式不唯一，但所有原胞的体积完全相同
B. 任何原胞内部平均只包含 $1$ 个格点
C. 维格纳-赛茨原胞是原胞的一种特殊选法，它完整保留了格子的点群对称性
D. 复式格子的原胞内部只能包含 $1$ 个原子

::: details 思路提示
区分“格点”与“原子”两个概念。
:::

::: details 参考答案与解析
**参考答案**：D

**解析**：原胞内只含 $1$ 个**格点**，每个格点携带 $1$ 个基元。对于复式格子（如 hcp、金刚石、NaCl），每个基元含 $2$ 个（或更多）原子，因此复式格子的原胞中包含多个原子。A、B、C 均正确。
:::

---

`CH01-KP1-04`（填空）写出下列三种典型化合物晶体的布拉伐格子类型及原胞内的离子（原子）数：
1. NaCl：____ 布拉伐格子，原胞含 ____ 个离子；
2. CsCl：____ 布拉伐格子，原胞含 ____ 个离子；
3. 闪锌矿（GaAs）：____ 布拉伐格子，原胞含 ____ 个原子。

::: details 思路提示
将同类原子单独抽出，观察其构成哪种布拉伐格子，再确定每个格点附带的基元。
:::

::: details 参考答案与解析
**参考答案**：
1. 面心立方（fcc），$2$
2. 简立方（sc），$2$
3. 面心立方（fcc），$2$

**解析**：
- NaCl 由 $\mathrm{Na^+}$ 和 $\mathrm{Cl^-}$ 两套 fcc 沿棱边平移 $\frac{a}{2}$ 套构而成，布拉伐格子为 fcc，基元含 1 个 $\mathrm{Na^+}$ 和 1 个 $\mathrm{Cl^-}$。
- CsCl 由两套 sc 沿体对角线平移 $\frac{1}{2}$ 套构而成，布拉伐格子为 sc，基元含 1 个 $\mathrm{Cs^+}$ 和 1 个 $\mathrm{Cl^-}$。
- GaAs 由 Ga 和 As 两套 fcc 沿体对角线平移 $\frac{1}{4}$ 套构而成，布拉伐格子为 fcc，基元含 1 个 Ga 和 1 个 As。
:::

#### 题型一：空间致密度与理想轴比计算

`CH01-KP1-05` 已知单晶硅（Si）具有金刚石结构，晶格常数 $a = 5.43\ \text{Å}$。
1. 在刚球相切模型下，证明金刚石结构的空间致密度为 $\frac{\sqrt{3}\pi}{16} \approx 34.0\%$；
2. 计算硅晶体的最近邻原子间距 $d_{\mathrm{nn}}$ 和原子数密度 $n$（单位：$\mathrm{cm^{-3}}$）。

::: details 思路提示
先由最近邻间距确定刚球半径 $R = \frac{1}{2}d_{\mathrm{nn}}$，再按“惯用胞内全部刚球体积 / 惯用胞体积 $a^3$”求致密度；计算数密度时注意 $1\ \text{Å} = 10^{-8}\ \mathrm{cm}$。
:::

::: details 参考答案与解析
**参考答案**：
1. 致密度 $\eta = \frac{\sqrt{3}\pi}{16} \approx 34.0\%$（证明见下）；
2. $d_{\mathrm{nn}} \approx 2.35\ \text{Å}$，$n \approx 5.00 \times 10^{22}\ \mathrm{cm^{-3}}$。

**解析**：
1. 金刚石结构的立方惯用胞边长为 $a$，体积 $V = a^3$，内含 $8$ 个原子。最近邻原子沿立方体体对角线相距 $\frac{1}{4}$ 体对角线长，即
   $$d_{\mathrm{nn}} = \frac{\sqrt{3}}{4}a$$
   刚球相切时原子半径 $R = \frac{d_{\mathrm{nn}}}{2} = \frac{\sqrt{3}}{8}a$。由此得致密度：
   $$\eta = \frac{8 \times \frac{4}{3}\pi R^3}{a^3} = \frac{8 \times \frac{4}{3}\pi \left(\frac{\sqrt{3}}{8}a\right)^3}{a^3} = \frac{\sqrt{3}\pi}{16} \approx 0.3401 = 34.0\%$$

2. 代入 $a = 5.43\ \text{Å} = 5.43 \times 10^{-8}\ \mathrm{cm}$：
   $$d_{\mathrm{nn}} = \frac{\sqrt{3}}{4} \times 5.43\ \text{Å} \approx 2.351\ \text{Å} \approx 2.35\ \text{Å}$$
   $$n = \frac{8}{a^3} = \frac{8}{(5.43 \times 10^{-8}\ \mathrm{cm})^3} \approx 4.997 \times 10^{22}\ \mathrm{cm^{-3}} \approx 5.00 \times 10^{22}\ \mathrm{cm^{-3}}$$
:::

---

`CH01-KP1-06` 在理想刚球密排模型下，证明六角密排结构（hcp）的轴比满足 $\frac{c}{a} = \sqrt{\frac{8}{3}} \approx 1.633$，并计算其空间致密度。

::: details 思路提示
hcp 中间层（B 层）的原子落在底层（A 层）三个相切原子构成的等边三角形重心正上方，四个原子构成棱长为 $a$ 的正四面体，层间距为 $\frac{c}{2}$。
:::

::: details 参考答案与解析
**参考答案**：$\frac{c}{a} = \sqrt{\frac{8}{3}} \approx 1.633$，致密度 $\eta = \frac{\sqrt{2}\pi}{6} \approx 74.0\%$。

**解析**：
1. **理想轴比**：设底面（A 层）等边三角形边长为 $a$（刚球半径 $R = \frac{a}{2}$）。B 层原子位于该等边三角形重心正上方高度 $h = \frac{c}{2}$ 处，与底层三原子构成棱长为 $a$ 的正四面体。
   等边三角形顶角到重心的距离为：
   $$r = \frac{2}{3}\cdot\frac{\sqrt{3}}{2}a = \frac{a}{\sqrt{3}}$$
   由勾股定理：
   $$\left(\frac{c}{2}\right)^2 + r^2 = a^2 \implies \frac{c^2}{4} = a^2 - \frac{a^2}{3} = \frac{2}{3}a^2 \implies \frac{c}{a} = \sqrt{\frac{8}{3}} \approx 1.633$$

2. **空间致密度**：取简六角原胞，底面为边长 $a$、夹角 $120^\circ$（或 $60^\circ$）的菱形，高为 $c$，体积为
   $$\Omega = a^2 \sin 60^\circ \cdot c = \frac{\sqrt{3}}{2}a^2 c$$
   每个原胞内含 $2$ 个原子（基元 2 原子），刚球半径 $R = \frac{a}{2}$，则
   $$\eta = \frac{2 \times \frac{4}{3}\pi (a/2)^3}{\frac{\sqrt{3}}{2}a^2 c} = \frac{\frac{1}{3}\pi a^3}{\frac{\sqrt{3}}{2}a^3 \cdot \sqrt{\frac{8}{3}}} = \frac{\frac{1}{3}\pi}{\sqrt{2}} = \frac{\sqrt{2}\pi}{6} \approx 74.05\%$$
   与 fcc 致密度完全相同（两者仅密排面堆垛次序不同：fcc 为 ABCABC，hcp 为 ABAB）。
:::

---

### 知识点 2：晶向指数、晶面指数与晶面间距

#### 概念选择与填空

`CH01-KP2-01`（单选）某晶面在晶轴 $\mathbf{a}_1, \mathbf{a}_2, \mathbf{a}_3$ 上的截距分别为 $2a_1, -3a_2, \infty$，则该晶面的米勒指数为（ ）。
A. $(2\bar{3}0)$
B. $(3\bar{2}0)$
C. $(3\bar{2}1)$
D. $(\bar{3}20)$

::: details 思路提示
求截距的倒数，乘以最小公倍数化为互质整数，负号写成上划线。
:::

::: details 参考答案与解析
**参考答案**：B

**解析**：截距数依次为 $2, -3, \infty$，取倒数得 $\frac{1}{2}, -\frac{1}{3}, 0$，通分乘以最小公倍数 $6$ 得 $(3, -2, 0)$，记作 $(3\bar{2}0)$。注意 $(3\bar{2}0)$ 与 $(\bar{3}20)$ 属于同一组平行晶面，但在单选中按给定截距直接导出为 $(3\bar{2}0)$。
:::

---

`CH01-KP2-02`（填空）在立方晶系中，若按法向区分晶面正反取向（即构成封闭多面体的面数），等效晶面族 $\{100\}$、$\{110\}$、$\{111\}$ 分别包含 ____、____、____ 个等效晶面；若将平行晶面归为同一组，则分别对应 ____、____、____ 组不平行的晶面。

::: details 思路提示
统计三个指标的位置排列数与正负号组合总数；法向相反的两个晶面如 $(100)$ 与 $(\bar{1}00)$ 属于同一组平行晶面。
:::

::: details 参考答案与解析
**参考答案**：$6$、$12$、$8$（区分法向正负）；$3$、$6$、$4$（平行晶面归为一组）。

**解析**：
- $\{100\}$：$1$ 在 3 个位置可选，取 $\pm 1$，共 $3 \times 2 = 6$ 个取向（对应立方体 6 面，含 $3$ 组平行面）。
- $\{110\}$：$0$ 在 3 个位置可选，其余两位取 $\pm 1$，共 $3 \times 2^2 = 12$ 个取向（对应菱形十二面体 12 面，含 $6$ 组平行面）。
- $\{111\}$：三位均取 $\pm 1$，共 $2^3 = 8$ 个取向（对应正八面体 8 面，含 $4$ 组平行面）。
:::

---

`CH01-KP2-03`（单选）关于晶向与晶面的关系，下列判断正确的是（ ）。
A. 对任意晶系，晶向 $[hkl]$ 均垂直于晶面 $(hkl)$
B. 晶向 $[11\bar{2}]$ 位于晶面 $(111)$ 内
C. 同一晶体中，米勒指数越大的晶面族，其晶面间距越大、面原子密度越高
D. 晶向 $[111]$ 位于晶面 $(11\bar{1})$ 内

::: details 思路提示
逐项核验立方晶系条件以及晶带定律 $hu+kv+lw=0$。
:::

::: details 参考答案与解析
**参考答案**：B

**解析**：
- A 错：$[hkl] \perp (hkl)$ 仅在立方晶系（及部分特殊对称方向）成立，一般非立方晶系不成立。
- B 对：检验晶带定律 $1\times 1 + 1\times 1 + 1\times(-2) = 0$，故 $[11\bar{2}]$ 位于 $(111)$ 面内。
- C 错：对立方晶系 $d_{hkl} = a/\sqrt{h^2+k^2+l^2}$，指数越大，晶面间距越小，由 $\rho_{\text{面}} = d / \Omega_{\text{单原子}}$ 知面原子密度也越低。
- D 错：$1\times 1 + 1\times 1 + (-1)\times 1 = 1 \ne 0$。
:::

#### 题型一：晶面间距、面原子密度与晶面夹角

`CH01-KP2-04` 已知面心立方（fcc）晶体的立方惯用胞边长为 $a$。
1. 分别计算 `(100)`、`(110)`、`(111)` 三种晶面的面原子密度 $\rho$（单位面积上的原子数）；
2. 写出这三族相邻实际原子平面之间的有效晶面间距 $d_{\text{eff}}$，并指出哪种晶面是 fcc 的最密排面。

::: details 思路提示
注意 fcc 中沿 `[100]` 和 `[110]` 方向在两惯用胞边界之间还插有面心原子层，因此实际相邻原子面间距分别对应 `(200)` 和 `(220)`；也可先算面原子密度 $\rho$，再利用 $d_{\text{eff}} = \rho \cdot \Omega_{\text{单原子}}$（其中 $\Omega_{\text{单原子}} = a^3/4$）交叉验算。
:::

::: details 参考答案与解析
**参考答案**：
1. $\rho_{(100)} = \frac{2}{a^2}$，$\rho_{(110)} = \frac{\sqrt{2}}{a^2} \approx \frac{1.414}{a^2}$，$\rho_{(111)} = \frac{4}{\sqrt{3}a^2} \approx \frac{2.309}{a^2}$；
2. $d_{\text{eff},(100)} = \frac{a}{2}$，$d_{\text{eff},(110)} = \frac{\sqrt{2}}{4}a$，$d_{\text{eff},(111)} = \frac{a}{\sqrt{3}}$；最密排面为 `(111)`。

**解析**：
1. **面原子密度**：
   - **`(100)` 面**（正方形，面积 $a^2$）：含 $4$ 个顶角原子（各占 $\frac{1}{4}$）和 $1$ 个面心原子（占 $1$），共 $2$ 个原子：
     $$\rho_{(100)} = \frac{2}{a^2}$$
   - **`(110)` 面**（矩形，边长 $a$ 与 $\sqrt{2}a$，面积 $\sqrt{2}a^2$）：含 $4$ 个顶角（各占 $\frac{1}{4}$）和 $2$ 个边中点面心原子（各占 $\frac{1}{2}$），共 $2$ 个原子：
     $$\rho_{(110)} = \frac{2}{\sqrt{2}a^2} = \frac{\sqrt{2}}{a^2}$$
   - **`(111)` 面**（等边三角形，边长 $\sqrt{2}a$，面积 $\frac{\sqrt{3}}{4}(\sqrt{2}a)^2 = \frac{\sqrt{3}}{2}a^2$）：含 $3$ 个顶角（各占 $\frac{1}{6}$）和 $3$ 个边中点面心原子（各占 $\frac{1}{2}$），共 $2$ 个原子：
     $$\rho_{(111)} = \frac{2}{\frac{\sqrt{3}}{2}a^2} = \frac{4}{\sqrt{3}a^2} \approx \frac{2.309}{a^2}$$

2. **有效晶面间距**：每个原子占体积 $\Omega_0 = \frac{a^3}{4}$。由单位体积原子数相等关系 $\frac{\rho}{d_{\text{eff}}} = \frac{1}{\Omega_0}$，得 $d_{\text{eff}} = \rho \Omega_0$：
   - $d_{\text{eff},(100)} = \frac{2}{a^2}\cdot\frac{a^3}{4} = \frac{a}{2}$（即 $d_{200}$）；
   - $d_{\text{eff},(110)} = \frac{\sqrt{2}}{a^2}\cdot\frac{a^3}{4} = \frac{\sqrt{2}}{4}a$（即 $d_{220}$）；
   - $d_{\text{eff},(111)} = \frac{4}{\sqrt{3}a^2}\cdot\frac{a^3}{4} = \frac{a}{\sqrt{3}}$（即 $d_{111}$）。
   比较可知 `(111)` 晶面的面原子密度最大且晶面间距最大，是 fcc 的最密排面。
:::

---

`CH01-KP2-05` 在立方晶体中，求晶面 `(111)` 与 `(110)` 之间的锐夹角 $\theta$，并求出两晶面交线的晶向指数。

::: details 思路提示
立方晶系中 `(hkl)` 的法向量就是 `[hkl]`；两平面夹角等于法向量夹角，交线方向同时垂直于两法向量，用叉乘即可求出。
:::

::: details 参考答案与解析
**参考答案**：$\theta = \arccos\sqrt{\frac{2}{3}} \approx 35.26^\circ$；交线晶向为 $[\bar{1}10]$（或 $[1\bar{1}0]$）。

**解析**：
1. 立方晶系中两晶面法向量分别为 $\mathbf{n}_1 = (1,1,1)$ 与 $\mathbf{n}_2 = (1,1,0)$，故
   $$\cos\theta = \frac{\mathbf{n}_1 \cdot \mathbf{n}_2}{|\mathbf{n}_1||\mathbf{n}_2|} = \frac{1\times 1 + 1\times 1 + 1\times 0}{\sqrt{3}\cdot\sqrt{2}} = \frac{2}{\sqrt{6}} = \sqrt{\frac{2}{3}} \approx 0.8165$$
   得 $\theta \approx 35.26^\circ$。
2. 交线同时位于两晶面内，其方向矢量平行于两法向量的叉积：
   $$\mathbf{n}_1 \times \mathbf{n}_2 = \begin{vmatrix} \hat{\mathbf{x}} & \hat{\mathbf{y}} & \hat{\mathbf{z}} \\ 1 & 1 & 1 \\ 1 & 1 & 0 \end{vmatrix} = (-1, 1, 0)$$
   故交线晶向为 $[\bar{1}10]$（反向为 $[1\bar{1}0]$）。
:::

---

### 知识点 3：晶体对称性与对称操作

#### 概念选择与填空

`CH01-KP3-01`（单选）三维周期晶体中，晶系、布拉伐格子、点群和空间群的数目依次为（ ）。
A. 7，14，32，230
B. 7，14，64，230
C. 6，14，32，230
D. 7，12，32，210

::: details 思路提示
回顾晶体对称分类的四个基本整数。
:::

::: details 参考答案与解析
**参考答案**：A

**解析**：三维周期晶体按对称性划分为 **7 大晶系**（三斜、单斜、正交、四方、三方、六角、立方）、**14 种布拉伐格子**、**32 种宏观晶体学点群**和 **230 种空间群**。
:::

---

`CH01-KP3-02`（填空）判定一个晶体属于立方晶系，其**特征对称元素**是具有 ____ 条 ____ 重旋转对称轴（沿 ____ 晶向族）。

::: details 思路提示
四方晶系也存在一条四重轴，因此四重轴不是立方晶系的唯一充分特征；真正区分立方晶系的特征对称元素沿体对角线分布。
:::

::: details 参考答案与解析
**参考答案**：$4$、$3$、`<111>`

**解析**：立方晶系的特征对称元素是沿立方体 4 条体对角线 `<111>` 方向的 **4 条三重旋转轴**（如正四面体点群 $T$ 虽无四重轴，但因有 4 条三重轴仍属立方晶系）。
:::

---

`CH01-KP3-03`（单选）1984 年谢赫特曼（Shechtman）在急冷铝锰合金的电子衍射花样中发现尖锐的十重（五重）对称衍射斑点，由此确立了**准晶体**。下列关于准晶体的描述正确的是（ ）。
A. 准晶体像玻璃一样属于无序非晶态，既无平移序也无取向序
B. 准晶体具有严格的三维周期平移对称性，只是基元非常复杂
C. 准晶体没有周期平移对称性，但具有长程准周期有序和长程取向序
D. 准晶体的存在说明晶体旋转对称限制定理在数学推导上是错误的

::: details 思路提示
衍射斑点尖锐说明存在长程有序；出现 5 重/10 重对称说明必然打破了严格的周期平移对称。
:::

::: details 参考答案与解析
**参考答案**：C

**解析**：晶体旋转对称限制定理的前提是**严格周期平移对称性**；准晶体打破了周期平移前提（呈准周期排列，如斐波那契序列或彭罗斯拼图），因而允许 5 重、8 重、10 重等旋转对称，同时保持长程取向序，从而产生尖锐的布拉格衍射斑点。
:::

#### 题型一：晶体旋转对称阶数限制定理

`CH01-KP3-04` 从晶格平移周期性出发，证明三维周期晶体中只允许存在 $1, 2, 3, 4, 6$ 重旋转对称轴，不可能存在 $5$ 重或 $n \ge 7$ 重旋转对称轴。

::: details 思路提示
设垂直于旋转轴的平面内有一最短格矢 $\mathbf{a}$，将其绕轴分别顺时针、逆时针旋转角度 $\theta = \frac{2\pi}{n}$，利用旋转后所得矢量之差（或之和）仍必为格矢且平行于 $\mathbf{a}$ 来建立整数约束。
:::

::: details 参考答案与解析
**参考答案**：证明见下（关键方程 $2\cos\theta = m \in \mathbb{Z}$）。

**解析**：
设旋转对称轴垂直于纸面，在该平面内存在最短非零晶格平移矢量 $\mathbf{a}$（设原点 $O$ 及点 $A$ 为格点，$\overrightarrow{OA} = \mathbf{a}$）。
1. 由旋转对称性，分别绕点 $O$ 将 $\mathbf{a}$ 逆时针旋转 $\theta$、顺时针旋转 $\theta$（$\theta = \frac{2\pi}{n}$），所得矢量 $\mathbf{a}'$ 与 $\mathbf{a}''$ 必仍为格矢。
2. 两个格矢之和 $\mathbf{a}' + \mathbf{a}''$ 也必为格矢。由对称性，其方向与 $\mathbf{a}$ 共线，大小为 $2a\cos\theta$。
3. 因为 $\mathbf{a}$ 是该方向上的最短格矢，故 $\mathbf{a}' + \mathbf{a}''$ 必为 $\mathbf{a}$ 的整数倍：
   $$2a\cos\theta = m a \implies \cos\theta = \frac{m}{2} \quad (m \in \mathbb{Z})$$
4. 由 $|\cos\theta| \le 1$，整数 $m$ 只能取 $-2, -1, 0, 1, 2$ 五个值：
   - $m = 2 \implies \cos\theta = 1 \implies \theta = 2\pi$（$n = 1$ 重轴）；
   - $m = 1 \implies \cos\theta = \frac{1}{2} \implies \theta = \frac{\pi}{3}$（$n = 6$ 重轴）；
   - $m = 0 \implies \cos\theta = 0 \implies \theta = \frac{\pi}{2}$（$n = 4$ 重轴）；
   - $m = -1 \implies \cos\theta = -\frac{1}{2} \implies \theta = \frac{2\pi}{3}$（$n = 3$ 重轴）；
   - $m = -2 \implies \cos\theta = -1 \implies \theta = \pi$（$n = 2$ 重轴）。

因此，周期晶体只允许 $1, 2, 3, 4, 6$ 重旋转对称轴，不可能存在 $5$ 重或 $n \ge 7$ 重轴。
:::

---

### 知识点 4：倒格子与布里渊区

![二维正方与六角晶格布里渊区](/figures/ch01-brillouin-2d.svg)

<p class="fig-caption">图 1-2 二维正方晶格的第一、二布里渊区及二维六角晶格的第一布里渊区</p>

#### 概念选择与填空

`CH01-KP4-01`（单选）若某三维晶体的正格子为边长 $a$ 的面心立方（fcc）格子，则其倒格子为（ ）。
A. 边长为 $\frac{2\pi}{a}$ 的面心立方格子
B. 边长为 $\frac{4\pi}{a}$ 的体心立方格子
C. 边长为 $\frac{2\pi}{a}$ 的体心立方格子
D. 边长为 $\frac{4\pi}{a}$ 的简立方格子

::: details 思路提示
牢记对偶关系 `bcc ↔ fcc`，并用原胞体积关系 $\Omega^* = (2\pi)^3/\Omega$ 验算倒格子立方惯用胞边长 $A$。
:::

::: details 参考答案与解析
**参考答案**：B

**解析**：fcc 惯用胞含 4 个格点，原胞体积 $\Omega_{\mathrm{fcc}} = \frac{a^3}{4}$，故倒格子原胞体积 $\Omega^* = \frac{(2\pi)^3}{a^3/4} = \frac{32\pi^3}{a^3}$。倒格子为 bcc 结构（惯用胞含 2 个格点），设其立方边长为 $A$，则 $\frac{A^3}{2} = \frac{32\pi^3}{a^3} \implies A^3 = \left(\frac{4\pi}{a}\right)^3 \implies A = \frac{4\pi}{a}$。
:::

---

`CH01-KP4-02`（填空）第一布里渊区是倒格子中的 ____ 原胞；若正格子原胞体积为 $\Omega$，则第一布里渊区的体积为 ____，第二布里渊区的体积为 ____，第一布里渊区边界上波矢 $\mathbf{k}$ 满足的方程为 ____。

::: details 思路提示
各阶布里渊区都可通过平移倒格矢 $\mathbf{G}$ 完整折合回第一布里渊区，故体积处处相等。
:::

::: details 参考答案与解析
**参考答案**：维格纳-赛茨（Wigner-Seitz）；$\frac{(2\pi)^3}{\Omega}$；$\frac{(2\pi)^3}{\Omega}$；$\mathbf{k}\cdot\mathbf{G} = \frac{1}{2}G^2$（或 $\mathbf{k}\cdot\frac{\mathbf{G}}{2} = \left(\frac{G}{2}\right)^2$）。

**解析**：第一布里渊区由原点到最近邻倒格点连线的中垂面包围而成，即倒格子的 W-S 原胞，其体积等于倒格子原胞体积 $\Omega^* = \frac{(2\pi)^3}{\Omega}$；所有高阶布里渊区经倒格矢平移后均与第一布里渊区一一对应，故体积完全相等。
:::

---

`CH01-KP4-03`（单选）对于晶格常数为 $a$ 的二维正六角（三角）格子，其正格子基矢 $\mathbf{a}_1, \mathbf{a}_2$ 夹角为 $120^\circ$（或 $60^\circ$）。关于其倒格子与第一布里渊区，下列说法正确的是（ ）。
A. 倒格子为二维正方格子
B. 倒格子仍为二维六角格子，倒格矢长度为 $\frac{2\pi}{a}$
C. 倒格子仍为二维六角格子，倒格矢长度为 $\frac{4\pi}{\sqrt{3}a}$，第一布里渊区为正六边形
D. 倒格子为矩形格子，第一布里渊区为菱形

::: details 思路提示
由 $\mathbf{a}_i \cdot \mathbf{b}_j = 2\pi\delta_{ij}$ 计算 $|\mathbf{b}_1| = \frac{2\pi}{a\sin 60^\circ}$。
:::

::: details 参考答案与解析
**参考答案**：C

**解析**：正格子基矢夹角为 $60^\circ$（或 $120^\circ$）时，$\mathbf{b}_1 \perp \mathbf{a}_2$ 且 $\mathbf{a}_1 \cdot \mathbf{b}_1 = a b \cos 30^\circ = 2\pi$，故倒格子基矢长度 $b = \frac{2\pi}{a\cdot \frac{\sqrt{3}}{2}} = \frac{4\pi}{\sqrt{3}a}$，相对正格子旋转 $30^\circ$，仍为二维六角格子，其 W-S 原胞（第一布里渊区）为正六边形（见图 1-2 右）。
:::

#### 题型一：由正格子基矢求倒格子基矢及正倒格子关系证明

`CH01-KP4-04` 已知体心立方（bcc）晶格的立方惯用胞边长为 $a$。
1. 写出其一组标准原胞基矢 $\mathbf{a}_1, \mathbf{a}_2, \mathbf{a}_3$，并计算原胞体积 $\Omega$；
2. 求其倒格子基矢 $\mathbf{b}_1, \mathbf{b}_2, \mathbf{b}_3$，证明 bcc 的倒格子为边长 $\frac{4\pi}{a}$ 的面心立方（fcc）格子；
3. 求 bcc 第一布里渊区的体积。

::: details 思路提示
取体心到三个顶角的矢量 $\mathbf{a}_1 = \frac{a}{2}(-\hat{\mathbf{x}}+\hat{\mathbf{y}}+\hat{\mathbf{z}})$ 等（见图 1-1 左），代入 $\mathbf{b}_1 = 2\pi\frac{\mathbf{a}_2\times\mathbf{a}_3}{\Omega}$ 计算，并将结果与 fcc 原胞基矢对照。
:::

::: details 参考答案与解析
**参考答案**：
1. $\mathbf{a}_1 = \frac{a}{2}(-\hat{\mathbf{x}}+\hat{\mathbf{y}}+\hat{\mathbf{z}}),\ \mathbf{a}_2 = \frac{a}{2}(\hat{\mathbf{x}}-\hat{\mathbf{y}}+\hat{\mathbf{z}}),\ \mathbf{a}_3 = \frac{a}{2}(\hat{\mathbf{x}}+\hat{\mathbf{y}}-\hat{\mathbf{z}})$，$\Omega = \frac{a^3}{2}$；
2. $\mathbf{b}_1 = \frac{2\pi}{a}(\hat{\mathbf{y}}+\hat{\mathbf{z}}),\ \mathbf{b}_2 = \frac{2\pi}{a}(\hat{\mathbf{x}}+\hat{\mathbf{z}}),\ \mathbf{b}_3 = \frac{2\pi}{a}(\hat{\mathbf{x}}+\hat{\mathbf{y}})$，恰为边长 $A=\frac{4\pi}{a}$ 的 fcc 原胞基矢；
3. 第一布里渊区体积 $\Omega^* = \frac{16\pi^3}{a^3}$。

**解析**：
1. 计算混合积得原胞体积：
   $$\mathbf{a}_2 \times \mathbf{a}_3 = \frac{a^2}{4}\begin{vmatrix} \hat{\mathbf{x}} & \hat{\mathbf{y}} & \hat{\mathbf{z}} \\ 1 & -1 & 1 \\ 1 & 1 & -1 \end{vmatrix} = \frac{a^2}{4}(0, 2, 2) = \frac{a^2}{2}(\hat{\mathbf{y}}+\hat{\mathbf{z}})$$
   $$\Omega = \mathbf{a}_1 \cdot (\mathbf{a}_2 \times \mathbf{a}_3) = \frac{a}{2}(-1,1,1)\cdot\frac{a^2}{2}(0,1,1) = \frac{a^3}{2}$$
2. 由倒格子基矢定义：
   $$\mathbf{b}_1 = 2\pi\frac{\mathbf{a}_2\times\mathbf{a}_3}{\Omega} = 2\pi\frac{\frac{a^2}{2}(\hat{\mathbf{y}}+\hat{\mathbf{z}})}{a^3/2} = \frac{2\pi}{a}(\hat{\mathbf{y}}+\hat{\mathbf{z}})$$
   由轮换对称性立得：
   $$\mathbf{b}_2 = \frac{2\pi}{a}(\hat{\mathbf{x}}+\hat{\mathbf{z}}), \quad \mathbf{b}_3 = \frac{2\pi}{a}(\hat{\mathbf{x}}+\hat{\mathbf{y}})$$
   令 $A = \frac{4\pi}{a}$，则 $\mathbf{b}_1 = \frac{A}{2}(\hat{\mathbf{y}}+\hat{\mathbf{z}}),\ \mathbf{b}_2 = \frac{A}{2}(\hat{\mathbf{x}}+\hat{\mathbf{z}}),\ \mathbf{b}_3 = \frac{A}{2}(\hat{\mathbf{x}}+\hat{\mathbf{y}})$，正是边长为 $A = \frac{4\pi}{a}$ 的 fcc 原胞基矢（对照图 1-1 右）。
3. 第一布里渊区体积：
   $$\Omega^* = \frac{(2\pi)^3}{\Omega} = \frac{8\pi^3}{a^3/2} = \frac{16\pi^3}{a^3}$$
:::

---

`CH01-KP4-05` 设正格子以原胞基矢 $\mathbf{a}_1, \mathbf{a}_2, \mathbf{a}_3$ 标定，$(hkl)$ 为互质整数构成的晶面指数。证明：
1. 倒格矢 $\mathbf{G}_{hkl} = h\mathbf{b}_1 + k\mathbf{b}_2 + l\mathbf{b}_3$ 垂直于晶面族 `(hkl)`；
2. 该晶面族相邻晶面的间距为 $d_{hkl} = \frac{2\pi}{|\mathbf{G}_{hkl}|}$。

::: details 思路提示
取离原点最近的 `(hkl)` 晶面，它在三基矢上的截距分别为 $\frac{\mathbf{a}_1}{h}, \frac{\mathbf{a}_2}{k}, \frac{\mathbf{a}_3}{l}$；利用面内任意两个不共线矢量与 $\mathbf{G}_{hkl}$ 的点积为零证明垂直性，再用单位法向量投影求原点到该面的距离。
:::

::: details 参考答案与解析
**参考答案**：证明见下。

**解析**：
1. **证明垂直性**：离原点最近的一张 `(hkl)` 晶面在三基矢上的截距矢量分别为 $\frac{\mathbf{a}_1}{h}, \frac{\mathbf{a}_2}{k}, \frac{\mathbf{a}_3}{l}$。该晶面内两条不共线的矢量可取为 $\frac{\mathbf{a}_1}{h} - \frac{\mathbf{a}_2}{k}$ 与 $\frac{\mathbf{a}_2}{k} - \frac{\mathbf{a}_3}{l}$。利用 $\mathbf{a}_i\cdot\mathbf{b}_j = 2\pi\delta_{ij}$：
   $$\mathbf{G}_{hkl} \cdot \left(\frac{\mathbf{a}_1}{h} - \frac{\mathbf{a}_2}{k}\right) = h\cdot\frac{2\pi}{h} - k\cdot\frac{2\pi}{k} = 0$$
   同理 $\mathbf{G}_{hkl} \cdot \left(\frac{\mathbf{a}_2}{k} - \frac{\mathbf{a}_3}{l}\right) = 0$。故 $\mathbf{G}_{hkl}$ 垂直于 `(hkl)` 晶面族。

2. **证明晶面间距**：由于原点本身位于一张 `(hkl)` 晶面上，原点到上述最近邻 `(hkl)` 晶面的垂直距离即为晶面间距 $d_{hkl}$。取单位法向量 $\hat{\mathbf{n}} = \frac{\mathbf{G}_{hkl}}{|\mathbf{G}_{hkl}|}$，将截距矢量 $\frac{\mathbf{a}_1}{h}$ 沿 $\hat{\mathbf{n}}$ 投影：
   $$d_{hkl} = \frac{\mathbf{a}_1}{h} \cdot \hat{\mathbf{n}} = \frac{\mathbf{a}_1}{h} \cdot \frac{h\mathbf{b}_1 + k\mathbf{b}_2 + l\mathbf{b}_3}{|\mathbf{G}_{hkl}|} = \frac{2\pi}{|\mathbf{G}_{hkl}|}$$
   （当 $h,k,l$ 互质时，原点与该平面之间不含其他格点，故此距离恰为相邻晶面间距。）
:::

#### 题型二：二维布里渊区几何作图与特征距离计算

`CH01-KP4-06` 考虑晶格常数为 $a$ 的二维正方格子（正格子基矢 $\mathbf{a}_1 = a\hat{\mathbf{x}},\ \mathbf{a}_2 = a\hat{\mathbf{y}}$）。
1. 写出其倒格子基矢及最短、次短非零倒格矢；
2. 结合图 1-2（左），求第一布里渊区中心 $\Gamma$ 到边界中点 $X$ 和顶角 $M$ 的距离；
3. 计算第二布里渊区的面积，并验证其与第一布里渊区面积相等。

::: details 思路提示
最短倒格矢有 4 条（沿 $\pm k_x, \pm k_y$），其中垂线围成第一布里渊区；次短倒格矢有 4 条（沿对角线 $\pm\frac{2\pi}{a}\hat{\mathbf{x}} \pm \frac{2\pi}{a}\hat{\mathbf{y}}$），其中垂线围成外侧旋转正方形。
:::

::: details 参考答案与解析
**参考答案**：
1. $\mathbf{b}_1 = \frac{2\pi}{a}\hat{\mathbf{x}},\ \mathbf{b}_2 = \frac{2\pi}{a}\hat{\mathbf{y}}$；最短倒格矢 $(\pm\frac{2\pi}{a},0),(0,\pm\frac{2\pi}{a})$；次短倒格矢 $(\pm\frac{2\pi}{a},\pm\frac{2\pi}{a})$；
2. $|\Gamma X| = \frac{\pi}{a}$，$|\Gamma M| = \frac{\sqrt{2}\pi}{a}$；
3. $S_{\text{2nd}} = S_{\text{1st}} = \left(\frac{2\pi}{a}\right)^2$。

**解析**：
1. 由 $\mathbf{a}_i\cdot\mathbf{b}_j = 2\pi\delta_{ij}$ 得 $\mathbf{b}_1 = \frac{2\pi}{a}\hat{\mathbf{x}},\ \mathbf{b}_2 = \frac{2\pi}{a}\hat{\mathbf{y}}$。
   - 最短非零倒格矢（长度 $\frac{2\pi}{a}$）：$\pm\mathbf{b}_1,\ \pm\mathbf{b}_2$（共 4 条），中垂线为 $k_x = \pm\frac{\pi}{a},\ k_y = \pm\frac{\pi}{a}$；
   - 次短非零倒格矢（长度 $\frac{2\sqrt{2}\pi}{a}$）：$\pm\mathbf{b}_1 \pm \mathbf{b}_2$（共 4 条），中垂线方程为 $|k_x| + |k_y| = \frac{2\pi}{a}$。
2. 第一布里渊区为 $|k_x| \le \frac{\pi}{a},\ |k_y| \le \frac{\pi}{a}$ 的正方形，高对称点坐标 $\Gamma(0,0)$、$X(\frac{\pi}{a},0)$、$M(\frac{\pi}{a},\frac{\pi}{a})$，因此：
   $$|\Gamma X| = \frac{\pi}{a}, \quad |\Gamma M| = \frac{\sqrt{2}\pi}{a}$$
3. 第一布里渊区面积：
   $$S_{\text{1st}} = \left(\frac{2\pi}{a}\right)^2 = \frac{4\pi^2}{a^2}$$
   次短倒格矢中垂线围成的菱形（旋转正方形）两条对角线长均为 $\frac{4\pi}{a}$，其总面积为 $\frac{1}{2}\times\frac{4\pi}{a}\times\frac{4\pi}{a} = \frac{8\pi^2}{a^2}$。扣除第一布里渊区后，第二布里渊区由 4 个等腰直角三角形组成，总面积为：
   $$S_{\text{2nd}} = \frac{8\pi^2}{a^2} - \frac{4\pi^2}{a^2} = \frac{4\pi^2}{a^2} = S_{\text{1st}}$$
:::

---

### 知识点 5：X 射线衍射与几何结构因子

![布拉格反射几何与厄瓦尔德球](/figures/ch01-ewald-bragg.svg)

<p class="fig-caption">图 1-3 X 射线衍射的实空间布拉格几何与倒空间厄瓦尔德球作图</p>

#### 概念选择与填空

`CH01-KP5-01`（单选）关于 X 射线弹性衍射的劳厄方程与布拉格方程，下列说法**错误**的是（ ）。
A. 劳厄方程 $\mathbf{k}' - \mathbf{k} = \mathbf{G}$ 与弹性条件 $|\mathbf{k}'|=|\mathbf{k}|$ 联立等价于布拉格方程 $2d\sin\theta = n\lambda$
B. 发生衍射时，入射波矢 $\mathbf{k}$ 的端点必落在倒空间的某一布里渊区边界上
C. 只有当入射 X 射线波长 $\lambda \le 2d_{\max}$ 时才可能观察到衍射峰
D. 晶体中只要满足布拉格方程的晶面族 `(hkl)`，其衍射峰强度必然不为零

::: details 思路提示
布拉格方程只给出格点周期性导致的相干条件，没有考虑基元内多个原子散射波之间的干涉相消。
:::

::: details 参考答案与解析
**参考答案**：D

**解析**：
- A、B 对：由 $|\mathbf{k}+\mathbf{G}|^2 = k^2 \implies 2\mathbf{k}\cdot\mathbf{G} + G^2 = 0$，即入射波矢满足布里渊区边界方程，且由 $|\Delta\mathbf{k}| = 2k\sin\theta = |\mathbf{G}| = \frac{2\pi n}{d}$ 立即导出 $2d\sin\theta = n\lambda$。
- C 对：由 $\sin\theta = \frac{n\lambda}{2d} \le 1$ 可知，若 $\lambda > 2d_{\max}$，无法发生衍射（可见光波长远大于晶格常数，因此不能产生晶体衍射）。
- D 错：衍射强度 $I \propto |S(\mathbf{G})|^2$，当几何结构因子 $S(\mathbf{G}) = 0$ 时会发生**系统消光**。
:::

---

`CH01-KP5-02`（填空）按立方惯用胞指标 $(hkl)$，在 X 射线粉末衍射中，令 $N = h^2 + k^2 + l^2$：
1. 简立方（sc）前四条允许衍射线的 $N$ 依次为 ____；
2. 体心立方（bcc）前四条允许衍射线的 $N$ 依次为 ____；
3. 面心立方（fcc）前四条允许衍射线的 $N$ 依次为 ____；
4. 金刚石结构前四条允许衍射线的 $N$ 依次为 ____。

::: details 思路提示
逐一检验系统消光条件：sc 无消光（注意 $N=7$ 不能写成三个整数平方和）；bcc 要求 $h+k+l$ 为偶；fcc 要求 $h,k,l$ 全奇或全偶；金刚石在 fcc 基础上排除 $h+k+l = 4m+2$。
:::

::: details 参考答案与解析
**参考答案**：
1. $1,\ 2,\ 3,\ 4$（对应 `(100), (110), (111), (200)`）
2. $2,\ 4,\ 6,\ 8$（对应 `(110), (200), (211), (220)`，比值为 $1:2:3:4$）
3. $3,\ 4,\ 8,\ 11$（对应 `(111), (200), (220), (311)`）
4. $3,\ 8,\ 11,\ 16$（对应 `(111), (220), (311), (400)`；注意 `(200)` 与 `(222)` 消光）

**解析**：在粉末衍射中 $\sin^2\theta = \frac{\lambda^2}{4a^2}(h^2+k^2+l^2) \propto N$，因此上述整数比值是快速识别未知立方晶体结构的标准判据。
:::

---

`CH01-KP5-03`（单选）NaCl 和 KCl 具有完全相同的晶体结构（fcc + 双离子基元），但在 X 射线粉末衍射实验中，NaCl 能观察到 `(111)` 衍射峰，而 KCl 的 `(111)` 衍射峰却几乎消失，其衍射谱表现出类似简立方的特征。其物理原因是（ ）。
A. KCl 实际属于简立方结构而非 NaCl 型结构
B. $\mathrm{K^+}$ 与 $\mathrm{Cl^-}$ 离子半径相近，导致晶格常数缩减一半
C. $\mathrm{K^+}$ 与 $\mathrm{Cl^-}$ 具有相同的核外电子数（均为 18），原子散射因子 $f_{\mathrm{K^+}} \approx f_{\mathrm{Cl^-}}$，使全奇指标结构因子近似为零
D. KCl 吸收了 `(111)` 方向的 X 射线

::: details 思路提示
写出 NaCl 型结构的几何结构因子 $S(hkl) = [f_+ + f_- e^{-i\pi(h+k+l)}] S_{\mathrm{fcc}}(hkl)$，代入全奇指标查看结果。
:::

::: details 参考答案与解析
**参考答案**：C

**解析**：NaCl 型结构可看作 fcc 格子配基元：阳离子在 $(0,0,0)$，阴离子在 $(\frac{1}{2},0,0)$。其结构因子为：
$$S(hkl) = S_{\mathrm{fcc}}(hkl)\left[f_+ + f_- e^{-i\pi(h+k+l)}\right]$$
当 $h,k,l$ 全奇时，$h+k+l$ 为奇数，$S(hkl) = 4(f_+ - f_-)$。对 NaCl，$f_{\mathrm{Na^+}}$（10 电子）与 $f_{\mathrm{Cl^-}}$（18 电子）相差较大，故 `(111)` 有明显衍射；而对 KCl，$\mathrm{K^+}$ 与 $\mathrm{Cl^-}$ 均为 18 电子的等电子体，故 $f_{\mathrm{K^+}} \approx f_{\mathrm{Cl^-}}$，导致 $S(111) \approx 0$，仅余全偶指标，外观与边长为 $a/2$ 的简立方衍射谱一致。
:::

#### 题型一：几何结构因子推导与系统消光判据

`CH01-KP5-04` 将面心立方（fcc）结构和金刚石结构均视为以立方惯用胞为基准的复式格子（设同类原子散射因子为 $f$）：
1. 计算 fcc 结构的几何结构因子 $S_{\mathrm{fcc}}(hkl)$，导出其消光条件；
2. 利用基元分解，计算金刚石结构的几何结构因子 $S_{\mathrm{dia}}(hkl)$，说明为何 `(200)` 和 `(222)` 晶面发生消光而 `(111)` 与 `(220)` 不消光。

::: details 思路提示
先写出 fcc 惯用胞内 4 个原子的分数坐标；金刚石结构是在 fcc 每个格点上挂 2 个原子 $(0,0,0)$ 和 $(\frac{1}{4},\frac{1}{4},\frac{1}{4})$，故其结构因子可分解为“基元因子 × fcc 因子”的乘积。
:::

::: details 参考答案与解析
**参考答案**：
1. $S_{\mathrm{fcc}}(hkl) = f\left[1 + e^{-i\pi(h+k)} + e^{-i\pi(k+l)} + e^{-i\pi(l+h)}\right]$；$h,k,l$ 全奇或全偶时 $S_{\mathrm{fcc}} = 4f$，奇偶混杂时 $S_{\mathrm{fcc}} = 0$。
2. $S_{\mathrm{dia}}(hkl) = S_{\mathrm{fcc}}(hkl)\left[1 + e^{-i\frac{\pi}{2}(h+k+l)}\right]$；在 fcc 允许条件下，$h+k+l = 4m+2$ 时消光。

**解析**：
1. **fcc 结构**：惯用胞内 4 个原子分数坐标为 $(0,0,0),\ (\frac{1}{2},\frac{1}{2},0),\ (0,\frac{1}{2},\frac{1}{2}),\ (\frac{1}{2},0,\frac{1}{2})$，故：
   $$S_{\mathrm{fcc}}(hkl) = f\left[1 + e^{-i\pi(h+k)} + e^{-i\pi(k+l)} + e^{-i\pi(l+h)}\right]$$
   - 若 $h,k,l$ 全奇或全偶，则 $h+k,\ k+l,\ l+h$ 均为偶数，各项均为 $+1$，$S_{\mathrm{fcc}} = 4f$；
   - 若 $h,k,l$ 奇偶混杂（一奇两偶或两奇一偶），则 $h+k,\ k+l,\ l+h$ 中必有两奇一偶，指数项为 $1 + 1 - 1 - 1 = 0$，发生系统消光。

2. **金刚石结构**：由两套 fcc 相对平移 $(\frac{1}{4},\frac{1}{4},\frac{1}{4})$ 构成，故：
   $$S_{\mathrm{dia}}(hkl) = S_{\mathrm{fcc}}(hkl)\left[1 + e^{-i\frac{\pi}{2}(h+k+l)}\right]$$
   仅在 $h,k,l$ 全奇或全偶时 $S_{\mathrm{fcc}} = 4f \ne 0$，此时分情况讨论基元因子 $B = 1 + (-i)^{h+k+l}$：
   - **$h,k,l$ 全奇**：$h+k+l$ 为奇数，$B = 1 \pm i \ne 0$，$|S_{\mathrm{dia}}| = 4\sqrt{2}f$，**不消光**（如 `(111)`）；
   - **$h,k,l$ 全偶且 $h+k+l = 4m$**：$B = 1 + 1 = 2$，$|S_{\mathrm{dia}}| = 8f$，**不消光**（如 `(220)`，$2+2+0=4$）；
   - **$h,k,l$ 全偶且 $h+k+l = 4m+2$**：$B = 1 - 1 = 0$，$S_{\mathrm{dia}} = 0$，**发生消光**（如 `(200)` 和 `(222)`，$h+k+l$ 分别为 $2$ 和 $6$）。
:::

#### 题型二：X 射线粉末衍射谱指标化与晶格常数计算

`CH01-KP5-05` 用波长 $\lambda = 1.5418\ \text{Å}$（$\mathrm{Cu}\ K_\alpha$）的 X 射线对某未知立方单质金属粉末进行衍射实验，测得小角端前四条衍射线的衍射角 $2\theta$ 依次为：
$$2\theta_1 = 43.35^\circ,\quad 2\theta_2 = 50.49^\circ,\quad 2\theta_3 = 74.19^\circ,\quad 2\theta_4 = 90.03^\circ$$
1. 通过计算 $\sin^2\theta$ 的比值，判定该金属的布拉伐格子类型（sc、bcc 或 fcc）；
2. 写出这四条衍射线对应的晶面指数 `(hkl)`；
3. 计算该金属的晶格常数 $a$ 及最近邻原子间距 $d_{\mathrm{nn}}$。

::: details 思路提示
由立方晶系布拉格方程得 $\sin^2\theta = \frac{\lambda^2}{4a^2}(h^2+k^2+l^2)$。先算 $\theta_i = (2\theta_i)/2$ 与 $\sin^2\theta_i$，再全部除以 $\sin^2\theta_1$ 看其比例接近 `1:2:3:4`（sc/bcc）还是 `3:4:8:11`（fcc）。
:::

::: details 参考答案与解析
**参考答案**：
1. 面心立方（fcc）；
2. `(111)`、`(200)`、`(220)`、`(311)`；
3. $a \approx 3.615\ \text{Å}$，$d_{\mathrm{nn}} \approx 2.556\ \text{Å}$（该金属为铜 Cu）。

**解析**：
1. 列出各衍射线的 $\theta$、$\sin^2\theta$ 及归一化比值：

   | 序号 | $2\theta$ | $\theta$ | $\sin^2\theta$ | $\sin^2\theta / \sin^2\theta_1$ | 乘以 $3$ | $N = h^2+k^2+l^2$ | `(hkl)` |
   | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
   | 1 | $43.35^\circ$ | $21.675^\circ$ | $0.1364$ | $1.000$ | $3.00$ | $3$ | `(111)` |
   | 2 | $50.49^\circ$ | $25.245^\circ$ | $0.1819$ | $1.334$ | $4.00$ | $4$ | `(200)` |
   | 3 | $74.19^\circ$ | $37.095^\circ$ | $0.3638$ | $2.667$ | $8.00$ | $8$ | `(220)` |
   | 4 | $90.03^\circ$ | $45.015^\circ$ | $0.5002$ | $3.667$ | $11.00$ | $11$ | `(311)` |

   比值严格符合 $3:4:8:11$，满足 $h,k,l$ 全奇或全偶的消光规律，故该金属为**面心立方（fcc）**结构。

2. 对应晶面指数依次为 `(111)`、`(200)`、`(220)`、`(311)`。

3. 由 $a = \frac{\lambda\sqrt{N}}{2\sin\theta}$，取第一条线 `(111)`（$N = 3$）计算：
   $$a = \frac{1.5418 \times \sqrt{3}}{2\sin 21.675^\circ} \approx \frac{2.6705}{0.7387} \approx 3.615\ \text{Å}$$
   （其余三条线算得结果均为 $3.615\ \text{Å}$。）
   fcc 结构的最近邻原子间距为：
   $$d_{\mathrm{nn}} = \frac{\sqrt{2}}{2}a = \frac{\sqrt{2}}{2} \times 3.615\ \text{Å} \approx 2.556\ \text{Å}$$
:::
