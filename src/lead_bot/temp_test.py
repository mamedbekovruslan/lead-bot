from lead_bot.extract import extract
from lead_bot.samples import SAMPLES


text = SAMPLES[0]
print(text)

for temp in [0, 1]:
    print(f"\n=== temperature = {temp} ===")
    for run in range(1, 4):
        lead = extract(text, temperature=temp)
        print(f"{run}: {lead.need}")