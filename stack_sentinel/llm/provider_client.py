import os
from typing import Optional

from stack_sentinel.llm.base import LLMClient


class ProviderLLMClient(LLMClient):
    """Cliente opcional para usar uma LLM real fora dos testes obrigatorios.

    O lab nao depende deste cliente para passar nos exercicios. Ele existe para
    demos ou alunos que ja tenham chave configurada e queiram comparar uma LLM
    real com o FakeLLM.
    """

    def __init__(self, provider: Optional[str] = None, api_key: Optional[str] = None, model: Optional[str] = None):
        self.provider = provider or os.getenv("LLM_PROVIDER", "fake")
        self.api_key = api_key or os.getenv("LLM_API_KEY")
        self.model = model or os.getenv("LLM_MODEL", "gpt-4.1-mini")

    def classify_intent(self, user_input: str) -> str:
        """Classifica intencao usando uma LLM real quando configurada.

        Neste scaffolding, o metodo falha de forma explicita para evitar que os
        testes ou a aula dependam de rede, custo ou credenciais. Alunos podem
        implementar este metodo como trilha opcional, preservando o contrato:
        retornar apenas ticket, build, docs ou unknown.
        """
        if not self.api_key:
            raise RuntimeError(
                "LLM real nao configurada. Use FakeLLMClient para os testes ou defina LLM_API_KEY."
            )
        raise NotImplementedError(
            "ProviderLLMClient e trilha opcional. Implemente a chamada ao provedor escolhido mantendo o contrato."
        )

    @staticmethod
    def normalize_intent(value: str) -> str:
        allowed = {"ticket", "build", "docs", "unknown"}
        normalized = value.strip().lower()
        return normalized if normalized in allowed else "unknown"
