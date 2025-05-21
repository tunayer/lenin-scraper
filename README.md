# SovietRelations - Lenin Crawler 🕵️‍♂️📚

This project is a Scrapy-based web crawler that scans [marxists.org](https://www.marxists.org/archive/lenin/works/cw/index.htm) for Lenin’s collected works. It automatically parses volumes and part files to extract paragraphs that contain specified keywords related to **Turkey**, **Ottoman history**, or key political figures.

## What It Does

- Crawls all `volumeXX.htm` pages listed on the Lenin Collected Works index
- It is set to specifically the "volume15.htm". It can be modified
- Follows links to `partXX.htm` files inside each volume
- Extracts all `<p>` tags
- Filters paragraphs that contain any of the following keywords:

```python
["turkey", "pasha", "ottoman", "mustafa", "kemal", "ismet", "suphi", "ethem", "istanbul", "ankara"]
