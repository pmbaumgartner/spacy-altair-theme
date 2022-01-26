import altair as alt
import spacy_altair_theme
from spacy_altair_theme import __version__


def test_version():
    assert __version__ == "0.1.0"


def test_base_theme():
    r = alt.themes.enable("spacy-base")
    assert r.registry.active == "spacy-base"


def test_monotheme():
    r = alt.themes.enable("spacy-mono")
    assert r.registry.active == "spacy-mono"
