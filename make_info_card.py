import os

def create_info_card():
    # You can customize these details!
    lines = [
        "<tspan class='key'>Now</tspan>        <tspan class='val'>Building SynthSHrk Extension</tspan>",
        "<tspan class='key'>Prev</tspan>       <tspan class='val'>Bug Bounty Bootcamp</tspan>",
        "<tspan class='key'>Stack</tspan>      <tspan class='val'>JavaScript, Python, Cybersecurity</tspan>",
        "<tspan class='key'>Highlights</tspan> <tspan class='val'>Srijan 6.0</tspan>"
    ]

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" width="490" height="250" viewBox="0 0 490 250">
    <style>
        .title {{ font-family: monospace; font-weight: bold; font-size: 16px; fill: #58a6ff; }}
        .text {{ font-family: monospace; font-size: 14px; fill: #c9d1d9; }}
        .key {{ fill: #7ee787; font-weight: bold; }}
        .val {{ fill: #c9d1d9; }}
        .line {{ opacity: 0; animation: fadeIn 0.5s forwards; }}
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(5px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
    </style>
    <rect width="490" height="250" fill="#0d1117" rx="6"/>
    <text x="20" y="40" class="title">harshit@github ~ $ neofetch</text>
    <text x="20" y="80" class="text line" style="animation-delay: 0.2s;">{lines[0]}</text>
    <text x="20" y="110" class="text line" style="animation-delay: 0.4s;">{lines[1]}</text>
    <text x="20" y="140" class="text line" style="animation-delay: 0.6s;">{lines[2]}</text>
    <text x="20" y="170" class="text line" style="animation-delay: 0.8s;">{lines[3]}</text>
    <rect x="20" y="210" width="15" height="15" fill="#ff7b72" />
    <rect x="40" y="210" width="15" height="15" fill="#79c0ff" />
    <rect x="60" y="210" width="15" height="15" fill="#d2a8ff" />
    <rect x="80" y="210" width="15" height="15" fill="#a5d6ff" />
</svg>"""

    os.makedirs(os.path.dirname(os.path.abspath(__file__)) + "/../output", exist_ok=True)
    with open(os.path.dirname(os.path.abspath(__file__)) + "/../output/info-card.svg", "w", encoding="utf-8") as f:
        f.write(svg_content)
    print("info-card.svg generated!")

if __name__ == "__main__":
    create_info_card()
