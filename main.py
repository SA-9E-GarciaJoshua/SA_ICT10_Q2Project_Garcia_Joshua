from pyscript import display, document

def clear_element(element_id):
    """Clear the innerHTML of an element if it exists."""
    el = document.getElementById(element_id)
    if el:
        el.innerHTML = ""

def get_float(element_id):
    """Return the float value of an input, or 0.0 if invalid/empty."""
    try:
        value = document.getElementById(element_id).value
        return float(value) if value else 0.0
    except ValueError:
        return 0.0

# Calculator
def general_weighted_average(e):
    """Calculate and display the General Weighted Average (GWA)."""
    for element in ["student_info", "summary", "output", "gwa_image"]:
        clear_element(element)

    first_name = document.getElementById("first_name").value
    last_name = document.getElementById("last_name").value

    subjects = ["Science", "Math", "English", "Filipino", "ICT", "PE"]
    grades = {sub: get_float(sub.lower()) for sub in subjects}
    units = {"Science":5, "Math":5, "English":5, "Filipino":3, "ICT":2, "PE":1}

    weighted_sum = sum(grades[sub] * units[sub] for sub in subjects)
    total_units = sum(units.values())
    gwa = weighted_sum / total_units if total_units else 0

    display(f"Name: {first_name} {last_name}", target="student_info")
    summary_text = "\n".join(f"{sub}: {grade:.0f}" for sub, grade in grades.items())
    display(summary_text, target="summary")
    display(f"Your general weighted average is {gwa:.2f}", target="output")

    if gwa > 2.75:
        gwa_image_html = '<img src="donut.png" alt="Donut" width="150" style="margin-top:20px;">'
        document.getElementById("gwa_image").innerHTML = gwa_image_html

# Club
club_info = {
    "puppet": {
        "name": "Puppet Club",
        "description": "Learn to bring puppets to life with movement, expression, and storytelling.",
        "meeting_time": "Every Monday 3:30–5:00 PM",
        "location": "Room 068",
        "advisor": "Mr. Henson",
        "members": 10,
        "category": "Performance",
        "image": "puppet.png"
    },
    "gymnastics": {
        "name": "Gymnastics Club",
        "description": "Build strength, flexibility, and coordination through fun and challenging routines.",
        "meeting_time": "Every Tuesday and Thursday 4:00–5:30 PM",
        "location": "Gymnasium",
        "advisor": "Mr. Ulo",
        "members": 18,
        "category": "Performance",
        "image": "gymnastics.png"
    },
    "acrobatics": {
        "name": "Acrobatics Club",
        "description": "Master flips, balance, and dynamic movements with style and grace.",
        "meeting_time": "Every Wednesday 3:45–5:15 PM",
        "location": "Gymnasium",
        "advisor": "Mr. Paglieri",
        "members": 15,
        "category": "Performance",
        "image": "acrobatics.png"
    },
    "magic": {
        "name": "Magic Club",
        "description": "Learn the dark secrets behind illusions, sleight-of-hand tricks, and stage magic.",
        "meeting_time": "Every Friday 3:30–5:00 PM",
        "location": "Room 067",
        "advisor": "Mr. Siegfried",
        "members": 15,
        "category": "Performance",
        "image": "magic.png"
    },
    "improv": {
        "name": "Improv Club",
        "description": "Develop quick thinking, humor, and stage presence through improvisation games.",
        "meeting_time": "Every Wednesday 3:45–5:15 PM",
        "location": "Room 069",
        "advisor": "Ms. Fey",
        "members": 20,
        "category": "Performance",
        "image": "improv.png"
    },
    "debate": {
        "name": "Debate Club",
        "description": "Hone critical thinking, research, and public speaking skills while competing in debates.",
        "meeting_time": "Every Thursday 3:30–5:00 PM",
        "location": "Room 070",
        "advisor": "Mr. Jennings",
        "members": 12,
        "category": "Academic",
        "image": "debate.jpg"
    },
}

def show_club_info(e):
    """Display information about the selected club and show its image."""
    clear_element("club-info")
    selected = document.getElementById("club-select").value
    info = club_info.get(selected)

    if info:
        output = (
            f"{info['name']}\n"
            f"Description: {info['description']}\n"
            f"Meeting Time: {info['meeting_time']}\n"
            f"Location: {info['location']}\n"
            f"Advisor: {info['advisor']}\n"
            f"Number of Members: {info['members']}\n"
            f"Category: {info['category']}"
        )
        display(output, target="club-info")
        
        if 'image' in info:
            img_html = f'<img src="{info["image"]}" alt="{info["name"]}">'
            document.getElementById("club-info").innerHTML += img_html
