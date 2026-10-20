import asyncio
import time

async def fake_ask(name):
    print(f"{name} 送出")
    await asyncio.sleep(2)          # 模擬等模型回答
    print(f"{name} 收到")
    return f"{name} 的回答"

async def main():
    start = time.time()
    # 一個一個等
    await fake_ask("A")
    await fake_ask("B")
    await fake_ask("C")
    print(f"一個一個：{time.time() - start:.1f} 秒\n")

    start = time.time()
    # 同時開始
    results = await asyncio.gather(fake_ask("A"), fake_ask("B"), fake_ask("C"))
    print(results)
    print(f"gather：{time.time() - start:.1f} 秒")

asyncio.run(main())