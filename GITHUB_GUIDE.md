# GitHub Guide

本指南说明如何把 GitHub 仓库维护为可信、可运行、可协作、可长期演进的高质量项目。它适用于 Portfolio、商业项目和开源项目。

## 1. 建立清晰的仓库目标

- 用一句话说明目标用户、问题和价值。
- 在 README 顶部提供状态、Demo、技术栈和快速开始入口。
- 明确 MVP、非目标、已知限制和维护状态。
- 每个业务项目使用独立仓库；本实验室负责规划、标准和状态管理。
- 从 [`templates/project-template`](templates/project-template/) 创建新项目基础结构。

## 2. 使用标准文件结构

高质量项目至少考虑以下文件：

```text
README.md
LICENSE
.gitignore
CHANGELOG.md
CONTRIBUTING.md
CODE_OF_CONDUCT.md
SECURITY.md
AGENTS.md
PROJECT_RULES.md
TASKS.md
TECH_STACK.md
docs/
src/
tests/
```

不适用的文件可以省略，但必须确保用户能够理解、运行、测试和安全报告项目。

## 3. 维护高质量 README

README 应回答：

- 项目解决什么问题，适合谁使用？
- 当前状态和主要功能是什么？
- 如何安装、配置、运行和测试？
- 架构和技术栈在哪里说明？
- Demo、截图或演示视频在哪里？
- 有哪些已知限制和安全注意事项？
- 如何贡献、报告问题和查看许可证？

所有命令和链接应在干净环境中验证。不要在 README 中展示无法复现的结果或虚构指标。

## 4. 管理 Issue 与任务

- 每个 Issue 只描述一个问题、需求或决策。
- 提供背景、目标、非目标、验收标准和复现证据。
- 使用 P0–P3 优先级和类型标签，例如 bug、feature、docs、security。
- 使用里程碑组织可交付版本，不让 backlog 变成无期限愿望列表。
- 及时关闭 duplicate、invalid 或不再计划的事项，并说明原因。
- 将内部执行状态同步到 `TASKS.md`，避免多处信息冲突。

## 5. 分支策略

- 使用 `main` 作为稳定、可发布的默认分支。
- 功能、修复和文档使用短生命周期分支。
- 推荐分支名：`feature/<name>`、`fix/<name>`、`docs/<name>`、`refactor/<name>`。
- 定期与目标分支同步，尽早解决冲突。
- 保护 `main`，限制强制推送和删除，并要求必要检查。
- 不保留已经合并且不再需要的远端分支。

## 6. 提交规范

- 每个提交只表达一个逻辑目的，并保持可评审和可回滚。
- 使用祈使句描述结果，例如 `Add user authentication`。
- 提交前检查 `git status`、`git diff` 和暂存内容。
- 不提交密钥、生产配置、依赖目录、构建产物或临时文件。
- 不用无意义信息，例如 `update`、`fix stuff` 或 `changes`。
- 重要提交应能关联到 Issue、需求或决策记录。

## 7. Pull Request 规范

PR 描述至少包含：

- **What**：修改了什么。
- **Why**：为什么需要修改。
- **Impact**：对用户、API、数据和兼容性的影响。
- **Validation**：运行了哪些检查和结果。
- **Risk**：已知风险、迁移和回滚方式。
- **Evidence**：截图、Demo、日志或指标。

使用 [`CODE_REVIEW_CHECKLIST.md`](CODE_REVIEW_CHECKLIST.md) 自查和评审。PR 保持小而聚焦；发现无关问题时另建任务。

## 8. 自动化质量门禁

根据技术栈配置 GitHub Actions，至少考虑：

- 格式检查和静态分析。
- 单元、集成和适用的端到端测试。
- 构建与打包验证。
- 依赖、许可证、秘密和代码安全扫描。
- 文档链接或 Markdown 检查。
- 部署预览或发布候选验证。

仅授予 Actions 必要的 `GITHUB_TOKEN` 权限。固定第三方 Actions 的可信版本或提交 SHA，不让 CI 访问不必要的生产秘密。

## 9. 安全维护

- 执行 [`SECURITY_CHECKLIST.md`](SECURITY_CHECKLIST.md)。
- 启用适用的 Dependabot、secret scanning、push protection 和 code scanning。
- 建立 `SECURITY.md`，为漏洞提供私密报告渠道。
- 定期检查依赖、Actions、Deploy Keys、OAuth Apps 和协作者权限。
- 密钥泄露后立即撤销和轮换，不能只删除文件。
- 使用 GitHub Security Advisory 私密协作处理公开仓库漏洞。

部分安全功能取决于仓库可见性、账号方案和组织配置；以 GitHub 当前设置页面为准。

## 10. 文档与决策同步

- 产品范围变化时更新产品文档和验收标准。
- 架构、API、数据或技术栈变化时同步对应文档。
- 用户或维护者可见变化记录到 `CHANGELOG.md`。
- 使用 ADR 记录关键技术决策、替代方案和后果。
- 文档必须与实际代码、配置和部署行为一致。
- 删除失效说明，不让历史文档被误认为当前事实。

## 11. 版本与发布

- 使用语义化版本管理公开接口和兼容性。
- 从可重复构建且已验证的提交创建 tag 和 Release。
- 发布说明包含新增、变更、修复、安全、迁移和已知问题。
- 在发布前验证安装、升级、数据库迁移和回滚。
- 保存构建、测试、审批和部署证据。
- 维护受支持版本和弃用时间表。

## 12. 开源协作

- 提供 LICENSE、CONTRIBUTING、CODE_OF_CONDUCT 和 SECURITY 文档。
- 使用 Issue/PR 模板减少信息缺失。
- 标记适合新贡献者的 `good first issue`，但确保任务真实可完成。
- 对贡献提供尊重、具体且及时的反馈。
- 合并前检查范围、测试、文档、许可证和维护成本。
- 公开路线图和支持边界，不承诺无法维护的功能或期限。

## 13. Portfolio 展示标准

- 仓库必须可运行、可测试、可演示，而不只是代码快照。
- README 清楚说明个人贡献、关键决策和结果。
- 使用真实数据、性能、用户反馈或质量证据说明价值。
- 提供稳定 Demo 或可信演示视频与截图。
- 保留清晰提交历史，展示迭代和问题解决过程。
- 在 [`PORTFOLIO_STATUS.md`](PORTFOLIO_STATUS.md) 中同步完成度和简历价值。

## 14. 维护节奏

### 每次变更

- 检查差异、测试、文档、安全和 Changelog。
- 通过 PR 或明确的评审流程合并。

### 每周

- 清理 Issue/PR、BLOCKED 任务和失败 CI。
- 检查依赖、安全告警和 Demo 可用性。

### 每个版本

- 完成回归、安全、部署和回滚验证。
- 更新版本、Changelog、Release 和 Portfolio 状态。

### 每季度

- 审查仓库权限、依赖健康、文档准确性和项目维护价值。
- 归档长期无价值或无法维护的项目。

## 高质量仓库完成定义

一个仓库只有同时满足以下条件，才可以标记为 Portfolio Ready：

- [ ] 目标、用户、价值和范围清晰。
- [ ] 安装、运行、测试和 Demo 已验证。
- [ ] 核心代码有测试、评审和安全证据。
- [ ] 文档、API、数据和部署信息准确。
- [ ] 许可证、贡献和安全报告方式明确。
- [ ] 发布、监控、回滚和维护责任清晰。
- [ ] 项目成果真实、可解释且适合目标岗位展示。

## 相关文档

- [`DEVELOPMENT_WORKFLOW.md`](DEVELOPMENT_WORKFLOW.md)
- [`CODE_REVIEW_CHECKLIST.md`](CODE_REVIEW_CHECKLIST.md)
- [`SECURITY_CHECKLIST.md`](SECURITY_CHECKLIST.md)
- [`PORTFOLIO_MISSION.md`](PORTFOLIO_MISSION.md)
- [`PROJECT_ROADMAP.md`](PROJECT_ROADMAP.md)
- [`PORTFOLIO_STATUS.md`](PORTFOLIO_STATUS.md)
