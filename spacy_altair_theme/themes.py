import altair as alt

# category: blue, green, purple following themes on spacy.io
# Note that the blue is the "darker" blue which meets WCAG AA contrast ratio standards
spacy_category = ["#077fa6", "#047c5c", "#6642d1"]

spacy_sequential = [
    "#8efcff",
    "#6bddff",
    "#46c0f5",
    "#0da6d9",
    "#018abb",
    "#006f9f",
    "#005583",
    "#003d68",
    "#00254e",
]

spacy_diverging = [
    "#047c5c",
    "#50957b",
    "#81ad9b",
    "#afc5bc",
    "#dedede",
    "#bacfdd",
    "#94c1db",
    "#66b2d9",
    "#09a4d7",
]


def spacy_base_theme():
    primary_color = "#077fa6"
    font_color = "#1a1e23"
    grey_color = "#f5f5f5"
    base_size = 21.6
    lg_font = 22.4
    sm_font = 20.8
    xs_font = 17.6

    config = {
        "config": {
            "arc": {"fill": primary_color},
            "area": {"fill": primary_color},
            "circle": {"fill": primary_color, "stroke": font_color, "strokeWidth": 0.5},
            "line": {"stroke": primary_color},
            "path": {"stroke": primary_color},
            "point": {"stroke": primary_color},
            "rect": {"fill": primary_color},
            "shape": {"stroke": primary_color},
            "symbol": {"fill": primary_color},
            "title": {
                "color": font_color,
                "fontSize": lg_font,
            },
            "axis": {
                "titleColor": font_color,
                "titleFontSize": sm_font,
                "labelColor": font_color,
                "labelFontSize": sm_font,
                "gridColor": grey_color,
                "domainColor": font_color,
                "tickColor": "#fff",
            },
            "header": {
                "labelFontSize": base_size,
                "titleFontSize": base_size,
            },
            "legend": {
                "titleColor": font_color,
                "titleFontSize": sm_font,
                "labelColor": font_color,
                "labelFontSize": xs_font,
            },
            "range": {
                "category": spacy_category,
                "diverging": spacy_diverging,
                "heatmap": spacy_sequential,
                "ramp": spacy_sequential,
                "ordinal": spacy_sequential,
            },
        }
    }
    return config


def spacy_mono_theme():
    font = "JetBrains Mono"
    bold_font = "JetBrains Mono"
    primary_color = "#077fa6"
    font_color = "#1a1e23"
    grey_color = "#f5f5f5"
    base_size = 19.2  # smaller base size for this font
    lg_font = base_size * 1.03703704  # proportion from website sizes
    sm_font = base_size * 0.96296296  # proportion from website sizes
    xs_font = base_size * 0.81481481  # proportion from website sizes
    config = {
        "config": {
            "arc": {"fill": primary_color},
            "area": {"fill": primary_color},
            "circle": {"fill": primary_color, "stroke": font_color, "strokeWidth": 0.5},
            "line": {"stroke": primary_color},
            "path": {"stroke": primary_color},
            "point": {"stroke": primary_color},
            "rect": {"fill": primary_color},
            "shape": {"stroke": primary_color},
            "symbol": {"fill": primary_color},
            "title": {
                "font": bold_font,
                "color": font_color,
                "fontSize": lg_font,
            },
            "axis": {
                "titleFont": bold_font,
                "titleColor": font_color,
                "titleFontSize": sm_font,
                "labelFont": font,
                "labelColor": font_color,
                "labelFontSize": sm_font,
                "gridColor": grey_color,
                "domainColor": font_color,
                "tickColor": "#fff",
            },
            "header": {
                "labelFont": font,
                "titleFont": bold_font,
                "labelFontSize": base_size,
                "titleFontSize": base_size,
            },
            "legend": {
                "titleFont": bold_font,
                "titleColor": font_color,
                "titleFontSize": sm_font,
                "labelFont": font,
                "labelColor": font_color,
                "labelFontSize": xs_font,
            },
            "range": {
                "category": spacy_category,
                "diverging": spacy_diverging,
                "heatmap": spacy_sequential,
                "ramp": spacy_sequential,
                "ordinal": spacy_sequential,
            },
        }
    }
    return config


alt.themes.register("spacy-base", spacy_base_theme)
alt.themes.register("spacy-mono", spacy_mono_theme)
