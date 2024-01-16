#! /usr/bin/env python3
from __future__ import annotations

import click
import lxml.etree


@click.command()
@click.argument("sitemap", type=click.File("r"), default="-")
def extract_sitemap_urls(sitemap: click.File):
    """Extract URLs from sitemap.xml"""
    tree = lxml.etree.parse(sitemap)
    root = tree.getroot()
    for url in root.iter("{http://www.sitemaps.org/schemas/sitemap/0.9}url"):
        loc = url.find("{http://www.sitemaps.org/schemas/sitemap/0.9}loc").text
        click.echo(loc)


if __name__ == "__main__":
    extract_sitemap_urls()
