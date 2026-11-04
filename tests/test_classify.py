"""Run with:  python -m pytest -q"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from classify import classify, parse_html  # noqa: E402


def c(title, prose="", bullets=None, dept="", commitment=""):
    return classify(title, dept, commitment, prose, bullets or [])


# ---- level ----
def test_new_grad_is_entry():
    assert c("Software Engineer, New Grad")["level"] == "entry"

def test_senior_is_not_entry():
    assert c("Senior Software Engineer")["level"] == "other"

def test_intern():
    assert c("Data Science Intern")["level"] == "intern"

def test_internal_is_not_intern():
    r = c("Internal Audit Associate")
    assert r["level"] == "entry" and r["function"] == "finance_accounting"

def test_years_decide_level():
    assert c("Financial Analyst", "Requirements: 0-2 years of experience in FP&A.")["level"] == "entry"
    assert c("Financial Analyst", "You have 1+ year of experience in FP&A.")["level"] == "entry"
    assert c("Financial Analyst", "You have 5+ years of experience in FP&A.")["level"] == "other"

def test_two_plus_years_is_not_entry():
    # Labeling decision: a posting that asks for 2+ years is not entry-level, whatever the title.
    assert c("Global Operations Associate", "You have 2+ years of experience in logistics.")["level"] == "other"
    assert c("Software Engineer, Payments", "2+ years of professional experience")["level"] == "other"

def test_years_written_as_words():
    assert c("Operations Associate", "At least two (2) years of experience in brokerage.")["level"] == "other"

def test_apm_product_name_is_not_associate_pm():
    assert c("Staff Product Designer, APM", "10+ years of experience")["level"] == "other"

def test_numbered_levels():
    assert c("Software Engineer I")["level"] == "entry"
    assert c("Software Engineer II")["level"] == "other"

def test_associate_product_manager():
    r = c("Associate Product Manager")
    assert r["level"] == "entry" and r["function"] == "product_design"


# ---- function ----
def test_sales_engineer_is_sales():
    assert c("Sales Engineer")["function"] == "sales_marketing"

def test_software_engineer_data_is_software():
    assert c("Software Engineer, Data Platform")["function"] == "software_eng"

def test_recruiter_is_hr():
    assert c("Recruiting Coordinator")["function"] == "hr_people"


# ---- AI requirement ----
def test_boilerplate_is_not_a_skill():
    r = c("Accountant", "We are building AI to transform finance.", ["Requirements\tBachelor's degree in accounting"])
    assert r["ai_any"] and not r["ai_skill"]

def test_ai_tool_use_is_a_skill():
    r = c("People Operations Coordinator", "", ["What you'll need\tComfortable using AI tools like ChatGPT to speed up research"])
    assert r["ai_skill"] and r["ai_type"] == "use"

def test_ai_build_is_a_skill():
    r = c("Software Engineer, New Grad", "", ["Nice to have\tExperience with PyTorch and LLM fine-tuning"])
    assert r["ai_skill"] and r["ai_type"] == "build"

def test_perk_is_not_a_skill():
    r = c("Analyst", "", ["Benefits\tMonthly stipend for AI tools and learning"])
    assert not r["ai_skill"]

def test_about_us_bullets_are_skipped():
    r = c("Analyst", "", ["About Acme\tBacked by leading AI investors"])
    assert not r["ai_skill"]

def test_ai_titled():
    assert c("Machine Learning Engineer, New Grad")["ai_titled"]
    assert not c("Tax Associate")["ai_titled"]


# ---- HTML ----
def test_parse_html_keeps_section_headings():
    prose, bullets = parse_html(
        "<p>About the role</p><h3>Requirements</h3><ul><li><strong>Python</strong> skills</li>"
        "<li>SQL</li></ul><h3>Benefits</h3><ul><li>401k</li></ul>"
    )
    assert "About the role" in prose
    assert bullets == ["Requirements\tPython skills", "Requirements\tSQL", "Benefits\t401k"]


def test_function_fixes_from_validation():
    assert c("Forward Deployed Engineer Intern (HR Technology)")["function"] == "software_eng"
    assert c("Analytics Engineer, HR Analytics")["function"] == "data_ml"
    assert c("Scale Solution Engineer")["function"] == "sales_marketing"
    assert c("Customer Support Specialist")["function"] == "other"
    assert c("Infrastructure Business Operations Associate")["function"] == "consulting_strategy_ops"
    assert c("Deployment Strategist, Internship")["function"] == "consulting_strategy_ops"
    assert c("Processing Cost Analyst")["function"] == "finance_accounting"
    assert c("Administrative Coordinator")["function"] == "other"
    assert c("BIM Designer & Coordinator")["function"] == "other"
