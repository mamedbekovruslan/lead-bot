import json, os, time

from dotenv import load_dotenv
from openai import OpenAI
from lead_bot.schema import Lead


load_dotenv()

client = OpenAI(base_url=os.getenv("LLM_BASE_URL"), api_key=os.getenv("LLM_API_KEY", "ollama"))
MODEL = os.getenv("LLM_MODEL")

SYSTEM = f"""Ты разбираешь заявки клиентов веб-студии.
Верни ТОЛЬКО JSON по схеме:
{json.dumps(Lead.model_json_schema(), ensure_ascii=False)}
Если данных нет в тексте - null. Ничего не выдумывай"""

def extract(text: str) -> Lead:
    resp = client.chat.completions.create(
        model=MODEL,
        temperature=0,
        response_format={"type": "json_object"},
        messages=[{"role": "system", "content": SYSTEM},
                 {"role": "user", "content": text}],
    )
    return Lead.model_validate_json(resp.choices[0].message.content)

if __name__ == "__main__":
    from lead_bot.samples import SAMPLES

    for i, text in enumerate(SAMPLES, start=1):
        print(f"\n--- #{i}: {text}")
        t = time.perf_counter()
        try:
            print(extract(text))
        except Exception as e:
            print(f"ОШИБКА: {e}")
        print(f"{time.perf_counter() - t:.2f} c")