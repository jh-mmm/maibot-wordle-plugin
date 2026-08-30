# 🎮 MaiBot Wordle 猜单词插件

<p align="center">
  <img src="./assets/icon.svg" width="96" height="96" alt="Wordle Icon" onerror="this.style.display='none'"/>
</p>

<p align="center">
  <strong>经典的 5 字母 Wordle 猜单词游戏，为 MaiBot 提供极简无干扰的群聊互动体验</strong>
</p>

<p align="center">
  <a href="https://github.com/jh-mmm/maibot-wordle-plugin/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License"></a>
  <a href="https://docs.mai-mai.org/plugin/"><img src="https://img.shields.io/badge/MaiBot-Plugin%20SDK%20v2-blue.svg" alt="SDK"></a>
  <a href="https://plugins.maibot.chat/"><img src="https://img.shields.io/badge/MaiBot-Plugin%20Store-purple.svg" alt="Plugin Center"></a>
</p>

---

## ✨ 核心特性

- 🎯 **标准 Wordle 规则与判定**：严格遵循官方判定算法，完美处理重复字母匹配与余量着色，无任何误判。
- 🎨 **极简 6x5 矩阵卡片**：基于 `ctx.render.html2png` 生成现代极简质感的高清对战卡片，去除冗余键盘与干扰元素。
- 💬 **自然极简交互**：开局后直接在群聊中发送 **5 字母英文单词**（如 `CLASH` 或 `FIRST`）即可直接触发猜测。
- 🛡️ **双模自动降级**：当宿主环境未安装渲染内核时，自动无缝降级为 Emoji 文本棋盘（`🟩🟨⬛`），保证 100% 可用性。
- 📖 **中英音标与释义学习**：收录 3,100+ 目标词典（支持仅限四六级 1,000+ 核心词开关）与 14,800+ 检验词库，游戏结算时展示音标、词性及中文含义，娱乐与学习兼备。
- 📊 **多维度战绩统计**：自动记录玩家与群聊总场次、胜率、当前连胜、最高连胜及 1~6 步猜词分布图表。
- 🤖 **大模型 Tool 深度集成**：声明 `@Tool("wordle_game")`，支持在自然语言对话中让 Maisaka 陪玩或协助猜词。
- 💾 **跨重启持久化**：游戏会话与玩家统计数据自动持久化保存于 `ctx.paths.data_dir`，Bot 重启不丢局。

---

## 🕹️ 游戏规则

系统随机生成一个 **5 字母** 的秘密英文单词，玩家有 **6 次** 猜测机会：

| 颜色标记 | 状态 | 含义 |
| :--- | :--- | :--- |
| 🟩 **绿色** | `Correct` | 字母与位置**完全正确** |
| 🟨 **黄色** | `Present` | 字母在单词中，但**位置不正确** |
| ⬛ **灰色** | `Absent` | 字母**不在单词中**（或多次出现已被扣除） |

---

## ⌨️ 常用命令

| 命令 / 输入 | 缩写 / 示例 | 说明 |
| :--- | :--- | :--- |
| `/wordle` | `/w`, `/guess` | 发起一局新游戏 / 查看当前棋盘 |
| 直接发送 5 字母单词 | `CLASH`, `first`, `/wordle apple` | 进行 5 字母猜测（需开启 `allow_direct_guess`） |
| `/wordle hint` | `/w hint` | 获取线索提示（首字母或词义线索） |
| `/wordle stop` | `/w stop` | 认输并揭晓正确单词与详细释义 |
| `/wordle restart` | `/w restart` | 放弃当前局并重新开启一局新游戏 |
| `/wordle stats` | `/wordle stat`, `/w stats` | 查看个人胜率、连胜记录与步数分布图 |
| `/wordle help` | `/w help` | 查看玩法规则与指令说明 |

---

## ⚙️ 配置文件说明

插件首次运行会在对应插件目录生成 `config.toml`，也可在 WebUI 的 **插件管理** 界面进行可视化配置：

```toml
[plugin]
config_version = "1.0.0"

[game]
# 最大猜测次数（默认 6）
max_attempts = 6

# 是否要求猜测必须是有效英文单词（默认开启）
enforce_dictionary = true

# 是否允许获取游戏提示（默认开启）
allow_hints = true

# 每局最多允许获取提示次数（默认 2 次）
max_hints_per_game = 2

# 未操作超时自动结算时间（分钟，默认 15 分钟）
session_timeout_minutes = 15

# 有进行中游戏时，直接发送 5 字母单词是否自动识别为猜测（默认开启）
allow_direct_guess = true

# 是否仅抽取大学英语四六级 (CET-4/6) 词汇作为目标单词（默认关闭，开启可避免偏门生僻词）
cet_only = false

[display]
# 是否优先使用 HTML 转图片卡片展示（默认开启，失败时自动降级为 Emoji 文本棋盘）
use_image_render = true

# 游戏结束时是否显示单词中文释义与音标（默认开启）
show_definition = true

[access]
group_mode = "off"          # off=不限制 | whitelist=仅名单内群 | blacklist=名单内群不启用
group_whitelist = ["123456789"]
group_blacklist = []
user_mode = "off"           # off=不限制 | whitelist=仅名单内用户 | blacklist=名单内用户不启用
user_whitelist = []
user_blacklist = ["10001"]
```

---

## 🛡️ 访问控制：群 / 用户黑白名单

在 `[access]` 段可以按**群号**和**用户 QQ 号**两个维度限制哪些消息或群聊可以使用 Wordle 插件。

```toml
[access]
group_mode = "off"          # off=不限制 | whitelist=仅名单内群 | blacklist=名单内群不启用
group_whitelist = ["123456789"]
group_blacklist = []
user_mode = "off"           # off=不限制 | whitelist=仅名单内用户 | blacklist=名单内用户不启用
user_whitelist = []
user_blacklist = ["10001"]
```

### 规则说明

- **两个维度是「与」关系**：群维度和用户维度都通过，才允许发起或参与 Wordle 游戏。
- **同一维度同一时刻只有一份名单生效**：由该维度的 `mode` 决定；`mode = "off"` 时忽略两份名单。
- **`whitelist` 模式下名单为空 = 全部拒绝**。如需放行所有人/群请将 `mode` 设为 `"off"`，避免留空白名单。
- **私聊不受群名单影响**：私聊消息没有群号，群维度自动跳过；用户名单在群聊和私聊中均生效。
- **非侵入式放行**：被名单拦截的消息会正常交给麦麦 AI 或其他插件处理，Wordle 插件完全隐形不打扰。
- **号码格式**：名单里的号码建议写成**字符串**（如 `["123456789"]`）。

#### 配置示例：仅在指定群开启并拉黑个别用户

```toml
[access]
group_mode = "whitelist"
group_whitelist = ["123456789", "987654321"]
user_mode = "blacklist"
user_blacklist = ["10001"]
```

---

## 📦 安装方式

### 方式一：插件市场安装（推荐）
1. 打开 MaiBot WebUI，进入 **插件市场**。
2. 搜索 `Wordle 猜单词` 或 `jh-mmm.maibot-wordle-plugin`。
3. 点击 **安装** 即可。

### 方式二：手动安装
将本项目克隆或解压至 MaiBot 的 `plugins/` 目录下：
```bash
cd MaiBot/plugins
git clone https://github.com/jh-mmm/maibot-wordle-plugin.git wordle-plugin
```
启动 MaiBot 即可自动加载。

---

## 📄 开源许可证与更新日志

- 本项目基于 [MIT License](LICENSE) 开源。
- 第三方数据与词库引用详见 [THIRD_PARTY_LICENSES.md](THIRD_PARTY_LICENSES.md)。
- 版本更新历史详见 [CHANGELOG.md](CHANGELOG.md)。
