def detect_intent(user_text: str) -> str:
    text = user_text.lower()

    interested_keywords = ["yes", "interested", "okay", "sure", "go ahead", "tell me"]
    busy_keywords = ["busy", "later", "not now", "call back", "another time"]
    reject_keywords = ["no", "not interested", "stop", "don't call", "never"]

    if any(word in text for word in interested_keywords):
        return "INTERESTED"
    if any(word in text for word in busy_keywords):
        return "BUSY"
    if any(word in text for word in reject_keywords):
        return "REJECT"

    return "UNKNOWN"
