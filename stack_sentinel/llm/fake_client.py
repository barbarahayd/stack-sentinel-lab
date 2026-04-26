from stack_sentinel.llm.base import LLMClient


class FakeLLMClient(LLMClient):
    def classify_intent(self, user_input: str) -> str:
        text = user_input.lower()
        if "ticket" in text or "tck-" in text:
            return "ticket"
        if "build" in text or "bld-" in text:
            return "build"
        if "doc" in text or "documentação" in text or "incidente" in text or "severidade" in text:
            return "docs"
        return "unknown"

