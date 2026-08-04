from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    HRFlowable,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output" / "pdf" / "Kyungtack_Lee_Resume_NVIDIA.pdf"

NAVY = colors.HexColor("#17324D")
GREEN = colors.HexColor("#5A8F00")
DARK = colors.HexColor("#20262E")
MUTED = colors.HexColor("#56616D")
LIGHT = colors.HexColor("#D8DEE5")


def make_styles():
    base = getSampleStyleSheet()
    return {
        "name": ParagraphStyle(
            "Name",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=20,
            leading=22,
            textColor=NAVY,
            alignment=TA_LEFT,
            spaceAfter=1,
        ),
        "tagline": ParagraphStyle(
            "Tagline",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=10.4,
            leading=12,
            textColor=GREEN,
            spaceAfter=3,
        ),
        "contact": ParagraphStyle(
            "Contact",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=8.2,
            leading=10,
            textColor=MUTED,
            spaceAfter=4,
        ),
        "section": ParagraphStyle(
            "Section",
            parent=base["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=11,
            leading=13,
            textColor=NAVY,
            spaceBefore=7,
            spaceAfter=4,
            keepWithNext=True,
        ),
        "summary": ParagraphStyle(
            "Summary",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=9.4,
            leading=12.2,
            textColor=DARK,
            spaceAfter=2,
        ),
        "entry": ParagraphStyle(
            "Entry",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=9.2,
            leading=11.5,
            textColor=DARK,
            spaceAfter=1.5,
        ),
        "entry_head": ParagraphStyle(
            "EntryHead",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=9.8,
            leading=11.8,
            textColor=DARK,
        ),
        "date": ParagraphStyle(
            "Date",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=8.8,
            leading=11,
            textColor=MUTED,
            alignment=TA_RIGHT,
        ),
        "bullet": ParagraphStyle(
            "Bullet",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=9,
            leading=11.3,
            leftIndent=9,
            firstLineIndent=-7,
            textColor=DARK,
            spaceAfter=1.8,
        ),
        "small": ParagraphStyle(
            "Small",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=8.6,
            leading=10.8,
            textColor=DARK,
            spaceAfter=1.4,
        ),
    }


S = make_styles()


def section(title):
    return [
        Paragraph(escape(title.upper()), S["section"]),
        HRFlowable(width="100%", thickness=0.7, color=GREEN, spaceAfter=3),
    ]


def bullet(text, style="bullet"):
    return Paragraph(f"- {text}", S[style])


def entry_header(title, organization, dates):
    left = Paragraph(
        f"<b>{escape(title)}</b> | {escape(organization)}", S["entry_head"]
    )
    right = Paragraph(escape(dates), S["date"])
    table = Table([[left, right]], colWidths=[150 * mm, 27 * mm])
    table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
            ]
        )
    )
    return table


def add_page_number(canv, doc):
    canv.saveState()
    canv.setStrokeColor(LIGHT)
    canv.setLineWidth(0.4)
    canv.line(doc.leftMargin, 18 * mm, A4[0] - doc.rightMargin, 18 * mm)
    canv.setFont("Helvetica", 7.5)
    canv.setFillColor(MUTED)
    canv.drawString(doc.leftMargin, 13.5 * mm, "Kyungtack Lee | Resume")
    canv.drawRightString(A4[0] - doc.rightMargin, 13.5 * mm, f"Page {doc.page}")
    canv.restoreState()


def build_resume():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(OUTPUT),
        pagesize=A4,
        leftMargin=16 * mm,
        rightMargin=16 * mm,
        topMargin=13 * mm,
        bottomMargin=22 * mm,
        title="Kyungtack Lee - Resume",
        author="Kyungtack Lee",
        subject="Vehicle Motion Control and Autonomous Driving",
    )

    story = []
    story.append(Paragraph("Kyungtack Lee", S["name"]))
    story.append(
        Paragraph(
            "VEHICLE MOTION CONTROL &amp; AUTONOMOUS DRIVING ENGINEER",
            S["tagline"],
        )
    )
    story.append(
        Paragraph(
            'Seoul, Republic of Korea | +82 10-2632-3242 | '
            '<link href="mailto:kyungtacklee@gmail.com" color="#56616D">kyungtacklee@gmail.com</link> | '
            '<link href="https://kyungtacklee.github.io/" color="#56616D">kyungtacklee.github.io</link> | '
            '<link href="https://github.com/kyungtacklee" color="#56616D">github.com/kyungtacklee</link>',
            S["contact"],
        )
    )

    story.extend(section("Professional Summary"))
    story.append(
        Paragraph(
            "Vehicle motion control and autonomous driving engineer with more than ten years of experience in production automotive engineering. Technical lead and project owner for safety-critical planning and control functions, with end-to-end responsibility spanning function architecture, algorithm development, modeling and simulation, real-time implementation, vehicle integration, calibration, and validation. Expertise includes motion planning, trajectory generation and tracking, vehicle dynamics, integrated chassis control, state estimation, and optimization-based control.",
            S["summary"],
        )
    )

    story.extend(section("Core Competencies"))
    skills = [
        ("Planning &amp; Control", "Motion planning, trajectory generation, path tracking, integrated chassis control, optimization-based control"),
        ("Vehicle Engineering", "Vehicle dynamics, state estimation, actuator coordination, calibration, in-vehicle testing, recorded-data analysis"),
        ("Programming", "C for production software analysis and development; MATLAB; Python"),
        ("Real-Time Development", "MATLAB/Simulink, dSPACE MicroAutoBox II, real-time model build and deployment, rapid control prototyping"),
        ("NVIDIA Platforms", "NVIDIA Jetson AGX; Isaac Sim"),
        ("Simulation &amp; Process", "CarSim, CarMaker, AUTOSAR-aligned development, unit/integration testing; familiarity with ISO 26262, ISO 21448 SOTIF, and Automotive SPICE"),
    ]
    for label, value in skills:
        story.append(bullet(f"<b>{label}:</b> {value}"))

    story.extend(section("Professional Experience"))
    story.append(entry_header("Senior Research Engineer", "HL Mando", "2015.08 - Present"))
    story.append(
        bullet(
            "<b>Mobility Motion Control (2020 - Present):</b> Technical lead and project owner for planning and control functions including Integrated Chassis Control, Vehicle Stability Control Assist, Evasive Collision Avoidance, Smart Hitching Assist, Trailer Parking Assist, and Minimum Risk Maneuver."
        )
    )
    story.append(
        bullet(
            "Lead function definition and algorithm development through simulation, real-time deployment, system integration, vehicle tuning, scenario-based testing, and measurable vehicle-level evaluation."
        )
    )
    story.append(
        bullet(
            "Develop and analyze production software in C; build and deploy MATLAB/Simulink control models to dSPACE MicroAutoBox II; use NVIDIA Jetson AGX for vehicle evaluation."
        )
    )
    story.append(
        bullet(
            "<b>System Design (2019 - 2020):</b> E-Corner Module system design and analysis."
        )
    )
    story.append(
        bullet(
            "<b>Gear Design (2015 - 2019):</b> Electric Power Steering, Steer-by-Wire, Shift-by-Wire, and e-Drive systems; durability analysis, optimization, and in-house engineering tool development."
        )
    )
    story.append(Spacer(1, 2))
    story.append(
        entry_header(
            "Research Engineer", "Samsung Techwin (now Hanwha Aerospace)", "2012.08 - 2015.07"
        )
    )
    story.append(
        bullet(
            "Designed integral helical gears for turbo compressors and performed core-system design and dynamic-system analysis."
        )
    )
    story.append(Spacer(1, 2))
    story.append(entry_header("Engineering Intern", "General Motors Korea", "2011.07 - 2011.08"))
    story.append(bullet("Supported engine-map tuning and validation."))

    story.append(PageBreak())

    story.extend(section("Selected Projects"))
    story.append(entry_header("Trailer Parking Assist & Minimum Risk Maneuver", "HL Mando", "2026 - Present"))
    story.append(
        bullet(
            "Technical lead and project owner for planning and control architecture, simulation, real-time implementation, system integration, and vehicle-level evaluation."
        )
    )
    story.append(
        bullet(
            "Developing robust maneuver generation and safe fallback behavior for production-oriented automated-driving functions."
        )
    )
    story.append(Spacer(1, 2.5))
    story.append(entry_header("Smart Hitching Assist", "HL Mando", "2025"))
    story.append(
        bullet(
            "Led end-to-end function architecture, planning and control development, real-time deployment, vehicle integration, calibration, and validation."
        )
    )
    story.append(
        bullet(
            "Delivered a successful customer demonstration; received a Company Special Recognition Award in December 2025."
        )
    )
    story.append(Spacer(1, 2.5))
    story.append(entry_header("Evasive Collision Avoidance", "HL Mando", "2024"))
    story.append(
        bullet(
            "Owned the complete planning and control scope: evasive path generation, path tracking control, and vehicle stability coordination."
        )
    )
    story.append(
        bullet(
            "Integrated and validated the unified framework through simulation, dSPACE real-time execution, in-vehicle tuning, and safety-critical scenario testing."
        )
    )
    story.append(Spacer(1, 2.5))
    story.append(entry_header("Vehicle Stability Control Assist", "HL Mando", "2024"))
    story.append(
        bullet(
            "Developed a hierarchical integrated chassis controller combining differential braking and semi-active suspension damping."
        )
    )
    story.append(
        bullet(
            "Published simulation and real-world evaluation results showing approximately 17.4% lower maximum roll angle and 8.7% lower maximum sideslip angle versus respective conventional methods."
        )
    )

    story.extend(section("Education"))
    story.append(entry_header("Ph.D. Candidate, Mechanical Engineering", "Seoul National University", "2023.03 - Present"))
    story.append(
        Paragraph(
            "Interactive and Networked Robotics Laboratory (INRoL), Advisor: Professor Dongjun Lee<br/>Research: Supervisory Integrated Chassis Control Using Model Predictive Path Integral Control with Legacy Controllers",
            S["small"],
        )
    )
    story.append(Spacer(1, 3))
    story.append(entry_header("M.S., Mechanical Engineering", "Seoul National University", "2020.09 - 2022.06"))
    story.append(
        Paragraph(
            "Vehicle Dynamics and Control Laboratory (VDCL), Advisor: Professor Kyongsu Yi<br/>Thesis: Path Tracking Control of Four-Wheel-Independent-Steering-and-Driving Vehicle Based on Adaptive-Weight Optimal Control",
            S["small"],
        )
    )
    story.append(Spacer(1, 3))
    story.append(entry_header("B.S., Mechanical Engineering", "Ajou University", "2006.03 - 2012.06"))

    story.extend(section("Selected Honors"))
    honors = [
        ("2025.12", "Company Special Recognition Award - Smart Hitching Assist development and customer demonstration, HL Mando"),
        ("2025.11", "Outstanding Paper Award (Oral Session), Korean Society of Automotive Engineers"),
        ("2024.12", "Excellence Award - R&D Outstanding Paper, HL Mando"),
        ("2024.11", "Outstanding Paper Award (Poster Session), Korean Society of Automotive Engineers"),
        ("2024.03", "Best Dialogue Award, EVS37 International Electric Vehicle Symposium and Exhibition"),
    ]
    for date, honor in honors:
        story.append(bullet(f"<b>{date}</b> | {escape(honor)}", style="small"))

    story.extend(section("Selected Publications & Patents"))
    publications = [
        "K. Lee and J. Seol, \"Development of Integrated Chassis Control of Semi-Active Suspension with Differential Brake for Vehicle Lateral Stability,\" World Electric Vehicle Journal, 16(2):91, 2025.",
        "K. Lee et al., \"Lyapunov-Informed Model Predictive Path Integral Control for Robust Trailer Hitch Assist under Perception Uncertainty,\" KSAE Annual Conference, 2025.",
        "K. Lee et al., \"Continuous Curvature Path Planning Based on Bezier Curves for Autonomous Driving in Complex Environments,\" KSAE Annual Conference, 2024.",
    ]
    for publication in publications:
        story.append(bullet(escape(publication), style="small"))
    story.append(
        bullet(
            "Inventor or co-inventor on 19 patent applications spanning automotive chassis, steering, suspension, vehicle-state estimation, trailer assistance, and mechanical systems.",
            style="small",
        )
    )

    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
    print(OUTPUT)


if __name__ == "__main__":
    build_resume()
