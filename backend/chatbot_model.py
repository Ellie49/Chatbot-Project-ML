import json
import re
from pathlib import Path
from typing import List, Dict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def _normalize(text: str) -> str:
    text = text.lower().strip()
    # remove extra spaces and punctuation spacing
    text = re.sub(r"\s+", " ", text)
    return text

class ChatbotModel:
    """
    A lightweight retrieval-based chatbot.
    - Loads a small knowledge base of Q&A pairs from JSON.
    - Uses TF-IDF + cosine similarity to find the best answer.
    - Includes a few rule-based fallbacks for greetings and small talk.
    """
    def __init__(self, kb_path: str = "knowledge_base.json", threshold: float = 0.25):
        self.threshold = threshold
        self.kb_path = Path(kb_path)
        with self.kb_path.open("r", encoding="utf-8") as f:
            self.kb: List[Dict[str, str]] = json.load(f)

        self.questions = [_normalize(item["question"]) for item in self.kb]
        self.answers = [item["answer"] for item in self.kb]
        self.vectorizer = TfidfVectorizer()
        self.q_matrix = self.vectorizer.fit_transform(self.questions)

        # simple rules
        self.rules = {
            r"\b(hi|hello|hey)\b": "Hello! How can I help you today?",
            r"\bhow are you\b": "I'm doing great and ready to help. How are you?",
            r"\bthank(s| you)\b": "You're welcome! 🙂",
            r"\bbye|goodbye|see you\b": "Goodbye! Have a wonderful day!"
        }

    def _rule_based(self, text: str) -> str:
        for pattern, reply in self.rules.items():
            if re.search(pattern, text):
                return reply
        return ""

    def get_response(self, user_text: str) -> str:
        user_text_norm = _normalize(user_text)

        if not user_text_norm:
            return "Please type something so I can help."

        # Rule-based quick replies
        rule = self._rule_based(user_text_norm)
        if rule:
            return rule

        # Retrieval-based
        vec = self.vectorizer.transform([user_text_norm])
        sims = cosine_similarity(vec, self.q_matrix)[0]
        best_idx = sims.argmax()
        best_score = float(sims[best_idx])

        if best_score >= self.threshold:
            return self.answers[best_idx]

        return "I'm not sure yet. Could you rephrase or ask in a different way?"