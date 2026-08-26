EXERCISE_OPTIONS = [
    "Squats",
    "Push-ups",
    "Biceps Curls (Dumbbell)",
    "Shoulder Press",
    "Lunges",
]

POSE_CONNECTIONS = [
    (11, 12), (11, 13), (13, 15), (12, 14), (14, 16),
    (11, 23), (12, 24), (23, 24),
    (23, 25), (24, 26), (25, 27), (26, 28), (27, 29), (28, 30),
    (29, 31), (30, 32), (27, 31), (28, 32),
]

METRICS_FIELDS = {
    "Squats": {"knee_angle": 0, "back_angle": 0, "depth_status": "N/A"},
    "Push-ups": {"elbow_angle": 0, "body_alignment": "N/A", "hip_status": "N/A"},
    "Biceps Curls (Dumbbell)": {"elbow_angle": 0, "shoulder_status": "N/A", "swing_status": "N/A"},
    "Shoulder Press": {"elbow_angle": 0, "extension_status": "N/A", "back_arch_status": "N/A"},
    "Lunges": {"front_knee_angle": 0, "torso_angle": 0, "balance_status": "N/A"},
}

PROMPT = """
You are Apna AI Coach, a professional AI gym trainer monitoring a live workout.

Give one short, natural coaching cue (10–15 words). Speak directly to the athlete,
be specific about the exercise and visible form issue, and prioritize safety.
Never greet or thank the athlete. For good form, give an energetic encouragement.
For no_pose_detected, tell the athlete to step fully into the camera frame.
""".strip()
