from pyscript import display, document

def general_weighted_average(e):
    # Clear previous outputs
    document.getElementById('student_info').innerHTML = ''
    document.getElementById('summary').innerHTML = ''
    document.getElementById('output').innerHTML = ''
    document.getElementById('gwa_image').innerHTML = ''  # clear previous image

    subjects = ['Science', 'Math', 'English', 'Filipino', 'ICT', 'PE']
    units_subject = (5, 3, 2, 1)

    first_name = document.getElementById('first_name').value
    last_name = document.getElementById('last_name').value

    science = float(document.getElementById('science').value)
    math = float(document.getElementById('math').value)
    english = float(document.getElementById('english').value)
    filipino = float(document.getElementById('filipino').value)
    ict = float(document.getElementById('ict').value)
    pe = float(document.getElementById('pe').value)

units = {
    "science": 5,
    "math": 5,
    "english": 5,
    "filipino": 3,
    "ict": 2,
    "pe": 1
}

weighted_sum = (
    science * units["science"] +
    math * units["math"] +
    english * units["english"] +
    filipino * units["filipino"] +
    ict * units["ict"] +
    pe * units["pe"]
)

total_units = sum(units.values())

    summary = f"""
    {subjects[0]}: {science:.0f}
    {subjects[1]}: {math:.0f}
    {subjects[2]}: {english:.0f}
    {subjects[3]}: {filipino:.0f}
    {subjects[4]}: {ict:.0f}
    {subjects[5]}: {pe:.0f}
    """

    # Display info
    display(f'Name: {first_name} {last_name}', target="student_info")
    display(summary, target='summary')
    display(f'Your general weighted average is {gwa:.2f}', target='output')

    # Show donut image if GWA > 2.75
    if gwa > 2.75:
        document.getElementById('gwa_image').innerHTML = '<img src="donut.png" alt="Donut" width="150" style="margin-top:20px;">'




club_info = {
    "chess": {
        "name": "Chess Club",
        "description": "A club for chess enthusiasts of all skill levels.",
        "meeting_time": "Every Wednesday 3:30–5:00 PM",
        "location": "Room 405",
        "advisor": "Mr. Santos",
        "members": 20,
        "category": "Academic"
    },
    "drama": {
        "name": "Drama Club",
        "description": "For students interested in theater, acting, and stage production.",
        "meeting_time": "Every Monday and Thursday 4:00–6:00 PM",
        "location": "MM Hall",
        "advisor": "Ms. Evangelista",
        "members": 22,
        "category": "Arts"
    },
    "robotics": {
        "name": "Robotics Club",
        "description": "Design, build, and program robots for competitions.",
        "meeting_time": "Every Tuesday 3:45–5:30 PM",
        "location": "Computer Lab",
        "advisor": "Ms. Pasco",
        "members": 18,
        "category": "Academic"
    },
    "debate": {
        "name": "Debate Club",
        "description": "Develop public speaking and argumentation skills.",
        "meeting_time": "Every Friday 3:30–5:00 PM",
        "location": "Room 507",
        "advisor": "Ms. Carabot",
        "members": 12,
        "category": "Academic"
    },
    "art": {
        "name": "Art Club",
        "description": "Explore various art mediums and techniques.",
        "meeting_time": "Every Wednesday 3:45–5:15 PM",
        "location": "Art Room",
        "advisor": "Mr. Balajadia",
        "members": 20,
        "category": "Arts"
    },
    "": {
        "name": "",
        "description": "",
        "meeting_time": "",
        "location": "",
        "advisor": "",
        "members": "",
        "category": ""
    }
}

def show_club_info(e):
    document.getElementById('club-info').innerHTML = ''
    selected_club = document.getElementById("club-select").value
    info = club_info.get(selected_club, club_info[""])

    output = f"""
    {info['name']}
    Description: {info['description']}
    Meeting Time: {info['meeting_time']}
    Location: {info['location']}
    Advisor: {info['advisor']}
    Number of Members: {info['members']}
    Category: {info['category']}
    """

    display(output, target="club-info")
