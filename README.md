# AI Tools Repository

A curated collection of artificial intelligence tools, resources, and research notes. This repository serves as an intelligent bookmark system and knowledge base for AI technologies, implementations, and discoveries.

## 🔗 Related Repositories

This is part of a three-repository toolkit for comprehensive technology research and implementation:

- **[ai-tools](.)** - AI/ML tools, models, frameworks, and research
- **[dev-tools (private) ](#)** - Development tools, frameworks, and utilities  - needs to be "de-personalized"
- **[sec-tools (private) ](#)** - Security tools, vulnerability research, and hardening resources - same as above

## 🚀 Quick Start

**New to AI workflows?** Start here: **[Getting Into AI Workflows Very Quickly](mcp/get-started/lets-gooooo.md)** 

This comprehensive guide covers:
- Environment setup with UV (the best Python package manager) + [UV Quick Guide](mcp/get-started/uv-quickstart.md)
- Model Context Protocol (MCP) tutorial with real implementations
- Personal recommendations and troubleshooting tips
- Enterprise MCP implementations from major players

## 📋 Purpose

This repository functions as a hybrid between Raindrop.io and GitLab, but with enhanced documentation and implementation tracking. It serves as:

- **Research Queue**: Bookmarked sites and tools that warrant deeper investigation
- **Knowledge Base**: Detailed notes on tools that have been evaluated or implemented
- **Implementation Log**: Documentation of actual deployments, configurations, and lessons learned
- **Reference Library**: Quick access to AI tools and resources across different categories

The workflow: *Discovery → Bookmark → Research → Evaluate → Implement → Document*

## 📂 Current Directory Structure

### 🧠 LLM (Large Language Models)
```
LLM/
├── huggingface/          # Hugging Face platform and models
├── models/               # Model-specific documentation
│   ├── google/          # Gemini and other Google models
│   ├── meta/            # Llama and Meta AI models
│   └── openai/          # ChatGPT and OpenAI API resources
└── training/            # Training data and methodologies
```

### ☁️ AI Clouds
```
ai-clouds/
├── comparing-ai-in-clouds.md    # Cloud AI service comparisons
└── runpod.md                    # RunPod GPU cloud platform
```

### 💻 AI IDE
```
ai-ide/
└── ai-ide.md                    # AI-powered development environments
```

### 🤖 Coding Assistants
```
coding-assistants/
└── cognition-ai.md              # Cognition AI and similar tools
```

### 🔒 Cybersecurity
```
cybersecurity/
├── ai-incident-database.md      # AI security incident tracking
├── ai-risk.md                   # AI risk assessment and mitigation
└── owasp-llm-genai-security.md  # OWASP AI/LLM security guidelines
```

### 🔧 Hardware
```
hardware/
└── ai-hardware.md               # AI-specific hardware and infrastructure
```

### 🔌 MCP (Model Context Protocol) ⭐ **HOT**
```
mcp/
├── enterprise/
│   └── hubspot-mcp.md          # HubSpot MCP integration
├── get-started/
│   ├── lets-gooooo.md          # 🚀 COMPREHENSIVE GETTING STARTED GUIDE
│   └── uv-quickstart.md        # UV Package Manager with examples & aliases
└── tools/
    ├── coding/                 # MCP coding tools
    ├── frontend/               # Frontend component building
    ├── memory/                 # Knowledge graph and memory servers
    └── web-searching/          # Search and mapping tools
```

**Why MCP is Hot**: The ecosystem is exploding! Major players (GitHub, AWS, GitLab, Slack, HubSpot) all have MCP servers. This is the future of AI integration.

### 🧪 Testing
```
testing/
├── benchmarking/
│   └── what-is-benchmarking.md # AI model benchmarking methodologies
└── weights-and-bias/
    └── weights-and-bias-dev-platform.md # W&B development platform
```

## 🏆 Personal Recommendations

### Must-Have Tools
- **UV Package Manager** - Best Python package manager, implemented in Rust
- **Claude Desktop** - Essential for MCP integration
- **MCP Protocol** - Start with the getting started guide above

### Learning Path
1. **Start**: [Complete MCP tutorial](mcp/get-started/lets-gooooo.md)
2. **Practice**: GitHub MCP + Copilot Pro (budget permitting)
3. **Alternative**: Free tier Gemini, Claude, or ChatGPT
4. **Develop**: Practice outside production with Python
5. **Demo**: Present to product and architecture teams
6. **Scale**: Translate successful prototypes to production languages

### Standout Implementations
- **Figma MCP** - Just released, will change development workflows
- **HubSpot MCP** - Game changer for sales teams
- **AWS MCP Suite** - Comprehensive coordination platform
- **Slack Integration** - Enterprise-ready chat interfaces

## 🚀 Usage

### Research Phase
- Add new discoveries as markdown files in appropriate directories
- Include source URLs, key features, and initial assessment
- Tag with implementation priority and use case relevance

### Implementation Phase
- Document setup procedures, configurations, and integration notes
- Record performance metrics and real-world usage results
- Note any issues, workarounds, or optimization discoveries

### Reference Phase
- Maintain updated links and version information
- Cross-reference related tools and alternatives
- Keep implementation status current

## 📝 Contributing to This Repository

### Adding New Tools
1. **Categorize**: Determine the appropriate directory structure
2. **Document**: Create detailed markdown with:
   - Tool description and primary use case
   - Installation/setup instructions (if implemented)
   - Key features and capabilities
   - Pros/cons from evaluation
   - Implementation status and notes
3. **Link**: Update this README if new directories are created
4. **Cross-reference**: Link to related tools in dev-tools or sec-tools repos

### File Naming Convention
- Use descriptive, lowercase filenames with hyphens
- Include version numbers for version-specific documentation
- Group related tools in subdirectories when appropriate

### Documentation Standards
- Include source URLs and documentation links
- Add implementation date and last updated information
- Document dependencies and requirements
- Note any security considerations or limitations

---

*This repository represents hands-on experience with AI tools, not just bookmarks. Each entry includes real implementation notes and personal recommendations based on actual usage.*
