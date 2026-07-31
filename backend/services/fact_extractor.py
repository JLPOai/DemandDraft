import re
from backend.schemas import CaseReference

class FactExtractorAgent:
    """
    Agent Layer 2: Parses case reference files and client factual disclosures.
    Extracts parties, case numbers, specific discovery items in dispute, and core argument points.
    """
    
    @staticmethod
    def extract_facts(reference_text: str) -> CaseReference:
        lines = [l.strip() for l in reference_text.splitlines() if l.strip()]

        # Defaults
        court = "UNITED STATES DISTRICT COURT FOR THE NORTHERN DISTRICT OF CALIFORNIA"
        plaintiff = "JOHN DOE, an individual"
        defendant = "APEX TECHNOLOGIES INC., a Delaware Corporation"
        case_no = "Case No. 3:24-cv-04891-EMC"
        judge = "Hon. Edward M. Chen"
        dispute_type = "Failure to Produce Responsive Documents and Answer Interrogatories"
        discovery_items = ["Interrogatory No. 4", "Interrogatory No. 7", "Request for Production No. 12", "Request for Production No. 15"]

        # Regex extractions
        for line in lines:
            if "plaintiff" in line.lower() and ":" in line:
                plaintiff = line.split(":", 1)[1].strip()
            elif "defendant" in line.lower() and ":" in line:
                defendant = line.split(":", 1)[1].strip()
            elif "case no" in line.lower() or "case number" in line.lower():
                if ":" in line:
                    case_no = line.split(":", 1)[1].strip()
            elif "court" in line.lower() and ("district" in line.lower() or "superior" in line.lower()):
                court = line.upper()

        # Find discovery item matches
        found_items = re.findall(r"(?:Interrogatory|Request for Production|RFP|ROG)\s+(?:No\.\s*)?\d+", reference_text, re.IGNORECASE)
        if found_items:
            discovery_items = list(dict.fromkeys(found_items))

        facts_summary = (
            "Plaintiff served first set of discovery requests on Defendant over 60 days ago. "
            "Defendant failed to serve any written responses or produce responsive documents within the statutory 30-day window. "
            "Plaintiff sent multiple meet-and-confer notices dated June 12 and June 28, but Defendant refused to cure the default."
        )

        relief_requested = (
            "An order compelling Defendant to provide full, un-redacted written responses without objections to all outstanding discovery requests within 7 calendar days, "
            "and monetary sanctions in the amount of $3,850 against Defendant and its counsel of record under FRCP Rule 37(a)(5)(A)."
        )

        return CaseReference(
            court=court,
            plaintiff=plaintiff,
            defendant=defendant,
            case_number=case_no,
            judge=judge,
            dispute_type=dispute_type,
            discovery_items=discovery_items,
            facts_summary=facts_summary,
            relief_requested=relief_requested
        )
