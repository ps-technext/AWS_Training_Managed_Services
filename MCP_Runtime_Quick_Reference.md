# MCP Runtime Quick Reference — Windows

## Python-based MCP

Use:

```text
uv / uvx
```

Check:

```powershell
uv --version
uvx --version
```

Example:

```powershell
uvx awslabs.aws-network-mcp-server@latest
```

## Node.js-based MCP

Use:

```text
npm / npx
```

Check:

```powershell
node --version
npm --version
npx --version
```

AWS Pricing Calculator MCP:

```powershell
npx -y sample-aws-pricing-calculator-mcp@latest
```

draw.io MCP:

```powershell
npx -y @drawio/mcp
```

## Kiro Workspace Config

```text
<workspace>\.kiro\settings\mcp.json
```

Example:

```text
C:\Managed-Service\Customer-A\.kiro\settings\mcp.json
```

## Recommended Standard

```text
Python MCP → uvx
Node MCP   → npx
AWS Access → IAM Identity Center Profile
Customer   → Separate Kiro Workspace
Production → Read-Only First
```
