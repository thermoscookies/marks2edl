#!python3
import json
import glob
import os

FPS = 30  # change to your timeline fps


def sec_to_tc(seconds, fps=FPS):
    total_frames = int(round(seconds * fps))

    h = total_frames // (3600 * fps)
    total_frames %= (3600 * fps)

    m = total_frames // (60 * fps)
    total_frames %= (60 * fps)

    s = total_frames // fps
    f = total_frames % fps

    return f"{h:02}:{m:02}:{s:02}:{f:02}"


def add_one_frame(seconds, fps=FPS):
    return sec_to_tc(seconds + 1 / fps)


def convert_file(mark_file):
    with open(mark_file, "r") as f:
        events = json.load(f)

    lines = [
        "TITLE: XBOXGO_FALCON_MARKERS",
        "FCM: NON-DROP FRAME",
        ""
    ]

    event_num = 1

    for e in events:
        if e["type"] == "start":  # skip start
            continue

        t = e["time"] - 15  # the -15 is to set the timer 15 seconds before the click
        name = e["type"].upper()

        src_in = sec_to_tc(0)
        src_out = sec_to_tc(1 / FPS)
        rec_in = sec_to_tc(t)
        rec_out = add_one_frame(t)

        lines.append(
            f"{event_num:03}  AX       V     C        "
            f"{src_in} {src_out} {rec_in} {rec_out}"
        )
        lines.append(f" |C:ResolveColorBlue |M:{name} |D:20")

        event_num += 1

    edl_file = os.path.splitext(mark_file)[0] + ".edl"

    with open(edl_file, "w") as f:
        f.write("\n".join(lines))

    print(f"✓ {mark_file} → {edl_file}")


def main():
    files = glob.glob("*.mark")

    if not files:
        print("No .mark files found.")
        return

    for f in files:
        convert_file(f)


if __name__ == "__main__":
    main()
