import json
import os

PALETTE = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353", "#69f0a0"]

def render_heatmap():
    data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/contributions.json")
    
    if not os.path.exists(data_path):
        print("No contributions.json found. Generating empty heatmap.")
        days = [{"level": 0} for _ in range(365)]
    else:
        with open(data_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            days = data.get("days", [])
            
    # SVG Constants
    box_size = 11
    gap = 4
    weeks = 53
    width = weeks * (box_size + gap) + 40
    height = 7 * (box_size + gap) + 40
    
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">']
    svg.append('<style>')
    svg.append('.box { animation: slideDown 1s ease-out forwards; opacity: 0; }')
    svg.append('@keyframes slideDown { from { transform: translateY(-10px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }')
    svg.append('</style>')
    svg.append('<rect width="100%" height="100%" fill="#0d1117" rx="6"/>')
    svg.append(f'<g transform="translate(20, 20)">')
    
    # Render boxes
    for i, day in enumerate(days):
        week = i // 7
        day_of_week = i % 7
        level = min(day.get("level", 0), 5)
        color = PALETTE[level]
        
        x = week * (box_size + gap)
        y = day_of_week * (box_size + gap)
        
        # Stagger animation delay diagonally
        delay = (week * 0.02) + (day_of_week * 0.02)
        
        svg.append(f'<rect class="box" x="{x}" y="{y}" width="{box_size}" height="{box_size}" fill="{color}" rx="2" style="animation-delay: {delay}s;"/>')

    svg.append('</g>')
    svg.append('</svg>')
    
    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "contrib-heatmap.svg")
    
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(svg))
    print("contrib-heatmap.svg generated!")

if __name__ == "__main__":
    render_heatmap()
