# VS Code Release Notes

Welcome to the May 2025 release of Visual Studio Code. There are many updates in this version that we hope you'll like, some of the key highlights include:

MCP

Expand your agent coding flow with support for prompts, resources, and sampling (Show more).
Access MCP servers that require authentication (Show more).
Debug MCP servers with development mode (Show more).
Publish MCP servers from an extension (Show more).
Chat

Group and manage related tools by combining them in a tool set (Show more).
Source Control

View files in Source Control Graph view (Show more).
Assign and track work for GitHub Copilot Coding Agent from within VS Code (Show more).
If you'd like to read these release notes online, go to Updates on code.visualstudio.com. Insiders: Want to try new features as soon as possible? You can download the nightly Insiders build and try the latest updates as soon as they are available.




MCP support for prompts
VS Code's Model Context Protocol support now includes prompt support. Prompts can be defined by MCP servers to generate reusable snippets or tasks for the language model. Prompts are accessible as slash / commands in chat, in the format /mcp.servername.promptname. You can enter plain text or include command output in prompt variables, and we also support completions when servers provide it.

### Chat

**Chat [tool set](**

VS Code now enables you to define tool sets, either through a proposed API or through the UI. A tool set is a collection of different tools that can be used just like individual tools. Tool sets make it easier to group related tools together, and quickly enable or disable them in agent mode. For instance, the tool set below is for managing GitHub notifications (using the GitHub MCP server).

```
{
  "gh-news": {
    "tools": [
      "list_notifications",
      "dismiss_notification",
      "get_notification_details",
    ],
    "description": "Manage GH notification",
    "icon": "github-project"
  }
}
```

To create a tool set, run the Configure Tool Sets > Create new tool sets file command from the Command Palette. You can then select the tools you want to include in the tool set, and provide a description and icon.

To use a tool set in a chat query, reference it by #-mentioning its name, like #gh-news. You can also choose it from the tool picker in the chat input box.

