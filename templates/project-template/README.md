# <PROJECT_NAME>

用一句话说明项目面向谁、解决什么问题，以及带来什么价值。

> 使用模板后，先替换所有 `<PLACEHOLDER>`，确认许可证与安全联系渠道，再开始业务开发。

## Status

`Planning` | `In Development` | `Demo Available` | `Portfolio Ready`

当前状态：`<CURRENT_STATUS>`

## Problem

- **目标用户**：`<TARGET_USERS>`
- **核心问题**：`<PROBLEM_STATEMENT>`
- **解决方案**：`<SOLUTION_SUMMARY>`
- **成功指标**：`<SUCCESS_METRICS>`

## Features

- `<CORE_FEATURE_1>`
- `<CORE_FEATURE_2>`
- `<CORE_FEATURE_3>`

## Tech Stack

查看 [TECH_STACK.md](TECH_STACK.md) 获取技术选型、版本和决策依据。

## Project Structure

```text
.
├── .github/
│   ├── ISSUE_TEMPLATE/
│   └── PULL_REQUEST_TEMPLATE.md
├── docs/
│   ├── adr/
│   ├── API.md
│   ├── ARCHITECTURE.md
│   ├── DATABASE.md
│   └── PRODUCT.md
├── src/
├── tests/
├── .editorconfig
├── .gitattributes
├── .gitignore
├── AGENTS.md
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── PROJECT_RULES.md
├── SECURITY.md
├── SUPPORT.md
├── TASKS.md
├── TECH_STACK.md
└── README.md
```

## Template Setup Checklist

- [ ] 替换所有占位符并删除不适用的示例。
- [ ] 确认目标用户、范围、非目标和成功指标。
- [ ] 更新 `LICENSE` 的年份与版权主体，或选择适合项目的许可证。
- [ ] 在 `SECURITY.md` 中配置私密漏洞报告地址。
- [ ] 根据技术栈配置格式、静态检查、测试、构建和安全 CI。
- [ ] 配置 Dependabot、secret scanning、push protection 和 `main` 分支规则。
- [ ] 验证安装、运行、测试、Demo 和全部文档链接。

## Quick Start

### Prerequisites

- `<RUNTIME_AND_VERSION>`
- `<PACKAGE_MANAGER_AND_VERSION>`
- `<REQUIRED_SERVICES>`

### Installation

```bash
<INSTALL_COMMAND>
```

### Configuration

复制环境变量示例并填写本地配置。不要提交真实密钥。

```bash
<CONFIGURATION_COMMAND>
```

### Run

```bash
<RUN_COMMAND>
```

### Test

```bash
<TEST_COMMAND>
```

## Documentation

- [Product](docs/PRODUCT.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Database](docs/DATABASE.md)
- [API](docs/API.md)
- [Architecture Decisions](docs/adr/)
- [Tasks](TASKS.md)
- [Changelog](CHANGELOG.md)
- [Contributing](CONTRIBUTING.md)
- [Security](SECURITY.md)
- [Support](SUPPORT.md)

## Demo

- **Live Demo**：`<DEMO_URL>`
- **Demo Video**：`<VIDEO_URL>`

## Quality Evidence

- Tests：`<TEST_SUMMARY>`
- Performance：`<PERFORMANCE_RESULT>`
- Security：`<SECURITY_CHECKS>`
- Known limitations：`<KNOWN_LIMITATIONS>`

## License

默认提供 MIT License。发布前确认 [LICENSE](LICENSE) 与项目实际授权方式一致。
