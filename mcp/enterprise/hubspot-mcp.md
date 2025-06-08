# HubSpot MCP Server Setup Guide

## Pre-requisites

### 1. Install Node and NPM

Visit [Node.js Downloads](https://nodejs.org/en/download) to install Node.js and npm.

### 2. Create a Private App in HubSpot

1. Navigate to **Settings > Integrations > Private Apps** in HubSpot.
2. Click **"Create private app"**.
3. Name your app and set the required scopes (start with read-only if you're unsure).
4. Click **"Create app"**.
5. Copy the generated **Access Token** and store it securely.

---

## Using the MCP Server

### Claude Desktop

**Download:** [Claude Desktop Download](https://www.anthropic.com)

**Configuration File:**

Path (macOS): `~/Library/Application Support/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "hubspot": {
      "command": "npx",
      "args": ["-y", "@hubspot/mcp-server"],
      "env": {
        "PRIVATE_APP_ACCESS_TOKEN": "<your-private-app-access-token>"
      }
    }
  }
}
```

Save and restart Claude.

More info: [HubSpot MCP Server on npm](https://www.npmjs.com/package/@hubspot/mcp-server)

---

### Cursor

**Create Config File:**

```bash
mkdir -p .cursor && touch .cursor/mcp.json
```

**Add Configuration:**

```json
{
  "mcpServers": {
    "hubspot": {
      "command": "npx",
      "args": ["-y", "@hubspot/mcp-server"],
      "env": {
        "PRIVATE_APP_ACCESS_TOKEN": "<your-private-app-access-token>"
      }
    }
  }
}
```

Save and restart Cursor.

More info: [HubSpot MCP Server on npm](https://www.npmjs.com/package/@hubspot/mcp-server)

---

## Other MCP Clients

A list of supported clients is available [here](https://www.npmjs.com/package/@hubspot/mcp-server).

---

## Example Prompts

### 🔍 Get Insights from HubSpot

* Get me the latest update about **Acme Inc.**
* Summarize all deals in the **"Decision maker bought in"** stage with deal value > \$1000.
* Summarize the last five tickets for **Alex Smith**.

### ✍️ Create and Update CRM Records

* Update the address for **John Smith**.
* Create a new contact **"[John.Johnson@email.com](mailto:John.Johnson@email.com)"** for **Acme Inc.**

### 🔗 CRM Associations

* List all associated contacts and their roles for **Acme Inc.**
* Associate **John Smith** with **Acme Inc.** as a company.

### 📌 Add Engagements

* Add a task to send a thank-you note to **[jane@example.com](mailto:jane@example.com)**.
* Add a note for **Acme Inc.**
* List my overdue HubSpot tasks.
* Count how many contacts I have in HubSpot.

---

## 🛠 Tools Provided by MCP Server

| Category     | Tool Name                             | Description                                 |
| ------------ | ------------------------------------- | ------------------------------------------- |
| OAuth        | `hubspot-get-user-details`            | Authenticates token and provides user info. |
| Objects      | `hubspot-list-objects`                | Retrieves CRM records for object types.     |
|              | `hubspot-search-objects`              | Search CRM records with filters.            |
|              | `hubspot-batch-create-objects`        | Create multiple records at once.            |
|              | `hubspot-batch-update-objects`        | Update multiple records at once.            |
|              | `hubspot-batch-read-objects`          | Read multiple records by IDs.               |
|              | `hubspot-get-schemas`                 | View custom object schemas.                 |
| Properties   | `hubspot-list-properties`             | List properties for CRM objects.            |
|              | `hubspot-get-property`                | View a specific property.                   |
|              | `hubspot-create-property`             | Create custom properties.                   |
|              | `hubspot-update-property`             | Update existing properties.                 |
| Associations | `hubspot-create-association`          | Link CRM records.                           |
|              | `hubspot-list-associations`           | View relationships between records.         |
|              | `hubspot-get-association-definitions` | Get valid association types and labels.     |
| Engagements  | `hubspot-create-engagement`           | Add Notes or Tasks.                         |
|              | `hubspot-get-engagement`              | Retrieve engagement by ID.                  |
|              | `hubspot-update-engagement`           | Modify existing engagements.                |
| Workflows    | `hubspot-list-workflows`              | List workflows.                             |
|              | `hubspot-get-workflow`                | Detailed view of a workflow.                |
| Links        | `hubspot-generate-feedback-link`      | Create feedback links.                      |
|              | `hubspot-get-link`                    | Generate HubSpot UI URLs.                   |

---

> **Note:** Replace `<your-private-app-access-token>` with your actual token from the HubSpot private app you created earlier.
