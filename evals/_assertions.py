"""Retained assertion semantics for the upstream regression fixtures."""
import json


def _dig(obj, path):
    cur = obj
    for part in path.split("."):
        if isinstance(cur, list):
            part = int(part)
        cur = cur[part]
    return cur


def check_assertion(a, proc):
    """Return (ok, detail) for one assertion against a finished process."""
    t = a["type"]
    if t == "exit_code":
        return proc.returncode == a["equals"], f"exit={proc.returncode}"
    if t == "stdout_contains":
        return a["value"] in proc.stdout, "stdout"
    if t == "stdout_not_contains":
        return a["value"] not in proc.stdout, "stdout"
    if t == "stderr_not_contains":
        return a["value"] not in proc.stderr, "stderr"
    if t == "violation_phrase_contains":
        try:
            data = json.loads(proc.stdout)
            phrases = [v.get("phrase", "") for v in data.get("violations", [])]
        except Exception as e:  # noqa: BLE001
            return False, f"json error: {e}"
        return any(a["value"] in phrase for phrase in phrases), f"phrases={phrases}"
    if t == "violation_category_equals":
        try:
            data = json.loads(proc.stdout)
            categories = [v.get("category", "") for v in data.get("violations", [])]
        except Exception as e:  # noqa: BLE001
            return False, f"json error: {e}"
        return a["value"] in categories, f"categories={categories}"
    if t == "json":
        try:
            data = json.loads(proc.stdout)
            actual = _dig(data, a["path"])
        except Exception as e:  # noqa: BLE001
            return False, f"json error: {e}"
        if "equals" in a:
            return actual == a["equals"], f"{a['path']}={actual}"
        if "gte" in a:
            return actual >= a["gte"], f"{a['path']}={actual}"
        if "lte" in a:
            return actual <= a["lte"], f"{a['path']}={actual}"
        return False, "no comparator"
    return False, f"unknown assertion type {t}"
