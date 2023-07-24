import os.path
import json

def _get_version():
    OCRD_TOOL_JSON="ocrd-tool.json"
    if not os.path.exists(OCRD_TOOL_JSON):
        return None

    with open(OCRD_TOOL_JSON, "r") as fp:
        return json.load(fp)["version"]

    return None
