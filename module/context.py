from dataclasses import dataclass, field

@dataclass
class CallContext:
    customer_name: str | None = None
    interested: bool = False
    busy: bool = False
    rejected: bool = False
    preferred_location: str | None = None
    property_type: str | None = None
    budget: str | None = None
    follow_up_time: str | None = None
    raw_notes: list[str] = field(default_factory=list)

    @property
    def outcome_status(self) -> str:
        if self.interested:
            return "INTERESTED"
        if self.busy:
            return "BUSY - CALL LATER"
        if self.rejected:
            return "NOT INTERESTED"
        return "UNKNOWN"

    @property
    def summary_notes(self) -> str:
        notes = []

        if self.customer_name:
            notes.append(f"Customer name: {self.customer_name}")

        if self.preferred_location:
            notes.append(f"Preferred location: {self.preferred_location}")

        if self.property_type:
            notes.append(f"Property type: {self.property_type}")

        if self.budget:
            notes.append(f"Budget: {self.budget}")

        if self.raw_notes:
            notes.append("Extra notes: " + " | ".join(self.raw_notes))

        if not notes:
            return "No additional details collected."
        return " | ".join(notes)
