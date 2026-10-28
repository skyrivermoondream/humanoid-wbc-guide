"""Original SVG artwork for the guide: a stylised humanoid (2D forward kinematics),
the inspection-corridor scene, and small line icons. Colours come from CSS classes so
light/dark themes both work, including inside <use> clones."""
import math

# ---------------------------------------------------------------- robot ----
THIGH, SHIN, FOOT = 62, 60, 22
TORSO, NECK = 80, 14
UARM, FARM = 50, 46


def _down(length, deg):
    """Vector of `length` pointing down, rotated `deg` toward +x (forward)."""
    r = math.radians(deg)
    return (length * math.sin(r), length * math.cos(r))


def _up(length, deg):
    r = math.radians(deg)
    return (length * math.sin(r), -length * math.cos(r))


def _add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def leg_ankle(thigh_deg, shin_deg):
    k = _down(THIGH, thigh_deg)
    return k, _add(k, _down(SHIN, shin_deg))


def robot(pelvis, pose, scale=1.0, cls=""):
    """Return SVG markup for a humanoid facing +x.

    pose keys: lean (torso, deg forward), head (deg), near_leg/far_leg (thigh, shin),
    near_arm/far_arm (upper, fore), foot_near/foot_far (deg of foot, 90 = flat forward).
    """
    px, py = pelvis
    lean = pose.get("lean", 0)
    sh = _add((px, py), _up(TORSO, lean))
    parts = []

    def limb(points, width, klass):
        d = "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in points)
        return (f'<path d="{d}" class="{klass}" stroke-width="{width}" '
                f'fill="none" stroke-linecap="round" stroke-linejoin="round"/>')

    def leg(spec, foot_deg, klass):
        t, s = spec
        knee, ankle = leg_ankle(t, s)
        knee = _add((px, py), knee)
        ankle = _add((px, py), ankle)
        toe = _add(ankle, _down(FOOT, foot_deg))
        return limb([(px, py), knee, ankle], 13, klass) + limb([ankle, toe], 9, klass)

    def arm(spec, klass, shoulder):
        u, f = spec
        elbow = _add(shoulder, _down(UARM, u))
        hand = _add(elbow, _down(FARM, f))
        return (limb([shoulder, elbow, hand], 10, klass)
                + f'<circle cx="{hand[0]:.1f}" cy="{hand[1]:.1f}" r="6" class="{klass}-fill"/>')

    far_sh = _add(sh, (-4, 3))
    parts.append(arm(pose.get("far_arm", (8, 14)), "rb-far", far_sh))
    parts.append(leg(pose.get("far_leg", (-6, -4)), pose.get("foot_far", 90), "rb-far"))
    # backpack (behind torso)
    mid = _add((px, py), _up(TORSO * 0.62, lean))
    parts.append(
        f'<g transform="translate({mid[0]:.1f} {mid[1]:.1f}) rotate({lean:.1f})">'
        f'<rect x="-50" y="-30" width="30" height="54" rx="7" class="rb-pack"/>'
        f'<rect x="-45" y="-22" width="20" height="5" rx="2" class="rb-pack-line"/>'
        f'<circle cx="-35" cy="13" r="3.2" class="rb-led"/>'
        f'<path d="M-44 -30 L-48 -46" class="rb-ant" stroke-width="2.4" stroke-linecap="round"/>'
        f'</g>')
    # torso + pelvis
    parts.append(
        f'<g transform="translate({px:.1f} {py:.1f}) rotate({lean:.1f})">'
        f'<rect x="-21" y="-{TORSO + 6}" width="42" height="{TORSO - 4}" rx="13" class="rb-body"/>'
        f'<path d="M-10 -{TORSO - 16} L12 -{TORSO - 16}" class="rb-trim" stroke-width="2.4" stroke-linecap="round"/>'
        f'<rect x="-17" y="-16" width="34" height="24" rx="9" class="rb-body"/>'
        f'</g>')
    # head
    hd = pose.get("head", 0) + lean * 0.4
    neck_top = _add(sh, _up(NECK, lean))
    parts.append(
        f'<g transform="translate({neck_top[0]:.1f} {neck_top[1]:.1f}) rotate({hd:.1f})">'
        f'<rect x="-6" y="-4" width="12" height="10" rx="3" class="rb-body"/>'
        f'<rect x="-19" y="-38" width="40" height="36" rx="12" class="rb-body"/>'
        f'<rect x="2" y="-30" width="21" height="13" rx="6" class="rb-visor"/>'
        f'</g>')
    parts.append(leg(pose.get("near_leg", (6, 4)), pose.get("foot_near", 90), "rb-near"))
    parts.append(arm(pose.get("near_arm", (-6, 6)), "rb-near", sh))
    g = "".join(parts)
    tf = f' transform="translate({px:.1f} {py:.1f}) scale({scale}) translate({-px:.1f} {-py:.1f})"' if scale != 1 else ""
    return f'<g class="robot {cls}"{tf}>{g}</g>'


def ankle_offsets(pose):
    _, near = leg_ankle(*pose.get("near_leg", (6, 4)))
    _, far = leg_ankle(*pose.get("far_leg", (-6, -4)))
    return near, far


# ------------------------------------------------------------ the scene ----
GROUND = 470

POSES = {
    # 1 stepping out of a wet patch onto a grated step
    "step": dict(lean=6, near_leg=(65, 0), far_leg=(-15, -10), foot_far=100,
                 near_arm=(-24, -10), far_arm=(22, 34)),
    # 2 crouch-walking under a low pipe rack
    "crouch": dict(lean=30, head=-12, near_leg=(75, -25), far_leg=(45, -45),
                   foot_far=95, near_arm=(30, 70), far_arm=(-5, 35)),
    # 3 kneeling to read a low gauge
    "kneel": dict(lean=-3, head=4, near_leg=(88, 0), far_leg=(0, -88), foot_far=170,
                  near_arm=(28, 82), far_arm=(6, 18)),
    # 4 standing, reaching the cabinet handle
    "reach": dict(lean=0, near_leg=(10, 5), far_leg=(-8, -6),
                  near_arm=(95, 80), far_arm=(10, 18)),
}


def place(pose, contact, which="far", y=GROUND):
    """Pelvis position so that the chosen ankle sits on (contact_x, y)."""
    near, far = ankle_offsets(pose)
    a = far if which == "far" else near
    return (contact - a[0], y - a[1])


def scene_symbol():
    s = []
    W, H = 1200, 560
    # wall + seams
    s.append(f'<rect x="0" y="96" width="{W}" height="{GROUND - 96}" class="sc-wall"/>')
    for x in range(60, W, 120):
        s.append(f'<path d="M{x} 104 V{GROUND}" class="sc-seam"/>')
    # ceiling + cable tray
    s.append(f'<rect x="0" y="86" width="{W}" height="12" class="sc-ceiling"/>')
    s.append('<rect x="0" y="118" width="930" height="14" rx="3" class="sc-tray"/>')
    for x in range(14, 930, 26):
        s.append(f'<path d="M{x} 120 V130" class="sc-tray-rib"/>')
    # floor slab + painted walkway line
    s.append(f'<rect x="0" y="{GROUND}" width="{W}" height="{H - GROUND}" class="sc-floor"/>')
    s.append(f'<path d="M0 {GROUND} H{W}" class="sc-floor-edge"/>')
    # painted floor-lane edge (static); the animated walkway line is drawn by the hero
    s.append('<path d="M0 534 H1200" class="sc-lane"/>')

    # zone 1: puddle + grated step
    s.append('<ellipse cx="112" cy="474" rx="70" ry="9" class="sc-water"/>')
    s.append('<path d="M70 474 h26 M120 476 h34 M92 471 h14" class="sc-water-glint"/>')
    s.append('<rect x="206" y="437" width="112" height="33" rx="2" class="sc-step"/>')
    for x in range(214, 316, 9):
        s.append(f'<path d="M{x} 441 V466" class="sc-grate"/>')
    s.append('<path d="M206 437 h112" class="sc-step-edge"/>')

    # zone 2: low pipe rack
    for x in (352, 560):
        s.append(f'<path d="M{x} 132 V196" class="sc-hanger"/>')
    for i, y in enumerate((206, 224, 242)):
        s.append(f'<rect x="318" y="{y - 8}" width="282" height="16" rx="8" class="sc-pipe sc-pipe-{i}"/>')
    s.append('<rect x="336" y="196" width="10" height="56" rx="2" class="sc-clamp"/>')
    s.append('<rect x="566" y="196" width="10" height="56" rx="2" class="sc-clamp"/>')
    # low-clearance band
    s.append('<g class="sc-hazard"><rect x="420" y="252" width="84" height="10" rx="2"/></g>')
    for x in range(424, 504, 12):
        s.append(f'<path d="M{x} 262 l8 -10" class="sc-hazard-stripe"/>')

    # zone 3: gauge on a riser pipe
    s.append('<rect x="806" y="286" width="18" height="184" rx="4" class="sc-pipe sc-pipe-1"/>')
    s.append('<rect x="772" y="294" width="40" height="12" rx="3" class="sc-pipe sc-pipe-2"/>')
    s.append('<circle cx="770" cy="300" r="23" class="sc-gauge-ring"/>')
    s.append('<circle cx="770" cy="300" r="16" class="sc-gauge-face"/>')
    s.append('<path d="M770 300 l9 -9" class="sc-needle"/>')
    s.append('<path d="M757 307 a16 16 0 0 1 4 -20" class="sc-gauge-arc"/>')

    # zone 4: electrical cabinet (shifted right so the reach pose fits)
    cx0 = 952
    s.append(f'<rect x="{cx0}" y="170" width="160" height="300" rx="4" class="sc-cabinet"/>')
    s.append(f'<rect x="{cx0 + 8}" y="180" width="144" height="280" rx="2" class="sc-door"/>')
    s.append(f'<rect x="{cx0 + 14}" y="262" width="9" height="38" rx="3" class="sc-handle"/>')
    for i, c in enumerate(("sc-led-g", "sc-led-y", "sc-led-o")):
        s.append(f'<circle cx="{cx0 + 104 + i * 15}" cy="198" r="4.5" class="{c}"/>')
    s.append(f'<path d="M{cx0 + 64} 222 l16 28 h-32 z" class="sc-warn"/>')
    s.append(f'<path d="M{cx0 + 65} 230 l-5 10 h6 l-4 9" class="sc-warn-bolt"/>')
    for y in range(340, 452, 14):
        s.append(f'<path d="M{cx0 + 36} {y} h88" class="sc-vent"/>')

    # zone 6: remote operator booth
    s.append('<g class="sc-booth">'
             '<rect x="996" y="14" width="190" height="62" rx="8" class="sc-booth-box"/>'
             '<rect x="1110" y="24" width="64" height="40" rx="4" class="sc-screen"/>'
             '<path d="M1118 54 l12 -12 l10 8 l14 -16" class="sc-screen-line"/>'
             '<circle cx="1046" cy="36" r="11" class="sc-op"/>'
             '<rect x="1030" y="31" width="32" height="10" rx="5" class="sc-vr"/>'
             '<path d="M1026 76 q20 -26 40 0" class="sc-op"/>'
             '<path d="M1074 44 q14 -10 24 0" class="sc-signal"/>'
             '</g>')
    s.append('<path d="M1000 70 C 930 120, 900 170, 880 214" class="sc-link"/>')

    # robots (zone order)
    pa = POSES
    s.append(robot(place(pa["step"], 150), pa["step"], cls="r-step"))
    s.append(robot(place(pa["crouch"], 452), pa["crouch"], cls="r-crouch"))
    kp = (668, GROUND - leg_ankle(0, -88)[0][1])  # far knee on the ground
    s.append(robot(kp, pa["kneel"], cls="r-kneel"))
    s.append('<path d="M684 290 L744 298" class="sc-sight"/>')
    s.append(robot(place(pa["reach"], 846), pa["reach"], cls="r-reach"))
    return f'<symbol id="scene" viewBox="0 0 {W} {H}">' + "".join(s) + "</symbol>"


# Hero overlay: animated walkway line + numbered checkpoints linking to the needs list.
MARKS = [
    # n, x, y, leader (x1,y1,x2,y2) or None
    (1, 168, 512, None),
    (2, 455, 512, None),
    (3, 690, 512, None),
    (4, 900, 512, None),
    (5, 372, 372, (398, 322, 380, 358)),
    (6, 972, 46, None),
]


def hero_overlay(labels):
    out = ['<path class="hero-route" d="M24 512 H1176" pathLength="1"/>']
    for i, (n, x, y, lead) in enumerate(MARKS):
        if lead:
            out.append(f'<path d="M{lead[0]} {lead[1]} L{lead[2]} {lead[3]}" class="sc-leader"/>')
        out.append(
            f'<a href="#need-{n}" class="sc-mark" style="--i:{i}" aria-label="{n}. {labels[n]}">'
            f'<title>{labels[n]}</title>'
            f'<circle cx="{x}" cy="{y}" r="17"/><text x="{x}" y="{y + 6.5}">{n}</text></a>')
    return "".join(out)


# --------------------------------------------------------------- icons -----
ICONS = {
    # 1 human motion source: person + capture markers
    "motion": '<circle cx="24" cy="9" r="4.5"/><path d="M24 14 V29 M24 18 L14 24 M24 18 L34 13 M24 29 L17 42 M24 29 L32 41"/>'
              '<circle cx="14" cy="24" r="2" class="i-dot"/><circle cx="34" cy="13" r="2" class="i-dot"/>'
              '<circle cx="17" cy="42" r="2" class="i-dot"/><circle cx="32" cy="41" r="2" class="i-dot"/>',
    # 2 retargeting: human -> robot
    "retarget": '<circle cx="10" cy="12" r="3.5"/><path d="M10 16 V28 M10 20 L4 25 M10 20 L16 25 M10 28 L6 38 M10 28 L14 38"/>'
                '<path d="M19 25 H28 M25 21 L29 25 L25 29"/>'
                '<rect x="33" y="8" width="11" height="9" rx="3"/><rect x="34" y="19" width="9" height="12" rx="3"/>'
                '<path d="M36 31 V40 M41 31 V40 M34 21 L31 28 M43 21 L46 28"/>',
    # 3 massively parallel simulation
    "sim": '<rect x="5" y="6" width="38" height="36" rx="5"/>'
           '<path d="M5 18 H43 M5 30 H43 M17.7 6 V42 M30.3 6 V42" class="i-thin"/>'
           '<circle cx="11.3" cy="12" r="2.2" class="i-dot"/><circle cx="24" cy="24" r="2.2" class="i-dot"/>'
           '<circle cx="36.6" cy="36" r="2.2" class="i-dot"/><circle cx="36.6" cy="12" r="2.2" class="i-dot"/>'
           '<circle cx="11.3" cy="36" r="2.2" class="i-dot"/>',
    # 4 general tracker = cerebellum in the robot head
    "tracker": '<rect x="8" y="8" width="32" height="28" rx="9"/><path d="M14 22 h5 l3 -7 l4 14 l3 -7 h6"/>'
               '<path d="M20 36 V42 M28 36 V42 M16 42 H32"/>',
    # 5 high-level commander: VR goggles + instruction bubble
    "command": '<path d="M5 26 q0 -9 9 -9 h20 q9 0 9 9 v3 q0 6 -6 6 h-6 l-4 -4 h-6 l-4 4 h-6 q-6 0 -6 -6 z"/>'
               '<path d="M26 4 h17 q3 0 3 3 v6 q0 3 -3 3 h-9 l-4 4 v-4 h-4 q-3 0 -3 -3 v-6 q0 -3 3 -3 z" class="i-thin"/>',
    # 6 real robot: sim box -> real ground
    "real": '<rect x="4" y="8" width="16" height="16" rx="3" class="i-dash"/><path d="M22 16 H28 M25 13 L28 16 L25 19"/>'
            '<rect x="32" y="6" width="11" height="9" rx="3"/><rect x="33" y="17" width="9" height="12" rx="3"/>'
            '<path d="M35 29 V39 M40 29 V39 M28 42 H47"/>',
}


def icon(name, cls="ico"):
    return (f'<svg class="{cls}" viewBox="0 0 48 48" aria-hidden="true" fill="none" '
            f'stroke-linecap="round" stroke-linejoin="round">{ICONS[name]}</svg>')
