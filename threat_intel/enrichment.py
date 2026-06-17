LOCAL_THREAT_INTEL = {
    "192.168.1.150": {
        "reputation": "malicious",
        "confidence": 90,
        "category": "brute_force_source",
        "provider": "local_lab_feed"
    },
    "192.168.1.200": {
        "reputation": "suspicious",
        "confidence": 65,
        "category": "scanner",
        "provider": "local_lab_feed"
    }
}


def enrich_ip(source_ip: str):
    if not source_ip:
        return {
            "reputation": "unknown",
            "confidence": 0,
            "category": "unknown",
            "provider": "local_lab_feed"
        }

    return LOCAL_THREAT_INTEL.get(source_ip, {
        "reputation": "clean",
        "confidence": 10,
        "category": "none",
        "provider": "local_lab_feed"
    })


def enrich_alert(alert: dict):
    source_ip = alert.get("source_ip")
    intel = enrich_ip(source_ip)

    alert["threat_intel"] = intel

    if intel["reputation"] == "malicious":
        alert["severity"] = "critical"
        alert["confidence"] = "very_high"

    return alert