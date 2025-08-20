def set_context(self, ctx: Dict[str, Any]):
    self.student_context = ctx or {}

def respond(self, message: str) -> str:
    text = (message or "").lower()
    if not text.strip():
        return "Ask me anything about budgeting, credit, investing, or economics."
    # Pick category by keyword overlap
    best = None; score = 0
    for k, v in self.kb.items():
        s = sum(1 for kw in v["keywords"] if kw in text)
        if s > score:
            score = s; best = k
    if best:
        ans = random.choice(self.kb[best]["answers"])
        # Light personalization
        if best == "budgeting" and self.student_context.get("work_context","").lower().startswith("farm"):
            ans += "\n\nRural note: If farm work is seasonal, set aside a slice from peak months."
        return ans + "\n\nWant more detail, a calculation, or an example?"
    return "I can help with budgeting, credit, investing, and economics—try including those words or ask a specific question."
