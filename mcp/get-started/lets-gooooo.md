# Getting Into AI Workflows Very Quickly

An intro guide to setting up powerful AI workflows using Model Context Protocol (MCP) and modern development tools.

## 🚀 Prerequisites & Environment Setup

### Essential Tools You Need

Before diving in, make sure you have these tools installed:

- **Python 3.10 or higher** - Required for most AI workflows
- **Node.js** - For JavaScript-based AI tools and MCP servers
- **UV Package Manager** - ⭐ **HIGHLY RECOMMENDED** ([Detailed Setup Guide](uv-quickstart.md)) 

### UV Installation & Setup (Personal Recommendation)

If you've never used UV, go to: https://docs.astral.sh/uv/getting-started/installation/

UV is implemented in Rust by Astral and is **by far the best Python package manager I've used**. 

```bash
# Recommended installation method - simple curl
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Alternative installation methods available:**
- pip
- Cargo  
- Homebrew
- Scoop
- Docker
- Winget
- GitHub releases

But honestly, just do the curl request - it's straightforward.

### Important UV Setup Tips

**Enable Shell Auto-Completion** - This is a game changer! 
- Instructions are on the installation page towards the bottom
- It gives you guidance on figuring out what shell you're using if you don't know
- Just put it into your shell configuration
- Makes the experience way easier

**Take 15 minutes to explore UV** if you've never seen it before:
- Run through the scripts and guides - it's a little different but worth it
- Tools like UVX let you invoke tools without installing them in the virtual environment
- Much easier virtual environment and package management

📚 **Detailed UV Guide**: Check out my comprehensive [UV Quick Guide](uv-quickstart.md) with code examples, shell aliases, and workflow optimizations!

### Claude Desktop

Download Claude Desktop if you don't have it - you'll need this for MCP integration.

## 🔌 Introduction to Model Context Protocol (MCP)

MCP is **huge** right now! Anthropic open-sourced it and the ecosystem is exploding.

**Essential Reading** (in this order):
1. [MCP Introduction](https://modelcontextprotocol.io/introduction) - Should be a quick read
2. [Server Developers Tutorial](https://modelcontextprotocol.io/quickstart/server) - Start here after the intro

**Browser Note**: My privacy settings on Safari were bugging out, so I used Firefox to read the directions. Try different browsers if you have issues.

## 🛠️ Setting Up Your First MCP Server

### Folder Structure Setup

Create a folder structure that will house both server and client implementations:

```
/mcp/
├── mcp-server/
└── mcp-client/
```

**Important**: Do this close to your user folder because you'll need to type absolute paths. I had Node installed with multiple services (brew and herd) which was giving me errors, so absolute paths saved me.

### Building the Weather Server

1. **Get the code**: Go to the GitHub repo and copy the **raw code** for `weather.py`
   - Don't piece it together from the article - they split up the code to explain it
   - If you copy and paste incorrectly, it might error
   - If you're not a Python expert, this can throw you off

2. **Create virtual environment**:
   ```bash
   cd /mcp/mcp-server
   uv venv
   source .venv/bin/activate
   uv add anthropic-mcp-server
   # Install other dependencies as needed
   ```

3. **Start the server**:
   ```bash
   python weather.py
   ```

### Claude Desktop Configuration

1. **Config file setup**: Follow the directions for the config file in Claude Desktop
2. **Use absolute paths** for both:
   - UV (should be in your `.local` directory)
   - The `weather.py` file you just created

3. **Critical restart sequence**: After you save the config file and have already exited Claude:
   - **Don't start Claude back up yet!**
   - Stop the server
   - Deactivate the environment  
   - Reactivate the environment
   - Start the server again
   - **Then** restart Claude Desktop

   This may have been because of my personal setup, but you need to restart the server if you make changes to the config file.

### Testing Your Setup

1. **Look for the hammer icon**: The directions show a little hammer icon that should show up if you did it right
   - **I never saw that icon**, but it worked just fine
   - So if you aren't seeing errors, proceed with testing

2. **Test the connection**: Ask Claude something like:
   ```
   "How's the weather in San Francisco?"
   ```

3. **Permission prompt**: Unless you've already given Claude permissions, the desktop app should prompt you to access the server file - say yes

4. **Success**: The desktop app should be connecting with your server at this point

5. **Cleanup**: When you're done and confirmed it works:
   - Kill the server
   - Deactivate the venv

## 💻 Building an MCP Client

### Client Setup

Follow the directions at: https://modelcontextprotocol.io/quickstart/client

Create the client in the same folder structure (`/mcp/mcp-client`).

### API Key Setup

You'll need an API key from Anthropic for the `.env` file.

**Critical**: Make sure the `.env` file is **perfect** or it will error.

### Getting the Client Code

There's a lot of code for this one, so I **highly recommend copying from the GitHub repo** after you've read through the tutorial:

https://github.com/modelcontextprotocol/quickstart-resources/blob/main/mcp-client-python/client.py

This avoids transcription errors.

### Testing the Full Setup

**Before starting the client**:
1. Go back to the server directory
2. Activate the venv
3. Start the server

**Then run the client**:
1. Go to the client directory  
2. Activate the client venv
3. Run the Python script

You should be able to run it from the command line and ask it "How's the weather in San Francisco?" (or anywhere else) and it should query successfully.

**Congratulations!** If you get this working, you've basically made your CLI chatbot connect to a third-party service using an LLM.

## 🔧 How MCP Works Under the Hood

When you submit a query:

1. **Tool Discovery**: The client gets the list of available tools from the server
2. **Query Processing**: Your query is sent to Claude along with tool descriptions  
3. **Decision Making**: Claude decides which tools (if any) to use
4. **Execution**: The client executes any requested tool calls through the server
5. **Results**: Results are sent back to Claude
6. **Response**: Claude provides a natural language response
7. **Display**: The response is displayed to you

## 🏢 The MCP Ecosystem is Exploding!

### Major Players with MCP Servers

The big names all have MCP servers now:
- **GitHub** 
- **AWS**
- **GitLab**
- **Git**
- **Slack** 
- **SQLite**
- **PostgreSQL**

Plus lots of templates, reference servers, and marketplaces.

### Current Reference Servers

These are available right now:

- **Filesystem** - Secure file operations with configurable access controls
- **Fetch** - Web content fetching and conversion optimized for LLM usage  
- **Memory** - Knowledge graph-based persistent memory system
- **Sequential Thinking** - Dynamic problem-solving through thought sequences

### Official MCP Servers List

Check out the comprehensive list: https://github.com/modelcontextprotocol/servers

## 🌟 Standout MCP Implementations

### Puppeteer MCP - Accessibility Testing
https://github.com/modelcontextprotocol/servers-archived/tree/main/src/puppeteer

Could be relevant for design teams doing accessibility work.

### Elasticsearch MCP - Natural Language Data Queries  
https://github.com/elastic/mcp-server-elasticsearch

Lets you query your data using natural language.

### AWS MCP Suite - The Coordinator
https://github.com/awslabs/mcp

AWS has **lots** of MCPs! They even have an MCP that coordinates with all the other MCPs.

### Azure MCP - ChatGPT Integration
https://github.com/Azure/azure-mcp

Opens up ChatGPT usage with MCP, allows different LLMs and multiple agents to work on the same task.

### Google AI Toolbox - Database Interactions
https://github.com/googleapis/genai-toolbox

Interact with your databases through natural language.

### HubSpot MCP - Sales Team Game Changer
https://developers.hubspot.com/mcp

The sales team could more easily interact with HubSpot data.

### Figma MCP - The Most Impressive 🤯
https://www.figma.com/blog/introducing-figmas-dev-mode-mcp-server/

**This just came out a few days ago** and will change development as we know it. It allows you to connect Figma to your IDE to rapidly build features, cutting down development time significantly.

## 💬 Slack Integration - Enterprise Ready

With almost all of these implementations, there's built-in or easy-to-implement connections with Slack or Teams. You can query many data sources directly from Slack or a custom chat application.

**Example**: The HubSpot MCP could be connected with Slack so sales team members could get or put any info they need directly from chat.

### Slack MCP Client Features

From Anthropic's description:

> Slack MCP Client acts as a bridge between Slack and Model Context Protocol (MCP) servers. Using Slack as the interface, it enables large language models (LLMs) to connect and interact with various MCP servers through standardized MCP tools.

**Key features:**
- **Supports Popular LLM Providers**: OpenAI, Anthropic, and Ollama
- **Dynamic and Secure Integration**: Dynamic MCP tool registration, works in channels and DMs, secure credential management
- **Easy Deployment**: Official Docker images, Helm chart for Kubernetes, Docker Compose for local development

## 🎯 Next Steps & Recommendations

### Immediate Next Step
I suggest using **GitHub's MCP server with Copilot Pro** after you've explored these docs. 

**Budget considerations**: It's a little expensive, so if you don't want to pay for it, you can use free versions of:
- Gemini
- Claude  
- Copilot
- ChatGPT

Use these to help edit templates or create your own.

### Practice Strategy
**Practice outside of production networks** without any client data using Python. If you think you have a good idea:
1. Demo it to product and architecture teams
2. If approved, translate to PHP or other production languages

## 🛡️ Best Practices

### Error Handling
- Always wrap tool calls in try-catch blocks
- Provide meaningful error messages  
- Gracefully handle connection issues

### Resource Management
- Use AsyncExitStack for proper cleanup
- Close connections when done
- Handle server disconnections

### Security  
- Store API keys securely in `.env`
- Validate server responses
- Be cautious with tool permissions

### Common Troubleshooting Issues

From the troubleshooting docs, the biggest problems are usually:
- **PATH issues**
- **SHELL configuration** 
- **Node version conflicts**
- **Python version issues**

## 🤔 Still Confused?

If you're still wondering "what the heck is this," read this FAQ that spells it out clearly:

https://modelcontextprotocol.io/faqs

---

**Bottom Line**: MCP is revolutionizing how AI systems interact with tools and data. Start with the weather server tutorial above, and you'll be building powerful AI workflows in no time!
