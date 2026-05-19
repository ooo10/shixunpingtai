# 部署到 GitHub Pages

## 概述

本项目支持通过 GitHub Actions 自动部署到 GitHub Pages。

## 前置条件

1. 已创建 GitHub 仓库
2. 仓库已启用 GitHub Pages（Settings > Pages）
3. Node.js 18+ 环境

## 配置步骤

### 1. 启用 GitHub Pages

1. 进入仓库 Settings
2. 找到 Pages 选项
3. Source 选择 `GitHub Actions`

### 2. 配置环境变量（可选）

如需配置自定义域名或其他环境变量，在仓库 Settings > Secrets and variables > Actions 中添加：

| 变量名 | 说明 |
|--------|------|
| `CUSTOM_DOMAIN` | 自定义域名 |

### 3. 手动部署命令

```bash
# 安装依赖
npm install

# 构建项目
npm run build

# 部署到 GitHub Pages
npm run deploy
```

## GitHub Actions 自动部署

项目已配置自动部署工作流，推送到 `main` 分支时自动触发。

### 工作流文件

- `.github/workflows/deploy.yml` - 前端部署工作流
- `.github/workflows/backend.yml` - 后端测试工作流

### 部署状态

部署成功后，可在以下地址访问：

```
https://<username>.github.io/<repository>/
```

例如：`https://yourname.github.io/aigc-training-platform/`

## 部署结构

```
├── .github/
│   └── workflows/
│       ├── deploy.yml      # 前端部署工作流
│       └── backend.yml     # 后端CI工作流
├── dist/                   # 构建产物（自动生成）
├── vite.config.js          # Vite配置（包含base路径）
└── package.json            # 包含deploy脚本
```

## 注意事项

1. **base路径配置**: `vite.config.js` 中已配置 `base: '/aigc-training-platform/'`
2. **路由模式**: 使用 `history` 模式时需配置 404 回退
3. **API代理**: GitHub Pages 仅支持静态文件，后端API需部署到其他服务器

## 后端部署

后端服务建议部署到以下平台：

- **Vercel** - 免费额度充足
- **Render** - 支持 Python 后端
- **Heroku** - 经典 PaaS 平台
- **AWS EC2** - 灵活配置

部署后更新前端的 API 地址配置。

## 故障排查

### 部署失败

1. 检查 Actions 日志
2. 确保 `npm run build` 能正常运行
3. 检查 `dist` 目录是否正确生成

### 页面空白

1. 检查浏览器控制台错误
2. 确认 base 路径配置正确
3. 检查资源加载路径

### 路由404

1. 使用 Hash 模式或配置 404 回退
2. 在 GitHub Pages 设置中配置自定义 404 页面

---

**文档版本**: v1.0.0  
**更新时间**: 2026-05-18