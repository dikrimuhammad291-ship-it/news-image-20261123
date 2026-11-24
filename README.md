[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/dikrimuhammad291-ship-it/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/dikrimuhammad291-ship-it/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

# World news front page, 23 November 2026

A program that draws one image summing up the world's news of Monday,
23 November 2026, as the front page of a newspaper called
**THE WORLD TODAY**.

## The image

A 1024x1024 PNG on off-white newsprint: a masthead with the date, one
big lead story, and six short news cards across regions and beats.

- **Lead — EU proposes sweeping Russia sanctions.** The European
  Commission proposes its 22nd sanctions package: about 60 Russian
  banks cut from SWIFT, curbs on crypto platforms and payment networks,
  more than 70 further shadow-fleet vessels listed, a ban on tankers
  insured in Russia from EU ports, and a ban on Russian teams and
  athletes competing under the Russian flag at EU events. A proposal —
  it needs unanimous approval by all 27 EU member states.
- **Middle East — Iran vows "all means" against US blockade.** Iran
  calls the US naval blockade of the Strait of Hormuz military
  aggression. UKMTO confirmed three tanker attacks near Khasab, Oman,
  on 20–21 Nov; Iran claims two more supertankers hit mines on 22 Nov
  — unverified.
- **Europe — Moscow warns Estonia; Finland summons envoy.** Russia
  warns Estonia's border-closure plan risks open war; Finland summons
  Russia's ambassador over a suspected airspace violation and a
  Ukrainian drone strike on the cargo ship Sparta II.
- **Libya — Sea drones sink Russian corvette off Libya.** Suspected
  Ukrainian naval drones hit the corvette Merkury at Benghazi naval
  base; Libyan officials say she sank, 10 injured. Unconfirmed by
  Kyiv and Moscow.
- **Ukraine — Russian drones hit flats near Kyiv.** A five-storey
  apartment block in Dymer, north of Kyiv, early Sunday: 2 killed,
  11 missing including 2 children.
- **Trade — EU and Indonesia sign trade deal.** After a decade of
  talks; a combined market of 730 million people.
- **Science — BepiColombo enters Mercury orbit.** After an eight-year
  journey, the Europe–Japan probe entered orbit around Mercury on
  21 Nov — only the second mission ever to do so.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Writes `out/entry.png` (1024x1024, under 1 MiB). Runs offline with
only the standard library and Pillow, and is deterministic: two runs
produce byte-identical files.

## Files

- `main.py` — entrypoint; reads `MAKEFUN_OUTPUT_DIR` (default
  `/output`) and writes `entry.png` there.
- `render.py` — draws the front page with Pillow and the DejaVu fonts.
- `LICENSE` — MIT.

Built for the make.fun competition `news-image-20261123`.
