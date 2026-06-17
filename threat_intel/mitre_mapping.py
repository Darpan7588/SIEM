MITRE_ATTACK_MAPPING = {
    "brute_force_login": {
        "technique_id": "T1110",
        "technique_name": "Brute Force",
        "tactic": "Credential Access"
    }
}


def get_mitre_mapping(attack_type: str):
    return MITRE_ATTACK_MAPPING.get(
        attack_type,
        {
            "technique_id": "UNKNOWN",
            "technique_name": "Unknown",
            "tactic": "Unknown"
        }
    )