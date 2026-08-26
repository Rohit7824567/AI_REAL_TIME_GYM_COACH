import time
import streamlit as st


class VoicePipeline:
    ISSUE_COOLDOWN_SECONDS = 6
    ENCOURAGEMENT_COOLDOWN_SECONDS = 15
    NO_POSE_COOLDOWN_SECONDS = 8

    def __init__(self, llm, tts):
        self.llm = llm
        self.tts = tts
        self.last_spoken_at = 0.0

    def _find_form_issue(self, exercise, metrics):
        if "issue" in metrics:
            return metrics["issue"]

        if exercise == "Squats":
            if metrics.get("depth_status") == "TOO HIGH":
                return "The squat is not deep enough. Bend your knees further."
            if metrics.get("back_angle", 180) < 130:
                return "The athlete is leaning too far forward during the squat."

        elif exercise == "Push-ups":
            if metrics.get("body_alignment") == "Poor Form":
                return "The body is not straight during the push-up."
            if metrics.get("hip_status") == "SAGGING":
                return "The hips are sagging during the push-up."
            if metrics.get("hip_status") == "PIKED UP":
                return "The hips are too high during the push-up."

        elif exercise == "Biceps Curls (Dumbbell)":
            if metrics.get("swing_status") == "SWINGING":
                return "The torso is swinging during the curl."
            if metrics.get("shoulder_status") == "ELBOW DRIFTING":
                return "The elbow is drifting away from the body."

        elif exercise == "Shoulder Press":
            if metrics.get("back_arch_status") == "Excessive Arch":
                return "The lower back is arching excessively during the press."
            if metrics.get("back_arch_status") == "Slight Arch":
                return "A slight back arch is visible. Brace the core."

        elif exercise == "Lunges" and metrics.get("balance_status") == "OFF BALANCE":
            return "The athlete is losing balance during the lunge."

        return None

    def process_event(self, event, exercise, metrics):
        issue = self._find_form_issue(exercise, metrics)
        now = time.time()

        if event == "ongoing_form_check":
            cooldown = self.ISSUE_COOLDOWN_SECONDS if issue else self.ENCOURAGEMENT_COOLDOWN_SECONDS
        elif event == "no_pose_detected":
            cooldown = self.NO_POSE_COOLDOWN_SECONDS
        else:
            cooldown = 0

        if now - self.last_spoken_at < cooldown:
            return None

        text = self.llm.give_feedback(event, issue)
        voice = self.tts.speak(text)
        self.last_spoken_at = now
        return voice, text


def autoplay_audio(audio_bytes):
    if not audio_bytes:
        return

    st.markdown("<style>[data-testid='stAudio'] {display: none;}</style>", unsafe_allow_html=True)
    st.audio(audio_bytes, format="audio/mp3", autoplay=True)
