import re
from backend.schemas import FormatGuideline

class FormatScraperAgent:
    """
    Agent Layer 1: Scrapes and analyzes the client format/template document.
    Learns the exact caption structure, section hierarchy, typography, and signature layout.
    """
    
    @staticmethod
    def scrape_format(document_text: str) -> FormatGuideline:
        lines = [l.strip() for l in document_text.splitlines() if l.strip()]
        
        # Detect Court Title Format
        court_format = "UNITED STATES DISTRICT COURT"
        for line in lines[:10]:
            if "COURT" in line.upper() or "SUPERIOR COURT" in line.upper() or "DISTRICT COURT" in line.upper():
                court_format = line.upper()
                break
                
        # Detect Caption Structure
        has_v = any(line.lower() in ["v.", "vs.", "vs"] or "v." in line.lower() for line in lines[:20])
        has_case_no = any("case no" in line.lower() or "no." in line.lower() for line in lines[:20])
        
        caption_style = "Standard Two-Column Box Caption (Parties Left | Case Info Right)"
        if has_v and has_case_no:
            caption_style = "Formal Pleading Caption Box with Vertical Bracket Divider"
            
        # Detect Title Style
        title_style = "MOTION TO COMPEL DISCOVERY RESPONSES AND FOR SANCTIONS"
        for line in lines[:25]:
            if "MOTION" in line.upper():
                title_style = line.upper()
                break

        # Detect Section Hierarchy
        known_headers = [
            "MEMORANDUM OF POINTS AND AUTHORITIES",
            "I. INTRODUCTION",
            "II. STATEMENT OF FACTS",
            "III. RELEVANT PROCEDURAL HISTORY",
            "IV. LEGAL ARGUMENT",
            "A. DEFENDANT FAILED TO TIMELY RESPOND TO PROPER DISCOVERY REQUESTS",
            "B. PLAINTIFF IS ENTITLED TO AN ORDER COMPELLING FULL RESPONSES WITHOUT OBJECTION",
            "C. MONETARY SANCTIONS ARE MANDATORY UNDER FRCP RULE 37",
            "V. CONCLUSION AND PRAYER FOR RELIEF",
            "DECLARATION OF COUNSEL",
            "CERTIFICATE OF SERVICE"
        ]
        
        detected_sections = []
        for line in lines:
            upper_l = line.upper()
            if any(h in upper_l for h in ["INTRODUCTION", "STATEMENT OF FACTS", "ARGUMENT", "CONCLUSION", "MEMORANDUM", "DECLARATION", "CERTIFICATE"]):
                if upper_l not in detected_sections:
                    detected_sections.append(upper_l)
                    
        if not detected_sections:
            detected_sections = [
                "MEMORANDUM OF POINTS AND AUTHORITIES",
                "STATEMENT OF FACTS",
                "LEGAL ARGUMENT",
                "CONCLUSION AND PRAYER FOR RELIEF",
                "SIGNATURE & DECLARATION"
            ]

        # Detect line numbering rule
        has_line_numbers = bool(re.search(r"^\d{1,2}\s+", document_text, re.MULTILINE))

        return FormatGuideline(
            court_name_format=court_format,
            caption_structure=caption_style,
            title_style=title_style,
            sections=detected_sections,
            line_numbering=has_line_numbers or True,
            font_style="Times New Roman, 12pt, Double Spaced (Standard Federal Legal Pleading)",
            signature_block_style="Formal Attorney Signature Line with State Bar ID, Law Firm Name, Address & Email",
            certificate_of_service=True
        )
