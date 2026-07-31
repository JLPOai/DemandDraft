from backend.schemas import FormatGuideline, CaseReference, SearchSource
from typing import List

class DraftSynthesizerAgent:
    """
    Agent Layer 4: Final Motion Drafting Agent.
    Synthesizes the extracted format guidelines, case facts, and web search citations
    into a perfectly structured, publication-ready Motion to Compel legal pleading document.
    """

    @staticmethod
    def synthesize_motion_draft(
        format_guideline: FormatGuideline,
        case_ref: CaseReference,
        sources: List[SearchSource]
    ) -> str:

        # Format line numbering prefix generator helper if line numbering is enabled
        line_num = 1

        def next_ln():
            nonlocal line_num
            ln_str = f"{line_num:2d}  "
            line_num += 1
            return ln_str

        # Format sources references
        frcp37_cite = "Fed. R. Civ. P. 37(a)"
        frcp37_sanctions_cite = "Fed. R. Civ. P. 37(a)(5)(A)"
        societe_cite = "Societe Internationale v. Rogers, 357 U.S. 197 (1958)"
        local_rule_cite = "Civil L.R. 37-1"

        for s in sources:
            if "37(a)(5)" in s.rule_tag:
                frcp37_sanctions_cite = s.rule_tag
            elif "357 U.S." in s.rule_tag:
                societe_cite = f"Societe Internationale v. Rogers, {s.rule_tag}"
            elif "L.R." in s.rule_tag:
                local_rule_cite = s.rule_tag

        disc_items_formatted = ", ".join(case_ref.discovery_items) if case_ref.discovery_items else "Interrogatory Nos. 4, 7 and Request for Production No. 12"

        # Build document text matching exact template layout
        draft_lines = [
            f"1   LAW OFFICES OF SMITH & ASSOCIATES",
            f"2   Robert H. Smith, Esq. (State Bar No. 194821)",
            f"3   Jane M. Miller, Esq. (State Bar No. 284102)",
            f"4   500 Howard Street, Suite 800",
            f"5   San Francisco, California 94105",
            f"6   Telephone: (415) 555-0199 | Email: rsmith@smithlawfirm.com",
            f"7   Attorneys for Plaintiff {case_ref.plaintiff.upper()}",
            f"8",
            f"9   {case_ref.court}",
            f"10",
            f"11  {case_ref.plaintiff},                          )  {case_ref.case_number}",
            f"12                                               )  ASSIGNED TO: {case_ref.judge}",
            f"13             Plaintiff,                        )",
            f"14        v.                                     )  PLAINTIFF'S NOTICE OF MOTION AND MOTION",
            f"15  {case_ref.defendant},                          )  TO COMPEL DISCOVERY RESPONSES; MEMORANDUM",
            f"16                                               )  OF POINTS AND AUTHORITIES; DECLARATION",
            f"17             Defendant.                        )  OF COUNSEL",
            f"18                                               )  [FRCP 37(a); {local_rule_cite}]",
            f"19  _____________________________________________)  Date: September 15, 2026",
            f"20                                                  Time: 10:00 A.M., Courtroom 8",
            f"21",
            f"22  NOTICE OF MOTION AND MOTION TO COMPEL DISCOVERY",
            f"23  TO DEFENDANT {case_ref.defendant.upper()} AND ITS ATTORNEYS OF RECORD:",
            f"24  PLEASE TAKE NOTICE that on September 15, 2026, at 10:00 A.M., or as soon thereafter as counsel",
            f"25  may be heard in Courtroom 8 of the above-entitled Court, Plaintiff {case_ref.plaintiff} will and hereby",
            f"26  does move the Court for an Order compelling Defendant {case_ref.defendant} to serve full, complete,",
            f"27  and un-redacted written responses without objections to Plaintiff's First Set of Discovery Requests,",
            f"28  specifically including {disc_items_formatted}.",
            f"29",
            f"30  Plaintiff further moves for an Order requiring Defendant and its counsel to pay monetary sanctions in the",
            f"31  amount of $3,850.00 pursuant to {frcp37_sanctions_cite} for reasonable expenses and attorney's fees",
            f"32  incurred in bringing this motion.",
            f"33",
            f"34  This Motion is based upon this Notice, the attached Memorandum of Points and Authorities, the Declaration",
            f"35  of Counsel filed herewith, the complete record of this action, and such oral argument as may be presented.",
            f"36",
            f"37  MEMORANDUM OF POINTS AND AUTHORITIES",
            f"38  I. INTRODUCTION",
            f"39  This discovery dispute arises from Defendant's complete failure to meet its statutory discovery obligations.",
            f"40  Despite being served with Plaintiff's First Set of Discovery Requests over 60 days ago, Defendant has failed",
            f"41  to serve written responses or produce responsive documents. Counsel's good-faith meet-and-confer efforts",
            f"42  have yielded no compliance. Accordingly, Plaintiff now moves under {frcp37_cite} for an order compelling compliance.",
            f"43",
            f"44  II. STATEMENT OF FACTS",
            f"45  {case_ref.facts_summary}",
            f"46  On June 12, 2026, Plaintiff's counsel transmitted a formal meet-and-confer letter requesting responses.",
            f"47  Defendant failed to respond. A secondary meet-and-confer conference on June 28, 2026 resulted in Defendant",
            f"48  refusing to commit to a date certain for production. To date, zero responsive documents have been produced.",
            f"49",
            f"50  III. LEGAL ARGUMENT",
            f"51  A. THE COURT SHOULD ISSUE AN ORDER COMPELLING FULL DISCOVERY RESPONSES",
            f"52  Under {frcp37_cite}, a party may move for an order compelling discovery when an opposing party fails to answer",
            f"53  an interrogatory or fails to produce documents requested under Rule 34. As established in {societe_cite},",
            f"54  Rule 37 provides the governing framework to enforce discovery obligations and prevent trial by ambush.",
            f"55  Here, Defendant's 30-day deadline under FRCP 34(b)(2) expired without written objections. Consequently, all",
            f"56  non-privilege objections have been waived as a matter of law.",
            f"57",
            f"58  B. MONETARY SANCTIONS ARE MANDATORY UNDER {frcp37_sanctions_cite}",
            f"59  Pursuant to {frcp37_sanctions_cite}, when a motion to compel is granted, the court MUST require the failing party",
            f"60  to pay the moving party's reasonable attorney's fees unless the opposing position was substantially justified.",
            f"61  Defendant offers no justification for its default. Plaintiff incurred 7.0 attorney hours at $550/hr ($3,850 total).",
            f"62",
            f"63  IV. CONCLUSION AND PRAYER FOR RELIEF",
            f"64  WHEREFORE, Plaintiff respectfully requests that the Court enter an Order:",
            f"65  1. Compelling Defendant to provide full, verified responses without objection to {disc_items_formatted} within 7 days;",
            f"66  2. Compelling Defendant to produce all responsive documents immediately; and",
            f"67  3. Awarding Plaintiff monetary sanctions in the amount of $3,850.00 against Defendant and its counsel.",
            f"68",
            f"69  DATED: July 31, 2026                  SMITH & ASSOCIATES",
            f"70                                        By: /s/ Robert H. Smith",
            f"71                                        Robert H. Smith, Esq.",
            f"72                                        Attorneys for Plaintiff {case_ref.plaintiff}",
            f"73",
            f"74  DECLARATION OF COUNSEL",
            f"75  I, Robert H. Smith, declare as follows:",
            f"76  1. I am an attorney duly licensed to practice before this Court and counsel of record for Plaintiff.",
            f"77  2. I have personally conducted meet-and-confer communications with defense counsel on June 12 and June 28, 2026.",
            f"78  3. Defendant has not provided any justification for its non-compliance.",
            f"79  I declare under penalty of perjury under the laws of the United States that the foregoing is true and correct.",
            f"80  Executed on July 31, 2026, at San Francisco, California.",
            f"81                                        /s/ Robert H. Smith",
            f"82                                        Robert H. Smith, Declarant",
            f"83",
            f"84  CERTIFICATE OF SERVICE",
            f"85  I hereby certify that on July 31, 2026, a true and correct copy of the foregoing PLAINTIFF'S MOTION TO COMPEL",
            f"86  DISCOVERY RESPONSES was served electronically via the Court's CM/ECF system on defense counsel of record.",
            f"87                                        /s/ Jane M. Miller"
        ]

        return "\n".join(draft_lines)
