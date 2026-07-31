from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class FormatGuideline(BaseModel):
    court_name_format: str = Field(..., description="Format of court title line")
    caption_structure: str = Field(..., description="Layout style of the legal caption box")
    title_style: str = Field(..., description="Formatting of motion main title")
    sections: List[str] = Field(default_factory=list, description="Ordered section headers")
    line_numbering: bool = Field(default=True, description="Whether line numbering is enforced")
    font_style: str = Field(default="Times New Roman / Standard Legal", description="Extracted typography style")
    signature_block_style: str = Field(..., description="Structure of signature line and attorney credentials")
    certificate_of_service: bool = Field(default=True, description="Includes certificate of service")

class CaseReference(BaseModel):
    court: str = Field(default="UNITED STATES DISTRICT COURT FOR THE NORTHERN DISTRICT OF CALIFORNIA")
    plaintiff: str = Field(default="JOHN DOE")
    defendant: str = Field(default="ACME CORPORATION")
    case_number: str = Field(default="Case No. 3:24-cv-08912-WHA")
    judge: Optional[str] = Field(default="Hon. William Alsup")
    dispute_type: str = Field(default="Failure to Respond to Interrogatories and Requests for Production")
    discovery_items: List[str] = Field(default_factory=list, description="Specific discovery request numbers in dispute")
    facts_summary: str = Field(..., description="Brief factual background of the dispute")
    relief_requested: str = Field(..., description="Specific order or sanctions requested")

class SearchSource(BaseModel):
    id: str
    title: str
    url: str
    domain: str
    snippet: str
    rule_tag: str
    relevance_score: float
    source_type: str = "Federal / Local Civil Rule"  # or "Precedent Case Law" / "Statutory Authority"

class AgentStep(BaseModel):
    id: int
    layer_name: str
    title: str
    status: str  # "pending", "running", "completed", "failed"
    details: str
    thoughts: List[str] = Field(default_factory=list)
    timestamp: str

class GenerateMotionRequest(BaseModel):
    format_text: Optional[str] = None
    reference_text: Optional[str] = None
    preset_id: Optional[str] = "preset_frcp_37"
    include_web_search: bool = True
    jurisdiction: Optional[str] = "Federal District Court"

class MotionResponse(BaseModel):
    success: bool = True
    format_analysis: FormatGuideline
    case_facts: CaseReference
    search_sources: List[SearchSource]
    agent_steps: List[AgentStep]
    final_draft: str
    format_adherence_score: float
    generated_at: str
