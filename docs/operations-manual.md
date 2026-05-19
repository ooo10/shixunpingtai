# AIGC实训平台 - 运维手册

## 目录
1. 部署指南
2. 运维命令
3. 监控与告警
4. 故障排查
5. 回滚方案
6. 备份与恢复

---

## 1. 部署指南

### 1.1 环境要求
- Kubernetes 1.20+
- Docker 20.10+
- Helm 3.0+（可选）

### 1.2 部署步骤

```bash
# 1. 创建命名空间
kubectl apply -f k8s/namespace.yaml

# 2. 创建密钥（需要提前base64编码）
echo -n "your-api-key" | base64
kubectl apply -f k8s/secrets.yaml

# 3. 部署后端服务
kubectl apply -f k8s/backend-deployment.yaml
kubectl apply -f k8s/backend-service.yaml

# 4. 部署前端服务
kubectl apply -f k8s/frontend-deployment.yaml
kubectl apply -f k8s/frontend-service.yaml

# 5. 验证部署
kubectl get pods -n aigc-training
kubectl get services -n aigc-training
```

### 1.3 镜像构建与推送

```bash
# 后端镜像
cd backend
docker build -t registry.example.com/aigc-backend:v1.0.0 .
docker push registry.example.com/aigc-backend:v1.0.0

# 前端镜像
docker build -f Dockerfile.frontend -t registry.example.com/aigc-frontend:v1.0.0 .
docker push registry.example.com/aigc-frontend:v1.0.0
```

---

## 2. 运维命令

### 2.1 查看状态

```bash
# 查看Pod状态
kubectl get pods -n aigc-training

# 查看服务状态
kubectl get services -n aigc-training

# 查看部署状态
kubectl get deployments -n aigc-training

# 查看日志
kubectl logs -n aigc-training <pod-name> -f

# 执行命令
kubectl exec -n aigc-training <pod-name> -- <command>
```

### 2.2 扩缩容

```bash
# 后端扩容到5个副本
kubectl scale deployment/aigc-training-backend --replicas=5 -n aigc-training

# 前端扩容到4个副本
kubectl scale deployment/aigc-training-frontend --replicas=4 -n aigc-training
```

### 2.3 更新镜像

```bash
# 更新后端镜像
kubectl set image deployment/aigc-training-backend backend=registry.example.com/aigc-backend:v1.1.0 -n aigc-training

# 更新前端镜像
kubectl set image deployment/aigc-training-frontend frontend=registry.example.com/aigc-frontend:v1.1.0 -n aigc-training
```

---

## 3. 监控与告警

### 3.1 监控指标

| 指标 | 说明 | 告警阈值 |
|------|------|----------|
| CPU使用率 | 容器CPU使用百分比 | >80%持续5分钟 |
| 内存使用率 | 容器内存使用百分比 | >85%持续5分钟 |
| 请求延迟 | API响应时间 | P95 > 2s |
| 错误率 | HTTP 5xx错误占比 | >5% |
| Pod存活数 | 运行中的Pod数量 | < 最小副本数 |

### 3.2 Prometheus配置

```yaml
scrape_configs:
  - job_name: 'aigc-backend'
    kubernetes_sd_configs:
      - role: pod
        namespaces:
          names: ['aigc-training']
    relabel_configs:
      - source_labels: [__meta_kubernetes_pod_label_app]
        regex: backend
        action: keep
```

### 3.3 Grafana仪表盘

仪表盘应包含：
- 请求量趋势
- 响应时间分布
- 错误率监控
- 资源使用率
- API调用次数统计

---

## 4. 故障排查

### 4.1 Pod启动失败

```bash
# 查看Pod详细信息
kubectl describe pod <pod-name> -n aigc-training

# 查看事件
kubectl get events -n aigc-training

# 常见原因
# 1. 镜像拉取失败 - 检查镜像名称和凭证
# 2. 资源不足 - 检查节点资源
# 3. 配置错误 - 检查环境变量和配置文件
```

### 4.2 API服务不可用

```bash
# 检查服务是否正常
kubectl port-forward service/backend 8000:8000 -n aigc-training
curl http://localhost:8000/health

# 检查Pod日志
kubectl logs -n aigc-training <backend-pod-name>
```

### 4.3 前端页面无法访问

```bash
# 检查前端服务端口
kubectl get service frontend -n aigc-training

# 检查Ingress配置（如有）
kubectl get ingress -n aigc-training

# 检查前端Pod日志
kubectl logs -n aigc-training <frontend-pod-name>
```

---

## 5. 回滚方案

### 5.1 手动回滚

```bash
# 查看部署历史
kubectl rollout history deployment/aigc-training-backend -n aigc-training

# 回滚到上一版本
kubectl rollout undo deployment/aigc-training-backend -n aigc-training

# 回滚到指定版本
kubectl rollout undo deployment/aigc-training-backend --to-revision=3 -n aigc-training

# 前端回滚
kubectl rollout undo deployment/aigc-training-frontend -n aigc-training
```

### 5.2 自动回滚条件

Kubernetes自动回滚触发条件：
- livenessProbe失败超过阈值
- readinessProbe失败超过阈值
- Pod启动失败次数过多

### 5.3 回滚验证

```bash
# 验证回滚状态
kubectl rollout status deployment/aigc-training-backend -n aigc-training

# 检查当前版本
kubectl describe deployment/aigc-training-backend -n aigc-training | grep Image
```

---

## 6. 备份与恢复

### 6.1 数据备份

```bash
# 备份MySQL数据库
kubectl exec -n aigc-training <mysql-pod> -- mysqldump -u root -p<password> aigc > backup.sql

# 备份配置文件
kubectl get secrets -n aigc-training -o yaml > secrets-backup.yaml
kubectl get configmaps -n aigc-training -o yaml > configmaps-backup.yaml
```

### 6.2 数据恢复

```bash
# 恢复数据库
kubectl exec -i -n aigc-training <mysql-pod> -- mysql -u root -p<password> aigc < backup.sql

# 恢复配置
kubectl apply -f secrets-backup.yaml
kubectl apply -f configmaps-backup.yaml
```

### 6.3 备份策略

| 备份类型 | 频率 | 保留期限 |
|----------|------|----------|
| 数据库全量备份 | 每日0点 | 7天 |
| 数据库增量备份 | 每小时 | 24小时 |
| 配置文件备份 | 部署前 | 版本控制 |

---

## 7. 紧急联系

| 角色 | 联系方式 |
|------|----------|
| 开发负责人 | 138xxxx1234 |
| 运维负责人 | 139xxxx5678 |
| 7x24值班 | 137xxxx9012 |

---

**文档版本**: v1.0.0  
**更新时间**: 2026-05-18