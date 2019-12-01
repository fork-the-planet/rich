from typing import Dict

from .style import Style

DEFAULT_STYLES: Dict[str, Style] = {
    "none": Style(),
    "reset": Style.reset(),
    "dim": Style(dim=True),
    "bright": Style(dim=False),
    "bold": Style(bold=True),
    "b": Style(bold=True),
    "italic": Style(italic=True),
    "i": Style(italic=True),
    "underline": Style(underline=True),
    "u": Style(underline=True),
    "blink": Style(blink=True),
    "blink2": Style(blink2=True),
    "reverse": Style(reverse=True),
    "strike": Style(strike=True),
    "s": Style(strike=True),
    "black": Style(color="black"),
    "red": Style(color="red"),
    "green": Style(color="green"),
    "yellow": Style(color="yellow"),
    "magenta": Style(color="magenta"),
    "cyan": Style(color="cyan"),
    "white": Style(color="white"),
}

MARKDOWN_STYLES = {
    "markdown.paragraph": Style(),
    "markdown.text": Style(),
    "markdown.emph": Style(italic=True),
    "markdown.strong": Style(bold=True),
    "markdown.code": Style(dim=True, bold=True),
    "markdown.code_block": Style(dim=True, color="cyan", bgcolor="black"),
    "markdown.block_quote": Style(color="magenta"),
    "markdown.list": Style(color="cyan"),
    "markdown.item": Style(),
    "markdown.item.bullet": Style(color="yellow", bold=True),
    "markdown.item.number": Style(color="yellow", bold=True),
    "markdown.hr": Style(dim=True),
    "markdown.h1.border": Style(),
    "markdown.h1": Style(bold=True),
    "markdown.h2": Style(bold=True, underline=True),
    "markdown.h3": Style(bold=True),
    "markdown.h4": Style(bold=True, dim=True),
    "markdown.h5": Style(underline=True),
    "markdown.h6": Style(italic=True),
    "markdown.h7": Style(italic=True, dim=True),
    "markdown.link": Style(bold=True),
    "markdown.link_url": Style(underline=True),
}
DEFAULT_STYLES.update(MARKDOWN_STYLES)