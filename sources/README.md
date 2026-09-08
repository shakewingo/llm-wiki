# Source access

Complete source bodies stay in Yuque and Notion. This directory stores only the
registry and connection instructions; never store credentials or permanent source
exports here.

## Environment

The sync scripts read credentials from the process environment:

```bash
export YUQUE_API_KEY='...'
export NOTION_API_KEY='...'
```

An interactive agent should inherit these variables from its launcher or shell
profile. A cron/systemd/container deployment must inject both variables into the
job environment. Do not add tokens to prompts, command arguments, this repository,
or job logs.

The Notion token must belong to an integration with read-content capability, and
each registered page must be shared with that integration. A valid token without
page access is reported by Notion as `403` or `404`.

## Preview and temporary fetch

Run metadata-only plans first:

```bash
python scripts/sync_yuque.py plan
python scripts/sync_notion.py plan
```

After approval, fetch a registered Notion page as Notion-flavored Markdown through
the official API into temporary processing storage:

```bash
python scripts/sync_notion.py export \
  --source-id notion:388cad4f-b605-8074-8c53-ff558a15beb0 \
  --output /tmp/alisa-llm-source.json
```

The exporter rejects destinations outside temporary directories and refuses to
overwrite an existing file. Delete the export after synthesis. It contains the
source body and must never be committed.

After updating the derived wiki and passing all required validation, acknowledge
the exact provider version:

```bash
python scripts/sync_notion.py acknowledge \
  --source-id notion:388cad4f-b605-8074-8c53-ff558a15beb0
```

`sync_notion.py` uses `https://api.notion.com/v1`, sends `Authorization: Bearer`
from `NOTION_API_KEY`, and pins `Notion-Version: 2026-03-11`. The Markdown endpoint
usually retrieves the whole page in one request; if Notion reports truncated or
unknown subtrees, the exporter follows their block IDs. It never prints or persists
the token.

Official references: [retrieve a page](https://developers.notion.com/reference/retrieve-a-page),
[retrieve a page as Markdown](https://developers.notion.com/reference/retrieve-page-markdown),
and [API versioning](https://developers.notion.com/reference/versioning).
