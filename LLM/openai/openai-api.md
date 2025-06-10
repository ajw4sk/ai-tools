# OpenAI API: Models, Security, and Compliance Overview

OpenAI's API provides access to advanced AI models for text generation, code assistance, image generation, speech recognition, and more. This document outlines available models, pricing, account security practices, data privacy controls, and compliance standards.

---

## 📊 Model Offerings

| Model Name       | Capabilities                     | Input Cost (per 1M tokens) | Output Cost (per 1M tokens) | Notes                                         |
|------------------|----------------------------------|----------------------------|-----------------------------|-----------------------------------------------|
| GPT-4o           | Multimodal: text, image, audio   | $2.50                      | $10.00                      | Fastest, most capable, and cost-efficient     |
| GPT-3.5 Turbo    | Text only                        | $0.50                      | $1.50                       | Cost-effective for everyday language tasks    |
| DALL·E           | Image generation from text       | Varies                     | Varies                      | Based on resolution and features like editing |
| Whisper          | Speech-to-text                   | $0.006/minute              | N/A                         | For transcribing audio to text                |

> For the latest prices, visit [OpenAI Pricing](https://openai.com/api/pricing)

---

## 🔐 Security Configurations

### Data Usage & Retention

- **Training Policy**: API usage data is **not used** to train OpenAI models.
- **Retention Window**: API request data may be stored for up to **30 days** for abuse monitoring.
- **Zero Data Retention**: Available upon request for eligible use cases (e.g., healthcare, finance).

### MFA & Access Control

- **Multi-Factor Authentication (MFA)**: Strongly recommended for all accounts.
  - Visit [platform.openai.com/account](https://platform.openai.com/account)
  - Go to **Settings > Security**
  - Enable 2FA with an authenticator app

### API Key Best Practices

- Store API keys in secure environment variables.
- **Never expose keys** in frontend or client-side code.
- Rotate keys periodically using the [API Keys dashboard](https://platform.openai.com/account/api-keys)
- Use role-based scoping where applicable.

---

## 🛡️ Compliance & Trust

- **SOC 2 Type II**: Audited and certified.
- **HIPAA**: BAA available for eligible enterprise customers.
- **GDPR**: Compliant with data subject rights and international transfers.
- **Data Residency**: Options for U.S. and EU regional processing available.

> Visit the [OpenAI Trust Portal](https://trust.openai.com) to download certifications and legal docs.

---

## ⚙️ Recommended Account Settings

1. **Enable MFA** to prevent unauthorized access.
2. **Limit API key scopes** and usage.
3. **Activate Zero Data Retention** if handling sensitive data.
4. **Review usage logs regularly** from the OpenAI dashboard.
5. **Restrict user/team access** using workspace roles.

---

## 📚 Resources

- **Docs**: [platform.openai.com/docs](https://platform.openai.com/docs)
- **Quickstart**: [platform.openai.com/docs/quickstart](https://platform.openai.com/docs/quickstart)
- **Cookbook**: [cookbook.openai.com](https://cookbook.openai.com)
- **Community Forum**: [community.openai.com](https://community.openai.com)
- **GitHub SDKs**:
  - [Python](https://github.com/openai/openai-python)
  - [Node.js](https://github.com/openai/openai-node)

---

> ℹ️ Last updated: June 2025 — refer to [OpenAI](https://openai.com) for the most accurate and up-to-date information.
