from lead_bot.extract import client, MODEL

for temp in [0, 1]:
    print(f"\n=== temperature = {temp} ===")
    for run in range(1, 4):
        resp = client.chat.completions.create(
            model=MODEL,
            temperature=temp,
            messages=[{"role": "user", "content": "Придумай одно название для кофейни. Ответь только названием."}],
        )
        print(f"{run}: {resp.choices[0].message.content}")
        print(resp.usage)