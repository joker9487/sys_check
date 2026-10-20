import asyncio
import time
import httpx

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen2.5:3b"

async def ask(client, prompt):
    print("開始")
    r = await client.post(
        OLLAMA_URL,
        json={"model": MODEL, "prompt": prompt, "stream": False},
        timeout=120,
    )
    print("結束")
    r.raise_for_status()
    return r.json()["response"]

async def main():
    questions = ["用一句話解釋 Docker", "用一句話解釋 RAG", "用一句話解釋 API"]
    async with httpx.AsyncClient() as client:
        start = time.time()
        answers = await asyncio.gather(*(ask(client, q) for q in questions))
        print(f"花了 {time.time() - start:.1f} 秒")
    for q, a in zip(questions, answers):
        print(f"Q: {q}\nA: {a}\n")

asyncio.run(main())